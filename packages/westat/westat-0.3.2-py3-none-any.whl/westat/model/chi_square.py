def chi_square(data, precision=4):
    """
        计算指定数据的信息熵
        Args:
            data: 需要计算卡方的数据频数表 DataFrame
            precision: 数据精度，小数点位数，默认为2

        Returns:
            返回计算后的卡方
    """
    import numpy as np
    import pandas as pd

    # 转换数据格式为np.array
    if isinstance(data, pd.DataFrame):
        data = np.array(data)

    # 计算边际总和
    row_totals = [sum(row) for row in data]
    col_totals = [sum(col) for col in zip(*data)]
    total = sum(row_totals)

    # 计算期望频数
    expected = [[(row_total * col_total) / total for col_total in col_totals] for row_total in row_totals]

    # 计算卡方值
    chi2 = sum((data[i][j] - expected[i][j]) ** 2 / expected[i][j] for i in range(2) for j in range(2))
    return round(chi2, precision)


