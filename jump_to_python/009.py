# Greedy vs Non-Greedy
# Greedy(탐욕스러운)란 무엇인가.
# 다음 예제는 <html> 을 돌려주기를 기대한 예제이다.
import re

test_string01 = "<html><head><title></title></head><body></body></html>"
regexp01 = re.compile(r"<.*>")
print(regexp01.match(test_string01))

# 반복 메타 문자는 탐욕스럽기 때문에 마지막 > 을 만날 때 까지 매치시킨다.
# 그 결과 전체 문자열을 출력하게 된다.
# 이 때 사용하는 것이 non-greedy 문자인 ? 이다.
# *?, +?, ??, {m,n}? 와 같이 사용하면 가능한 한 가장 최소한의 반복을 수행한다.
regexp02 = re.compile(r"<.*?>")
print(regexp02.match(test_string01))
