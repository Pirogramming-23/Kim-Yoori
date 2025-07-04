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
#변수 num 을 이용하여, 2단계에서 입력한 수만큼 숫자를 출력하는 코드를 작성하여라.
#예를 들어, 2단계에서 playerA가 3을 입력했다면, 1,2,3을 아래와 같은 형식으로 출력하여라.
#playerA : 1
#playerA : 2
#playerA : 3
for i in range (num):
    print("playerA : %d" % (i+1))
