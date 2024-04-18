import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.svm import SVC
import joblib
import torch
from . import saxi_nets
from .saxi_dataset import SaxiIcoDataset_fs_test
from .saxi_transforms import UnitSurfTransform
from torch.utils.data import DataLoader
from torch import nn
from tqdm import tqdm
import os

#Read the data
df = pd.read_csv('/CMF/data/floda/tool_qc_data.csv')
df.head()

#Split into input and target
X = df.drop(columns = ["subject", "fsqc_qc"])
y = df["fsqc_qc"]

#Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y) #70%/30%

X_test_saved = X_test.copy()

####################################################### FIRST MODEL : Logistic Regression ###################################################################

log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train, y_train)
print('Logistic Regression: {}'.format(log_reg.score(X_test, y_test)))

########################################################### SECOND MODEL : KNN model #######################################################################

#Create new a knn model
knn = KNeighborsClassifier()
#Create a dictionary of all values we want to test for n_neighbors
params_knn = {'n_neighbors': np.arange(1, 25)}
#Use gridsearch to test all values for n_neighbors
knn_gs = GridSearchCV(knn, params_knn, cv=5)
#Fit model to training data
knn_gs.fit(X_train, y_train)
print('KNN: {}'.format(knn_gs.best_score_))

######################################################## THIRD MODEL : Random Forest #######################################################################

#Create new random forest
rf = RandomForestClassifier()
params_rf = {'n_estimators': [50, 100, 200]}
rf_gs = GridSearchCV(rf, params_rf, cv=5)
rf_gs.fit(X_train, y_train)
rf_best = rf_gs.best_estimator_
print('Random forest: {}'.format(rf_best.score(X_test, y_test)))

############################################################# FOURTH MODEL : SVC #######################################################################

svc = SVC()
params_svc = {'C': [0.1, 1, 10], 'gamma': ['scale', 'auto']}
svc_gs = GridSearchCV(svc, params_svc, cv=5)
svc_gs.fit(X_train, y_train)
svc_best = svc_gs.best_estimator_
print('SVC: {}'.format(svc_best.score(X_test, y_test)))

################################################################## CUSTOM MODEL #######################################################################

def SaxiIcoClassification_fs_predict(df):
    device = "cuda:1"
    SAXINETS = getattr(saxi_nets, "SaxiIcoClassification_fs")
    model = SAXINETS.load_from_checkpoint('/CMF/data/floda/data_files_CT/train/fold4/epoch=6-val_loss=0.52.ckpt')
    model.to(torch.device(device))
    model.eval()
    test_ds = SaxiIcoDataset_fs_test(df,transform=UnitSurfTransform(),name_class="fsqc_qc",freesurfer_path="/CMF/data/floda/abcd_filtered")
    test_loader = DataLoader(test_ds, batch_size=1, num_workers=6, pin_memory=True)

    with torch.no_grad():
        # The prediction is performed on the test data
        probs = []
        predictions = []
        softmax = nn.Softmax(dim=1)

        for idx, batch in tqdm(enumerate(test_loader), total=len(test_loader)):
            # The generated CAM is processed and added to the input surface mesh (surf) as a point data array
            VL, FL, VFL, FFL, VR, FR, VFR, FFR, Y = batch 
            VL = VL.cuda(non_blocking=True,device=device)
            FL = FL.cuda(non_blocking=True,device=device)
            VFL = VFL.cuda(non_blocking=True,device=device)
            FFL = FFL.cuda(non_blocking=True,device=device)
            VR = VR.cuda(non_blocking=True,device=device)
            FR = FR.cuda(non_blocking=True,device=device)
            VFR = VFR.cuda(non_blocking=True,device=device)
            FFR = FFR.cuda(non_blocking=True,device=device)
            FFL = FFL.squeeze(0)
            FFR = FFR.squeeze(0)

            X = (VL, FL, VFL, FFL, VR, FR, VFR, FFR)
            x = model(X)

            x = softmax(x).detach()
            probs.append(x)
            predictions.append(torch.argmax(x, dim=1, keepdim=True))

        probs = torch.cat(probs).detach().cpu().numpy()
        predictions = torch.cat(predictions).cpu().numpy().squeeze()

        fname = "tool_qc_data.csv"
        out_dir = "/CMF/data/floda"
        df['pred'] = predictions
        out_name = os.path.join(out_dir, fname.replace(".csv", "_prediction.csv"))
        df.to_csv(out_name, index=False)

        return predictions

# custom_predictions = SaxiIcoClassification_fs_predict(df)

SAXINETS = getattr(saxi_nets, "SaxiIcoClassification_fs")
model = SAXINETS.load_from_checkpoint('/CMF/data/floda/data_files_CT/train/fold4/epoch=6-val_loss=0.52.ckpt')

# #########################################################################  VOTING CLASSIFIER  ##################################################################################################

voting_clf = VotingClassifier(estimators=[('rf', rf), ('svc', svc), ('knn', knn), ('log_reg', log_reg), ('custom', model)], voting='hard')
voting_clf.fit(X_train, y_train)
y_pred = voting_clf.predict(X_test)

conf_matrix = confusion_matrix(y_test, y_pred)
conf_matrix_normalized = conf_matrix.astype('float') / conf_matrix.sum(axis=1)[:, np.newaxis]

plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.title('Confusion Matrix')
plt.savefig('/CMF/data/floda/confusion_ensemble4.png')

plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix_normalized, annot=True, fmt='.2f', cmap='Blues', cbar=False)
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.title('Confusion Norm Matrix')
plt.savefig('/CMF/data/floda/confusion_norm_ensemble4.png')






