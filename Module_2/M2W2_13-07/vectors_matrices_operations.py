import numpy as np


def compute_vector_length(vector):

    len_of_vector = np.sqrt(np.sum(np.square(vector)))

    return len_of_vector


def compute_dot_product(vector1, vector2):

    vector1 = np.array(vector1)
    vector2 = np.array(vector2)

    result = np.sum(vector1 * vector2)

    return result


def matrix_multi_vector(matrix, vector):

    matrix = np.array(matrix)
    vector = np.array(vector)

    result = matrix.dot(vector)

    return result


def matrix_multi_matrix(matrix1, matrix2):

    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)

    result = matrix1.dot(matrix2)

    return result


def inverse_matrix(matrix):

    matrix = np.array(matrix)

    result = np.linalg.inv(matrix)

    return result


def compute_eigenvalues_eigenvectors(matrix):

    matrix = np.array(matrix)

    eigenvalues, eigenvectors = np.linalg.eig(matrix)

    return eigenvalues, eigenvectors


def cosine_similarity(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)

    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)

    cosine_similarity = dot_product / (norm_v1 * norm_v2)

    return cosine_similarity
