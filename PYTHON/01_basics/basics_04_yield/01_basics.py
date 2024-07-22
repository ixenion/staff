# YIELD
# tutorial
# https://habr.com/ru/post/132554/

# Для понимания, что делает yield, необходимо понимать, что такое генераторы.
# Генераторам же предшествуют итераторы. Когда вы создаёте список,
# вы можете считывать его элементы один за другим — это называется итерацией:

# ITERATORS

mylist = [1, 2, 3]
for i in mylist :
    print(i)

# Mylist является итерируемым объектом.
# Когда вы создаёте список, используя генераторное выражение,
# вы создаёте также итератор:

mylist = [x*x for x in range(3)]
for i in mylist :
    print(i)

# Всё, к чему можно применить конструкцию «for… in...»,
# является итерируемым объектом: списки, строки, файлы…
# Это удобно, потому что можно считывать из них значения сколько потребуется
# oднако все значения хранятся в памяти, а это не всегда желательно,
# если у вас много значений.

# GENERATORS

# Генераторы это тоже итерируемые объекты, но прочитать их можно лишь один раз.
# Это связано с тем, что они не хранят значения в памяти, а генерируют их на лету:

mygenerator = (x*x for x in range(3))
for i in mygenerator :
    print(i)

# Всё то же самое, разве что используются круглые скобки вместо квадратных.
# НО: нельзя применить конструкцию for i in mygenerator второй раз,
# так как генератор может быть использован только единожды: он вычисляет 0,
# потом забывает про него и вычисляет 1, завершаяя вычислением 4 — одно за другим.
print('generator sercond call')
for i in mygenerator :
    print(i)
# No error, but no output at all

# Yield
# Yield это ключевое слово, которое используется примерно как return
# отличие в том, что функция вернёт генератор.
def createGenerator() :
    mylist = range(3)
    for i in mylist :
        yield i*i

mygenerator = createGenerator() # создаём генератор
print(mygenerator) # mygenerator является объектом!
# <generator object createGenerator at 0xb7555c34>
print('yield first "for"')
for i in mygenerator:
    print(i)
print('yield second "for"')
for i in mygenerator:
    print(i)
# again nothing on second call
# but if call function again
mygenerator = createGenerator() # создаём генератор
print('yield third "for"')
for i in mygenerator:
    print(i)
