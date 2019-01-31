def debug(function):
    def _debug(*args,**kwargs):
        result=function(*args,**kwargs)
        print(function.__name__,args,kwargs,result)
        return result
    return _debug

@debug
def say_hello():
    print('hello')

say_hello()
