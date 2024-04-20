import json
import os
import pickle
from enum import Enum
from gql import gql
import pandas as pd
from pyhasura import gql_client, flatten_nested_dicts
import pyarrow as pa
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import IsolationForest
from sklearn_extra.cluster import KMedoids


class ExportFormat(Enum):
    FLATTEN = 1
    DATAFRAME = 2
    ARROW = 3
    NATURAL = 4
    PARQUET = 5
    CSV = 6


def create_empty_arrays(n):
    return [[] for _ in range(n)]


def compute_deltas(numbers):
    """
    Computes the deltas (differences) between consecutive elements in an array of numbers.

    Args:
        numbers (list or numpy.ndarray): Input array of numbers.

    Returns:
        list: Array of deltas (differences) between consecutive elements.
    """
    deltas = []
    for i in range(1, len(numbers)):
        delta = numbers[i] - numbers[i - 1]
        deltas.append(abs(delta))
    return deltas


def get_ordinal_of_smallest_number(numbers):
    m = None
    n = None
    for i, x in enumerate(numbers):
        if m is None:
            m = x
            n = i
        if x != 0 and x < m:
            m = x
            n = i
    return n


class HasuraClient:
    def __init__(self, uri, role=None, admin_secret=None, output_dir='.', headers=None):
        if headers is None:
            headers = {}
        if role is not None:
            headers['x-hasura-role'] = role
        if admin_secret is not None:
            headers['x-hasura-admin-secret'] = admin_secret
        self.uri = uri
        self.admin_secret = admin_secret
        self.client = gql_client(self.uri, headers=headers)
        self.result = {}
        self.native_result = {}
        self.vectorized_result = {}
        self.anomalies_result = {}
        self.output_dir = output_dir
        self.result_format = None

    def _transform_to_flatten(self):
        flatten_result = {key: flatten_nested_dicts(val) for key, val in self.native_result.items()}
        return flatten_result

    def _transform_to_dataframe(self):
        flatten_result = {key: pd.DataFrame(flatten_nested_dicts(val)) for key, val in self.native_result.items()}
        return flatten_result

    def _transform_to_arrow(self):
        flatten_result = {key: pa.Table.from_pandas(pd.DataFrame(flatten_nested_dicts(val))) for key, val in
                          self.native_result.items()}
        return flatten_result

    def execute(self, query, variables=None, output_format=ExportFormat.NATURAL):
        self.native_result = self.client.execute(gql(query), variables)
        self.result_format = output_format
        if output_format == ExportFormat.FLATTEN:
            self.result = self._transform_to_flatten()
        elif output_format in [ExportFormat.DATAFRAME, ExportFormat.PARQUET, ExportFormat.CSV]:
            self.result = self._transform_to_dataframe()
        elif output_format == ExportFormat.ARROW:
            self.result = self._transform_to_arrow()
        return self.result

    def get_file_path(self, extension):
        return os.path.join(self.output_dir, extension)

    @staticmethod
    def write_result_as_file(file_name, result_data):
        with open(file_name, 'w') as file:
            json.dump(result_data, file, indent=4)

    def vectorize_result(self):
        v = DictVectorizer(sparse=False)  # Set sparse=False for a dense array
        self.vectorized_result = {}
        for key in self.native_result:
            self.vectorized_result[key] = v.fit_transform(flatten_nested_dicts(self.native_result[key]))
        return self.vectorized_result

    def clusters(self, n_clusters):
        self.vectorize_result()
        clustered = {}
        for key in self.vectorized_result:
            kmedoids = KMedoids(n_clusters=n_clusters[key], random_state=42)
            kmedoids.fit(self.vectorized_result[key])
            cluster_labels = kmedoids.labels_
            clustered[key] = create_empty_arrays(cluster_labels.max() + 1)
            # Print the cluster assignments
            for i, cluster_label in enumerate(cluster_labels):
                clustered[key][cluster_label].append(self.native_result[key][i])
        return clustered

    def optimal_number_of_clusters(self, lower, upper):
        self.vectorize_result()
        clustered = {}
        for key in self.vectorized_result:
            costs = []
            for k in range(lower, upper + 1):
                kmedoids = KMedoids(n_clusters=min(k, len(self.vectorized_result[key]) - 1), random_state=42)
                kmedoids.fit(self.vectorized_result[key])
                costs.append(kmedoids.inertia_)
            clustered[key] = get_ordinal_of_smallest_number(compute_deltas(costs)) + 2
        return clustered

    def anomalies_training(self, output_dir=None):
        if output_dir is not None:
            self.output_dir = output_dir
        self.vectorize_result()
        clf = IsolationForest(contamination=0.1, random_state=42)
        filenames = {}
        for key in self.vectorized_result:
            clf.fit(self.vectorized_result[key])
            filename = os.path.join(self.output_dir, key + '.pkl')
            with open(filename, 'wb') as model_file:
                pickle.dump(clf, model_file)
            filenames[key] = filename
        return filenames

    def anomalies(self, training_files=None):
        self.anomalies_result = {}
        self.vectorize_result()
        # Initialize Isolation Forest
        clf = IsolationForest(contamination=0.1, random_state=42)
        for key in self.vectorized_result:
            if training_files is not None:
                with open(training_files[key], 'rb') as model_file:
                    clf = pickle.load(model_file)
            clf.fit(self.vectorized_result[key])
            self.anomalies_result[key] = clf.decision_function(self.vectorized_result[key])
        return self.anomalies_result

    def write_to_file(self, output_dir=None):
        if output_dir is not None:
            self.output_dir = output_dir

        def filename_mapper(_output, _key):
            return {
                ExportFormat.NATURAL: self.get_file_path('result.json'),
                ExportFormat.FLATTEN: self.get_file_path(_key + '.json'),
                ExportFormat.PARQUET: self.get_file_path(_key + '.pq'),
                ExportFormat.CSV: self.get_file_path(_key + '.csv'),
                ExportFormat.ARROW: self.get_file_path(_key + '.arrow')
            }[_output]

        format_writers = {
            ExportFormat.FLATTEN: self.write_result_as_file,
            ExportFormat.PARQUET: lambda _filename, data: data.to_parquet(_filename),
            ExportFormat.CSV: lambda _filename, data: data.to_csv(_filename, index=False),
            ExportFormat.ARROW: lambda _filename, data: pa.ipc.new_file(_filename, data.schema).write(
                data).close(),
        }
        filenames = []
        for key in self.result:
            filename = filename_mapper(self.result_format, key)
            filenames.append(filename)
            format_writers[self.result_format](filename, self.result[key])
        return filenames
