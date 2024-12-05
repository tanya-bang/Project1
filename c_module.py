"""

"""
# 진입점인 경우 : __name__
# 진입점이 아닌 경우 : 파일명

from util.utils import calcurate_hypotenuse

print('c_module:', __name__)

def study_import():
    """
    import : 외부모듈을 사용하기 위한 키워드
    import 모듈명 : 모듈 전체를 import
    from 모듈명 import 변수 or 함수 or 클래스 : 특정 변수, 함수, 클래스 import 할 때.
    """
    print(calcurate_hypotenuse(3,4))

study_import()