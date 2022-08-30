class A:
    a = 10
    b = 20

    def __init__(self):
        print("Call Constructor A")

    def add(self):
        print("Method From Class A")


class B(A):

    def __init__(self):
        super().__init__()
        print("Call Constructor B")

    def call(self):
        print("Method From Class B")
        super().add()
        print(super().a + super().b)


obj = B()
obj.call()
