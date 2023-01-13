# 파이썬으로 웹 요청 보낼 수 있는 라이브러리 불러오기

# 동행복권 로또 당첨 번호 api 사용하기
# (회차 직접 입력)
# 입력받은 회차에 해당하는 당첨번호 확인하기 -> 6개 (보너스번호 제외)

# (선택사항) - 보너스 번호 확인하기

import requests
import random

# turn = input('원하는 회차를 입력해주세요')
# response = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={turn}').json()
numbers = list(range(1,7))

# for no in numbers:
#     print(response[f'drwtNo{no}'])

# print(response[f'drwtNo1'])


# 4. 이걸 1000번 반복한다.
# 1. 로또 번호 6개를 추첨받는다.
# 2. 내가 추첨 받은 6개의 번호가 1049회차 당첨 번호와 일치 하는지 확인한다.
    # 2-1. 확인하는 방법은 내 번호 6개를 순회하면서
        # 1049회 당첨번호 목록에 해당 숫자가 있는지
        # 있다면 적중 횟수 + 1
# 그래서 적중 횟수가 6개면 1등
    # 5개면 3등
    # 4개면 4등
    # 3개면 5등
    # 2개 이하면 꽝을 출력한다.




lotto_num = list(range(1, 46))

lotto_1049 = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1049').json()
origin = []
for no in numbers:
    origin.append(lotto_1049[f'drwtNo{no}'])


count_list = {
    "!!1등!!" : 0,
    "2등" : 0,
    "3등" : 0,
    "4등" : 0,
    "5등" : 0,
    "꽝" : 0
}

for i in range(1000):
    lotto = random.sample(lotto_num, 6)
    cnt = 0
    for lot in lotto:
        if lot in origin:
            cnt += 1
    if cnt == 6:
        count_list["!!1등!!"] = count_list["!!1등!!"] + 1
    elif cnt == 5:
        count_list["3등"] = count_list["3등"] + 1
    elif cnt == 4:
        count_list["4등"] = count_list["4등"] + 1
    elif cnt == 3:
        count_list["5등"] = count_list["5등"] + 1 
    else:
        count_list["꽝"] = count_list["꽝"] + 1
               
print(count_list)
    

