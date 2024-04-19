class Cobra:
    def __init__(self, **kwargs):
        pass
    
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __call__(self, func):
        # 입력받은 함수 또는 클래스를 그대로 반환하는 데코레이터
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    
    @staticmethod
    def block(label):
        # block 메소드가 컨텍스트 관리자로도 사용될 수 있게 Cobra 인스턴스를 반환
        return Cobra()
