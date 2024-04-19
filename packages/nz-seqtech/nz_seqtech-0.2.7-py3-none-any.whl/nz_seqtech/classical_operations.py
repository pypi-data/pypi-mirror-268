import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skew, kurtosis
from .quantum_dna_encoding import is_valid_dna_seq

def analyze_dna_seq(seq, selected_analyses=None, selected_visualizations=None):
    """
    Analyzes a DNA sequence with selected computations and visualizations.

    Args:
        seq (str): The DNA sequence to analyze.
        selected_analyses (list): List of analyses to perform. Options include:
                                  'base_counts', 'expectation_values', 'variance', 'std_deviation',
                                  'covariance', 'correlation', 'skewness', 'kurtosis'.
                                  If None, all analyses are performed.
        selected_visualizations (list): List of visualizations to generate. Options include:
                                        'pie', 'bar', 'line'.
                                        If None, no visualization is generated.

    Returns:
        dict: A dictionary containing the requested analysis results.
    """
    seq = seq.upper()  # Convert the sequence to uppercase
    if not is_valid_dna_seq(seq):
        print("Error: This is not a DNA sequence. Please provide a valid DNA sequence.")
        return None
    
    base_counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for base in seq:
        if base in base_counts:
            base_counts[base] += 1
    total_bases = sum(base_counts.values())
    probabilities = {base: count / total_bases for base, count in base_counts.items()}

    results = {}
    analyses = selected_analyses if selected_analyses is not None else ['base_counts', 'expectation_values', 'variance', 'std_deviation', 'covariance', 'correlation', 'skewness', 'kurtosis']
    counts = list(base_counts.values())

    if 'base_counts' in analyses:
        results['base_counts'] = base_counts
    if 'expectation_values' in analyses:
        results['expectation_values'] = probabilities
    if 'variance' in analyses:
        results['variance'] = np.var(counts)
    if 'std_deviation' in analyses:
        results['std_deviation'] = np.std(counts)
    if 'covariance' in analyses:
        results['covariance'] = np.cov(counts, bias=True)
    if 'correlation' in analyses:
        results['correlation'] = np.corrcoef(counts)
    if 'skewness' in analyses:
        results['skewness'] = skew(counts)
    if 'kurtosis' in analyses:
        results['kurtosis'] = kurtosis(counts)

    visualizations = selected_visualizations if selected_visualizations is not None else []
    labels = list(base_counts.keys())
    
    if 'pie' in visualizations:
        plt.figure(figsize=(6, 6))
        plt.pie(counts, labels=labels, autopct='%1.1f%%')
        plt.title('Base Counts')
        plt.show()
    
    if 'bar' in visualizations:
        plt.figure(figsize=(8, 6))
        plt.bar(labels, probabilities.values())
        plt.xlabel('Bases')
        plt.ylabel('Probability')
        plt.title('Base Probability Distribution')
        plt.show()
    
    if 'line' in visualizations:
        plt.figure(figsize=(8, 6))
        x = np.arange(len(labels))
        plt.plot(x, counts, marker='o', linestyle='-')
        plt.xticks(x, labels)
        plt.xlabel('Bases')
        plt.ylabel('Count')
        plt.title('Base Count Distribution')
        plt.show()
    
