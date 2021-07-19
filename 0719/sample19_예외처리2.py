'''
    예외처리( exception handling)

    1. 예외 ( exception) ?
      --> 일반적으로 '에러' 라고 부른다
      --> 실행중에 발생되는 '문제발생'
      --> 예외가 발생되면 프로그램이 '비정상종료' 된다.
        예> 화면이 멈추거나...

    2. 예외처리(exception handling)?
        --> 프로그램 실행중에 어쩔수 없이 발생된 예외를
            '비정상종료'하도록 두지 않고
            '정상종료' 하도록 유도하는 작업을 의미한다.

    3. 예외처리 방법
        가. 예외클래스 사용( 시스템에서 제공 )
            -> 예외클래스도 상속관계로 되어 있다.

            -SyntaxError: 문법오류
            -ZeroDivisionError: 0으로 나누었을 때 발생
            -IndexError: 인덱스 범위가 넘어갔을때
            -KeyError: dict에서 key값 없을 때
            -FileNotFoundError: 파일이 없을 때
            -XXXError
        나. try ~ except 문장
            try:
                문장1(실행하고자 하는 문장)
                문장2(실행하고자 하는 문장)
                ...
            except 예외클래스 as 별칭
                문장(예외가 발생했을 때 예외처리문장) --> 사용자가 실행하고자 했던 작업이 실패한 이유를 알려주는것이다.
        ==> except에 지정하는 아무 클래스 사용하지 못하고 예외처리를 담당할 수 있는 적합한 예외클래스로 지정해야 한다.
            단, 상속관계 구조로 봤을 때 부모 예외클래스는 사용할 수 있다.
        ==> Exception은 XXXError 예외클래스들의 최상위 예외클래스로 간주되어 처리된다.
            except Exception as e:  어떤경우든 처리 가능
                pass
        ==> e 변수에는 실행중에 발생된 예외정보를 가지고 있다.
            print(e)
'''
print("1")

try:
    num = 0
    result = 10 / num
    print("결과값: ",result)
except ZeroDivisionError as e:
    print("0으로 나누어 예외발생",e) # division by zero
print("end(정상종료)")

print(ZeroDivisionError.mro())
