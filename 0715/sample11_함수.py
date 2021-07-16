'''
    함수(function)
1.용도 : 기능처리 담당
2.종류
    가.시스템 정의 함수( built-in)
        a. __built-ins__함수? ==> 그냥사용
            len,print,input,str,int,tuple,list,dict,
            zip,divmod,chr,ord,bin,float,bool,
            (sorted, reversed)복사본 ...
        b. 문자열 함수? ==> 변수명.함수
            upper,lower,capitalize,strip,lstrip,rstrip,
            find,count,
        c. list 함수?
            insert, append, pop, remove, clear, update,
            sort, reverse,count,index
        d. tuple 함수?
            count,index
        e. set 함수?
            difference, intersection,union...
        f. dict 함수?
            keys, values, items, update ....
    나. 사용자 정의 함수
        --> 시스템이 제공하지 않는 기능이 필요한 경우 사용자가 직접 생성해서 사용한다
        문법:
            def 함수명([변수,변수2,...]): <--파라미터 변수
                문장
                [return 값]  <-- 리턴값(반환값)
        --> 함수의 종류 4가지
            가. 파라미터 변수 없고 리턴값 없는 경우
                def 함수명():
                    문장

            나.파라미터 변수 있고 리턴값 없는 경우
                def 함수명(변수1,변수2,...):
                    문장

            다.파라미터 변수 없고 리턴값 있는 경우
                def 함수명():
                    문장
                    return 값

            라.파라미터 변수 있고 리턴값 있는 경우
                def 함수명(변수1,변수2,...
                    문장
                    return 값

3. 특징
    - 반드시 호출해야 실행된다. 호출이 되어 실행된 후에는 반드시 호출한 곳으로 돌아온다.(리턴)
    - 호출할 때는 반드시 파라미터 변수와 파라미터(인자값)의 개수가 같아야 한다.
    - 로컬변수(local) : 함수안에서 선언된 변수, 함수안에서만 변수 사용 가능(함수 scope)
      전역변수(global) :함수밖에서 선언된 변수, 모든 곳에서 사용 가능
    - 함수내에서 return문이 없으면 자동으로 return None 이 추가된다.
    - return되는 값은 반드시 하나만 된다. 여러개 리턴 할려면 집합형에 저장해서 반환하면 된다.
    예) return [10,20,30]
        return 10,20,30 ==> (10,20,30)
        return {"name":"홍길동","age":"20"}
    - return의 다른 용도는 함수의 실행 중지랗 때 사용된다

    -함수호출시 파라미터(인자값) 전달할 수 있는데
    집합형(리스트) 경우 전달받은 곳에서 값을 변경하면 원본이 변경된다.
    즉, 기본적으로 얕은 복사(주소값)로 파라미터가 전달된다.

    def xxx(n)                  복사
        pass                        얕은복사
                                    깊은복사
    xxx([10,20]) //얕은복사


4. 추가 특징
    가. default 파라미터
        --> 인자값(파라미터)가 파라미터 변수 개수도 같거나 작아야 한다.
    나. packing
        --> 인자값(파라미터)가 파라미터 변수 개수보다 많은경우
'''
