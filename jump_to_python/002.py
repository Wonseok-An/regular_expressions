# 파이썬에서 정규 표현식을 사용하는 방법
# 파이썬에서 정규 표현식을 사용하기 위해서는 re 모듈을 제공
import re

# compile 메서드
# 정규 표현식을 컴파일하여 작업을 수행할 수 있게 해준다. (re.Pattern 인스턴스 반환)
# 예시에서 사용한 정규 표현식은 소문자 알파벳에 대한 검사이다.
regexp = re.compile(r"[a-z]+")

test_string1 = "python"
test_string2 = "python 3"
test_string3 = "3 python"
test_string4 = "Life is too short"

# match 메서드
# 문자열의 처음부터 정규 표현식과 매치되는지 조사
# 매치될 때는 match 객체를 돌려주고, 매치되지 않을 때는 None을 돌려준다.
print(f"{test_string1}| match 결과: {regexp.match(test_string1)}")
print(f"{test_string2}| match 결과: {regexp.match(test_string2)}")
print(f"{test_string3}| match 결과: {regexp.match(test_string3)}")
print(f"{test_string4}| match 결과: {regexp.match(test_string4)}")
print()

# search 메서드
# 문자열 전체를 검색하여 정규 표현식과 매치되는지 조사
# 매치될 때는 match 객체를 돌려주고, 매치되지 않을 때는 None을 돌려준다.
print(f"{test_string1}| search 결과: {regexp.search(test_string1)}")
print(f"{test_string2}| search 결과: {regexp.search(test_string2)}")
print(f"{test_string3}| search 결과: {regexp.search(test_string3)}")
print(f"{test_string4}| search 결과: {regexp.search(test_string4)}")
print()

# findall
# 정규 표현식과 매치되는 모든 문자열을 리스트로 돌려준다.
print(f"{test_string1}| findall 결과: {regexp.findall(test_string1)}")
print(f"{test_string2}| findall 결과: {regexp.findall(test_string2)}")
print(f"{test_string3}| findall 결과: {regexp.findall(test_string3)}")
print(f"{test_string4}| findall 결과: {regexp.findall(test_string4)}")
print()

# finditer
# 정규 표현식과 매치되는 모든 문자열을 match 객체로 만들어 리스트로 돌려준다.
print(f"{test_string1}| finditer 결과: {regexp.finditer(test_string1)}")
print(f"{test_string2}| finditer 결과: {regexp.finditer(test_string2)}")
print(f"{test_string3}| finditer 결과: {regexp.finditer(test_string3)}")
print(f"{test_string4}| finditer 결과: {[match for match in regexp.finditer(test_string4)]}")
print()

# TIP. 정규 표현식을 꼭 컴파일하지 않아도 사용이 가능하다.
# 그러나 보통 같은 정규 표현식을 여러 번 사용할 땐 re.compile을 사용하는 것이 좋다.
print(f"{test_string1}| search 결과: {re.search(r'[a-z]+', test_string1)}")
print(f"{test_string2}| search 결과: {re.search(r'[a-z]+', test_string2)}")
print(f"{test_string3}| search 결과: {re.search(r'[a-z]+', test_string3)}")
print(f"{test_string4}| search 결과: {re.search(r'[a-z]+', test_string4)}")
print()
