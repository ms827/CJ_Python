
def main():
    '''
    List comprehension을 사용하여 입력된 리스트중에서 짝수값을 제거하고 출력하는 코드를 작성하시오.

      입력: [5,6,77,45,22,12,24]
      출력: [5, 77, 45]

    '''
    input_data = [5,6,77,45,22,12,24]
    output_data = None


    ####### 구현 시작 ################
    output_data = [a for a in input_data if a%2==1]
    ########구현 끝 #######################

    print("-------------------------------------------------------------------------------")
    print(output_data)
    print("-------------------------------------------------------------------------------")

# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
