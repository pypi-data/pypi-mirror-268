import pytest


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "properties(**kwargs): mark attach properties to a test"
    )


@pytest.fixture
def fix_properties(request):
    d = {}
    for mark in request.node.iter_markers("properties"):
        d.update(mark.kwargs) if mark.kwargs else None
    return d
