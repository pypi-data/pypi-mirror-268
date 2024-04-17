import plotnine as p9
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost
from nanoCEM.cem_utils import extract_kmer_feature
from sklearn.metrics import roc_curve, auc
import numpy as np

plt.rcParams['pdf.fonttype'] = 42
results_path = 'f5c_result_rna_re'
df = pd.read_csv(results_path + '/current_feature.csv')

kmer_list = [3, 5, 7]
final_df = pd.DataFrame()

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
    fpr, tpr, thresholds = roc_curve(y_test, y_pred)

    # 计算AUC（Area Under the Curve）
    roc_auc = auc(fpr, tpr)

    # 创建DataFrame
    df_roc = pd.DataFrame({'False Positive Rate': fpr, 'True Positive Rate': tpr})
    df_roc['kmer_length'] = str(item) + '-mer: ' + str(np.round(roc_auc, 2))
    final_df = pd.concat([final_df, df_roc], axis=0)

plot = p9.ggplot(final_df, p9.aes(x='False Positive Rate', y='True Positive Rate', color='kmer_length')) \
       + p9.scale_color_manual(['#9d906d', '#00c9aa', '#9f89ac']) \
       + p9.geom_smooth(method='loess', alpha=0.3) \
       + p9.geom_abline(linetype='dashed', alpha=0.8) \
       + p9.scale_y_continuous(breaks=[0, 0.25, 0.5, 0.75, 1],limits=(0, 1.15)) \
       + p9.labs(title='ROC Curve') \
       + p9.theme_bw() \
       + p9.theme(
    figure_size=(4, 4),
    panel_grid_minor=p9.element_blank(),
    axis_text=p9.element_text(size=13),
    axis_title=p9.element_text(size=13),
    title=p9.element_text(size=13, hjust=0.5),
    legend_position='bottom',
    legend_title=p9.element_blank(),
    strip_text=p9.element_text(size=13),
    strip_background=p9.element_rect(alpha=0),
)
plot.save(filename=results_path + "/roc_curve.pdf", dpi=300)
