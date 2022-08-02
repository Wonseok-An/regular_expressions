# 문자열 바꾸기
import re

test_string01 = "blue socks and red shoes"

# sub 메서드
regexp01 = re.compile(r"(blue|white|red)")
# 정규 표현식에 해당하는 모든 문자열을 바꾼다.
print(regexp01.sub("colour", test_string01))
# count를 정하면 앞에서 부터 일치하는 개수만큼 문자열을 바꾼다.
print(regexp01.sub("colour", test_string01, count=1))

# subn 메서드
# sub 메서드와 동일한 기능을 하지만 반환 결과를 튜플로 돌려준다는 차이가 있다.
# 첫 번째 요소는 변경된 문자열이고, 두 번째 요소는 바꾸기가 발생한 횟수이다.
print(regexp01.subn("colour", test_string01))

# sub 메서드를 사용할 때 참조 구문 사용
# \g<그룹 이름> 을 사용하면 정규 표현식의 그룹 이름을 참조할 수 있다.
# 참조 번호를 사용해도 같은 결과이다.
regexp02 = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)-\d+-\d+)")
print(regexp02.sub(r"\g<phone> \g<name>", "park 010-1234-1234"))
print(regexp02.sub(r"\g<2> \g<1>", "park 010-1234-1234"))


# sub 메서드의 매개변수로 함수 사용
def return_hex(match):
    return hex(int(match.group()))


regexp03 = re.compile(r"\d+")
print(regexp03.sub(return_hex, "Call 65490 for printing, 49152 for user code."))
