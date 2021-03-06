# Python 3.9.5 언어 레퍼런스 읽기 2

## 문자열과 바이트열 리터럴

역 슬래시(`\`) 문자는 혼자 쓰이면 프로그래밍에서 특별한 의미를 가지는 문자들을 escape할 때 사용된다.

```python
print("\"Hello World!\"")

>>> "Hello World!"
```

### String Prefix

#### `f` format
문자열과 변수를 결합할 때, 중괄호 `{}`를 사용하여 변수를 치환할 수 있다.

다른 문자열 리터럴은 항상 상수이지만, 포맷 문자열 리터럴은 실행시간에 계산되는 표현식이다.

```python
>>> name = "John"

>>> print("Hi, My name is " + name)

Hi, My name is John

>>> print("Hi, My name is {}".format(name))

Hi, My name is John

>>> print(f"Hi, My name is {name}")

Hi, My name is John
```

포맷 문자열에는 역 슬래시, 독스트링을 사용할 수 없다.

#### `b` bytes

문자열을 `bytes` 형 인스턴스로 만들 수 있다.

```python
>>> s = "Hello World!"
>>> type(s)

<Class 'str'>

>>> list(s)

['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']

>>> b = b"Hello World!"
>>> type(b)

<Class 'bytes'>

>>> b = B"Hello World!"
>>> type(b)

<Class 'bytes'>

>>> list(b)

[72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33]
```

#### `u` unicode

unicode를 의미한다. 

#### `r` raw

escape 문자를 특별하게 다루지 않고 그대로 문자열에 포함시킨다.

```python
>>> print("Hello \nWorld!")

Hello
World!

>>> print(r"Hello \nWorld!")

Hello \nWorld!
```

### 문자열 리터럴 이어붙이기

문자열이나 바이트 리터럴은 공백으로 분리하여 여러 개를 나열하는 것이 허용되고, 이것은 공백없이 이어붙인 하나의 리터럴로 인식된다(이 기능은 **컴파일 시간에 구현**되므로 주의해야 한다).

```python
>>> x = "[A-Za-z0-9]" "[A-Za-z0-9]" 
>>> print(x)

[A-Za-z0-9][A-Za-z0-9]
```

**실행 시간에 구현**되도록 하기 위해서는 `+` 연산자를 사용하면 된다.

```python
>>> x = "[A-Za-z0-9]"+"[A-Za-z0-9]"
>>> print(x)

[A-Za-z0-9][A-Za-z0-9]
```

다음은 [2.5 연산자](https://docs.python.org/ko/3/reference/lexical_analysis.html#operators)

---
참조
* [파이썬 언어 레퍼런스](https://docs.python.org/ko/3/reference/lexical_analysis.html)