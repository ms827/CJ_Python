
def main():
    '''
       사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.

    >> input number1: 10
	>> input number2: 9
	>> input number3: 20

      출력: 20
    '''

    number1 = input("input number1:")
    number2 = input("input number2:")
    number3 = input("input number3:")

    max_num=None
    num1=int(number1)
    num2=int(number2)
    num3=int(number3)
    ####### 구현 시작 ################
    if num1 > num2:
        max_num = num1
    else:
        max_num = num2

    if num3 > max_num:
       max_num = num3




    ########구현 끝 #######################


    print("-------------------------------------------------------------------------------")
    print(max_num)
    print("-------------------------------------------------------------------------------")
# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
