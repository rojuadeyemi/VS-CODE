from sklearn.datasets import load_breast_cancer, load_digits, load_iris
import numpy as np, pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

#Wine Classification

#Load the Data
data = pd.read_csv("/storage/emulated/0/UCDownloads/winequalityN.csv")

#Encode the label variables
coded = {i+3:i for i in range(7)}
data.replace({"type":{"white":0,"red":1},"quality":coded}, inplace =True)

#drop the na values
data = data.dropna()

#Standardize the data
scaler = StandardScaler()
X= scaler.fit_transform(data.drop("type",axis=1))

#split the data into training and test set 
X_train, X_test, y_train, y_test =train_test_split(X,data.type, test_size = 0.3, random_state = 24)

#Do data features reduction
pca_class = PCA(2)

#fit PCA on train data alone 
pca_class.fit(X_train)

# transform both 
pca_train = pca_class.transform(X_train)
pca_test = pca_class.transform(X_test)

#print("Explained Variation PC {}".format(pca_class.explained_variance_ratio_))

#fit model for pca_transformed and untransform data
model = LogisticRegression(solver = 'lbfgs')
model.fit(pca_train, y_train)

#Predict the outcome
predict_label = model.predict(pca_test)

#confusion matrix 	
#print(metrics.confusion_matrix(y_test, predict_label))

#Model Accuracy 
#print(model.score(pca_test, y_test))

# Example 2: Using Python dummy data
dat = load_breast_cancer()

#reshape the vector of target data into n by 1 matrix
label = np.reshape(dat.target, (-1,1))

#normalize the X matrix
X = scaler.fit_transform(dat.data) 

#Initialize the PCA with 2 components 
pca_class = PCA(2)
pca = pca_class.fit_transform(X)

# Variance(i)/sum(Variance)
print("Explained Variation per PC {}".format(pca_class.explained_variance_ratio_))

#Put the result in a DataFrame
result = pd.DataFrame(pca, columns=["PC1","PC2"])

#Plot the components against each other
targets = [0, 1]
colors = ['r', 'g']

for target, color in zip(targets,colors):
    indicesToKeep = label == target
    plt.scatter(result.loc[indicesToKeep, 'PC1'], result.loc[indicesToKeep, 'PC2'], c = color, s = 50)

plt.legend(["Benign", "Malignant"],prop={'size': 15})
plt.xticks(fontsize=12)
plt.yticks(fontsize=14)
plt.xlabel('Principal Component - 1', fontsize=20)
plt.ylabel('Principal Component - 2',fontsize=20)
plt.title("Principal Component Analysis of Breast Cancer Dataset",fontsize=15) 
plt.show() 

#EXAMPLE 3
#digits = load_digits()
#scaler = StandardScaler()
#data = scaler.fit_transform(digits.data)

#x_train, x_test, y_train, y_test = train_test_split(data, digits.target, test_size=0.3)

#pca = PCA(2)
#projected= pca.fit_transform(x_train)

#Explained Variance
#print(pca.explained_variance_ratio_)

#plt.scatter(projected[:, 0], projected[:, 1], c = digits.target, edgecolor='none', alpha=0.5,cmap=plt.cm.get_cmap('gnuplot', 10))
#plt.xlabel('component 1')
#plt.ylabel('component 2')
#plt.colorbar()
#plt.show()


#XAMPLE 3

iris = load_iris()

x1 = scaler.fit_transform(iris.data) 

y1 = iris.target

pca = PCA(2)

PC = pca.fit_transform(x1)
finalDf = pd.DataFrame(PC)

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)
targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['r', 'g', 'b']
for targe, color in zip(targets,colors):
    indicesToKeep = iris.target == targe
    ax.scatter(finalDf.loc[indicesToKeep, 'PC11'], finalDf.loc[indicesToKeep, 'PC2']
               , c = color
              , s = 50)
ax.legend(targets)
ax.grid()
#plt.show()

