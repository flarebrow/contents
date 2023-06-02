# 1. Hello, World!
print("Hello, World!")

# 2. 2つの数値の足し算
a = 10
b = 5
sum = a + b
print("Sum:", sum)

# 3. ユーザーからの入力と表示
name = input("名前を入力してください: ")
print("こんにちは、", name, "さん！")

# 4. リストの要素を表示
fruits = ["りんご", "ばなな", "オレンジ"]
for index, fruit in enumerate(fruits):
    print("Index:", index, "Fruit:", fruit)

# 5. 条件に基づくメッセージの表示
age = 18
if age >= 18:
    print("成人です。")
else:
    print("未成年です。")

# 6. 1から10までの合計の計算
total = sum(range(1, 11))
print("合計:", total)

# 7. 文字列の長さの計算
text = "Hello, World!"
length = len(text)
print("長さ:", length)

# 8. 辞書の要素を表示
person = {"名前": "太郎", "年齢": 25, "性別": "男性"}
for key, value in person.items():
    print(key + ":", value)

# 9. 関数の定義と呼び出し
def greet(name):
    print("こんにちは、", name, "さん！")

greet("太郎")

# 10. ファイルの読み込みと表示
with open("sample.txt", "r") as file:
    text = file.read()
    print(text)

# 11. 文字列の逆順表示
text = "Hello, World!"
reversed_text = text[::-1]
print("逆順表示:", reversed_text)

# 12. 列表の内包表記
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print("二乗数:", squared_numbers)

# 13. 辞書の内包表記
fruits = ["apple", "banana", "orange"]
fruit_lengths = {fruit: len(fruit) for fruit in fruits}
print("果物の長さ:", fruit_lengths)

# 14. ジェネレータ関数
def count_up(start, end):
    current = start
    while current <= end:
        yield current
        current += 1

for number in count_up(1, 5):
    print(number)

# 15. 例外処理
try:
    result = 10 / 0
except ZeroDivisionError:
    print("0で割ることはできません。")

# 16. クラスの定義とインスタンス化
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(5, 3)
print("面積:", rect.area())

# 17. モジュールのインポートと使用
import math

print("円周率:", math.pi)
print("2の平方根:", math.sqrt(2))

# 18. ファイルの書き込み
with open("output.txt", "w") as file:
    file.write("Hello, World!")

# 19. 無名関数（ラムダ関数）
double = lambda x: x * 2
print(double(5))

# 20. セットの操作
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2
print("和集合:", union_set)

intersection_set = set1 & set2
print("共通集合:", intersection_set)

difference_set = set1 - set2
print("差集合:", difference_set)

# 21. フィボナッチ数列の生成（再帰関数）
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(fibonacci(i))

# 22. クラスの継承
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "ワンワン"

class Cat(Animal):
    def speak(self):
        return "ニャー"

dog = Dog("ポチ")
print(dog.name, ":", dog.speak())

cat = Cat("タマ")
print(cat.name, ":", cat.speak())

# 23. デコレータ
def uppercase_decorator(function):
    def wrapper():
        result = function()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "hello"

print(greet())

# 24. モジュールの作成とインポート
# sample.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# main.py
import sample

sum_result = sample.add(2, 3)
print("Sum:", sum_result)

product_result = sample.multiply(4, 5)
print("Product:", product_result)

# 25. ランダムな数値の生成
import random

random_number = random.randint(1, 10)
print("ランダムな数:", random_number)

# 26. スリープ（遅延）処理
import time

print("処理を開始します。")
time.sleep(2)
print("処理が完了しました。")

# 27. JSONの読み書き
import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# JSONファイルへの書き込み
with open("data.json", "w") as file:
    json.dump(data, file)

# JSONファイルからの読み込み
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print("読み込まれたデータ:", loaded_data)

# 28. ジェネレータ式
squared_numbers = (x**2 for x in range(1, 6))
for number in squared_numbers:
    print(number)

# 29. 文字列のフォーマット
name = "Alice"
age = 25
print("私の名前は{}です。年齢は{}歳です。".format(name, age))

# 30. 正規表現の使用
import re

text = "My phone number is 123-456-7890"
pattern = r"\d{3}-\d{3}-\d{4}"
match = re.search(pattern, text)
if match:
    print("電話番号が見つかりました:", match.group())

# 31. 1から10までの偶数のリストを作成
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)

# 32. 文字列のリストから大文字の要素だけを抽出
words = ["Apple", "banana", "Cherry", "Date"]
uppercase_words = [word for word in words if word[0].isupper()]
print(uppercase_words)

# 33. 2つのリストの要素を組み合わせたタプルのリストを作成
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
combined_list = [(x, y) for x in list1 for y in list2]
print(combined_list)

# 34. 辞書の値を2倍にした辞書を作成
original_dict = {"a": 1, "b": 2, "c": 3}
doubled_dict = {key: value * 2 for key, value in original_dict.items()}
print(doubled_dict)

# 35. 文字列を逆順にしてリストに格納
text = "Hello, World!"
reversed_list = [char for char in reversed(text)]
print(reversed_list)

# 36. 2つのリストの要素をペアにしてタプルのリストを作成
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
paired_list = list(zip(list1, list2))
print(paired_list)

# 37. 複数のリストの要素を組み合わせたタプルのリストを作成
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
list3 = ["apple", "banana", "cherry"]
combined_list = list(zip(list1, list2, list3))
print(combined_list)

# 38. 辞書のキーと値を入れ替えた辞書を作成
original_dict = {"a": 1, "b": 2, "c": 3}
swapped_dict = {value: key for key, value in original_dict.items()}
print(swapped_dict)

# 39. 文字列とそのインデックスをペアにした辞書を作成
text = "Hello"
indexed_dict = {index: char for index, char in enumerate(text)}
print(indexed_dict)

# 40. 複数のリストから要素を取り出して表示
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print("Name:", name, "Age:", age)

# 41. 再帰関数を使用した階乗の計算
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print("Factorial:", result)

# 42. ファイルの単語数をカウントする
def count_words(filename):
    with open(filename, "r") as file:
        text = file.read()
        words = text.split()
        return len(words)

word_count = count_words("sample.txt")
print("Word Count:", word_count)

# 43. クラスの継承と多重継承
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "ワンワン"

class Cat(Animal):
    def speak(self):
        return "ニャー"

class DogCat(Dog, Cat):
    pass

dog_cat = DogCat()
print(dog_cat.speak())  # ワンワン

# 44. マルチスレッド処理
import threading

def print_numbers():
    for i in range(1, 6):
        print(i)

def print_letters():
    for letter in "ABCDE":
        print(letter)

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# 45. デコレータと引数を持つ関数の作成
def repeat(n):
    def decorator_function(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_function

@repeat(3)
def greet(name):
    print("Hello, ", name)

greet("Alice")

# 46. メタクラスの使用
class Meta(type):
    def __new__(cls, name, bases, attrs):
        new_attrs = {}
        for attr_name, attr_value in attrs.items():
            new_attrs[attr_name.upper()] = attr_value
        return super().__new__(cls, name, bases, new_attrs)

class MyClass(metaclass=Meta):
    name = "John"

print(MyClass.NAME)  # JOHN

# 47. コルーチンの使用
def coroutine_example():
    while True:
        x = yield
        print("Received:", x)

coroutine = coroutine_example()
next(coroutine)
coroutine.send("Hello")
coroutine.send("World")

# 48. ジェネレータの作成
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci = fibonacci_generator()
for _ in range(10):
    print(next(fibonacci))
