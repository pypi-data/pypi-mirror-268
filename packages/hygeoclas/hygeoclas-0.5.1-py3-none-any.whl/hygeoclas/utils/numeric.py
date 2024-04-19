import math
import numpy as np

def dct(x: np.array, M: int) -> list:
    """
    Computes the Discrete Cosine Transform (DCT-II) of the input array.

    The DCT-II is used in signal and image processing, particularly for lossy compression applications, such as JPEG.

    Args:
        x (np.array): The input data array.
        M (int): The number of DCT coefficients to compute.

    Returns:
        list: The first M DCT-II coefficients.

    Note:
        This function computes the DCT-II using the formula:

        Y[k] = sqrt(2/N) * sum_{n=0}^{N-1} x[n] * cos(pi*(2n+1)*k / 2N)

        where:
        - N is the length of the input array.
        - x[n] is the nth element of the input array.
        - k ranges from 0 to M-1.
    """
    N = len(x)
    DCT = []
    for i in range(1, M+1):
        DK = 1 if i==1 else 0         
        summation = sum(x[n] * (1/math.sqrt(1+DK)) * math.cos((math.pi*(2*n-1)*(i-1))/(2*N)) for n in range(N))
        DCT.append(math.sqrt(2/N) * summation)

    return DCT

class Equal:
    """
    A class that acts as a placeholder for a scaler but doesn't change the data.

    This class can be used in place of a scaler when you don't want to scale the data,
    but you want to keep the same structure of code that includes a fit and transform method.
    """

    def fit(self, XTrain: np.ndarray) -> 'Equal':
        """
        Fit method for the Equal class.

        This method doesn't actually do anything as it's just a placeholder.

        Args:
            XTrain (np.ndarray): The training data.

        Returns:
            Equal: A reference to the instance that called the method, to allow method chaining.
        """
        return self

    def transform(self, X: np.ndarray) -> np.ndarray:
        """
        Transform method for the Equal class.

        This method doesn't actually do anything as it's just a placeholder. It returns the input data as is.

        Args:
            X (np.ndarray): The data to be transformed.

        Returns:
            np.ndarray: The original data, unchanged.
        """
        return X