def number_baseball_game():
    count=0 # 시도횟수
    import random
    # 난이도 선택 화면
    print('''--------------------------
Level
1. 쉬움
2. 중간
3. 어려움
--------------------------''')
    # 난이도 선택 반복문
    while True :
        ba_level=int(input('난이도를 선택해주세요 : '))
        if 1<=ba_level<=3:
            answer=random.sample([0,1,2,3,4,5,6,7,8,9],ba_level+2)
            if answer[0]==0:
                answer.reverse() # 첫 자리 0방지를 위한 순서 뒤집기
            break
        else:
            print('다시 입력하세요!') # 잘못된 값을 입력하면 반복문 다시 실행
    # 메인코드 반복문
    while True :
        ip_an=input((f'숫자 {ba_level+2}자리를 입력해주세요 : ')) # 사용자 입력
        if len(ip_an) != ba_level+2 :
            print('잘못입력함!') # 자리 수가 다르면 다시 입력
            continue
        count += 1 # 시도 횟수 증가
        ip_list=[int(x) for x in ip_an] # 문자열로 입력받은 숫자들을 리스트에 저장
        strike = 0 # 스트라이크 개수 초기화
        # 스트라이크 판별
        for s in range(ba_level+2) :
            if ip_list[s]==answer[s] :
                strike += 1
        # 볼 판별 (공통된 숫자 수 - 스트라이크 수)
        ball=len(set(ip_list)&set(answer)) - strike
        # 정답을 맞췄을 경우
        if strike == ba_level+2 :
            print(count,'번 만에 홈런') # 시도 횟수 출력 후 종료
            break
        # 아무 숫자도 안 맞았을 경우
        if ball == 0 and strike == 0 :
            print('OUT')
        else :
            print('스트라이크 :',strike)
            print('볼 :',ball)

if __name__ == "__main__":
    number_baseball_game()