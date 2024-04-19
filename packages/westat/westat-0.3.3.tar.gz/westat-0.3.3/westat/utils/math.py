import math


def cos(number, precision=4):
    """
    返回cos函数结果
    Args:
        number:
        precision:

    Returns:

    """
    result = round(math.cos(number), precision)
    return result


def sin(number, precision=4):
    """
    返回cos函数结果
    Args:
        number:
        precision:

    Returns:

    """
    result = round(math.sin(number), precision)
    return result


def get_bin(n,k,p,precision=4):
    """
    返回重复n次实验，每次成功概率为p，k次成功的概率
    Args:
        n:实验次数
        k:成功次数
        p:每次成功的概率
        precision:返回数据精度

    Returns:
        二项分布的概率
    """
    from math import factorial,pow
    result = factorial(n) / (factorial(k) * factorial(n-k)) * pow(p,k) * pow((1-p),(n-k))
    return result 