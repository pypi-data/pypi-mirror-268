import ray
from . import init_in_context
# ===
@ray.remote
class ActorGeneric:
    """
    Generic ray actor that runs a function on a group_object that has an associated group_id
    Parameters:
    - func_apply - same as apply_parallel(..., func_apply, ...)
    - func_init  - same as apply_parallel(..., func_init , ...)
    """
    def __init__(self, func_apply, func_init):
        self.func_apply = func_apply
        self.val_init = None if func_init is None else func_init()
    def apply(self, group_id, group_object):
        return (group_id, self.func_apply(group_object, self.val_init))

from ray.util.actor_pool import ActorPool
import multiprocessing as mp
def apply_parallel(group_l, func_apply, init_kwargs=dict(), func_init=None, n_jobs=None):
    """
    Runs a function in parallel
    Parameters:
    group_l - iterable of tuples of 2 elements: group_id, group_object
    func_apply - callable with signature like "lambda group_object, val_init: ..."
                 where val_init is None or the return value of func_init
    func_init - None or callable with signature like "lambda: ..."
    """
    def _apply_remote(a, v):
        assert type(a)==ray.actor.ActorHandle, type(a)
        assert type(v)==tuple, type(v)
        assert len(v)==2, len(v)
        group_id, group_object = v
        return a.apply.remote(group_id, group_object)
    # Note: the generic "ActorGeneric" class uses 1 cpu per actor for simplicity
    n_jobs = n_jobs or (
        min(mp.cpu_count(), len(group_l)) if type(group_l)==list else
        mp.cpu_count()
    )
    assert n_jobs >= 1, n_jobs
    with init_in_context(**init_kwargs):
        pool = ActorPool([ActorGeneric.remote(func_apply=func_apply, func_init=func_init) for i in range(n_jobs)])
        generator = pool.map_unordered(_apply_remote, group_l)
        for group_id, group_object in generator:
            yield (group_id, group_object)
