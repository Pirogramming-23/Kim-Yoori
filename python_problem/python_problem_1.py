#9단계
import random

def brGame(turn, count):
    num = 0
    if turn == 'player':
        while True:
            try:
                num = int(input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능): "))
                if num not in [1,2,3]:
                    print("1,2,3 중 하나를 입력하세요")
                else:
                    break
            except ValueError:
                print("정수를 입력하세요")
    elif turn == 'computer':
        num = random.randint(1,3)

    for i in range (num):
        if count == 31:
            print("%s : %d" % (turn, count))
            return count + 1
        print("%s : %d" % (turn, count))
        count += 1

    return count

game_count = 1
play_turn = "player"

while True:
    game_count = brGame(play_turn, game_count)

    if game_count > 31:
        if play_turn == "player":
           print("computer win!")
        else:
           print("player win!")
        break

    if play_turn == "player":
        play_turn = "computer"
    else:
        play_turn = "player"