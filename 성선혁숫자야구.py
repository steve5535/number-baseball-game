count=0
import random
print('''--------------------------
Level
1. 쉬움
2. 중간
3. 어려움
--------------------------''')
while True :
    
    ba_level=int(input('난이도를 선택해주세요 : '))
    if 1<=ba_level<=3:
        answer=random.sample([0,1,2,3,4,5,6,7,8,9],ba_level+2)
        if answer[0]==0:
            answer.reverse()
        break
    else:
        print('다시 입력하세요!')
while True :
    ip_an=input((f'숫자 {ba_level+2}자리를 입력해주세요 : '))
    if len(ip_an) != ba_level+2 :
        print('잘못입력함!')
        continue
    count += 1
    ip_list=[int(x) for x in ip_an]
    strike = 0
    for s in range(ba_level+2) :
        if ip_list[s]==answer[s] :
            strike += 1
    ball=len(set(ip_list)&set(answer)) - strike
    if strike == ba_level+2 :
        print(count,'번 만에 홈런')
        break
    if ball == 0 and strike == 0 :
        print('OUT')
    else :
        print('스트라이크 :',strike)
        print('볼 :',ball)