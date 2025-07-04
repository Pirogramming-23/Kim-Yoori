#1단계
num = 0

#6단계
#배스킨라빈스31 게임은 참여자가 번갈아가며 숫자를 부른다. 
#게임이 끝날 때까지 playerA와 playerB에게 번갈아가며 부를 숫자의 개수를 입력 받는 코드를 작성하여라.
# 게임은 누군가 31을 부르면 끝난다.
game_count = 1
play_turn = "playerA"

while True:
    #3단계
    while True:
        try:
            #2단계
            num = int(input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능): "))
            if num not in [1,2,3]:
                print("1,2,3 중 하나를 입력하세요")
            else:
                break
        except ValueError:
            print("정수를 입력하세요")

    #4단계
    for i in range (num):
        print("%s : %d" % (play_turn, game_count))
        game_count += 1

    if game_count > 31:
       break

    #차례 번갈아 가기
    if play_turn == "playerA":
        play_turn = "playerB"
    else:
        play_turn = "playerA"