import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.gaussian_process.kernels import RBF
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
import warnings
warnings.simplefilter('ignore') #
#modification
def knn_model(X_train=None, X_test=None, y_train=None, y_test=None, suggested_data=False, test_size=0.25, random_state=1):
    """
    Train and evaluate the K Nearest Neighbors classifier.

    Args:
        X_train (numpy array): Training data features.
        X_test (numpy array): Testing data features.
        y_train (numpy array): Training data labels.
        y_test (numpy array): Testing data labels.
        suggested_data (bool): Whether to use the suggested dataset or not.
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): Seed used by the random number generator.

    Returns:
        str: Classification report containing precision, recall, F1-score, and support metrics.
            The report provides information about the model's performance on the test data.
            If data loading or formatting fails, None is returned.
    """    
    if suggested_data:
        X_train, X_test, y_train, y_test = load_dataset(suggested_data=True, test_size=test_size, random_state=random_state)

    if X_train is None or X_test is None or y_train is None or y_test is None:
        print("Data loading failed.")
        return None

    if len(X_train.shape) != 2 or len(X_test.shape) != 2 or len(y_train.shape) != 1 or len(y_test.shape) != 1:
        print("The provided data does not have the appropriate format.")
        return None
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report = print(classification_report(y_test, y_pred))
    return report
    
def gaussian_process_model(X_train=None, X_test=None, y_train=None, y_test=None, suggested_data=False, test_size=0.25, random_state=1):
    """
    Train and evaluate the Gaussian Process classifier.

    Args:
        X_train (numpy array): Training data features.
        X_test (numpy array): Testing data features.
        y_train (numpy array): Training data labels.
        y_test (numpy array): Testing data labels.
        suggested_data (bool): Whether to use the suggested dataset or not.
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): Seed used by the random number generator.

    Returns:
        str: Classification report containing precision, recall, F1-score, and support metrics.
            The report provides information about the model's performance on the test data.
            If data loading or formatting fails, None is returned.
    """
    if suggested_data:
        X_train, X_test, y_train, y_test = load_dataset(suggested_data=True, test_size=test_size, random_state=random_state)

    if X_train is None or X_test is None or y_train is None or y_test is None:
        print("Data loading failed.")
        return None

    if len(X_train.shape) != 2 or len(X_test.shape) != 2 or len(y_train.shape) != 1 or len(y_test.shape) != 1:
        print("The provided data does not have the appropriate format.")
        return None
    kernel = 1.0 * RBF(1.0)
    model = GaussianProcessClassifier(kernel)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report = print(classification_report(y_test, y_pred))
    return report
    
def decision_tree_model(X_train=None, X_test=None, y_train=None, y_test=None, suggested_data=False, test_size=0.25, random_state=1):
    """
    Train and evaluate the Decision Tree classifier.

    Args:
        X_train (numpy array): Training data features.
        X_test (numpy array): Testing data features.
        y_train (numpy array): Training data labels.
        y_test (numpy array): Testing data labels.
        suggested_data (bool): Whether to use the suggested dataset or not.
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): Seed used by the random number generator.

    Returns:
        str: Classification report containing precision, recall, F1-score, and support metrics.
            The report provides information about the model's performance on the test data.
            If data loading or formatting fails, None is returned.
    """
    if suggested_data:
        X_train, X_test, y_train, y_test = load_dataset(suggested_data=True, test_size=test_size, random_state=random_state)

    if X_train is None or X_test is None or y_train is None or y_test is None:
        print("Data loading failed.")
        return None

    if len(X_train.shape) != 2 or len(X_test.shape) != 2 or len(y_train.shape) != 1 or len(y_test.shape) != 1:
        print("The provided data does not have the appropriate format.")
        return None
    model = DecisionTreeClassifier(max_depth=5)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report = print(classification_report(y_test, y_pred))
    return report
    
def random_forest_model(X_train=None, X_test=None, y_train=None, y_test=None, suggested_data=False, test_size=0.25, random_state=1):
    """
    Train and evaluate the Random Forest classifier.

    Args:
        X_train (numpy array): Training data features.
        X_test (numpy array): Testing data features.
        y_train (numpy array): Training data labels.
        y_test (numpy array): Testing data labels.
        suggested_data (bool): Whether to use the suggested dataset or not.
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): Seed used by the random number generator.

    Returns:
        str: Classification report containing precision, recall, F1-score, and support metrics.
            The report provides information about the model's performance on the test data.
            If data loading or formatting fails, None is returned.
    """
    if suggested_data:
        X_train, X_test, y_train, y_test = load_dataset(suggested_data=True, test_size=test_size, random_state=random_state)

    if X_train is None or X_test is None or y_train is None or y_test is None:
        print("Data loading failed.")
        return None

    if len(X_train.shape) != 2 or len(X_test.shape) != 2 or len(y_train.shape) != 1 or len(y_test.shape) != 1:
        print("The provided data does not have the appropriate format.")
        return None
    model = RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report = print(classification_report(y_test, y_pred))
    return report
    
def neural_net_model(X_train=None, X_test=None, y_train=None, y_test=None, suggested_data=False, test_size=0.25, random_state=1):
    """
    Train and evaluate the Neural Network classifier.

    Args:
        X_train (numpy array): Training data features.
        X_test (numpy array): Testing data features.
        y_train (numpy array): Training data labels.
        y_test (numpy array): Testing data labels.
        suggested_data (bool): Whether to use the suggested dataset or not.
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): Seed used by the random number generator.

    Returns:
        str: Classification report containing precision, recall, F1-score, and support metrics.
            The report provides information about the model's performance on the test data.
            If data loading or formatting fails, None is returned.
    """
    if suggested_data:
        X_train, X_test, y_train, y_test = load_dataset(suggested_data=True, test_size=test_size, random_state=random_state)

    if X_train is None or X_test is None or y_train is None or y_test is None:
        print("Data loading failed.")
        return None

    if len(X_train.shape) != 2 or len(X_test.shape) != 2 or len(y_train.shape) != 1 or len(y_test.shape) != 1:
        print("The provided data does not have the appropriate format.")
        return None
    model = MLPClassifier(alpha=1)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report = print(classification_report(y_test, y_pred))
    return report
    
def adaboost_model(X_train=None, X_test=None, y_train=None, y_test=None, suggested_data=False, test_size=0.25, random_state=1):
    """
    Train and evaluate the AdaBoost classifier.

    Args:
        X_train (numpy array): Training data features.
        X_test (numpy array): Testing data features.
        y_train (numpy array): Training data labels.
        y_test (numpy array): Testing data labels.
        suggested_data (bool): Whether to use the suggested dataset or not.
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): Seed used by the random number generator.

    Returns:
        str: Classification report containing precision, recall, F1-score, and support metrics.
            The report provides information about the model's performance on the test data.
            If data loading or formatting fails, None is returned.
    """
    if suggested_data:
        X_train, X_test, y_train, y_test = load_dataset(suggested_data=True, test_size=test_size, random_state=random_state)

    if X_train is None or X_test is None or y_train is None or y_test is None:
        print("Data loading failed.")
        return None

    if len(X_train.shape) != 2 or len(X_test.shape) != 2 or len(y_train.shape) != 1 or len(y_test.shape) != 1:
        print("The provided data does not have the appropriate format.")
        return None
    model = AdaBoostClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report = print(classification_report(y_test, y_pred))
    return report
    
def gaussian_nb_model(X_train=None, X_test=None, y_train=None, y_test=None, suggested_data=False, test_size=0.25, random_state=1):
    """
    Train and evaluate the Gaussian Naive Bayes classifier.

    Args:
        X_train (numpy array): Training data features.
        X_test (numpy array): Testing data features.
        y_train (numpy array): Training data labels.
        y_test (numpy array): Testing data labels.
        suggested_data (bool): Whether to use the suggested dataset or not.
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): Seed used by the random number generator.

    Returns:
        str: Classification report containing precision, recall, F1-score, and support metrics.
            The report provides information about the model's performance on the test data.
            If data loading or formatting fails, None is returned.
    """
    if suggested_data:
        X_train, X_test, y_train, y_test = load_dataset(suggested_data=True, test_size=test_size, random_state=random_state)

    if X_train is None or X_test is None or y_train is None or y_test is None:
        print("Data loading failed.")
        return None

    if len(X_train.shape) != 2 or len(X_test.shape) != 2 or len(y_train.shape) != 1 or len(y_test.shape) != 1:
        print("The provided data does not have the appropriate format.")
        return None
    model = GaussianNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report = print(classification_report(y_test, y_pred))
    return report

def svm_linear_model(X_train=None, X_test=None, y_train=None, y_test=None, suggested_data=False, test_size=0.25, random_state=1):
    """
    Train and evaluate the Support Vector Machine (SVM) classifier with a linear kernel.

    Args:
        X_train (numpy array): Training data features.
        X_test (numpy array): Testing data features.
        y_train (numpy array): Training data labels.
        y_test (numpy array): Testing data labels.
        suggested_data (bool): Whether to use the suggested dataset or not.
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): Seed used by the random number generator.

    Returns:
        str: Classification report containing precision, recall, F1-score, and support metrics.
            The report provides information about the model's performance on the test data.
            If data loading or formatting fails, None is returned.
    """     
    if suggested_data:
        X_train, X_test, y_train, y_test = load_dataset(suggested_data=True, test_size=test_size, random_state=random_state)

    if X_train is None or X_test is None or y_train is None or y_test is None:
        print("Data loading failed.")
        return None

    if len(X_train.shape) != 2 or len(X_test.shape) != 2 or len(y_train.shape) != 1 or len(y_test.shape) != 1:
        print("The provided data does not have the appropriate format.")
        return None
    model = svm.SVC(kernel='linear')
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report = print(classification_report(y_test, y_pred))
    return report
    
def svm_rbf_model(X_train=None, X_test=None, y_train=None, y_test=None, suggested_data=False, test_size=0.25, random_state=1):
    """
    Train and evaluate the Support Vector Machine (SVM) classifier with an RBF kernel.

    Args:
        X_train (numpy array): Training data features.
        X_test (numpy array): Testing data features.
        y_train (numpy array): Training data labels.
        y_test (numpy array): Testing data labels.
        suggested_data (bool): Whether to use the suggested dataset or not.
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): Seed used by the random number generator.

    Returns:
        str: Classification report containing precision, recall, F1-score, and support metrics.
            The report provides information about the model's performance on the test data.
            If data loading or formatting fails, None is returned.
    """    
    if suggested_data:
        X_train, X_test, y_train, y_test = load_dataset(suggested_data=True, test_size=test_size, random_state=random_state)

    if X_train is None or X_test is None or y_train is None or y_test is None:
        print("Data loading failed.")
        return None

    if len(X_train.shape) != 2 or len(X_test.shape) != 2 or len(y_train.shape) != 1 or len(y_test.shape) != 1:
        print("The provided data does not have the appropriate format.")
        return None    
    model = svm.SVC(kernel='rbf')
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report = print(classification_report(y_test, y_pred))
    return report
    
def svm_sigmoid_model(X_train=None, X_test=None, y_train=None, y_test=None, suggested_data=False, test_size=0.25, random_state=1):
    """
    Train and evaluate the Support Vector Machine (SVM) classifier with a sigmoid kernel.

    Args:
        X_train (numpy array): Training data features.
        X_test (numpy array): Testing data features.
        y_train (numpy array): Training data labels.
        y_test (numpy array): Testing data labels.
        suggested_data (bool): Whether to use the suggested dataset or not.
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): Seed used by the random number generator.

    Returns:
        str: Classification report containing precision, recall, F1-score, and support metrics.
            The report provides information about the model's performance on the test data.
            If data loading or formatting fails, None is returned.
    """   
    if suggested_data:
        X_train, X_test, y_train, y_test = load_dataset(suggested_data=True, test_size=test_size, random_state=random_state)

    if X_train is None or X_test is None or y_train is None or y_test is None:
        print("Data loading failed.")
        return None

    if len(X_train.shape) != 2 or len(X_test.shape) != 2 or len(y_train.shape) != 1 or len(y_test.shape) != 1:
        print("The provided data does not have the appropriate format.")
        return None

    model = svm.SVC(kernel='sigmoid')
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report = print(classification_report(y_test, y_pred))
    return report

def load_dataset(X_train=None, X_test=None, y_train=None, y_test=None, suggested_data=False, test_size=0.25, random_state=1):
    """
    Load and preprocess the dataset for classification.

    Args:
        X_train (numpy array): Training data features.
        X_test (numpy array): Testing data features.
        y_train (numpy array): Training data labels.
        y_test (numpy array): Testing data labels.
        suggested_data (bool): Whether to use the suggested dataset or not.
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): Seed used by the random number generator.

    Returns:
        tuple: A tuple containing X_train, X_test, y_train, and y_test data arrays.
            The function loads the dataset and performs preprocessing steps like splitting
            into training and testing sets. If the provided data does not have the appropriate
            format or if data loading fails, None is returned for all arrays.
    """
    if X_train is not None and X_test is not None and y_train is not None and y_test is not None:
        if len(X_train.shape) != 2 or len(X_test.shape) != 2 or len(y_train.shape) != 1 or len(y_test.shape) != 1:
            print("The provided data does not have the appropriate format.")
            return None, None, None, None
        else:
            return X_train, X_test, y_train, y_test
    
    if suggested_data:
        X_train, X_test, y_train, y_test = suggested_dataset1(test_size, random_state)       
    return X_train, X_test, y_train, y_test 

def suggested_dataset1(test_size=0.25, random_state=1):
    """
    Load and preprocess a suggested dataset for classification.

    Args:
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): Seed used by the random number generator.

    Returns:
        tuple: A tuple containing X_train, X_test, y_train, and y_test data arrays.
            The function loads a dataset of promoter gene sequences and performs preprocessing steps,
            including one-hot encoding and train-test splitting. The resulting arrays are returned.
    """
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/molecular-biology/promoter-gene-sequences/promoters.data'
    names = ['Class', 'id', 'Sequence']

    # Load the dataset
    data = pd.read_csv(url, names=names)

    # Encoding
    clases = data.loc[:, 'Class']
    sequence = list(data.loc[:, 'Sequence'])
    dic = {}
    for i, seq in enumerate(sequence):
        nucleotides = list(seq)
        nucleotides = [char for char in nucleotides if char != '\t']
        nucleotides.append(clases[i])

        dic[i] = nucleotides

    df = pd.DataFrame(dic)
    df = df.transpose()
    df.rename(columns={57: 'Class'}, inplace=True)

    # Encoding
    numerical_df = pd.get_dummies(df)
    numerical_df.drop('Class_-', axis=1, inplace=True)
    numerical_df.rename(columns={'Class_+': 'Class'}, inplace=True)

    X = numerical_df.drop(['Class'], axis=1).values
    y = numerical_df['Class'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    return X_train, X_test, y_train, y_test
