#1단계
num = 0

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
count = 0
for i in range (num):
    print("playerA : %d" % (i+1))
count = i + 1 #player A가 부른 마지막 숫자

#5단계
# 아래의 내용이 만족하도록 코드를 작성하여라.
# 1에서 3사이의 정수를 입력 받는 코드를 작성하여라.
# 부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :
# 정수를 입력하지 않는 경우, 정수를 입력하세요를 출력한다.
# 1,2,3을 입력하지 않는 경우, 1,2,3 중 하나를 입력하세요를 출력한다.
# 올바른 값이 입력될 때까지 입력을 요구한다.
# 변수 num을 이용하여 입력한 수만큼 숫자를 출력하는 코드를 작성하여라.
# 예를 들어, 2단계에서 playerA가 3을 입력한 상태에서, playerB가 2를 입력하면 4,5를 아래와 같은 형식으로 출력하여라.
# playerB : 4
# playerB : 5
while True:
    try:
        num = int(input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능): "))
        if num not in [1,2,3]:
            print("1,2,3 중 하나를 입력하세요")
        else:
            break
    except ValueError:
        print("정수를 입력하세요")

for i in range(num):
    print("playerB : %d" %(count+i+1))

