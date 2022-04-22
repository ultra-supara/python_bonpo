word = 'python'
""" print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5]) """
print(word[:2]) #2番目までの文字を表示
print(word[2:]) #2番目から最後までの文字を表示
word = 'j' + word[1:]
print(word[:])
n = len(word)
print(n)

s = 'my name is mike'
print(s)
is_start = s.startswith('my')
print(is_start)
print(s.find('mike'))
print(s.rfind('mike'))
print(s.count('mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('mike', 'asupara'))

r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3, 3))
print(r.count(3))
if 5 in r:
    print('exist')
r.sort()
print(r)
r.sort(reverse = True)
print(r)
r.reverse()
print(r)
s = 'my name is mike'
to_split = s.split(' ')
print(to_split)
x = ' '.join(to_split)
print(x)

i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j =', j)
print('i =', i)

x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100
print('y =', y)
print('x =', x)

num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)

x, y = (10, 20)
print(x, y)

min, max = 0, 100
print(min, max)

i = 10
j = 20
tmp = i
i = j
j = tmp
print(i, j)

a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)

#3つの選択肢の中から2つを選ぶアプリを作る
chose_from_two = ('A', 'B', 'C')
#chose_from_two = ['A', 'B', 'C']
answer = []
answer.append('A')
answer.append('C')

print(chose_from_two)
print(answer)

x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y)

x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)

#オンラインサイトで果物をうる 辞書
fluits = {
    'apple': 100,
    'banana': 200,
    'orange': 300,
}
print(fluits['apple'])

#social mediaで共通の友達を探す　集合
my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_friends & A_friends)

f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)       #リストから集合に型を変換する
print(kind)

x = 10

if x < 0:
    print('nagative')
elif x == 0:
    print('zero')
elif x == 10:
    print('10')
else:
    print('positive')

a = -1
b = 1
# インデントをきっちり合わせることpythonではとても大事
if a > 0:
    print('a or b is positive')
elif b > 0:
        print('a or b is positive')
if a > 0 or b > 0:
    print('a or b is positive')

y = [1, 2, 3]
x = 1
#inは入っているかという意味
if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2
#数字の比較の際にnotを使うのはあまり好ましくない
if  a != b:
    print('not equal')

if a < b:
    print('not equal')

is_ok = [1,2,3]

if is_ok:
    print('ok')
else:
    print('No')

#isとは
is_empty = None

if is_empty is not None:#noneはemptyというオブジェクトか
    print('None')

print(1 == True)
print(1 is True)#これはダメ、オブジェクト同士が同じであるという認識をしなれば真とはならない
print(True is True)

"""  count = 0
while count < 5:
    print(count)
    count += 1  #count = count + 1 """

count = 0
while True:
    if count >= 5:
        break
    if count == 2:
        count += 1
        continue
    print(count)
    count += 1
else:
    print('done')

""" while True:
    word = input('Enter:')
    num = int(word)
    if num == 100:
        break
    print('next')
    break """

some_list = [1, 2, 3, 4, 5]
i = 0
"""  while i < len(some_list):
    print(some_list[i])
    i += 1 """
for i in some_list:#イテレーター
    print(i)
for s in 'abcde':
    print(s)
for word in ['My', 'name', 'is', 'mike']:
    if word == 'name':
        break
    print(word)

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in num_list:
    print(i)

for i in range(2, 10, 3):  #3こ飛ばしで2から10まで
    print(i)
for _ in range(10):
    print('hello')

for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)

days = ['mon', 'tue', 'wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

"""  for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])
    上と等しいコードをzip関数を使って下に書く"""

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

d = {'x': 100, 'y': 200}

for k, v in d.items():
    print(k, ':', v)

"""  def say_something():
    print('hi')

say_something()  #say_somethingは関数 """

def say_something():
    s = 'hi'
    return s

result = say_something()
print(result)

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I dont know"
result = what_is_this('red')
result = what_is_this('green')
result = what_is_this('yellow')
print(result)

def say_something():
    print('hi')

say_something()

def add_num(a: int, b: int) -> int:
    return a + b
r = add_num('a', 'b')
print(r)

"""  def menu(entree,drink,dessert):
    print(entree)
    print(drink)
    print(dessert)

menu('beef', 'beer', 'ice') """

def menu(entree,drink,dessert):
    print('entree =', entree)
    print('drink =' ,drink)
    print('dessert=' ,dessert)

menu(entree='beef', dessert='ice', drink='beer')

def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

"""y = [1, 2, 3]
r = test_func(100, y)
print(r)
"""
#pythonでは[]のリストはdefault引数で与えるべきではない
#いったん、noneを作る
r = test_func(100)
print(r)

def say_something(word, *args):
    print('word=',word)
    for arg in args:
        print(arg)
say_something('Hi','mike','nance')

""" def menu(entree='beef', drink='wine'):
    print(entree, drink)

menu(entree = 'beef', drink = 'wine') """

""" def menu(**kwargs):
    #print(kwargs)
    for k, v in kwargs.items():
        print(k,v)

d = {
    'entree': 'beef',
    'drink': 'wine'
}
menu(**d) """

def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu('banana','apple','orange',entree='beef',drink='coffee')

def example_func(param1, param2):
    print(param1)
    print(param2)
    return True

print(example_func.__doc__)

#関数内関数
def outer(a, b):
    def plus(c, d):
        return c + d

    r1 = plus(a, b)
    r2 = plus(b, a)
    print(r1 + r2)

outer(1, 2)

#クロージャーは発展のため飛ばす

#デコレーター functionに機能をつけるなど
def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_info
@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

""" def sub_num(a, b):
    return a - b

r = sub_num(10, 20)
print(r) """

f = print_info(add_num)
r = f(10, 20)
print(r)

#らむだ
l = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

def change_words(words, func):
    for word in words:
        print(func(word))

""" def sample_func(word):
    return word.capitalize()

def sample_func2(word):
    return word.lower() """

sample_func = lambda word: word.capitalize()
sample_func2 = lambda word: word.lower()
change_words(l, sample_func)

""" nampyでランダムな整数列を生成するには
import numpy as np
np.random.seed(シード値)
y = np.random.randint(整数値の下限, 整数値の上限, 整数の個数)
print(y) """

""" nampyでグラフを書くには
import matplotlib.pyplot as plt

plt.plot(x軸の配列, y軸の配列)
plt.show() """

l = ['Good morning', 'Good afternoon','Good night']

for i in l:
    print(i)

print("########################")

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

#for g in greeting:
#    print(g)

g = greeting()
print(next(g))

print("@@@@@@@")
print(next(g))
print("@@@@@@@")
print(next(g))

t = {1,2,3,4,5}
r = []
for i in t:
    r.append(i)

print(r)
#リスト内包表記する
r = [i for i in t]
print(r)

#辞書ない括表記
w = ['mon','tue','wed']
f = ['coffee','milk','water']

d = {}
for x,y in zip(w,f):
    d[x] = y

print(d)
#集合内包表記
s = set()

for i in range(10):
    if i % 2 == 0:
        s.add(i)
print(s)

s = {i for i in range(10) if i % 2 == 0}
print(s)

#ジェネレータ内包表記
def g():
    for i in range(10):
        yield i

g = g()
g = {i for i in range(10)}
print(g)

#名前空間とスコープ
animal = 'cat'
""" test test ############################################
    def f():
    #print(animal) ローカル変数を宣言前にprintで出力するのはよくない
    global animal
    animal = 'dog'
    #print('local', animal)
    print('local:',locals())

f()
print('global:',animal)
#print('global:',globals()) """

def f():
    """ Test Func doc """
    print(f.__name__)
    print(f.__doc__)
f()

#例外処理
l =[1,2,3]
i = 5

try:
    l[i]
except IndexError as ex:
    print("Don't worry: {}".format(ex))

except NameError as ex:
    print(ex)

except Exception as ex:
    print('other:{}'.format(ex))

else:
    print('done')

finally:
    print('clean up')

#独自例外の作成
class UppercaseError(Exception):
    pass

def check():
    words = ['apple','orange','banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next')

#6章 モジュールとパッケージ コマンドライン引数
import sys

print(sys.argv)
for i in sys.argv:
    print(i)

#lesson_73
import builtins
builtins.print()
ranking = {
    'A': 100,
    'B': 95,
    'C': 85,
}
print(sorted(ranking, key = ranking.get, reverse=True))

#74
""" defaultdict objectは新しいディクショナリ様のオブジェクトを返します
defaultdictは組み込みのdictのサブクラスです
メソッドをオーバーライドし書き込み可能なインスタンス変数を1つ追加している以外はdictクラスと同じです
同じ部分については以下では省略されています。
1つ目の引数はdefault_factory属性の初期値です
デフォルトはNoneです残りの引数はキーワード引数も含め、dictのコンストラクタに与えられた場合と同様に扱われます"""

s = "ertyuiolkjhgfdsxzxcv"
d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)

#d = {'f :10'}
for c in s:
    d.setdefault(c,0)
    d[c] += 1
print(d)

from collections import defaultdict
d = defaultdict(int)
for c in s:
    d[c] += 1
print(d)
#fは何個あるのかをみたい！
print(d['f'])

#sec7:objectとclassについて
#s = 'dfghjklkjhg'
#print(s.capitalize())

class Person(object):
    def __init__(self, name):
        self.name = name

    def say_something(self):
        print('I am {}. hello'.format(self.name))

person = Person('asupara')
person.say_something()

"""def person(name):
    if name == 'A':
        print('hello')"""

#コンストラクタを使うで！
class Person(object):
    def __init__(self, name):
        self.name = name

    def say_something(self):
        print('hello')
        self.run(10)

    def run(self,num):
        print('run')

    def __del__(self):
        print('good bye')

person = Person('asupara')
person.say_something()
del person

#classの継承
class Person(object):
    def __init__(self, age=1):
        self.age = age

    def drive(self):
        if self.age >= 18:
            print('ok')
        else:
            raise Exception('No drive')

class Baby(Person):
    def __init__(self, age = 1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

baby = Baby()
adult = Adult()

class Car(object):
    def __init__(self, model = None):
        self.model = model
    def run(self):
        print('run')
    def ride(self, person):
        person.drive()

car = Car()
car.ride(adult)
#ダッグタイピング

class Toyotacar(Car):
    def run(self):
        print('fast')

class Teslacar(Car):
    def __init__(self, model = 'Model S', enable_auto_run = False,):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
            self._enable_auto_run = is_enable

    def run(self):
        print('super fast')

    def auto_run(self):
        print('auto run')

"""car = Car()
car.run()
print('################')
toyota_car = Toyotacar('Lexus')
toyota_car.run.model()
print('################')"""

tesla_car = Teslacar('Model S')
tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)
#メソッドのオーバーライド, superによる親のメソッドの呼び出し--プロパティーの設定???↑

class T(object):
    pass
t = T()
t.name = 'asupara'
t.age = 20
print(t.name, t.age)


#多重継承
class Person(object):
    def talk(self):
        print('talk')

class Car (object):
    def run(self):
        print('run')

class Person_Car_Robot(Person, Car):
    def fly(self):
        print('fly')

person_car_robot = Person_Car_Robot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()

#class変数
class Person(object):

    def __init__(self, name):
        self.kind = 'human'
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)

a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()

class T(object):
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

c = T()
c.add_word('add1')
c.add_word('add2')
print(c.words)

d = T()
d.add_word('add 3')
d.add_word('add 4')
print(d.words)

#classとstatic
class Person(object):
    kind = 'human'

    def __init__(self):
        self.x = 100

    def what_is_your_kind(cls):
        return cls.kind

a = Person()
print(a.what_is_your_kind())
b = Person()
print(b.what_is_your_kind())

import string
s = """\
Hi $name.
$contents
Have a good day
"""
t = string.Template(s)
contents = t.substitute(name='asupara', contents='Ritsumeikan')
print(contents)

""" import csv

with open('test.csv', 'w') as csv_file:
    fieldnames = ['asupara','good']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name':'A','Count':1})
    writer.writerow({'Name':'B','Count':2}) """

""" import os
import pathlib
import glob
import shutil """

"""print(os.path.exists('output.txt'))
.txtfileの名前の書き換え
os.rename('output.txt', 'test.txt') """
#pathlib.Path('empty.txt').touch()
#os.remove('empty.txt').touch()
""" os.mkdir('test_dir')
os.mkdir('test_dir/testdir2')
print(os.listdir('test_dir')) """
#pathlib.Path('testdir/testdir2/empty.txt').touch()

#fileを圧縮したい。
""" import tarfile
with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('test_dir')

with tarfile.open('test.tar.gz', 'r:gz') as tr:
    withtr.extractfile('test_dir/sub_dir/sub_test.txt') """
