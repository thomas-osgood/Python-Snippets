#!/usr/bin/python3

def gen_fib():
    """
    Function Name: gen_fib
    Description:
        Generate fibonacci numbers when 'next' is called.
    Input(s):
        None
    Return(s):
        fib_num - fibonacci number (generator)
    """
    back_one = 0
    back_two = 0
    iterator = 1
    fib_num = 0

    """
    While loop for generation
    """
    while True:
        if ((iterator == 1) or (iterator == 2)):
            fib_num = 1
            back_one = 1
            back_two = 1
            iterator += 1
        else:
            back_two = back_one
            back_one = fib_num
            fib_num = back_one + back_two
            iterator += 1

        yield fib_num

    return

if __name__ == "__main__":
    i = 0
    gf = gen_fib()
    for i in range(10):
        print("Fib {0} : {1}".format(i+1, next(gf)))
