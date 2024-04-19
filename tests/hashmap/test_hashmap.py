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
    hashmap.put(key, value)
    assert hashmap.get(key) == value


@pytest.mark.parametrize(
    "key, value, new_value",
    [
        (1, "test1", "test"),
        ("apple", 1, "1"),
        (1234325, "apple", "fruit"),
        ("some", 3.14, "pi"),
        (0.5, "test", "test2"),
        ((1, 2, 3), "banana", "yellow"),
        (-123, "orange", "orange 0")
    ]
)
def test_set_new_value_by_key(hashmap, key, value, new_value):
    hashmap.put(key, value)
    hashmap.put(key, new_value)

    assert hashmap.get(key) == new_value
    assert hashmap.get(key) != value


@pytest.mark.timeout(5)
def test_resize(hashmap):
    items = [(f"Element {i}", i) for i in range(1000)]
    for key, value in items:
        hashmap.put(key, value)

    for key, value in items:
        assert hashmap.get(key) == value
    assert len(hashmap) == len(items)


def test_non_hashable_key(hashmap):
    with pytest.raises(TypeError):
        hashmap.put([1, 2], "list")


def test_missing_key(hashmap):
    with pytest.raises(KeyError):
        hashmap.get("missing_key")


def test_is_custom_dict(hashmap):
    is_dict = False
    for attr in hashmap.__dict__:
        if type(hashmap.__getattribute__(attr)) == dict:
            is_dict = True
    assert (
        not is_dict
    ), f"You should implement custom dictionary"
