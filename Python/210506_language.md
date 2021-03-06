# Python 3.9.5 언어 레퍼런스 읽기 1

## 인코딩 선언

파이썬 스크립트의 첫 번째나 두 번째 줄에 있는 주석이 정규식 `coding[=:]\s*([-\w.]+)` 과 매치되면, 이 주석은 인코딩 선언으로 처리된다. 이 정규식의 첫 번째 그룹은 소스 코드 파일의 인코딩 이름을 지정한다. 인코딩 선언은 줄 전체에서 하나만 나와야 한다. 두 번째 줄이라면, 첫 번째 줄은 주석이어야 한다. 인코딩 선언의 권장 형태는 두 개이다.

```python
# -*- coding: <encoding-name> -*-
```

```python
# vim:fileencoding=<encoding-name>
```

기본 인코딩 선언이 발견되지 않으면 기본 인코딩은 UTF-8이다. 추가로 파일의 처음이 `UTF-8 BOM(b'\xef\xbb\xbf')`이면 파일 인코딩이 UTF-8로 선언된 것으로 본다.

### BOM(Byte Order Mark)란?

UTF-8은 1993년 초기에 소개되었고, 16 비트 코드를 단위로 하고 ucs-2라는 방법으로 인코딩하는 Unicode text를 전성하는 방법이다. 바이트들을 16 비트 코드 단위로 표현할 수 있는 방법은 2가지가 있는데, 가장 의미있는 바이트가 앞에 오는 **Big Endian** 방법과 가장 의미있는 바이트가 뒤에 오는 **Little Endian** 방법이다.

전송을 받은 측에서는 Unicode를 해석하기 위해 어떤 방법으로 표현되었는지 알아야 했다. 그래서 의미를 가진 텍스트 앞에 U+FEFF라는 마법의 숫자를 넣기로 한다. 이 숫자가 **BOM(Byte Order Mark)** 이다.

![UTF-8 BOM](https://www.w3.org/International/questions/images/bom.png)

## 명시적인 줄 결합

둘 이상의 물리적인 줄은 역 슬래시 문자(`\`)를 사용해서 논리적인 줄로 결합할 수 있다. 물리적인 줄이 문자열 리터럴이나 주석의 일부가 아닌 역 슬래시 문자로 끝나면, 역 슬래시와 뒤따르는 개행 문자가 제거된 채로 합쳐진다. 

```python
if 19000 < year <2100 and 1 <= month <= 12 \
    and 1 <= day <= 31 and 0 <= hour < 24 \
    and 0 <= minute < 60 and 0 <= second < 60:
        return 1
```

## 들여쓰기

논리적인 줄의 제일 앞에 오는 공백은 줄의 들여쓰기 수준을 계산하는 데 사용되고, 이것은 다시 문장들의 묶음을 결정하는 데 사용된다.

탭은 (왼쪽에서 오른쪽으로) 1~8개의 스페이스로 변환되는데, 치환된 후의 총 스페이스 문자 수가 8의 배수가 되도록 맞춘다. (유닉스에서 사용되는 규칙에 맞추려는 것이다.) 첫 번째 비 공백 문자 앞에 나오는 공백의 총 수가 들여쓰기를 결정한다. 들여쓰기는 역 슬래시를 사용하여 나눠질 수 없다.

소스 파일이 탭과 스페이스를 섞어 쓰는 경우, 탭이 몇 개의 스페이스에 해당하는 지에 따라 다르게 해석될 수 있으며 이는 `TabError`를 일으킨다.

연속된 줄의 들여쓰기 수준은 스택을 사용하여 INDENT와 DEDENT 토큰을 만드는 데 사용된다.

파일의 첫 줄을 읽기 전에 0 하나를 스택에 넣는다(push). 이 값은 다시 꺼내는(pop) 일이 없다. 스택에 넣는 값은 항상 스택의 아래에서 위로 올라갈 때 단조 증가한다. 각 논리적인 줄의 처음에서 줄의 들여쓰기 수준이 스택의 가장 위에 있는 값과 비교된다. 같다면 아무런 일도 일어나지 않고 더 크다면 그 값을 스택에 넣고 하나의 INDENT 토큰을 만든다. 더 작다면 이 값은 스택에 있는 값 중 하나여야 한다. 이 값보다 큰 모든 스택의 값들을 꺼내고(pop), 꺼낸 횟수만큼의 DEDENT 토큰을 만든다. 파일의 끝에서, 스택에 남아있는 0보다 큰 값의 개수만큼 DEDENT 토큰을 만든다.

![들여쓰기 스택]()

## 키워드

다음의 식별자들은 예약어 또는 언어의 키워드로 사용되고, 일반적인 식별자로 사용될 수 없다.

```
Flase, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
```

## 식별자와 예약 영역

### `_*`

특별한 식별자 `_`는 대화형 인터프리터에서 마지막에 실행한 결과의 값을 저장하는 용도로 사용된다. `builtins` 모듈에 저장된다. 대화형 모드가 아닐 경우 `_`는 특별한 의미가 없고 정의되지도 않는다.

### `__*__`

시스템 정의 이름. 비공식적으로 <던더(dunder=**D**ouble **UNDER**score Method)>라고 알려졌다.

### `__*`

클래스 내의 비공개 부분을 정의하는 이름. 부모 클래스와 자식 클래스의 private attribute 간의 이름 충돌을 피하기 위해서이다.


다음은 [2.4 리터럴](https://docs.python.org/ko/3/reference/lexical_analysis.html#literals)

---
참조
* [파이썬 언어 레퍼런스](https://docs.python.org/ko/3/reference/lexical_analysis.html)
* [The byte-order mark(BOM) in HTML](https://www.w3.org/International/questions/qa-byte-order-mark)
