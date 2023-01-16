import pytest

from kubecontext_merger.utils import add_object_to_map


@pytest.mark.parametrize('map_, name_, object_, result', [
    (
            {}, 'test', {'name': 'test'}, {'test': {'name': 'test'}}
    ),
    (
            {'test': {'name': 'test'}},  # map_
            'test',
            {'name': 'test'},
            {'test': {'name': 'test'}, 'test-0': {'name': 'test'}}
    ),
    (
            {'test': {'name': 'test'}},
            'test',
            {'name': 'test'},
            {'test': {'name': 'test'}, 'test-0': {'name': 'test'}}
    )
])
def test_add_object_to_map(map_, name_, object_, result):
    add_object_to_map(map_, name_, object_)
    assert map_ == result
