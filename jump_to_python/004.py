# 컴파일 옵션
# 정규 표현식을 컴파일 할 때 사용할 수 있는 다양한 옵션이 있다.
import re

# DOTALL, S
# re.DOTALL / re.S
# 온점(.) 메타 문자는 개행(\n)를 제외한 모든 문자와 매치되는 규칙이 있다.
# 만약 온점(.)이 개행도 매치되도록 하고 싶을 때 해당 옵션을 부여한다.
regexp1 = re.compile(r"a.b")
regexp2 = re.compile(r"a.b", re.S)
test_string1 = "a\nb"
print(regexp1.match(test_string1))
print(regexp2.match(test_string1))
print()

# IGNORECASE, I
# 대소문자 구별없이 매치를 수행할 때 사용하는 옵션이다.
regexp3 = re.compile(r"[a-z]+")
regexp4 = re.compile(r"[a-z]+", re.I)
test_string2 = "Python"
test_string3 = "PYTHON"
print(regexp3.match(test_string2))
print(regexp3.match(test_string3))
print(regexp4.match(test_string2))
print(regexp4.match(test_string3))
print()

# MULTILINE, M
# 메타 문자 ^과 $에 연관된 옵션이다.
# 메타 문자 ^은 문자열의 처음을 의미하고, 메타 문자 $는 문자열의 마지막을 의미한다.
# 예를 들어 ^python 인 경우 문자열이 python으로 시작해야 하고, python$ 이라면 문자열의 마지막은 python으로 끝나야 한다.

test_string4 = """python one
life is too short
python two
you need python
python three"""

# 해당 정규 표현식은 python이라는 문자열로 시작하고 그 뒤에 whitespace, 그 뒤에 단어가 와야 한다는 의미이다.
regexp5 = re.compile(r"^python\s\w+")
print(regexp5.findall(test_string4))

# 메타 문자 ^를 문자열 전체의 처음이 아니라 각 라인의 처음으로 인식시키고 싶은 경우 MULTILINE, M을 사용하면 된다.
regexp6 = re.compile(r"^python\s\w+", re.M)
print(regexp6.findall(test_string4))
print()

# VERBOSE, X
# 연습을 위한 정규 표현식은 매우 간단하지만 복잡한 정규 표현식은 거의 암호 수준이다.
# 복잡한 정규 표현식을 줄 단위로 구분하고 주석을 달 수 있게 해주는 것이 VERBOSE, X 옵션이다.
# 해당 옵션을 사용하면 문자열에 사용된 whitespace는 컴파일할 때 제거된다.
# 단, [] 안에 사용한 whitespace는 제외한다.
regexp7 = re.compile(r"&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);")

regexp8 = re.compile(r"""
    &[#]
    (
        0[0-7]+     
        | [0-9]+   
        | x[0-9a-fA-F]+    
    )
    ;
""", re.VERBOSE)
