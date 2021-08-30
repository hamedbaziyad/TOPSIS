from Ideal_Solution import *
import numpy as np
import pandas as pd
def Euclidean_Distance(Ideal_Points, Weighted_normalizaed_Decision_matrix, Attribute_Type):
    Positive_Ideal_Point = Ideal_Solution(Weighted_normalizaed_Decision_matrix, Attribute_Type)[0]
    Negative_Ideal_Point = Ideal_Solution(Weighted_normalizaed_Decision_matrix, Attribute_Type)[1]
    
    Negative_Si = (np.sum((Weighted_normalizaed_Decision_matrix-Negative_Ideal_Point)**2, axis = 1))**0.5  
    Positive_Si = np.sum((Weighted_normalizaed_Decision_matrix-Positive_Ideal_Point)**2, axis = 1)**0.5

    C = Negative_Si/(Negative_Si + Positive_Si)
    return (Weighted_normalizaed_Decision_matrix,C)