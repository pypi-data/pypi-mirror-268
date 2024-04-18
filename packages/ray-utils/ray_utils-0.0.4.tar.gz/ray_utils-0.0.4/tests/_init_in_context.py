from ray_utils import init_in_context
def test__init_in_context():
    with init_in_context():
        print("bla")
