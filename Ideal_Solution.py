from Weighted_Normalized_Decision_Matrix import *

def Ideal_Solution(Weighted_normalizaed_Decision_matrix, Attribute_Type):
    Positive_Ideal_Solutions = []
    Negative_Ideal_Solutions = []
    for i in range(0, len(Attribute_Type)):
        if Attribute_Type[i] == 1:
            Positive_Ideal = max(Weighted_normalizaed_Decision_matrix.iloc[:, i]) 
            Negative_Ideal = min(Weighted_normalizaed_Decision_matrix.iloc[:, i])
            
            Positive_Ideal_Solutions.append(Positive_Ideal)
            Negative_Ideal_Solutions.append(Negative_Ideal)
        elif Attribute_Type[i] == 0:
            Positive_Ideal = min(Weighted_normalizaed_Decision_matrix.iloc[:, i]) 
            Negative_Ideal = max(Weighted_normalizaed_Decision_matrix.iloc[:, i])
        
            Positive_Ideal_Solutions.append(Positive_Ideal)
            Negative_Ideal_Solutions.append(Negative_Ideal)
            
    return (Positive_Ideal_Solutions, Negative_Ideal_Solutions)
            



