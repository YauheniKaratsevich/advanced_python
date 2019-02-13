class YourMetaClass(type):
    def __init__(self, name, bases, dct):
        new_dct = {}
        for name in dct.keys():
            v = getattr(self, name)
            if name.startswith('set_'):
                t = name.replace('set_', '')
                if t not in new_dct.keys():
                    new_dct[t] = [None, None, None]
                new_dct[t][1] = v
            if name.startswith('get_'):
                t = name.replace('get_', '')
                if t not in new_dct.keys():
                    new_dct[t] = [None, None, None]
                new_dct[t][0] = v
            if name.startswith('del_'):
                t = name.replace('del_', '')
                if t not in new_dct.keys():
                    new_dct[t] = [None, None, None]
                new_dct[t][2] = v
        for name, (getter, setter, deler) in new_dct.items():
            setattr(self, name, property(getter, setter, deler, ""))


class Example(metaclass=YourMetaClass):
    def __init__(self):
        self._x = None

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return 'y'


if __name__ == "__main__":
    ex = Example()
    ex.x = 255
    print(ex.x)
    print(ex.y)
