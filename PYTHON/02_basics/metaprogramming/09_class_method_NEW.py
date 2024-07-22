class SomeClass:
    def __new__(cls, *args, **kwargs):
    # equals to:
    # def __new__(SomeClass, *args, **kwargs):
        instance = super().__new__(SomeClass)
        print(f'cls:\t{SomeClass}')
        # В этом месте можно настроить свой экземпляр...
        return instance
    def __init__(self, val):
        print(f'self:\t{self}')
        self.val = val


a = SomeClass(12)
