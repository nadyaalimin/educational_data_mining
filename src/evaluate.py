import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score, \
                            confusion_matrix, roc_curve, auc


def create_eval_df(y_train_proba, y_test_proba, y_train, y_test):
    eval_train = pd.DataFrame({'idx':y_train.index.values, 'actual':y_train}).reset_index(drop=True)
    eval_train['proba'] = y_train_proba[:,1]
    eval_train['type'] = 'TRAIN'
    
    eval_test = pd.DataFrame({'idx':y_test.index.values, 'actual':y_test}).reset_index(drop=True)
    eval_test['proba'] = y_test_proba[:,1]
    eval_test['type'] = 'TEST'
    
    eval_data = pd.concat([eval_train, eval_test]).reset_index(drop=True)
    eval_data.index = eval_data['idx']
    eval_data = eval_data.drop('idx', axis=1)
    
    return eval_train, eval_test, eval_data


def get_metric_score(y_actual, y_proba, cutoff, metric):
    y_pred = [1 if t>=cutoff else 0 for t in y_proba]
    if metric=='precision':
        res = precision_score(y_true=y_actual, y_pred=y_pred, pos_label=1)
    elif metric=='recall':
        res = recall_score(y_true=y_actual, y_pred=y_pred, pos_label=1)
    elif metric=='accuracy':
        res = accuracy_score(y_true=y_actual, y_pred=y_pred)
    elif metric=='f1':
        res = f1_score(y_true=y_actual, y_pred=y_pred)
    else:
        res = None
    return res


def plot_metrics_cutoff(data, label_actual='actual', label_proba='proba', 
                        list_metric=['accuracy', 'precision', 'recall', 'f1'], px=0.005, list_grade=None):
    
    cutoff = pd.Series(np.arange(0,1,px))
    eval_all = pd.DataFrame({'cutoff':cutoff})
    
    if 'accuracy' in list_metric:
        eval_all['accuracy'] = \
        cutoff.map(lambda x: get_metric_score(data[label_actual], data[label_proba], x, metric='accuracy'))
        
    if 'precision' in list_metric:
        eval_all['precision'] = \
        cutoff.map(lambda x: get_metric_score(data[label_actual], data[label_proba], x, metric='precision'))
        
    if 'recall' in list_metric:
        eval_all['recall'] = \
        cutoff.map(lambda x: get_metric_score(data[label_actual], data[label_proba], x, metric='recall'))
        
    if 'f1' in list_metric:
        eval_all['f1'] = \
        cutoff.map(lambda x: get_metric_score(data[label_actual], data[label_proba], x, metric='f1'))

    eval_all_melt = pd.melt(eval_all, id_vars='cutoff', var_name='metric_name', value_name='metric_value')

    fig,ax = plt.subplots(1)
    fig.set_size_inches(8,8)

    ax = sns.pointplot(x='cutoff', y='metric_value', data=eval_all_melt, hue='metric_name', scale=0.25)
    ax.set_ylabel('Metrics Score')
    ax.set_xlabel('Probability Cutoff')
    ax.set_xticks(np.arange(0,cutoff.shape[0]+cutoff.shape[0]/10,cutoff.shape[0]/10))
    ax.set_xticklabels(np.arange(0,cutoff.shape[0]+cutoff.shape[0]/10,cutoff.shape[0]/10)/cutoff.shape[0])
    ax.set_yticks(np.arange(0,1.1,0.1))
    ax.set_yticklabels(np.around(np.arange(0,1.1,0.1),1))
    ax.legend(title='Metrics', loc='upper right')

    if list_grade!=None:
        for gr in list_grade:
            th = list_grade[gr]
            idx = int(th * (1/px))
            ax = plt.axvline(idx, 0,100, color='black', linewidth=0.5)   
            plt.text(idx, 1.0, "{}".format(gr))
            
    ax = plt.title("Probability vs Various Metrics")
        
    return eval_all


def plot_confusion_matrix(ax, eval_df, eval_type, thr=0.5):
    data = eval_df[eval_df['type']==eval_type]
    
    predicted_label = (data['proba']>thr).astype(int)
    cm = confusion_matrix(data['actual'], predicted_label)
    
    ax.set_title('Confusion Matrix ({}), thr={}'.format(eval_type, thr))
 
    sns.heatmap(cm, annot=True, cmap='Blues', fmt='g', cbar=False, ax=ax)
    
    ax.set_xticklabels(['success', 'fail'])
    ax.set_yticklabels(['success', 'fail'])
    
    
def plot_auc_roc(ax, y_train_actual=[], y_train_proba=[], y_test_actual=[], y_test_proba=[]):
    
    if ((len(y_train_actual)>0)&(len(y_train_proba)>0)):
        fpr_train, tpr_train, _ = roc_curve(y_train_actual, y_train_proba)
        roc_auc_train = auc(fpr_train, tpr_train)
        ax.plot(fpr_train, tpr_train)
    
    if ((len(y_test_actual)>0)&(len(y_test_proba)>0)):
        fpr_test, tpr_test, _ = roc_curve(y_test_actual, y_test_proba)
        roc_auc_test = auc(fpr_test, tpr_test)
        ax.plot(fpr_test, tpr_test)
        
    ax.plot([0, 1], [0, 1], 'k--')

    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.set_xlabel('False Positive Rate')
    ax.set_ylabel('True Positive Rate')
    ax.set_title('AUC-ROC Curve')
    
    train_text = None
    test_text = None
    if ((len(y_train_actual)>0)&(len(y_train_proba)>0)):
        train_text = 'TRAIN AUC = {:.2f}'.format(roc_auc_train)
    if ((len(y_test_actual)>0)&(len(y_test_proba)>0)):
        test_text = 'TEST  AUC = {:.2f}'.format(roc_auc_test)
    leg = []
    if ((len(y_train_actual)>0)&(len(y_train_proba)>0)):
        leg.append(train_text)
    if ((len(y_test_actual)>0)&(len(y_test_proba)>0)):
        leg.append(test_text)
    ax.legend(leg)
    
    
def plot_feature_importance(model, keys, top_n=10):
    importances = model.feature_importances_
    importance_frame = pd.DataFrame({'Importance': list(importances), 'Feature': list(keys)})
    importance_frame.sort_values(by = 'Importance', ascending=True, inplace = True)
    importance_frame.tail(top_n).plot(kind = 'barh', x = 'Feature', figsize = (8,8), color = 'orange')