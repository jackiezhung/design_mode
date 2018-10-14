from abc import ABCMeta, abstractmethod


class Operation(object):

    def operation(self, x, y):
        pass


class Add(Operation):

    def operation(self, x, y):
        return x + y


class Sub(Operation):

    def operation(self, x, y):
        return x - y


class Mul(Operation):

    def operation(self, x, y):
        return x * y


class Div(Operation):

    def operation(self, x, y):
        return x / y


class Factory:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_operation(self):
        pass


class AddFactory(Factory):

    def create_operation(self):
        return Add()


class SubFactory(Factory):

    def create_operation(self):
        return Sub()


class MulFactory(Factory):

    def create_operation(self):
        return Mul()


class DivFactory(Factory):

    def create_operation(self):
        return Sub()


if __name__ == '__main__':
    add = AddFactory().create_operation().operation
    sub = SubFactory().create_operation().operation
    mul = MulFactory().create_operation().operation
    div = DivFactory().create_operation().operation

    print add(2, 1)
    print sub(2, 1)
    print mul(2, 1)
    print div(2, 1)
