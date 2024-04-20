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
    FLAT = 1
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
    """
    HasuraClient

    A Python class for interacting with a Hasura GraphQL API.

    Parameters
    ----------
    uri : str
        The URI of the Hasura GraphQL API.
    role : str, optional
        The role to be used for authentication. Default is None.
    admin_secret : str, optional
        The admin secret to be used for authentication. Default is None.
    output_dir : str, optional
        The output directory to save the result files. Default is '.'.
    headers : dict, optional
        Additional headers to be included in the API request. Default is None.

    Methods
    -------
    _execute(query: str, variables: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = None,
             output_format: str = ExportFormat.NATURAL) -> Any:
        Executes a GraphQL query or mutation on the Hasura API and returns the result in the specified format.

    _vectorize_result() -> Dict[str, np.ndarray]:
        Vectorizes the last query result using DictVectorizer.

    _clusters(n_clusters: Dict[str, int]) -> Dict[str, List[List[Dict[str, Any]]]]:
        Performs clustering on the last vectorized result using the KMedoids algorithm.

    _optimal_number_of_clusters(lower: int, upper: int) -> Dict[str, int]:
        Find the optimal number of clusters for each key in the last query result.

    _anomalies_training(output_dir: Optional[str] = None) -> Dict[str, str]:
        Train anomaly detection models and save them to the specified output directory, using the last query result.

    _anomalies(training_files: Optional[Dict[str, str]] = None) -> Dict[str, np.ndarray]:
        Performs anomaly detection using an Isolation Forest algorithm.

    _convert_output_format(output_format: str) -> Any:
        Convert the output format of the last query result.

    _write_to_file(output_dir: Optional[str] = None, output_format: Optional[str] = None) -> List[str]:
        Writes the last query result data to file(s) in the specified output format and directory.
    """
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
        self.result = self.native_result
        return self.convert_output_format(output_format)

    def _get_file_path(self, extension):
        return os.path.join(self.output_dir, extension)

    @staticmethod
    def _write_result_as_file(file_name, result_data):
        with open(file_name, 'w') as file:
            json.dump(result_data, file, indent=4)

    def vectorize_result(self):
        """
        Vectorizes the last query result using DictVectorizer.

        :return: self.vectorized_result, a dictionary with the same keys as the last query, but with the values
                 transformed into dense arrays using DictVectorizer.
        """
        v = DictVectorizer(sparse=False)  # Set sparse=False for a dense array
        self.vectorized_result = {}
        for key in self.native_result:
            self.vectorized_result[key] = v.fit_transform(flatten_nested_dicts(self.native_result[key]))
        return self.vectorized_result

    def clusters(self, n_clusters):
        """
        :param n_clusters: A dictionary containing the number of clusters for each key
        :return: A dictionary containing the clustered data for each key

        Performs clustering on the vectorized result using the KMedoids algorithm.
        Clusters the data for each key separately and returns a dictionary containing the clustered data for each key.

        Example usage:
            self.clusters({
                'key1': 3,
                'key2': 5,
                ...
            })
        """
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
        """
        Find the optimal number of clusters for each key in the vectorized result.

        :param lower: The lower bound of the range of cluster numbers to consider.
        :param upper: The upper bound of the range of cluster numbers to consider.
        :return: A dictionary containing the optimal number of clusters for each key in the vectorized result.
        """
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
        """
        Train anomaly detection models and save them to the specified output directory.

        :param output_dir: Optional. The directory to save the trained models. If not specified, the models will be saved in the current working directory.
        :type output_dir: str

        :return: A dictionary containing the filenames of the saved models, with keys as the model names.
        :rtype: dict
        """
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

    def anomalies(self, training_files=None, threshold=0):
        """
        Find anomalies in the data.

        :param training_files: A dictionary of training file paths for each key in the vectorized result. If provided, the model will be loaded from the file before fitting. Default is None
        *.
        :param threshold: The threshold score below which a data point is considered an anomaly. Default is 0.
        :return: A dictionary where each key corresponds to a category in the vectorized result, and the value is a list of anomalies with scores below the threshold.

        """
        def add_score(item, index, score):
            item['__score__'] = score
            item['__index__'] = index
            return item

        self.anomalies_result = {}
        self.vectorize_result()
        # Initialize Isolation Forest
        clf = IsolationForest(contamination=0.1, random_state=42)
        for key in self.vectorized_result:
            if training_files is not None:
                with open(training_files[key], 'rb') as model_file:
                    clf = pickle.load(model_file)
            clf.fit(self.vectorized_result[key])
            scores = clf.decision_function(self.vectorized_result[key])
            merged = list(map(lambda x: add_score(self.native_result[key][x[0]], x[0], x[1]), enumerate(scores)))
            self.anomalies_result[key] = list(filter(lambda x: x['__score__'] < threshold, merged))
        return self.anomalies_result

    def convert_output_format(self, output_format):
        """
        Convert the output format of the result.

        :param output_format: The desired output format. Must be one of ExportFormat.FLAT, ExportFormat.DATAFRAME, ExportFormat.PARQUET, ExportFormat.CSV, ExportFormat.ARROW.
        :return: The converted result in the specified format.
        """
        self.result_format = output_format
        if output_format == ExportFormat.FLAT:
            self.result = self._transform_to_flatten()
        elif output_format in [ExportFormat.DATAFRAME, ExportFormat.PARQUET, ExportFormat.CSV]:
            self.result = self._transform_to_dataframe()
        elif output_format == ExportFormat.ARROW:
            self.result = self._transform_to_arrow()
        return self.result

    def write_to_file(self, output_dir=None, output_format=None):
        """
        Writes the result data to file(s) in the specified output format and directory.

        :param output_dir: The directory where the output file(s) will be written. If not provided, the current output directory is used.
        :param output_format: The format in which the output file(s) will be written. If not provided, the current output format is used.
        :return: A list of filenames corresponding to the output file(s) created.

        """
        if output_dir is not None:
            self.output_dir = output_dir
        if output_format is not None:
            self.convert_output_format(output_format)

        def filename_mapper(_output, _key):
            return {
                ExportFormat.NATURAL: self._get_file_path('result.json'),
                ExportFormat.FLAT: self._get_file_path(_key + '.json'),
                ExportFormat.PARQUET: self._get_file_path(_key + '.pq'),
                ExportFormat.CSV: self._get_file_path(_key + '.csv'),
                ExportFormat.ARROW: self._get_file_path(_key + '.arrow')
            }[_output]

        format_writers = {
            ExportFormat.NATURAL: self._write_result_as_file,
            ExportFormat.FLAT: self._write_result_as_file,
            ExportFormat.PARQUET: lambda _filename, data: data.to_parquet(_filename),
            ExportFormat.CSV: lambda _filename, data: data.to_csv(_filename, index=False),
            ExportFormat.ARROW: lambda _filename, data: pa.ipc.new_file(_filename, data.schema).write(
                data)
        }
        filenames = []
        if self.result_format == ExportFormat.NATURAL:
            filename = filename_mapper(self.result_format, '')
            format_writers[self.result_format](filename, self.native_result)
            return filename
        for key in self.result:
            filename = filename_mapper(self.result_format, key)
            filenames.append(filename)
            format_writers[self.result_format](filename, self.result[key])
        return filenames
