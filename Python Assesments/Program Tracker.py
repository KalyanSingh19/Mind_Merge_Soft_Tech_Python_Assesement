class ObjectTracker:
    def __init__(self):
        self.count = 0

    def __call__(self, cls):
        class WrappedClass(cls):
            def __new__(cls, *args, **kwargs):
                self.count += 1
                return super().__new__(cls, *args, **kwargs)

        return WrappedClass

@ObjectTracker()
class MyClass:
    pass


obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()

print("Number of objects created:", ObjectTracker().count)