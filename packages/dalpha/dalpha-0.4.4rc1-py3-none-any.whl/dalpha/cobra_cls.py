class Cobra:
    def __init__(self, **kwargs):
        pass
    
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __call__(self, func):
        def decorator(cls):
            return cls
        return decorator
