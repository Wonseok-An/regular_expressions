# 그루핑
# ()는 그룹을 만들어 주는 메타 문자
import re

# ABC 문자열이 계속해서 반복되는지 조사하는 정규식
regexp01 = re.compile(r"(ABC)+")
match01 = regexp01.search("ABCABCABC OK?")
print(match01)
print(match01.group(0))
print()

# ====================================================================================================

test_string01 = "park 010-1234-1234"

# 이름 + " " + 전화번호 형태의 문자열을 찾는 정규 표현식
regexp02 = re.compile(r"\w+\s+\d+-\d+-\d+")
print(regexp02.search(test_string01))
print()

# 이름만 뽑아내고 싶다면 어떻게 해야 할까?
# 그룹을 사용하는 두 가지 이유는 반복되는 문자열을 찾거나 매치된 문자열 중에서 특정 부분의 문자열만 뽑아내기 위함이다.
regexp03 = re.compile(r"(\w+)\s+\d+-\d+-\d+")
match02 = regexp03.search(test_string01)
print(f"이름: {match02.group(1)}")
print()

# group(0): 매치된 전체 문자열
# group(1): 첫 번째 그룹에 해당하는 문자열
# group(2): 두 번째 그룹에 해당하는 문자열
# group(n): n 번째 그룹에 해당하는 문자열

# 전화번호 부분도 뽑아내 보자.
regexp04 = re.compile(r"(\w+)\s+(\d+-\d+-\d+)")
match03 = regexp04.search(test_string01)
print(f"이름: {match03.group(1)}")
print(f"전화번호: {match03.group(2)}")
print()

# 국번도 뽑기 위해서는 다시 그루핑을 하면 된다.
# 중첩하여 사용하면 바깥쪽부터 시작하여 안쪽으로 들어갈수록 인덱스가 증가한다.
regexp05 = re.compile(r"(\w+)\s+((\d+)-\d+-\d+)")
match04 = regexp05.search(test_string01)
print(f"이름: {match04.group(1)}")
print(f"전화번호: {match04.group(2)}")
print(f"국번: {match04.group(3)}")
print()

# 그루핑된 문자열 재참조하기
# 그루핑한 문자열을 재참조(Backreferences)할 수 있다는 점이다.
# 아래와 같이 사용하면 2개의 동일한 단어를 연속적으로 사용해야만 매치된다.
# \1은 정규 표현식의 그룹 중 첫 번째 그룹을 가리킨다. (두 번째 그룹을 참조하려면 \2을 사용하면 된다.)
regexp06 = re.compile(r"(\b\w+)\s+\1")
print(regexp06.search("Paris in the the spring").group())
print()

# 그루핑된 문자열에 이름 붙이기
# 정규 표현식 안에 그룹이 여러 개가 되거나 모든 그룹을 인덱스로 참조한다면 버그 확률이 높아진다.
# 그럴 때 그룹에 인덱스가 아닌 이름(Named Groups)으로 참조할 수 있다.
# (?P<그룹이름>...) 를 사용하여 그룹 이름을 지정할 수 있다.
regexp07 = re.compile(r"(?P<name>\w+)\s+((\d+)-\d+-\d+)")
match04 = regexp07.search(test_string01)
print(f"이름: {match04.group('name')}")
print()

# (?P=<그룹이름>)을 이용하여 재참조를 할 수 있다.
regexp08 = re.compile(r"(?P<word>\b\w+)\s+(?P=word)")
