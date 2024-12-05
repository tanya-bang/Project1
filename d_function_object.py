"""
파이썬의 함수는 1급 객체이다.
1급 객체는 값으로 다룰 수 있음을 의미한다.
값으로 다룰 수 있다는 것은 변수에 할당할 수 있다는 것을 의미한다.
함수를 매개변수로 전달하거나, 반환값으로 쓸 수 있다는 뜻.
"""

def proxy_fn(fnc):
    proxy_var = '프록시함수의 지역변수 입니다.'
    call_cnt = 0
    print('프록시 함수 시작')
    fnc()
    print('프록시 함수 끝')
    
    def closure():
        nonlocal proxy_var
        nonlocal call_cnt
        call_cnt += 1
        print(proxy_var, call_cnt)
        
    return closure # closure() 라고 쓰면 함수 실행한 값을 반환하겠다는 거라 None이 반환됨
    
def target_fn():
    print('타겟함수 호출')
    
proxy_fn(target_fn)

fnc_closure = proxy_fn(target_fn)
fnc_closure()

"""
lambda : 익명함수
<lambda 매개변수:반환값>
파이썬의 lambda는 한 줄 밖에 쓸 수 없습니다.
return 키워드는 생략한다.
"""
# 함수 선언하기 귀찮을 때/너무 간단할 때 lambda처리
sum_fnc = lambda a,b: a+b
print(sum_fnc(10, 20))