# -*- coding: utf-8 -*-
"""EDA_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12Ik2GKWn5bGQ2K0uaiLIyLFqMw1U1ok1
"""

!pip3 install pandas_profiling --upgrade

import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('phishcoop.csv')

### To Create the Simple report quickly
profile = ProfileReport(df, title='Pandas Profiling Report', explorative=True)

profile.to_widgets()

profile.to_file("output1.html")

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats


# %matplotlib inline
plt.rcParams['figure.figsize'] = 10, 8
plt.style.use("seaborn")

#for machine learning

import statsmodels.formula.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_validate

df = pd.read_csv("phishcoop.csv")

"""# General Analysis"""

df.head()

# finrat = round((amount/price)*100,6 )
#     savings = round((income-expenses-(debt/100))/(amount/time),6 )

df.columns

df.shape

df.info()

"""## Checking missing values"""

df.isnull().any()

##########################################################################################

data = df

# area.replace(0, np.nan, inplace=True)area.replace(0, np.nan, inplace=True)

"""## Categorical Data"""

## checking if any categorical Features are there in the Dataset
categorical_data = data.select_dtypes(exclude=[np.number])
print ("There are {} categorical Columns in Dataset".format(categorical_data.shape[1]))

categorical_data.any()

from sklearn.preprocessing import LabelEncoder
model = LabelEncoder()

data.dtypes

"""Handling Missing values....

## Outlier Analysis
"""

df = data

"""Boxplot Analysis"""

sns.boxplot(y = "having_IP_Address",data=df)
plt.title("Box-Plot of income")
plt.show()

sns.boxplot(y = "HTTPS_token ",data=df)
plt.title("Box-Plot of time")
plt.show()

sns.boxplot(y = "Debt",data=df)
plt.title("Box-Plot of debt")
plt.show()

sns.boxplot(y = "Age",data=df)
plt.title("Box-Plot of age")
plt.show()

sns.boxplot(y = "Amount",data=df)
plt.title("Box-Plot of amount")
plt.show()

sns.boxplot(y = "Price",data=df)
plt.title("Box-Plot of price")
plt.show()

sns.boxplot(y = "Job",data=df)
plt.title("Box-Plot of job")
plt.show()

def outlier_capping(x):
    """A funtion to remove and replace the outliers for numerical columns"""
    x = x.clip(upper=x.quantile(0.95))
    return(x)

#outlier treatment
df = df.apply(lambda x: outlier_capping(x))

import pandas as pd
print(pd.__version__)

"""Correlation Study"""

##Correlation Matrix
df.corr()

#Visualize the correlation using seaborn heatmap
sns.heatmap(df.corr(),annot=True,fmt="0.2f",cmap="coolwarm")
plt.show()

df.shape

corr = df.corr()
sns.heatmap(corr)

## Correlation Values of all the Features with respect to Target Variable 'Status' 
## Top 10 Values
print (corr['Result'].sort_values(ascending=False)[:10], '\n')

## Last 5 Values
print (corr['Result'].sort_values(ascending=False)[-5:])

"""Histograms"""

num_bins = 10

data.hist(bins = num_bins, figsize=(20,15))
plt.savefig("Data_Histogram_Plots")
plt.show()

"""Scatterplots

Duplicates handling
"""

#drop duplicate rows 
df.drop_duplicates(subset=['having_IP_Address', 'URL_Length', 'Shortining_Service',
       'having_At_Symbol', 'double_slash_redirecting', 'Prefix_Suffix',
       'having_Sub_Domain', 'SSLfinal_State', 'Domain_registeration_length',
       'Favicon', 'port', 'HTTPS_token', 'Request_URL', 'URL_of_Anchor',
       'Links_in_tags', 'SFH', 'Submitting_to_email', 'Abnormal_URL',
       'Redirect', 'on_mouseover', 'RightClick', 'popUpWidnow', 'Iframe',
       'age_of_domain', 'DNSRecord', 'web_traffic', 'Page_Rank',
       'Google_Index', 'Links_pointing_to_page', 'Statistical_report',
       'Result'], inplace = True)

df.shape

# remove duplicate columns
_, i = np.unique(df.columns, return_index=True)
df=df.iloc[:, i]
df.shape

numerical = ['having_IP_Address', 'URL_Length', 'Shortining_Service',
       'having_At_Symbol', 'double_slash_redirecting', 'Prefix_Suffix',
       'having_Sub_Domain', 'SSLfinal_State', 'Domain_registeration_length',
       'Favicon', 'port', 'HTTPS_token', 'Request_URL', 'URL_of_Anchor',
       'Links_in_tags', 'SFH', 'Submitting_to_email', 'Abnormal_URL',
       'Redirect', 'on_mouseover', 'RightClick', 'popUpWidnow', 'Iframe',
       'age_of_domain', 'DNSRecord', 'web_traffic', 'Page_Rank',
       'Google_Index', 'Links_pointing_to_page', 'Statistical_report',
       'Result']

# Bivariate Analysis - Numeric(TTest)/ Categorical(Chisquare)
# Bivariate Analysis - Visualization
# Variable Reduction - Multicollinearity

## performing the independent t test on numerical variables
tstats_df = pd.DataFrame()

for eachvariable in numerical:
    tstats = stats.ttest_ind(df.loc[df["Result"] == -1,eachvariable],df.loc[df["Result"] == 1, eachvariable],equal_var=False)
    temp = pd.DataFrame([eachvariable, tstats[0], tstats[1]]).T
    temp.columns = ['Variable Name', 'T-Statistic', 'P-Value']
    tstats_df = pd.concat([tstats_df, temp], axis=0, ignore_index=True)
    
tstats_df =  tstats_df.sort_values(by = "P-Value").reset_index(drop = True)

tstats_df

# Bivariate Analysis
def BivariateAnalysisPlot(segment_by):
    """A funtion to analyze the impact of features on the target variable"""
    
    fig, ax = plt.subplots(ncols=1,figsize = (10,8))
    
    #boxplot
    sns.boxplot(x = 'Result', y = segment_by, data=df)
    plt.title("Box plot of "+segment_by)
    
    
    plt.show()

BivariateAnalysisPlot("Submitting_to_email")

# Multi Collinearity Check

from patsy import dmatrices
from statsmodels.stats.outliers_influence import variance_inflation_factor

features = "+".join(df.columns.difference(["Result"]))
features

#perform vif
a, b = dmatrices(formula_like= 'Status ~ ' + features,data=df,return_type="dataframe")
vif = pd.DataFrame()

vif["VIF Factor"] = [variance_inflation_factor(b.values, i) for i in range(b.shape[1])]
vif["Features"] = b.columns

vif

# boxplots to visualise outliers in the continuous variables 
# histograms to get an idea of the distribution

for var in numerical:
    plt.figure(figsize=(15,6))
    plt.subplot(1, 2, 1)
    fig = df.boxplot(column=var)
    fig.set_title('')
    fig.set_ylabel(var)
    
    plt.subplot(1, 2, 2)
    fig = df[var].hist(bins=20)
    fig.set_ylabel('number')
    fig.set_xlabel(var)

    plt.show()

# outlies in discrete variables
for var in numerical:
    (df.groupby(var)[var].count() / np.float(len(df))).plot.bar()
    plt.ylabel('Percentage of observations per label')
    plt.title(var)
    plt.show()
    #print(data[var].value_counts() / np.float(len(data)))
    print()

"""# Model"""

X = list( df.columns )
X.remove( 'Result' )
X

Y = df['Result']

X

credit_data = pd.get_dummies( df[X], drop_first = True )
len( credit_data.columns)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( df[X], Y, test_size = 0.3, random_state = 42 )

"""Smote for data imbalance"""

from imblearn.over_sampling import SMOTE
from collections import Counter

print('Original dataset shape {}'.format(Counter(y_train)))

smt = SMOTE(random_state=20)
X_train, y_train = smt.fit_sample(X_train, y_train)
print('New dataset shape {}'.format(Counter(y_train)))

from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import VarianceThreshold

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler

from sklearn import svm

from sklearn.metrics import roc_curve

### 4. Feature selection (Feature addition)

# the first step: using all the available features
# and then determine the importance of the features according
# to the algorithm

# set the seed for reproducibility
seed_val = 1000000000
np.random.seed(seed_val)

# build initial model using all the features
model_all_features = RandomForestClassifier()
model_all_features.fit(X_train, y_train)

# calculate the roc-auc in the test set
y_pred_test = model_all_features.predict_proba(X_test)[:, 1]
auc_score_all = roc_auc_score(y_test, y_pred_test)
print('Test all features RFC ROC AUC=%f' % (auc_score_all))

type(X_train)

# the second step consist of deriving the importance of 
# each feature and ranking them from the most to the least imp

# get feature name and importance
features = pd.Series(model_all_features.feature_importances_)
features.index =['having_IP_Address', 'URL_Length', 'Shortining_Service',
       'having_At_Symbol', 'double_slash_redirecting', 'Prefix_Suffix',
       'having_Sub_Domain', 'SSLfinal_State', 'Domain_registeration_length',
       'Favicon', 'port', 'HTTPS_token', 'Request_URL', 'URL_of_Anchor',
       'Links_in_tags', 'SFH', 'Submitting_to_email', 'Abnormal_URL',
       'Redirect', 'on_mouseover', 'RightClick', 'popUpWidnow', 'Iframe',
       'age_of_domain', 'DNSRecord', 'web_traffic', 'Page_Rank',
       'Google_Index', 'Links_pointing_to_page', 'Statistical_report']
       
# sort the features by importance
features.sort_values(ascending=False, inplace=True)

# plot
features.plot.bar(figsize=(20,6))

features = list(features.index)
features

# build model with only the most important feature

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( df[X], Y, test_size = 0.3, random_state = 42 ) 

# seed for reproducibility
seed_val = 1000000000
np.random.seed(seed_val)

# build initial model using all the features
model_one_feature = RandomForestClassifier()

X_train

X_train1= X_train['SFH'].to_frame()
X_train1.shape

# train using only the most important feature
model_one_feature.fit(X_train[features[0]].to_frame(), y_train)

# calculate the roc-auc in the test set
y_pred_test = model_one_feature.predict_proba(X_test[features[0]].to_frame())[:, 1]
auc_score_first = roc_auc_score(y_test, y_pred_test)
print('Test one feature xgb ROC AUC=%f' % (auc_score_first))

# add one at a time, from the most to the least
# important, and build an xgboost at each round.

# calculate the new roc-auc
# if the new roc-auc is bigger than the original one (with one feature), then we should keep it.

# if the increase is above this threshold,
# the feature will be kept
tol = 0.001

print('doing recursive feature addition')

# features we should keep
features_to_keep = [features[0]]

count = 1
for feature in features[1:]:
    print()
    print('testing feature: ', feature, ' which is feature ', count,
          ' out of ', len(features))
    count = count + 1


    model_int = RandomForestClassifier()
    # fit model 
    model_int.fit(
        X_train[features_to_keep + [feature] ], y_train)
    y_pred_test = model_int.predict_proba(
        X_test[features_to_keep + [feature] ])[:, 1]

    # new roc-auc
    auc_score_int = roc_auc_score(y_test, y_pred_test)
    print('New Test ROC AUC={}'.format((auc_score_int)))

    # print the original roc-auc with one feature
    print('All features Test ROC AUC={}'.format((auc_score_first)))

    # determine the increase in the roc-auc
    diff_auc = auc_score_int - auc_score_first

    # compare the increase in roc-auc with the tolerance
    # we set previously
    if diff_auc >= tol:
        print('Increase in ROC AUC={}'.format(diff_auc))
        print('keep: ', feature)
        print
        auc_score_first = auc_score_int
        features_to_keep.append(feature)
    else:
        print('Increase in ROC AUC={}'.format(diff_auc))
        print('remove: ', feature)
        print

print('total features to keep: ', len(features_to_keep))

features_to_keep

# capture the 8 selected features
seed_val = 1000000000
np.random.seed(seed_val)

final_xgb = RandomForestClassifier()
final_xgb.fit(X_train[features_to_keep], y_train)

y_pred_test = final_xgb.predict_proba(X_test[features_to_keep])[:, 1]
auc_score_final = roc_auc_score(y_test, y_pred_test)

print("['SFH',  'web_traffic',  'Statistical_report','SSLfinal_State',\n'Links_in_tags', 'Domain_registeration_length','popUpWidnow',\n 'Prefix_Suffix','double_slash_redirecting','URL_Length', \n'on_mouseover',   'Abnormal_URL',  'HTTPS_token', \n'having_At_Symbol', 'having_Sub_Domain',  'URL_of_Anchor']")

x = 89.26
print('Test selected features ROC AUC=%f' % (auc_score_final ))

"""Tune Hyper-parameters"""

from sklearn.model_selection import RandomizedSearchCV
n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
max_features = ['auto', 'sqrt']
max_depth = [int(x) for x in np.linspace(100, 500, num = 11)]
max_depth.append(None)
random_grid = {
 'n_estimators': n_estimators,
 'max_features': max_features,
 'max_depth': max_depth
 }
from sklearn.ensemble import RandomForestClassifier
rfc=RandomForestClassifier()
rfc_model = RandomizedSearchCV(estimator = rfc, param_distributions = random_grid, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1)

rfc_model.fit(X_train[features_to_keep], y_train)
print(rfc_model.best_params_)

seed_val = 1000

np.random.seed(seed_val)

rfc2 = RandomForestClassifier(n_estimators=600, max_depth=180, max_features='auto')
rfc2.fit(X_train[features_to_keep],y_train)
rfc2_predict = rfc2.predict_proba(X_test[features_to_keep])[:, 1]

auc_score_final2 = roc_auc_score(y_test, rfc2_predict)
print('Test selected features ROC AUC=%f' % (auc_score_final2))

print ('Model ROC AUC improvement is',(auc_score_final2-auc_score_final))

print('Test all features RFC ROC AUC=%f' % (auc_score_all))
print('Test selected features ROC AUC=%f' % (auc_score_final2))
print ('Model ROC AUC change is',(auc_score_final2-auc_score_all))

df = pd.concat([X_train.append(X_test), y_train.append(y_test)], axis = 1)

import sklearn.metrics as sklm

labels = np.array(df['Status'])
probabilities = rfc2.predict_proba(X_test[features_to_keep])

def score_model(probs, threshold):
    return np.array([1 if x > threshold else 0 for x in probs[:,1]])
scores = score_model(probabilities, 0.5)

def print_metrics(labels, scores):
    metrics = sklm.precision_recall_fscore_support(labels, scores)
    conf = sklm.confusion_matrix(labels, scores)
    print('                 Confusion matrix')
    print('                 Score positive    Score negative')
    print('Actual positive    %6d' % conf[0,0] + '             %5d' % conf[0,1])
    print('Actual negative    %6d' % conf[1,0] + '             %5d' % conf[1,1])
    print('')
    print('Accuracy  %0.2f' % sklm.accuracy_score(labels, scores))
    print(' ')
    print('           Positive      Negative')
    print('Num case   %6d' % metrics[3][0] + '        %6d' % metrics[3][1])
    print('Precision  %6.2f' % metrics[0][0] + '        %6.2f' % metrics[0][1])
    print('Recall     %6.2f' % metrics[1][0] + '        %6.2f' % metrics[1][1])
    print('F1         %6.2f' % metrics[2][0] + '        %6.2f' % metrics[2][1])
    
print_metrics(y_test, scores)

def plot_auc(labels, probs):
    fpr, tpr, threshold = sklm.roc_curve(labels, probs[:,1])
    auc = sklm.auc(fpr, tpr)
    plt.title('Receiver Operating Characteristic')
    plt.plot(fpr, tpr, color = 'orange', label = 'AUC = %0.2f' % auc)
    plt.legend(loc = 'lower right')
    plt.plot([0, 1], [0, 1],'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()
    
plot_auc(y_test, probabilities)

'''
import statsmodels.api as sm
logit = sm.Logit( y_train, sm.add_constant( X_train ) )
lg = logit.fit()

import pickle

pickle.dump(lg, open('model1.pkl','wb'))

model1=pickle.load(open('model1.pkl','rb'))

import numpy as np
import statsmodels.api as sm
# int_features = [1.0,3,3,60,26,3,0,0,35,83,0,0,1050,1156,90.83,7.42]
#int_features = [1.0,9,1,60,30,2,1,3,73,129,0,0,800,846,94.56264775,4.2] --> good aana chahiye 0.18 coming
#int_features = [1.0, 17,	1,	60,	58,	3,	1,	1,	48,	131,	0,	0,	1000,	1658, 60.31363088,	4.98] --> good aana chahiye, 0.631 coming
#int_features = [1.0,10,2,36,46,2,2,3,90,200,3000,0,2000,2985,67.00167504,1.98] --> bad aana chahiye, 0.026 coming
final_features = [int_features]
prediction = model1.predict( sm.add_constant(final_features))
#[0].predicted_prob.map( lambda x: 1 if x > 0.5 else 0)

prediction[0]
'''