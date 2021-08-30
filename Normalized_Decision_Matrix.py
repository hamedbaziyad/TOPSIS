from Normalization import *

def Normalize_Decision_Matrix(Decision_Matrix, Attribute_Type, Normal_Method):
    for i in range(0, len(Attribute_Type)):
        if Attribute_Type[i] == 1:
            Type = "profit"
        elif Attribute_Type[i] == 0:
            Type = "cost"
        else:
            "Please, fill the correct attribute type"

        Decision_Matrix.iloc[:, i] = Normal_Method(Decision_Matrix.iloc[:, i], Type)
    return Decision_Matrix
