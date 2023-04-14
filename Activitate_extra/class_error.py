class Value_Too_High_Err(Exception):  # we assign exception to the class param
    pass


class Value_Too_Small_Err(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise Value_Too_High_Err('Value is too high')
    if x < 5:
        raise Value_Too_Small_Err('Value is too small', x)


try:
    test_value(1)
except Value_Too_High_Err as e:
    print(e)
except Value_Too_Small_Err as e:
    print(e.message, e.value)
