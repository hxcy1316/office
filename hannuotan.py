def hano(n, a, b, c):
    '''
    汉诺塔的递归实现
    :param n: 代表几个盘子
    :param A: 代表第一个塔
    :param B: 代表第二个塔
    :param C: 代表第三个塔
    :return:
    '''
    if n == 1:
        print(a, "--->", c)
        return None
    if n == 2:
        print(a,"--->", b)
        print(a,"--->", c)
        print(b, "--->", c)
        return None
    # 把n-1个盘子，从A塔借助C塔，挪到B塔上去
    hano(n-1, a, c, b)
    print(a, "--->", c)
    # 把n-1个盘子，从B塔借助A塔，挪到C塔上去
    hano(n-1, b, a, c)

a = "A"
b = "B"
c = "C"
n = 5

hano(n,a,b,c)

