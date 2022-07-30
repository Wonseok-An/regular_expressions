# match 객체의 메서드
# 정규 표현식과 일치하는 문자열에 대한 정보를 담고 있고, 해당 정보를 잘 활용할 수 있게 다양한 메서드를 제공한다.

# group 메서드: 매치된 문자열을 돌려준다.
# start 메서드: 매치된 문자열의 시작 인덱스를 돌려준다.
# end 메서드: 매치된 문자열읠 끝 인덱스를 돌려준다.
# span 메서드: 매치된 문자열의 (시작 인덱스, 끝 인덱스)에 해당하는 튜플을 돌려준다.
import re

regexp = re.compile(r"[a-z]+")

test_string1 = "python"
match_result = regexp.match(test_string1)
print(f"{test_string1}| match 결과의 group: {match_result.group()}")
print(f"{test_string1}| match 결과의 start: {match_result.start()}")
print(f"{test_string1}| match 결과의 end: {match_result.end()}")
print(f"{test_string1}| match 결과의 span: {match_result.span()}")
print()

test_string2 = "3 python"
search_result = regexp.search(test_string2)
print(f"{test_string2}| search 결과의 group: {search_result.group()}")
print(f"{test_string2}| search 결과의 start: {search_result.start()}")
print(f"{test_string2}| search 결과의 end: {search_result.end()}")
print(f"{test_string2}| search 결과의 span: {search_result.span()}")
