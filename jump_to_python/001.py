"""
정규 표현식(Regular Expressions)
- 복잡한 문자열을 처리할 때 사용하는 기법
- 파이썬만의 고유 문법이 아니라 문자열을 처리하는 모든 곳에서 사용
"""
import re

# 문제: 아래와 같이 주민등록번호를 포함하고 있는 텍스트가 있다. 텍스트에 포함된 모든 주민등록번호의 뒷자리를 *로 변경하라.
# (이름과 주민등록번호 사이의 공백 개수가 다르고, 위아래에 개행이 있다. 이런 특징들이 정제된 데이터에서도 유지되어야 한다.)
data = """
park 800905-1049118 서울
kim  700905-1059119 경기도
lee  950705-1069120 서울 마포구
"""

print(data)
print("=" * 100)

# 정규 표현식 없이 해결 하는 법
result = list()
for line in data.split("\n"):
    word_list = list()
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = f"{word[:6]}-*******"
        word_list.append(word)
    result.append(" ".join(word_list))

print("\n".join(result))
print("=" * 100)

# 정규 표현식을 사용으로 해결하는 법
# 파이썬에서는 \(백슬래시)는 이스케이프 처리를 해줘야 하여 \\ 로 표시해야 하는 이슈가 있다.
# 만약 \\ 에 대한 match 를 위해서는 \\\\ 를 입력해야 하는 사태가 벌어진다.
# 그래서 r을 문자열 앞에 붙여주는 Raw String이 나오게 된다.
# Raw String을 사용하게 되면 이스케이프 처리를 해주지 않아도 된다.
regexp = re.compile(r"(\d{6})-\d{7}")
print(regexp.sub(r"\g<1>-*******", data))
