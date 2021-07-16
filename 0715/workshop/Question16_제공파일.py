
def main():
    '''
     다음과 같이 문자 데이터를 입력 받아서 대문자와 소문자 개수를 출력하는 코드를 작성하시오.

        입력: Hello world!
        출력: UPPER CASE: 1
            LOWER CASE: 9


    '''
    input_data = "Hello world!"
    upper_data = 0
    lower_data = 0

    ####### 구현 시작 ################
    for a in input_data:
        if a.isupper():
            upper_data += 1
        elif a.islower():
            lower_data +=1
        else:
            pass
    ########구현 끝 #######################

    print("-------------------------------------------------------------------------------")
    print("UPPER CASE:", upper_data)
    print("LOWER CASE:", lower_data)
    print("-------------------------------------------------------------------------------")

# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
