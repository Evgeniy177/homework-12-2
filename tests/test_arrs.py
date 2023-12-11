from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([1, 2, 3, 4], 5, "test") == "test"
    assert arrs.get([], 1) == None
    assert arrs.get([], -1) == None



def test_slice():
    assert arrs.my_slice([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5]) != [1, 2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4, 5], 2) == [3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], end=3) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3, 4, 5], start=-3, end=-1) == [3, 4]
    assert arrs.my_slice([1, 2, 3, 4, 5], start=2) == [3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], end=2) == [1, 2]
    assert arrs.my_slice([1, 2, 3, 4, 5], start=-3, end=-2) == [3]
    assert arrs.my_slice([1, 2, 3, 4, 5], start=-5, end=5) == [1, 2, 3, 4, 5]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1, 2, 3, 4, 5]) != []