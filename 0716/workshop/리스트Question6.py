
def main():
    '''
    입력으로 제공되는 상품정보(상품명, 가격)목록을 이용하여 상품가격이 높은 순으로 3개의 상품을 검색하는 프로그램을 작성하시오. (단, 상품가격이 같은 경우는 없다.)
입력1) [“television”, 500000], [“washer”, 890000], [“fridge”, 1200000], [“styler”, 990000], [“cleaner”, 250000]
출력1) [“fridge”, 1200000], [“styler”, 990000], [“cleaner”, 890000]
입력2) [“television”,5700000], [“washer”, 1250000], [“fridge”,1990000], [“styler”,1000000], [“cleaner”,850000]
출력2) [“television”, 5700000], [“fridge”, 1990000], [“washer”, 1250000]
    '''
    # 입력 : 상품 정보( 상품명,가격) 목록
    infomation= [ ["television", 500000], ["washer", 890000], ["fridge", 1200000], ["styler", 990000], ["cleaner", 250000]]
    # infomation = [["television", 5700000], ["washer", 1250000], ["fridge",1990000], ["styler",1000000], ["cleaner",850000]]

    top3_list = []
    top3_list = sorted(infomation, key=lambda x: x[1], reverse=True)[0:3]

    print("-------------------------------------------------------------------------------")
    print("가격이 높은 순으로 정렬된 상위 3개 상품 목록 : ", top3_list)
    print("-------------------------------------------------------------------------------")

# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
