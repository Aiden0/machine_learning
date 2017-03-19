import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from sklearn import mixture
import numpy as np
from sklearn import metrics

#Load Data
ref = np.ones(1000,1)
ref[1:500] = 0
#Load random feat Data
feat = np.random.random((30000,15))

#Separate features using ref vector 
feat1 = feat[np.where(ref == 1)[0]];
feat2 = feat[np.where(ref == 0)[0]];


# concatenate the two datasets into the final training set
#X_train = np.vstack([shifted_gaussian, stretched_gaussian])

gmm_NH = mixture.GaussianMixture(n_components=6, covariance_type='diag').fit(feat1)
gmm_H = mixture.GaussianMixture(n_components=6, covariance_type='diag').fit(feat2)



#Determine the monte Carlo of the KL Divergence
#KL(p||q) = \int p(x) log(p(x) / q(x)) dx = E_p[ log(p(x) / q(x))

#Produce enough random data using gaussian mix for feat1
X, _ = gmm_NH.sample(10**5)
#X=gmm_H.sample(10**5) 

#Log of feat1
log_NH_X = gmm_NH.score_samples(X)
#Log of feat2
log_H_X = gmm_H.score_samples(X)
#for JS Divergence
log_mix_X = np.logaddexp(log_NH_X, log_H_X)
#KL Divergence
test_KL = log_H_X.mean() - log_NH_X.mean()
print test_KL

#Produce enough random data using feat2 gaussian mixture
X2, _=gmm_H.sample(10**5)
#Log of No heart
log_NH_X2 = gmm_NH.score_samples(X2)
#Log of heart
log_H_X2 = gmm_H.score_samples(X2)
#for JS Divergence
log_mix_X2 = np.logaddexp(log_NH_X2, log_H_X2)
#KL Divergence
test_KL2 = log_NH_X2.mean() - log_H_X2.mean()
print test_KL2

test_JS = (log_NH_X.mean() - (log_mix_X.mean() - np.log(2)) + log_H_X2.mean() - (log_mix_X2.mean() - np.log(2))) / 2
print test_JS

#mutal info test
#Mut_test = metrics.mutual_info_score(log_NH_X,log_H_X)
#print Mut_test
#Mut_testA = metrics.adjusted_mutual_info_score(log_NH_X,log_H_X)
#Mut_test2 = metrics.mutual_info_score(log_NH_X2,log_H_X2)
#print Mut_test2
#Mut_testA2 = metrics.adjusted_mutual_info_score(log_NH_X2,log_H_X2)

#X = gmm_p.sample(n_samples)
#    log_p_X, _ = gmm_p.score_samples(X)
#    log_q_X, _ = gmm_q.score_samples(X)
#    log_mix_X = np.logaddexp(log_p_X, log_q_X)
#
#    Y = gmm_q.sample(n_samples)
#    log_p_Y, _ = gmm_p.score_samples(Y)
#    log_q_Y, _ = gmm_q.score_samples(Y)
#    log_mix_Y = np.logaddexp(log_p_Y, log_q_Y)
#
#test_JS = (log_p_X.mean() - (log_mix_X.mean() - np.log(2))
#            + log_q_Y.mean() - (log_mix_Y.mean() - np.log(2))) / 2




