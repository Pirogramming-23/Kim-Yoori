#8단계 
#6단계까지 중복되는 코드를 찾아 함수로 만들어라. 이때, 함수 이름은 brGame으로 한다.
def brGame(turn, count):
    #1단계
    num = 0
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
        print("%s : %d" % (turn, count))
        count += 1

    return count

#6단계
game_count = 1
play_turn = "playerA"

while True:
    #3단계
    game_count = brGame(play_turn, game_count)

    #7단계
    if game_count > 31:
        if play_turn == "playerA":
           print("playerB win!")
        else:
           print("playerA win!")
        break

    #차례 번갈아 가기
    if play_turn == "playerA":
        play_turn = "playerB"
    else:
        play_turn = "playerA"