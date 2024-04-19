def poisson(mu,k):
    """
    计算泊松分布，Poisson分布 衡量某种事件在一定期间出现的数目的概率
    Args:
        mu: 事件出现数目的均值
        k: 
        
    Returns:
        泊松分布的概率结果
    """
    import math
    result = math.pow(math.e,-mu) * (math.pow(mu,k) / math.factorial(k))
    return result

def plot_poisson(mu):
    """
    计算泊松分布，Poisson分布 衡量某种事件在一定期间出现的数目的概率
    Args:
        mu: 事件出现数目的均值
        
    Returns:
        泊松分布的概率分布图
    """
    list_mu = []
    x =[]
    for i in range(0,100):
        p = poisson(mu,i)
        list_mu.append(p)
        x.append(i)
    
    import matplotlib.pyplot as plt
        
    plt.plot(x, list_mu,marker='o')
    plt.xlim(0, 20)
    plt.xticks(range(0,20,5))
    plt.title('Possion Distribution')
    plt.show()