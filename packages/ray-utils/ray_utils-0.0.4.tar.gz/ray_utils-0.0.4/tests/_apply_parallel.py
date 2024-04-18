from ray_utils import apply_parallel
def test__apply_parallel_1():
    assert (
        set(apply_parallel(group_l=enumerate([1,2,3,4]), func_apply=lambda x, _: 2*x))
        ==
        set([(0, 2), (1, 4), (2, 6), (3, 8)])
    )

def test__apply_parallel_2():
    assert (
        set(apply_parallel(
            group_l=enumerate([1,2,3,4]),
            func_apply=lambda x, val_init: val_init*x,
            func_init=lambda: 3
        ))
        ==
        set([(0, 3), (1, 6), (2, 9), (3, 12)])
    )
