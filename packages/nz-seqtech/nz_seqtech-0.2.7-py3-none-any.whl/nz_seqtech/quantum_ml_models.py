import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from qiskit import Aer, QuantumCircuit
from qiskit.circuit.library import ZZFeatureMap, RealAmplitudes, ZFeatureMap, PauliFeatureMap
from qiskit.utils import QuantumInstance, algorithm_globals
from qiskit_machine_learning.algorithms.classifiers import NeuralNetworkClassifier
from qiskit_machine_learning.neural_networks import TwoLayerQNN
from qiskit.algorithms.optimizers import COBYLA, SPSA
from matplotlib import pyplot as plt
from IPython.display import clear_output
import time
import warnings
warnings.simplefilter('ignore')
def suggested_dataset_QNN(random_state=1, num_inputs=2, num_samples=100):
    """
    Generate a suggested dataset for Quantum Neural Networks (QNN).

    This function creates a synthetic dataset for binary classification suitable for training Quantum Neural Networks.
    It generates random input samples and assigns binary labels based on the sum of input features.

    Parameters:
    - random_state (int, optional): Seed for reproducibility of random data generation.

    Returns:
    tuple: A tuple containing:
        - X (numpy.ndarray): Input data of shape (num_samples, num_inputs), where each row represents a sample
          with `num_inputs` features.
        - y (numpy.ndarray): Binary labels corresponding to the input data, in {-1, +1} format.
    """
    X = 2 * algorithm_globals.random.random([num_samples, num_inputs]) - 1
    y = 1 * (np.sum(X, axis=1) >= 0)  # Labels in {0, 1}
    return X, y
def load_dataset_qnn(X=None, y=None, suggested_data=False, test_size=0.25, random_state=1):
    """
    Load or generate a dataset for Quantum Neural Networks (QNN) training.

    This function allows loading a user-provided dataset or generating a suggested synthetic dataset
    for binary classification suitable for training Quantum Neural Networks.

    Parameters:
    - X (numpy.ndarray, optional): Input data. If None, the function attempts to generate or load suggested data.
    - y (numpy.ndarray, optional): Binary labels corresponding to the input data. If None, the function attempts
      to generate or load suggested data.
    - suggested_data (bool, optional): If True, generate and return a suggested synthetic dataset using the
      `suggested_dataset_QNN` function.
    - test_size (float, optional): Proportion of the dataset to include in the test split if generating suggested data.
    - random_state (int, optional): Seed for reproducibility of random data generation.

    Returns:
    tuple: A tuple containing:
        - X (numpy.ndarray): Input data of shape (num_samples, num_inputs), where each row represents a sample
          with `num_inputs` features.
        - y (numpy.ndarray): Binary labels corresponding to the input data, in {-1, +1} format.

    Note:
    If `suggested_data` is True, the function either generates a suggested dataset or loads a previously generated one.
    If `suggested_data` is False and `X` and `y` are provided, the function checks the validity of the input data and
    returns it if in the appropriate format. If there are issues with the provided data, the function prints an error
    message and returns None.
    """
    if suggested_data:
        X_suggested, y_suggested = suggested_dataset_QNN(random_state)
        return X_suggested, y_suggested

    if X is None or y is None:
        print("Data loading failed.")
        return None, None

    if len(X.shape) != 2 or len(y.shape) != 1:
        print("The provided data does not have the appropriate format.")
        return None, None

    return X, y

def QNN(X=None, y=None, suggested_data=False, test_size=0.25, random_state=1, 
        num_iterations=60, feature_map_type='ZZFeatureMap', optimizer_type='COBYLA', print_circuit=False):
    """
    Train a Quantum Neural Network (QNN) classifier using the provided or suggested dataset.

    This function utilizes a Quantum Neural Network (QNN) to train a binary classifier. It can either use a
    user-provided dataset or generate a suggested synthetic dataset for training.

    Parameters:
    - X (numpy.ndarray, optional): Input data. If None, the function attempts to generate or load suggested data.
    - y (numpy.ndarray, optional): Binary labels corresponding to the input data. If None, the function attempts
      to generate or load suggested data.
    - suggested_data (bool, optional): If True, generate and use a suggested synthetic dataset using the
      `load_dataset_qnn` function.
    - test_size (float, optional): Proportion of the dataset to include in the test split if generating suggested data.
    - random_state (int, optional): Seed for reproducibility of random data generation.

    Returns:
    str: The classification report containing precision, recall, and F1-score for the test set.

    Note:
    If `suggested_data` is True, the function generates or loads a suggested dataset using the `load_dataset_qnn` function.
    If `suggested_data` is False and `X` and `y` are provided, the function checks the validity of the input data and
    proceeds with training the QNN classifier. If there are issues with the provided data, the function prints an error
    message and returns None.
    """
    if suggested_data:
        X, y = suggested_dataset_QNN(random_state)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Callback function for plotting
    objective_func_vals = []
    def callback_graph(weights, obj_func_eval):
        clear_output(wait=True)
        objective_func_vals.append(obj_func_eval)
        plt.plot(objective_func_vals, color='red')
        plt.title("Objective Function Value Over Iterations")
        plt.xlabel("Iteration")
        plt.ylabel("Objective Function Value")
        plt.show()

    # Feature map and ansatz selection
    feature_map = ZZFeatureMap(feature_dimension=X.shape[1], reps=2) if feature_map_type == 'ZZFeatureMap' \
        else ZFeatureMap(feature_dimension=X.shape[1], reps=2) if feature_map_type == 'ZFeatureMap' \
        else PauliFeatureMap(feature_dimension=X.shape[1], reps=2)
    ansatz = RealAmplitudes(X.shape[1], reps=2)

    # Quantum circuit composition
    qc = QuantumCircuit(X.shape[1])
    qc.compose(feature_map, inplace=True)
    qc.compose(ansatz, inplace=True)

    # Estimator and classifier setup
    optimizer = COBYLA(maxiter=num_iterations) if optimizer_type == 'COBYLA' else SPSA(maxiter=num_iterations)
    estimator_qnn = TwoLayerQNN(feature_map=feature_map, ansatz=ansatz,
                                quantum_instance=Aer.get_backend('statevector_simulator'))
    estimator_classifier = NeuralNetworkClassifier(estimator_qnn, optimizer=optimizer, callback=callback_graph)

    # Model training
    start_time = time.time()
    estimator_classifier.fit(X_train, y_train)
    training_time = time.time() - start_time

    # Predictions and evaluation
    y_pred_test = estimator_classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred_test)
    cm = confusion_matrix(y_test, y_pred_test, labels=[0, 1])
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[0, 1])
    if print_circuit:
        print(qc.draw()) 
    # Reporting
    print(f"Training time: {training_time:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}")
    print("Classification Report:")
    print(classification_report(y_test, y_pred_test, labels=[0, 1]))
    disp.plot(cmap=plt.cm.Blues)
    plt.title('Confusion Matrix')
    plt.show()
