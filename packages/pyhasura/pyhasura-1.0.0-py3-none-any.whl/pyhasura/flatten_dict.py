def flatten_nested_dicts(data):
    """
    Flattens an array of nested JSON dictionaries.
    :param data: List of dictionaries
    :return: List of flattened dictionaries
    """

    def flatten(d, parent_key='', sep='_'):
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten(v, new_key, sep=sep).items())
            elif isinstance(v, list):
                for i, item in enumerate(v):
                    items.extend(flatten(item, f"{new_key}{sep}{i}", sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    return [flatten(d) for d in data]


