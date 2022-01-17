import adder

print(adder.__dir__())


def test_can_add_two_numbers():
    assert adder.add(1, 2) == 3
