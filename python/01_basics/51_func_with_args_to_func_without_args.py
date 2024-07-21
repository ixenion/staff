from functools import partial

def foo(name: str):
    print(f"Hello, {name}!")

# Создаем новую функцию, где аргумент 'name' фиксируется со значением "123"
foo_with_name_123 = partial(foo, name="123")

def some_function(callback):
    # здесь можно вызвать callback() без аргументов, так как они уже зафиксированы
    callback()

# Передаем новую функцию без аргументов
some_function(foo_with_name_123)
