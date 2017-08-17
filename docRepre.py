# coding=utf-8
import pandas as pd
import numpy as np
from sklearn import preprocessing, metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC,LinearSVC
from sklearn.tree import DecisionTreeClassifier
import chardet
import time




start = time.clock()
df=pd.read_excel('excel/b12.xlsx')
# t = df.stopMove.tolist()

# -------------------------------sytax_pattern-------------------------------------
# from sytax_pattern import sytax_out
# sytax = sytax_out(t)
# df['stopMove'] = sytax

# --------------------------------feature matrix generate-------------------------------

freWord = CountVectorizer(stop_words='english')
transformer = TfidfTransformer()
fre_matrix_train = freWord.fit_transform(df['stopMove'])
# freWord1 = CountVectorizer(vocabulary=freWord.vocabulary_)

tfidf_train = transformer.fit_transform(fre_matrix_train)

# feature_names = freWord.get_feature_names()
# freWordVector_df = pd.DataFrame(fre_matrix_train.toarray())

tfidf_df = pd.DataFrame(tfidf_train.toarray())
le = preprocessing.LabelEncoder()
targets_train = np.array(le.fit_transform(df['class']))
# tfidf_df1 = np.array(tfidf_df)
# def guiyi(x):
#     x[x>1]=1
#     return x
# tfidf_df = tfidf_df.apply(guiyi)



# -----------------------------------------feature selection---------------------------------------------

# tf-idf
# tfidf_sx_featuresindex = tfidf_df.sum(axis=0).sort_values(ascending=False)[:5150].index
# freWord_tfsx_df = freWordVector_df.ix[:,tfidf_sx_featuresindex] # tfidf法筛选后的词向量矩阵  
# df_columns = pd.Series(feature_names)[tfidf_sx_featuresindex]
# def guiyi(x):
#     x[x>1]=1
#     return x
# new_tfidf_df = freWord_tfsx_df.apply(guiyi)
# new_tfidf_df.columns = df_columns
# tfidf_df = []
# print new_tfidf_df.shape

# chi
# from sklearn.feature_selection import SelectPercentile,chi2
# ch2 = SelectPercentile(chi2, percentile=6)
# new_tfidf_df = ch2.fit_transform(tfidf_df,targets_train)
# tfidf_df = []
# print new_tfidf_df.shape
#MI
# from sklearn.feature_selection import SelectPercentile
# from sklearn.metrics import mutual_info_score
# mi = SelectPercentile(lambda X, Y: np.array(map(lambda x:mutual_info_score(x, Y), X.T)).T, percentile=10)
# new_tfidf_df = mi.fit_transform(tfidf_df, targets_train)
# tfidf_df = []
# print new_tfidf_df.shape

#IG
# from sklearn.feature_selection import SelectPercentile
# from feature_selection_test import information_gain
# ig = SelectPercentile(information_gain, percentile=4)
# new_tfidf_df = ig.fit_transform(tfidf_df,targets_train)
# tfidf_df = []
# print new_tfidf_df.shape

# LDA
# from sklearn.decomposition import LatentDirichletAllocation
# new_tfidf_df = LatentDirichletAllocation(n_topics=100,learning_method='batch').fit_transform(tfidf_df,targets_train)
# tfidf_df = []
# print new_tfidf_df.shape

#-----------------------------------dataset split--------------------------------
X_train, X_test, y_train, y_test = train_test_split(tfidf_df, targets_train, test_size=0.2, random_state=0)
# -----------------------------------classifier-----------------------------------
# naive byece
# clf = MultinomialNB()
# clf.fit(X_train,y_train)
# pred = clf.predict(X_test)

# knn
# knnclf = KNeighborsClassifier(n_neighbors=15)
# knnclf.fit(X_train,y_train)
# pred = knnclf.predict(X_test)

# svm
# # svclf = LinearSVC()# default with 'rbf'
# svclf = SVC(kernel='linear')
# svclf.fit(X_train,y_train)
# pred = svclf.predict(X_test)

#decisionTree
# dtclf = DecisionTreeClassifier(random_state=0)
# dtclf.fit(X_train,y_train)
# pred = dtclf.predict(X_test)

# Randomforest
# rfclf = RandomForestClassifier(n_estimators=40)
# rfclf.fit(X_train,y_train)
# pred = rfclf.predict(X_test)

#
#----------------------------------------------calculation of matrix scores------------------------------------
# def calculate_result(actual,pred):
#     m_precision = metrics.precision_score(actual,pred,average = 'macro')
#     m_recall = metrics.recall_score(actual,pred,average= 'macro')
#     print 'predict info: precision recall f1-score'
#     print '{0:.3f}'.format(m_precision)
#     print '{0:0.3f}'.format(m_recall)
#     print '{0:.3f}'.format(metrics.f1_score(actual,pred,average='macro'))
#
# calculate_result(y_test,pred)
# end = time.clock()
# #
# print end - start
