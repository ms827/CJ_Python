def main():
    '''
    입력으로 제공되는 목록의 각 판매정보[가격, 판매수량]를 이용하여 총 판매금액을 계산하는 프로그램을 작성하시오. (총 판매금액 = 각 판매정보(가격 X 판매수량)의 총합)
입력1) [1500, 10], [9900, 2], [56000, 1], [19000, 5], [4500, 9]
출력1) 226300
입력2) [25300, 5], [3360, 15], [27900, 3], [18500,10], [43500,7]
출력2) 750100
    '''
    # 입력 : 판매 정보 목록 [가격, 판매수량]
    sales = [[1500, 10], [9900, 2], [56000, 1], [19000, 5], [4500, 9]]
    # sales = [[25300, 5], [3360, 15], [27900, 3], [18500,10] ,[43500,7]]

    total = 0
    for sale in sales:
        total = total + sale[0] * sale[1]
    print("-------------------------------------------------------------------------------")
    print("계산 결과 : ", total)
    print("-------------------------------------------------------------------------------")

# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
