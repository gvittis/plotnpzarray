import numpy as np
import numpy.typing as npt

def getDivisors(n: int) -> npt.NDArray: 
    """
    Computes the divisors of a given integer n and returns them as a numpy array.

    Parameters:
    -----------
    n : int
        The integer for which to find the divisors.

    Returns:
    --------
    numpy.ndarray
        A numpy array containing the divisors of n.
    """    

    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    res = []
    i = 1
    while i <= n : 
        if (n % i==0) : 
            res.append(i), 
        i = i + 1
    return np.array(res)

def get_closest_split(n: int, close_to: int):
    """
    Finds the divisor of n that is closest to the specified value.

    Parameters:
    -----------
    n : int
        The integer for which to find the closest divisor.
    close_to : int
        The value to which the closest divisor of n is sought.

    Returns:
    --------
    int
        The divisor of n that is closest to the value of close_to.

    Raises:
    -------
    ValueError
        - If the provided n is not a positive integer.
        - If the provided close_to is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(close_to, int) or close_to <= 0:
        raise ValueError("close_to must be a positive integer")
    
    all_divisors = getDivisors(n)
    return all_divisors[(np.abs(all_divisors - close_to)).argmin()]

def CompressOverY(inArray: npt.NDArray, Ny: int) -> npt.NDArray:
    """
    Compresses a 2D numpy array along the y-axis by summing over blocks of Ny elements.

    Parameters:
    -----------
    inArray : numpy.ndarray
        The input 2D array to be compressed.
    Ny : int
        The compression factor along the y-axis. Must be a positive integer.

    Returns:
    --------
    numpy.ndarray
        The compressed 2D array where the y-dimension is reduced by a factor of Ny.

    Raises:
    -------
    ValueError
        If Ny is less than 1.

    Notes:
    ------
    - The function do not ensure that the input array can be evenly divided by Ny along the y-axis to avoid shape mismatch errors.
    - The function reshapes the input array to group elements along the y-axis into blocks of size Ny.
    - The function then sums these blocks along the last axis to produce the compressed array.
    - If Ny is 1, the original array is returned unchanged.
    """    
    if Ny < 1:
        raise ValueError("Compression can't be smaller than 1!")
    if Ny == 1:
        return inArray
    
    NewShape = (inArray.shape[0], int(inArray.shape[1]/Ny), Ny)

    return inArray.reshape(NewShape).sum(axis=2)

def CompressOverX(inArray: npt.NDArray, Nx: int) -> npt.NDArray:
    """
    Compresses a 2D numpy array along the y-axis by summing over blocks of Ny elements.

    Parameters:
    -----------
    inArray : numpy.ndarray
        The input 2D array to be compressed.
    Ny : int
        The compression factor along the y-axis. Must be a positive integer.

    Returns:
    --------
    numpy.ndarray
        The compressed 2D array where the y-dimension is reduced by a factor of Ny.

    Raises:
    -------
    ValueError
        If Ny is less than 1.

    Notes:
    ------
    - The function do not ensure that the input array can be evenly divided by Ny along the y-axis to avoid shape mismatch errors.
    - The function reshapes the input array to group elements along the y-axis into blocks of size Ny.
    - The function then sums these blocks along the last axis to produce the compressed array.
    - If Ny is 1, the original array is returned unchanged.
    """    
    if Nx < 1:
        raise ValueError("Compression can't be smaller than 1!")
    if Nx == 1:
        return inArray
    
    NewShape = (int(inArray.shape[0]/Nx), Nx, inArray.shape[1])

    return inArray.reshape(NewShape).sum(axis=1)