import plotnine as p9
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost
from nanoCEM.cem_utils import  extract_kmer_feature
from sklearn.metrics import roc_curve, auc,precision_recall_curve
import numpy as np
plt.rcParams['pdf.fonttype'] = 42
results_path='f5c_result_rna_re'
df = pd.read_csv(results_path+'/current_feature.csv')

kmer_list = [3, 5, 7]
final_df=pd.DataFrame()

for item in kmer_list:
    feature_matrix, label = extract_kmer_feature(df, item, 2030)

    label[0] = label[0].apply(lambda x: 1 if x == 'Sample' else 0)

    X = feature_matrix.values
    y = label.values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)
    model = xgboost.XGBClassifier()

    # Train the model on the training data
    model.fit(X_train, y_train)
    y_pred = model.predict_proba(X_test)[:, 1]

    # y_pred = model.predict_proba(X)[:,1]
    precision, recall, thresholds = precision_recall_curve(y_test, y_pred)
    auc_value = auc(recall, precision)

    # 创建DataFrame
    df_pr = pd.DataFrame({'Precision': precision[:-1], 'Recall': recall[:-1]})
    df_pr['kmer_length'] = str(item)+'-mer: '+ str(np.round(auc_value,2))
    final_df = pd.concat([final_df,df_pr],axis=0)

plot = p9.ggplot(final_df, p9.aes(x='Recall', y='Precision',color='kmer_length')) \
       + p9.scale_color_manual(['#9d906d','#00c9aa','#9f89ac'])\
       + p9.geom_smooth(method='loess',alpha=0.3) \
       + p9.labs(title='PR Curve') \
       + p9.theme_bw() \
       + p9.theme(
    figure_size=(4, 4),
    panel_grid_minor=p9.element_blank(),
    axis_text=p9.element_text(size=13),
    axis_title=p9.element_text(size=13),
    title=p9.element_text(size=13,hjust=0.5),
    legend_position='bottom',
    legend_title=p9.element_blank(),
    strip_text=p9.element_text(size=13),
    strip_background=p9.element_rect(alpha=0),
)
plot.save(filename=results_path + "/pr_curve.pdf", dpi=300)