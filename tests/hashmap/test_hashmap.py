import pytest


@pytest.mark.parametrize(
    "key, value",
    [
        ("test1", "test1"),
        (1, "1"),
        ("apple", "fruit"),
        (3.14, "pi"),
        ("test2", "test2"),
        ("banana", "yellow"),
        ("orange", "orange")
    ]
)
def test_setitem_getitem(hashmap, key, value):
    hashmap[key] = value
    assert hashmap[key] == value


@pytest.mark.parametrize(
    "value, new_value",
    [
        ("test1", "test1"),
        (1, "1"),
        ("apple", "fruit"),
        (3.14, "pi"),
        ("test", "test2"),
        ("banana", "yellow"),
        ("orange", "orange 0")
    ]
)
def test_set_new_value_by_key(hashmap, value, new_value):
    hashmap["key"] = value
    hashmap["key"] = new_value
    assert hashmap["key"] == new_value


def test_resize(hashmap):
    for i in range(24):
        hashmap[i] = str(i)

    for i in range(24):
        assert hashmap[i] == str(i)


def test_non_hashable_key(hashmap):
    with pytest.raises(TypeError):
        hashmap[[1, 2]] = "list"
