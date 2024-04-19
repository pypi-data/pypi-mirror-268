import numpy as np
import pandas as pd

def get_weight(x,method='1',precision=4):
    """
    method:1 - 算术平均法，和法——取列向量的算术平均
    method:2 - 几何平均法
    method:3 - 特征值法
    """
    n = pd.DataFrame(x)

    if method ==  '1':
        for c in n.columns:
            n[c] = n[c] / n[c].sum()
        y= n.sum(axis=1)
        w = np.array( y/y.sum()).reshape(-1,1)
        w = np.round(w,precision)
        return w
    elif method == '2':
        s1 = []
        for i in range(len(n)):
            x = list(n.iloc[i,:])
            r = 1
            for j in x:
                r = r * j
            s1.append(r)
        
        s2 = []
        for j in s1:
            s2.append(np.power(j,1/len(s1)))
        
        w = np.array(s2 / sum(s2)).reshape(-1,1)
        w = np.round(w,precision)
        return w
    elif method=='3':
        eigenvalue, featurevector = np.linalg.eig(x)  # 特征值，特征向量

        y=pd.DataFrame(np.real(featurevector))
        s= y.iloc[:,0]
        w = np.array(s / sum(s)).reshape(-1,1)
        w = np.round(w,precision)
        return w


def get_lambda(x,method='1',precision=4):
    """
    method:1 - 算术平均法，和法——取列向量的算术平均
    method:2 - 和法——取列向量的算术平均
    """
    n = pd.DataFrame(x)
    w = get_weight(n)
    aw = x @ w
    n = aw / w
    result = n.sum()/len(A)
    result = round(result,precision)
    
    return result


def get_ci(x,n,precision=4):
    result = (x-n)/(n-1)
    return round(result,precision)


def get_coef(x,precision=4):
    n = pd.DataFrame(x)
    for c in n.columns:
        n[c] = n[c] / n[c].sum()
    y= n.sum(axis=1)
    w = np.array( y/y.sum()).reshape(-1,1)
    result = pd.DataFrame(w).apply(lambda x:round(x,4))
    return result

def get_ri(x):
    df_ri = pd.DataFrame(np.array([[1,2,3,4,5,6,7,8,9,10],[0,0,0.58,0.90,1.12,1.24,1.32,1.41,1.45,1.49]])).T
    df_ri.columns=['n','RI']
    result = df_ri.loc[df_ri['n']==x,'RI'].values[0]
    return result


def get_cr(x,precision=4):
    r = get_lambda(x,precision=20)
    CI=get_ci(r,len(x),precision=20)
    RI = get_ri(len(x))
    result = CI / RI
    return round(result,precision)
    