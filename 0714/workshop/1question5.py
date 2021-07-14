
def main():
    '''
     url 에 저장된 웹 페이지 주소에서 도메인을 출력하라.

    url = "http://sharebook.kr"
    url = "https://korea.co.kr"


    출력:
        kr

    '''
    url = "http://sharebook.kr"
    url = "https://korea.co.kr"

    domain = url[-2:]
    domain2 = url.rfind(".")+1
    ####### 구현 시작 ################
    print(url[domain2:])
    ########구현 끝 #######################

    print("-------------------------------------------------------------------------------")
    print(domain)
    print("-------------------------------------------------------------------------------")


# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
