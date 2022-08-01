# 정규 표현식 메타 문자
import re

# 문자 클래스 (Character class)
# []
# 의미: [] 사이의 문자들과 매치
# 예시 1. [abc] => a, b, c 중 한 개의 문자와 매치
regexp01 = re.compile(r"[abc]")
print(regexp01.match("a"))
print(regexp01.match("before"))
print(regexp01.match("dude"))
print()
# [] 안의 두 문자 사이에 하이픈(-)을 사용하면 두 문자 사이의 범위(From-To)를 의미
# 예를 들어 [a-c]는 [abc]와 동일하고, [0-5]는 [012345]와 동일
# [] 안에 ^ 메타 문자를 사용할 경우에는 not(반대)라는 의미
# 예를 들어 [^0-9]라는 정규 표현식은 숫자가 아닌 문자만 매치

r"""
자주 사용하는 문자 클래스는 정규 표현식에서 별도의 표기법으로 표현할 수 있다.

\d => 숫자와 매치, [0-9]
\D => 숫자가 아닌 것과 매치, [^0-9]
\s => whitespace 문자(space나 tab처럼 공백을 표현하는 문자)와 매치, [ \t\n\r\f\v]
\S => whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]
\w => 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식
\W => 문자+숫자(alphanumeric)와 매치, [^a-zA-Z0-9_]와 동일한 표현식
"""

# \w의 정규 표현식의 의미는 [a-zA-Z0-9_]와 동일하다.
# 하지만 Python의 re 모듈에서는 다른 의미를 가진다.
regexp02_string = r"[a-zA-Z0-9_]+"
regexp03_string = r"\w+"
regexp02 = re.compile(regexp02_string)
regexp03 = re.compile(regexp03_string)

test_string01 = "안녕하세요"
test_string02 = "Hello"
test_string03 = "おはようございます"

print(f"{test_string01} 에 대한 {regexp02_string} match 결과: {regexp02.match(test_string01)}")
print(f"{test_string02} 에 대한 {regexp02_string} match 결과: {regexp02.match(test_string02)}")
print(f"{test_string03} 에 대한 {regexp02_string} match 결과: {regexp02.match(test_string03)}")
print("=" * 100)
print(f"{test_string01} 에 대한 {regexp03_string} match 결과: {regexp03.match(test_string01)}")
print(f"{test_string02} 에 대한 {regexp03_string} match 결과: {regexp03.match(test_string02)}")
print(f"{test_string03} 에 대한 {regexp03_string} match 결과: {regexp03.match(test_string03)}")
print("=" * 100)

# 다른 결과를 보이는 이유는 Python의 re 모듈에서 다르게 구현했기 때문이다.
# Python의 re 모듈에서는 \w가 유니코드에 반응하도록 되어 있다.
# 만약 정규 표현식에서의 \w의 의미로 사용하기 위해서는 re.ASCII(re.A) 옵션을 넣어야 한다.
regexp04 = re.compile(regexp03_string, re.A)
print(f"{test_string01} 에 대한 옵션을 부여한 {regexp03_string} match 결과: {regexp04.match(test_string01)}")
print(f"{test_string02} 에 대한 옵션을 부여한 {regexp03_string} match 결과: {regexp04.match(test_string02)}")
print(f"{test_string03} 에 대한 옵션을 부여한 {regexp03_string} match 결과: {regexp04.match(test_string03)}")
print()

# ====================================================================================================

# Dot (.)
# 정규 표현식의 Dot(.) 메타 문자는 줄바꿈 문자인 \n을 제외한 모든 문자와 매치
# []에서 Dot(.)을 사용하게 되면 메타 문자가 아니라 문자 그대로 사용된다.
# 예를 들어 a.b 라고 하면 "a와 b 사이에 줄바꿈 문자를 제외한 어떤 문자가 들어가도 모두 매치" 라는 의미
regexp05 = re.compile(r"a.b")
print(regexp05.match("aab"))
print(regexp05.match("a\nb"))
print(regexp05.match("abc"))
print()

# ====================================================================================================

# 반복(*)
# * 문자 바로 앞에 있는 문자가 0번 이상 반복되면 매치 (0 or many)
# 예를 들어 ca*t 라고 하면 "c와 t 사이에 a가 0번 이상 들어가는 문자와 매치" 라는 의미
regexp06 = re.compile(r"ca*t")
print(regexp06.match("ct"))
print(regexp06.match("cat"))
print(regexp06.match("caaaat"))
print()

# ====================================================================================================

# 반복(+)
# + 문자 바로 앞에 있는 문자가 1번 이상 반복되면 매치 (1 or many)
# 예를 들어 ca+t 라고 하면 "c와 t 사이에 a가 1번 이상 들어가는 문자와 매치" 라는 의미
regexp07 = re.compile(r"ca+t")
print(regexp07.match("ct"))
print(regexp07.match("cat"))
print(regexp07.match("caaaat"))
print()

# ====================================================================================================

# ?
# ? 문자 바로 앞에 있는 문자가 0 or 1 일 때 매치 (0 or 1)
# 예를 들어 ca?t 라고 하면 "c와 t 사이에 a가 없거나 1개 일 때 문자와 매치" 라는 의미
regexp08 = re.compile(r"ca?t")
print(regexp08.match("ct"))
print(regexp08.match("cat"))
print(regexp08.match("caaaat"))
print()

# ====================================================================================================

# {m,n} 반복
# 반복 횟수를 m 회만 또는 m회부터 n회까지만 제한하고 싶을 때 사용한다.
# 예를 들어 {2}이라면 2회만, {2,}이라면 2회 이상, {2,4}이라면 2회 이상 4회 이하, {,4}이라면 4회 이하 를 의미한다.
regexp09_string = r"ca{2}t"
regexp10_string = r"ca{2,}t"
regexp11_string = r"ca{2,4}t"
regexp12_string = r"ca{,4}t"

regexp09 = re.compile(regexp09_string)
regexp10 = re.compile(regexp10_string)
regexp11 = re.compile(regexp11_string)
regexp12 = re.compile(regexp12_string)


def print_mn_example(regexp_string, regexp):
    test_strings = [
        "cat",
        "caat",
        "caaat",
        "caaaat",
        "caaaaat"
    ]
    for test_string in test_strings:
        print(f"{regexp_string}으로 {test_string} match 결과: {regexp.match(test_string)}")
    print("=" * 100)


print_mn_example(regexp09_string, regexp09)
print_mn_example(regexp10_string, regexp10)
print_mn_example(regexp11_string, regexp11)
print_mn_example(regexp12_string, regexp12)
print()

# ====================================================================================================

# |
# | 메타 문자는 or와 동일한 의미
# A|B라는 정규 표현식이 있다면 A 또는 B라는 의미
regexp13 = re.compile(r"dog|cat")
print(regexp13.search("cute dog"))
print(regexp13.search("cute cat"))
print(regexp13.search("cute cow"))
print()

# ====================================================================================================

# ^ 와 $
# ^ 메타 문자는 문자열의 맨 처음과 일치함을 의미
# $ 메타 문자는 문자열의 맨 마지막과 일치함을 의미
regexp14 = re.compile(r"^Beautiful")
regexp15 = re.compile(r"implicit$")

test_string04 = "Beautiful is better than ugly"
test_string05 = "Explicit is better than implicit"

print(regexp14.search(test_string04))
print(regexp14.search(test_string05))
print("=" * 100)
print(regexp15.search(test_string04))
print(regexp15.search(test_string05))
print()

# ====================================================================================================

# \A 와 \Z
# \A는 문자열의 맨 처음과 일치함을 의미
# \Z는 문자열의 맨 끝과 일치함을 의미
# 둘 다 각각 ^ 메타 문자와 $ 메타 문자와 같은 의미를 갖고 있지만 re.MULTILINE 옵션을 사용할 경우 차이가 있다.
# re.MULTILINE 옵션을 사용할 경우 ^ 메타 문자와 $ 메타 문자는 개행으로 구분된 각 줄에 매치되지만
# \A와 \Z은 옵션과 무관하게 전체 문자열에 매치된다.

# ====================================================================================================

# \b 와 \B
# \b는 단어 구분자(Word boundary)이다. 보통 단어는 whitespace에 의해 구분
# \B는 \b 메타 문자와 반대의 경우. whitespace로 구분된 단어가 아닌 경우에만 매치
regexp16 = re.compile(r"\bclass\b")
regexp17 = re.compile(r"\Bclass\B")

test_string06 = "no class at all"
test_string07 = "the declassified algorithm"

print(regexp16.search(test_string06))
print(regexp16.search(test_string07))
print("=" * 100)
print(regexp17.search(test_string06))
print(regexp17.search(test_string07))
print()
