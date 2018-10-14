class Operation(object):
    def __init__(self, x, y, op):
        self.x = x
        self.y = y
        self.op = op
        print("Operation %s %s %s" % (self.x, self.op, self.y))

    def operation(self):
        pass


class Add(Operation):

    def operation(self):
        return self.x + self.y


class Sub(Operation):

    def operation(self):
        return self.x - self.y


class Mul(Operation):

    def operation(self):
        return self.x * self.y


class Div(Operation):

    def operation(self):
        return self.x / self.y


def operation(x, y, op):
    opCode = {"+": Add,
              "-": Sub,
              "*": Mul,
              "/": Div}
    if op not in opCode.iterkeys():
        raise BaseException("Have not the operation: %s" % op)
    return opCode[op](x, y, op).operation()


if __name__ == '__main__':
    print operation(2, 1, "/")
    print operation(2, 1, "+")
    print operation(2, 1, "-")
    print operation(2, 1, "*")
