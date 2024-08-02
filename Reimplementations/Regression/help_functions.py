import numpy as np
import matplotlib.pyplot as plt

def evaluation(df, y_exact, y_predict, weights=None):
    """evaluates the model (scatter plot as qualitative
       measure, mse and expected values of predicted
       and observed target as quantitative measure)"""
    from sklearn.metrics import mean_squared_error
    if weights == None:
        weights = np.ones([y_exact.shape[0],])

    fig, ax = plt.subplots(1, 1, figsize=(24, 8));
    plt.scatter(y_predict, y_exact)
    plt.xlabel("model prediction", fontsize=24)
    plt.ylabel("observed", fontsize=24)
    plt.tick_params(axis='both', which='major', labelsize=24)
    plt.plot([y_predict.min(), y_predict.max()],
             [y_predict.min(), y_predict.max()],
             color='k', linestyle='-', linewidth=1)
    plt.title("Scatter plot", fontsize=24)
    plt.show()
    
    ew_predict = np.sum(y_predict * weights) / np.sum(weights)
    ew_exact = np.sum(y_exact * weights) / np.sum(weights)

    # MSE:
    print('MSE: ', mean_squared_error(y_exact, y_predict,
                                      sample_weight=weights), '\n')
    
    # EV:
    print('expected value of log. claims requirement (observed value): ',
          ew_exact)
    print('expected value of log. claims requirement (model value):    ',
          ew_predict, '\n')

def plot_feature_importances(feature_names, feature_importances):
    """visualization of feature importances in descent order"""
    indices = np.argsort(feature_importances)
    plt.title('Feature Importances')
    plt.barh(range(len(indices)), feature_importances[indices],
             color='b', align='center')
    plt.yticks(range(len(indices)), [feature_names[i] for i in indices],
               fontsize=8)
    plt.xticks(fontsize=8)
    plt.xlabel('Relative Importance')
    plt.show()
