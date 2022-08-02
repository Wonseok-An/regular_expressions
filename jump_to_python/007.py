# 전방 탐색(Lookahead Assertions) 확장 구문
import re

test_string01 = "https://google.com"

regexp01 = re.compile(r".+:")
match01 = regexp01.search(test_string01)
print(match01.group())
print()

# 정규 표현식과 일치하는 문자열로 https: 를 돌려주었다.
# 이 때, :을 제외하고 출력하려면 어떻게 해야 할까?
# 지금 예제는 간단하지만 훨씬 복잡한 정규 표현식이어서 그루핑은 추가할 수 없다는 조건까지 더해진다면 어떻게 해야 할까?

# 이럴 때 사용할 수 있는 것이 전방 탐색이다.
# 전방 탐색에는 긍정(Positive)와 부정(Negative)의 2종류가 있다.

# 긍정형 전방 탐색
# (?=...)
# ...에 해당하는 정규 표현식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않는다.

# 부정형 전방 탐색
# (?!...)
# ...에 해당하는 정규 표현식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않는다.

# 긍정형 전방 탐색을 사용하면 https:의 결과를 https로 바꿀 수 있다.
# 기존 정규 표현식과 검색에서는 동일한 효과를 발휘하지만
# :에 해당하는 문자열이 정규 표현식 엔진에 의해 소비되지 않아 (검색에는 포함되지만 검색 결과에는 제외됨)
# 검색 결과에서는 :이 제거된 후 돌려주는 효과가 있다.
regexp02 = re.compile(r".+(?=:)")
match02 = regexp02.search(test_string01)
print(match02.group())
print()

# 다음 정규 표현식은 파일 이름 + . + 확장자를 나타내는 정규 표현식이다. (foo.bar, autoexec.bat, sendmail.cf 등)
test_string02 = "foo.bar"
test_string03 = "autoexec.bat"
test_string04 = "sendmail.cf"

regexp03 = re.compile(r".*[.].*$")
print(regexp03.search(test_string02))
print(regexp03.search(test_string03))
print(regexp03.search(test_string04))
print("=" * 100)

# bat 파일을 제외해야 한다는 조건을 추가해 보자.
# 아래와 같이 추가를 하면 bar 확장자도 반응하지 못하는 문제가 생긴다.
regexp04 = re.compile(r".*[.][^b].*$")
print(regexp04.search(test_string02))
print(regexp04.search(test_string03))
print(regexp04.search(test_string04))
print("=" * 100)

# 첫 번째 문자가 b가 아니거나 두 번째 문자가 a가 아니거나 세 번째 문자가 t가 아닌 경우를 의미
# .cf 처럼 두 글자인 경우를 반응하지 못하는 문제가 생긴다.
regexp05 = re.compile(r".*[.]([^b]..|.[^a].|..[^t])$")
print(regexp05.search(test_string02))
print(regexp05.search(test_string03))
print(regexp05.search(test_string04))
print("=" * 100)

# 따라서 최종적으로 아래와 같이 수정하면 위 3개의 문자열에서는 정확히 동작한다.
# 그러나 exe 파일도 제외하라는 조건이 추가로 생기거나 한다면
# 모든 조건을 만족하는 정규 표현식을 구현하려면 패턴은 더 복잡해질 것이다.
regexp06 = re.compile(r".*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$")
print(regexp06.search(test_string02))
print(regexp06.search(test_string03))
print(regexp06.search(test_string04))
print("=" * 100)

# 위의 복잡한 패턴을 간단하게 만들어 주는 것이 부정형 전방 탐색이다.
# bat 이 아니라고 한다면 그 이후 정규 표현식 매치가 진행된다.
regexp07 = re.compile(r".*[.](?!bat$).*$")
print(regexp07.search(test_string02))
print(regexp07.search(test_string03))
print(regexp07.search(test_string04))
print("=" * 100)

# exe 등에 대한 추가도 부정형 전방 탐색을 이용하면 간단하게 사용 가능하다.
regexp08 = re.compile(r".*[.](?!bat$|exe$).*$")
