
#---------------------------------------- NumPy Basics ----------------------------------------
# NumPy(Numerical Python) is an open source python library that is widely used in the technical
# field of science and engineering. The NumPy library contains multi-dimensional array data
# structures along with a large library of functions that operate efficiently on these arrays.
# ----------------------------------------------------------------------------------------------
# IMPORTING NUMPY

import numpy as np

# #----------------------------------------------------------------------------------------------

def main():

    print("hello world :3")


    # 2-Dimensional Array      (outer brackets contain 1st dimension, inner brackets contain 2nd dimension)
    a = np.array([[1, 2, 3,4],      # row 1
                  [5, 6, 7, 8],     # row 2
                  [9, 10, 11, 12]]) # row 3
    # column-last, row-2nd_to_last
    print(a)

    # ----- ARRAY ACCESS -----
    b = a[0, 1]
    c = a[0, :3]



    # ----- ARRAY ATTRIBUTES -----
    np.ndim(a)  # Number of dimensions
    np.shape(a) # Tuple of number of elements in each dimension
    np.size(a)  # Fixed total number of elements
    d = a.dtype # Static data-type: "int64"

    # ----- ARRAY CREATION -----
    all_zero_array      = np.zeros(1)    #
    all_one_array       = np.ones(1)     #
    empty_random_array  = np.empty(1)    #
    ranged_array        = np.arange(1)   #
    linear_spaced_array = np.linspace(1, 1, 1) #


if __name__ == '__main__':
    main()
