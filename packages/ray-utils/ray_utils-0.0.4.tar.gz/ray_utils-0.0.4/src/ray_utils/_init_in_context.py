import ray
# ===
from contextlib import contextmanager
@contextmanager
def init_in_context(*args, **kwargs):
    """
    Instead of "ray.init(); ...; ray.shutdown()" whereby a "ray.shutdown()" could be forgotten or fail to be reached due to exceptions,
    wrap it in a context that always runs a shutdown after init.
    Example:
    with init_in_context(...):
        ...
        
    References:
    https://docs.ray.io/en/latest/ray-core/api/doc/ray.init.html
    https://github.com/ray-project/ray/blob/0da087b39a62dfae1a68fa595d7c2d79d1697da4/python/ray/_private/worker.py#L1214
    """
    try:
        print("ray.init(...)")
        ray.init(*args, **kwargs)
        yield
    finally:
        print("ray.shutdown()")
        ray.shutdown()
# ===
def test__init_in_context():
    with init_in_context():
        print("bla")
