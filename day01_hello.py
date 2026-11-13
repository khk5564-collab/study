# 1일차: 첫 Python 코드
# VS Code에서 이 파일을 열고 오른쪽 위 ▶ 버튼을 누르면 실행돼요.

import pandas as pd

name = "나"
goal = "마케팅·데이터 직무"
print(f"{name}의 목표: {goal}")

# 작은 마케팅 데이터 만들어 보기
data = pd.DataFrame({
    "채널": ["검색광고", "인스타그램", "유튜브", "이메일"],
    "광고비": [120, 80, 150, 20],
    "매출": [480, 200, 390, 140],
})

# ROAS(광고비 대비 매출) 계산
data["ROAS"] = data["매출"] / data["광고비"]
print(data.sort_values("ROAS", ascending=False))

# 도전 과제: 아래에 '전환수' 열을 직접 추가하고 '전환당 비용'을 계산해 보세요.
