class Decorator:
    def __new__(self,*args,**kwargs):
        self.decoree = None
        self.newargs = args
        self.newkwargs = kwargs
        if args:
            if isinstance(args[0],type):
                self.decoree = args[0]
            if callable(args[0]):
                if len(args) == 1 and len(kwargs) == 0:
                    return args[0]
            else:
                pass
        return self

    def __init__(self,*args,**kwargs):
        self.initargs = args
        self.initkwargs = kwargs
        if args and callable(args[0]):
            self.decoree = args[0]

    def __call__(self, *args, **kwargs):
        if args and callable(args[0]):
            self.decoree = args[0]
        if not callable(self.decoree):
            return self.decoree
        elif self.decoree:
            return self.decoree(*args,**kwargs)

    @staticmethod
    def create_wrapping_class(cls):
        from future.utils import with_metaclass
        class MetaNewClass(type):
            def __repr__(self):
                return repr(cls)

        class NewClass(with_metaclass(MetaNewClass,cls)):
            def __init__(self,*args,**kwargs):
                self.__instance = cls(*args,**kwargs)
            "This is the overwritten class"
            def __getattribute__(self, attr_name):
                if attr_name == "__class__":
                    return cls
                obj = super(NewClass, self).__getattribute__(attr_name)
                if hasattr(obj, '__call__'):
                    return obj
                return obj
            def __repr__(self):
                return repr(self.__instance)
        return NewClass


