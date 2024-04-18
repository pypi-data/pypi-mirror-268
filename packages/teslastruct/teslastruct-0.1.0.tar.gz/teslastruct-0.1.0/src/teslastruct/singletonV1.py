class Singleton(type):
    _cls = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._cls:
            cls._cls[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._cls[cls]

