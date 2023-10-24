
class Test:

    def __init__(self, string) -> None:
        self.msg = string


    def rept(func,vz=3):
        def wrapper(self, *args, **kwargs):
            for i in range(0,vz):
                func(self, *args, **kwargs)
        return wrapper
    
    
    def reptt(func,vz=3):
        def wrapper(self):
            for i in range(0,vz):
                func(self)
        return wrapper
    
    def miau(func):
        def wrapper(self):
            print('miau~')
            func(self)
        return wrapper

    def post(func):
        def wrapper(self):
            print('-----------')
            func(self)
            print('-----------')
        return wrapper

    @post
    @miau
    @reptt
    def my_func(self):
        print(self.msg)


def main():
    var1 = Test('Oi, mundo!')
    var1.my_func()

if __name__ == '__main__':
    main()

    # Defina o decorator
    def log_args(func):
        """
        Um decorator que registra os argumentos e a chamada da função decorada.
        """
        def wrapper(*args, **kwargs):
            arg_str = ', '.join([repr(arg) for arg in args])
            kwarg_str = ', '.join([f"{key}={value!r}" for key, value in kwargs.items()])
            arguments = ', '.join(filter(None, [arg_str, kwarg_str]))
            print(f"Chamando {func.__name__}({arguments})")
            result = func(*args, **kwargs)
            return result
        return wrapper

    # Aplique o decorator a uma função
    @log_args
    def soma(a, b):
        return a + b

    # Chame a função decorada
    rso = soma(2, 3)
    print(rso)