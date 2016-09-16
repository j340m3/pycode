class Decorator:
    def __new__(self,*args,**kwargs):
        print("new", args, kwargs)
        self.decoree = None
        self.newargs = args
        self.newkwargs = kwargs
        if args and callable(args[0]):
            if len(args) == 1 and len(kwargs) == 0:
                return args[0]
        elif args and isinstance(args[0],type):
            self.decoree = args[0]
        return self

    def __init__(self,*args,**kwargs):
        print ("init",args,kwargs)
        self.initargs = args
        self.initkwargs = kwargs
        if args and callable(args[0]):
            self.decoree = args[0]

    def __call__(self, *args, **kwargs):
        print ("call",args,kwargs)
        if args and callable(args[0]):
            self.decoree = args[0]
            return self.decoree
        elif self.decoree:
            return self.decoree(*args,**kwargs)

