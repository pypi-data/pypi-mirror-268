def plot_auc(y_true,
             y_score,
             return_data: bool = False,
             precision: int = 2):
    import matplotlib.pyplot as plt
    import pandas as pd
    from sklearn.metrics import roc_curve, auc

    fpr, tpr, thresholds = roc_curve(y_true, y_score, drop_intermediate=False)
    result = pd.DataFrame([fpr, tpr, thresholds]).T
    result.columns = ['fpr', 'tpr', 'thresholds']

    roc_auc = auc(fpr, tpr)
    plt.figure(figsize=(9, 6))
    # ROC曲线
    plt.title('ROC-AUC')
    plt.plot(fpr, tpr, 'b', label='AUC = ' + str(round(roc_auc, precision)))
    plt.legend(loc='upper left', fontsize=16)
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('False positive rate', fontsize=20)
    plt.ylabel('True positive rate', fontsize=20)
    plt.show()

    if return_data:
        return result
