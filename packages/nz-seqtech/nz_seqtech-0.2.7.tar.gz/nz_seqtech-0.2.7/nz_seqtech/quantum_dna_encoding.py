import numpy as np
import math
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile, Aer, IBMQ, execute
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from qiskit.providers.aer import QasmSimulator
from qiskit.visualization import plot_bloch_multivector, plot_state_hinton, plot_state_city, plot_state_paulivec

def is_valid_dna_seq(seq):
    """
    Checks if a given sequence is a valid DNA sequence.

    Args:
        seq (str): The sequence to be validated.

    Returns:
        bool: True if the sequence is a valid DNA sequence, False otherwise.
    """
    valid_letters = {'A', 'T', 'C', 'G', 'a', 't', 'c', 'g'}  # Include both lowercase and uppercase letters
    if any(letter not in valid_letters for letter in seq):
        return False
    return True
#####################################################################################    
#####################################################################################
def amplitude_encoding(dna_seq):
    """
    Encodes a DNA sequence into a quantum state using amplitude encoding.

    Args:
        dna_seq (str): The DNA sequence to be encoded.

    Returns:
        QuantumCircuit: The quantum circuit representing the amplitude encoding.
    """
    # Convert the DNA sequence to uppercase
    dna_seq = dna_seq.upper()

    # Check if the DNA sequence is valid
    if not is_valid_dna_seq(dna_seq):
        print("Error: This is not a valid DNA sequence. Please provide a valid DNA sequence.")
        return None
    
    # Define encoding for bases
    encoding_dict = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}
    
    # Calculate the number of qubits needed
    n = len(dna_seq)
    num_qubits = int(np.ceil(np.log2(n)))

    # Create the quantum circuit
    qc = QuantumCircuit(num_qubits)

    # Encode each base of the DNA sequence
    for i in range(n):
        base = dna_seq[i]
        encoded_bits = encoding_dict[base]
        
        # Encode each bit of the base
        for j in range(len(encoded_bits)):
            if encoded_bits[j] == '1':
                qc.x(j)
        
        # Apply a Hadamard gate to each qubit
        for j in range(len(encoded_bits)):
            qc.h(j)
        
        # Rotate qubits based on the encoded bits
        theta = 2 * np.arcsin(1 / np.sqrt(4))
        qc.rz(theta, list(range(len(encoded_bits))))
        
    return qc
#####################################################################################
#####################################################################################
def cosine_encoding(dna_seq):
    """
    Encodes a DNA sequence into a quantum state using cosine encoding.

    Args:
        dna_seq (str): The DNA sequence to be encoded.

    Returns:
        QuantumCircuit: The quantum circuit representing the cosine encoding.
    """
     # Convert the DNA sequence to uppercase   
    dna_seq = dna_seq.upper() 
    if not is_valid_dna_seq(dna_seq):
        print("Error: This is not a valid DNA sequence. Please provide a valid DNA sequence.")
        return None
    # Define the basis states |0⟩ and |1⟩
    zero = np.array([1, 0])
    one = np.array([0, 1])

    # Create a quantum circuit with one qubit for each base in the DNA sequence
    n = len(dna_seq)
    qc = QuantumCircuit(n)

    # Encode each base in the DNA sequence as a quantum state
    for i in range(n):
        base = dna_seq[i]
        if base == 'A':
            qc.initialize(zero, [i])
        elif base == 'C':
            qc.initialize(one, [i])
        elif base == 'G':
            qc.x(i)
            qc.initialize(zero, [i])
        elif base == 'T':
            qc.x(i)
            qc.initialize(one, [i])

    # Apply the cosine encoding transformation to each qubit
    for i in range(n):
        theta = np.arccos(1 / np.sqrt(n))
        qc.ry(theta, i)

    return qc
#####################################################################################
#####################################################################################
def qft_encoding(dna_seq):
    """
    Encodes a DNA sequence into a quantum state using QFT encoding.

    Args:
        dna_seq (str): The DNA sequence to be encoded.

    Returns:
        QuantumCircuit: The quantum circuit representing the QFT encoding.

    """
    # Convert the DNA sequence to uppercase
    dna_seq = dna_seq.upper()
    if not is_valid_dna_seq(dna_seq):
        print("Error: This is not a valid DNA sequence. Please provide a valid DNA sequence.")
        return Nonee
    n = len(dna_seq)
    qubits = n   # Number of qubits needed for the encoding 
    # Create a quantum circuit
    qc = QuantumCircuit(qubits)
    # Encode the DNA sequence
    for i, base in enumerate(dna_seq):
        if base == "A":
            qc.x(i)
        elif base == "T":
            qc.x(i)
            qc.h(i)
        elif base == "G":
            qc.h(i)
        elif base == "C":
            pass
    # Apply Quantum Fourier Transform (QFT)
    qc.h(range(n))
    for i in range(n):
        for j in range(i + 1, n):
            qc.cp(2 * math.pi / 2 ** (j - i), j, i)
    return qc
#####################################################################################
#####################################################################################
def phase_encoding(dna_seq):
    """
     Encodes a DNA sequence into a quantum state using phase encoding.

    Args:
        dna_sequence (str): The DNA sequence to be encoded.

    Returns:
        QuantumCircuit: The quantum circuit representing the phase encoding.

    """
    # Convert the DNA sequence to uppercase
    dna_seq = dna_seq.upper()
    if not is_valid_dna_seq(dna_seq):
        print("Error: This is not a valid DNA sequence. Please provide a valid DNA sequence.")
        return None
    n = len(dna_seq)

    # Creating quantum circuit
    qc = QuantumCircuit(n)

    # Apply phase encoding for each base in the DNA sequence
    for i, base in enumerate(dna_seq):
        if base == "A":
            pass
        elif base == "T":
            qc.z(i)
        elif base == "G":
            qc.x(i)
            qc.z(i)
        elif base == "C":
            qc.x(i)

    return qc
#####################################################################################
#####################################################################################


def NZ23_encoding(dna_seq, dna_ref, alpha):
    """
    Encodes a DNA sequence into a quantum state using NZ23 encoding.

    Args:
        dna_seq (str): The DNA sequence to be encoded.
        dna_ref (str): The reference DNA sequence used for encoding.
        alpha (float): A parameter controlling the level of encoding based on the Bhattacharyya distance.

    Returns:
        QuantumCircuit: The quantum circuit representing the NZ23 encoding.
    """
    # Convert the DNA sequence to uppercase

    if not is_valid_dna_seq(dna_seq):
        print("Error: This is not a valid DNA sequence. Please provide a valid DNA sequence.")
        return None
    if not is_valid_dna_seq(dna_ref):
        print("Error: This is not a DNA sequence reference. Please provid a valid reference DNA sequence.")
        return None
    # Check if the length of dna_seq and dna_ref are the same
    if len(dna_seq) != len(dna_ref):
        print("Error: The length of the DNA sequence and reference DNA must be the same.")
        return None
    # Convert the DNA sequence to uppercase   
    dna_seq = dna_seq.upper()
    dna_ref = dna_ref.upper()

    dna_dict = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}
    n = 2  # For example, using 2 qubits for each base
    
    num_qubits = len(dna_seq) * n
    qr = QuantumRegister(num_qubits, name='q')
    cr = ClassicalRegister(num_qubits, name='c')
    qc = QuantumCircuit(qr, cr)

    # Calculate probabilities
    def calculate_probability(dna_seq):
        bases = ['A', 'T', 'G', 'C']
        base_count = {base: dna_seq.count(base) for base in bases}
        seq_length = len(dna_seq)
        probability = {base: count / seq_length for base, count in base_count.items()}
        return probability
    
    probability_dna_seq = calculate_probability(dna_seq)
    probability_dna_ref = calculate_probability(dna_ref)

    # Calculate Bhattacharyya distance
    def calculate_bhattacharyya_distance(probability_p, probability_q):
        bhattacharyya_distance = 0.0
        for base, prob_p in probability_p.items():
            prob_q = probability_q[base]
            bhattacharyya_distance += math.sqrt(prob_p * prob_q)
        return -math.log(bhattacharyya_distance)
    
    bhattacharyya_distance = calculate_bhattacharyya_distance(probability_dna_seq, probability_dna_ref)
    
    # Define quantum gates based on the Bhattacharyya distance and alpha
    for i, base in enumerate(dna_seq):
        for bit in range(n):
            gate_name = f"{base}_{bit}"  # Name for the custom gate
            angle = -alpha * bhattacharyya_distance * math.pi  # Using Bhattacharyya distance and alpha
            qc.rx(angle, qr[i * n + bit])  # Apply an RX gate with the calculated angle
        
        for bit in range(1, n):
            qc.cx(qr[i * n], qr[i * n + bit])

    return qc
#####################################################################################
#####################################################################################
def NZ22_encoding(dna_seq, dna_ref, alpha):
    """
    Encodes a DNA sequence into a quantum state using NZ22 encoding.

    Args:
        dna_seq (str): The DNA sequence to be encoded.
        dna_ref (str): The reference DNA sequence used for encoding.
        alpha (float): A parameter controlling the level of encoding based on the Bhattacharyya distance.

    Returns:
        QuantumCircuit: The quantum circuit representing the NZ22 encoding.
    """
    if not is_valid_dna_seq(dna_seq):
        print("Error: This is not a valid DNA sequence. Please provide a valid DNA sequence.")
        return None
    if not is_valid_dna_seq(dna_ref):
        print("Error: This is not a DNA sequence reference. Please provid a valid reference DNA sequence.")
        return None
    # Check if the length of dna_seq and dna_ref are the same
    if len(dna_seq) != len(dna_ref):
        print("Error: The length of the DNA sequence and reference DNA must be the same.")
        return None
    # Convert the DNA sequence to uppercase   
    dna_seq = dna_seq.upper()
    dna_ref = dna_ref.upper()

    dna_dict = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}
    n = 2  # For example, using 2 qubits for each base
    
    num_qubits = len(dna_seq) * n
    qr = QuantumRegister(num_qubits, name='q')
    cr = ClassicalRegister(num_qubits, name='c')
    qc = QuantumCircuit(qr, cr)

    # Calculate probabilities
    def calculate_probability(dna_seq):
        bases = ['A', 'T', 'G', 'C']
        base_count = {base: dna_seq.count(base) for base in bases}
        seq_length = len(dna_seq)
        probability = {base: count / seq_length for base, count in base_count.items()}
        return probability
    
    probability_dna_seq = calculate_probability(dna_seq)
    probability_dna_ref = calculate_probability(dna_ref)

    # Calculate KL divergence
    def calculate_kl_divergence(probability_p, probability_q):
        kl_divergence = 0.0
        for base, prob_p in probability_p.items():
            prob_q = probability_q.get(base, 1e-9)
            if prob_p > 0 and prob_q > 0:
                kl_divergence += prob_p * math.log2(prob_p / prob_q)
        return kl_divergence
        
    kl_divergence = calculate_kl_divergence(probability_dna_seq, probability_dna_ref)
    
    # Define quantum gates based on the KL divergence and alpha
    for i, base in enumerate(dna_seq):
        for bit in range(n):
            gate_name = f"{base}_{bit}"  # Name for the custom gate
            angle = -alpha * kl_divergence * math.pi  # Using KL divergence and alpha
            qc.rx(angle, qr[i * n + bit])  # Apply an RX gate with the calculated angle
        
        for bit in range(1, n):
            qc.cx(qr[i * n], qr[i * n + bit])

    return qc
#####################################################################################
#####################################################################################
def draw_circuit(qc):
    """
    Draws a quantum circuit.

    Args:
        qc (QuantumCircuit): The quantum circuit to be drawn.

    # Function implementation here
    """
    return qc.draw(output='mpl')
#####################################################################################
#####################################################################################
def get_statevector(qc):
    """
    Executes a quantum circuit on a simulator and returns the resulting statevector.

    Args:
        qc (QuantumCircuit): The quantum circuit to be executed.

    Returns:
        ndarray: The statevector resulting from the execution of the circuit.

    """    
    # Function implementation here
    backend = Aer.get_backend('statevector_simulator')
    job = execute(qc, backend)
    result = job.result()
    statevector = result.get_statevector(qc)
    return statevector    
#####################################################################################
#####################################################################################
def visualize_bloch_multivector(statevector):
    """
    Visualizes the quantum state as a Bloch multivector.

    Args:
        statevector (ndarray): The quantum statevector to be visualized.

    Returns:
        Figure: The Bloch multivector plot.

    """
    return plot_bloch_multivector(statevector)
#####################################################################################
#####################################################################################
def visualize_state_hinton(statevector):
    """
    Visualizes the quantum state using a Hinton plot.

    Args:
        statevector (ndarray): The quantum statevector to be visualized.

    Returns:
        Figure: The Hinton plot.

    """
    return plot_state_hinton(statevector)
#####################################################################################
#####################################################################################
def visualize_state_city(statevector):
    """
    Visualizes the quantum state using a city plot.

    Args:
        statevector (ndarray): The quantum statevector to be visualized.

    Returns:
        Figure: The city plot.

    """
    return plot_state_city(statevector)
#####################################################################################
#####################################################################################
def visualize_state_paulivec(statevector):
    """
    Visualizes the quantum state using a Pauli vector representation.

    Args:
        statevector (ndarray): The quantum statevector to be visualized.

    Returns:
        Figure: The Pauli vector plot.

    """
    return plot_state_paulivec(statevector)
