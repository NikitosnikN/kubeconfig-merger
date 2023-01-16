import typing as t

import yaml

KUBECONTEXT_TYPE = t.Dict[str, t.Any]


def save_kubecontext(filename: str, data: KUBECONTEXT_TYPE) -> None:
    with open(filename, 'w') as f:
        yaml.safe_dump(data, f)

    return None


def load_kubecontext(filename: str) -> KUBECONTEXT_TYPE:
    with open(filename, 'r') as f:
        data = yaml.safe_load(f)

    return data


def add_object_to_map(map_: t.Dict, name: str, object_: t.Dict[str, t.Any]) -> None:
    temp_name = name
    counter = 0
    while temp_name in map_.keys():
        temp_name = name + f'-{counter}'
        counter += 1

    map_[temp_name] = object_
    return None


def merge_users(contexts_data: t.List[KUBECONTEXT_TYPE]) -> t.List[t.Dict[str, t.Any]]:
    list_ = []

    for context in contexts_data:
        users = context.get('users', [])

        for user in users:
            list_.append(user)

    return list_


def merge_clusters(contexts_data: t.List[KUBECONTEXT_TYPE]) -> t.List[t.Dict[str, t.Any]]:
    list_ = []

    for context in contexts_data:
        clusters = context.get('clusters', [])

        for cluster in clusters:
            list_.append(cluster)

    return list_


def merge_contexts(contexts_data: t.List[KUBECONTEXT_TYPE]) -> t.List[t.Dict[str, t.Any]]:
    list_ = []

    for data in contexts_data:
        contexts = data.get('contexts', [])

        for context in contexts:
            list_.append(context)

    return list_


def build_kubecontext(contexts_data: t.List[KUBECONTEXT_TYPE]) -> KUBECONTEXT_TYPE:
    contexts = merge_contexts(contexts_data)
    return {
        'apiVersion': 'v1',
        'kind': 'Config',
        'preferences': {},
        'clusters': merge_clusters(contexts_data),
        'contexts': contexts,
        'users': merge_users(contexts_data),
        'current-context': contexts[0]['name'] if contexts else '',
    }
