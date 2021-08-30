import numpy as np
import pandas as pd
def Linear_Max_Min(attribute, Type):
    """
    Patro, S. and Sahu, K.K., 2015. Normalization: A preprocessing stage.
    arXiv preprint arXiv:1503.06462.
    """
    MIN = min(attribute)
    MAX = max(attribute)
    Var = MAX - MIN
    attribute = np.array(attribute)
    if Type == "profit":
        Attribute = (attribute - MIN)/Var
    elif Type == "cost":
        Attribute = (MAX - attribute)/Var
    
    return Attribute

def Linear_Max(attribute, Type):
    """
    Çelen, A., 2014. Comparative analysis of normalization procedures in
    TOPSIS method: with an application to Turkish deposit banking market.
    Informatica, 25(2), pp.185-208.
    """
    MAX = max(attribute)
    attribute = np.array(attribute)
    if Type == "profit":
        Attribute = attribute/MAX
    elif Type == "cost":
        Attribute = 1 - attribute/MAX
    
    return Attribute

def Linear_sum(attribute, Type):
    """
    Jahan, A. and Edwards, K.L. (2014) ‘A state-of-the-art survey on the
    influence of normalization techniques in ranking: improving the materials
    selection process in engineering design’, Mater. Des., Vol. 65, No. 2015,
    pp.335–342.
    """
    SUM_1 = sum(attribute)
    SUM_2 = sum(1/attribute)
    attribute = np.array(attribute)
    if Type == "profit":
        Attribute = attribute/SUM_1 
    elif Type == "cost":
        Attribute = (1/attribute)/SUM_2
        
    return Attribute


def Vector_Normalization(attribute, Type):
    """
    Jahan, A. and Edwards, K.L. (2014) ‘A state-of-the-art survey on the
    influence of normalization techniques in ranking: improving the materials
    selection process in engineering design’, Mater. Des., Vol. 65, No. 2015,
    pp.335–342.
    """
    r = (sum(attribute**2))**(0.5)
    if Type == "profit":
        Attribute = attribute/r 
    elif Type == "cost":
        Attribute = 1 - attribute/r 
        
    return Attribute


def Logarithmic_normalisation(attribute, Type):
    """
    Jahan, A. and Edwards, K.L. (2014) ‘A state-of-the-art survey on the
    influence of normalization techniques in ranking: improving the materials
    selection process in engineering design’, Mater. Des., Vol. 65, No. 2015,
    pp.335–342.
    """
    r = np.log(np.prod(attribute))
    if Type == "profit":
        Attribute = np.log(attribute)/r
        
    if Type == "cost":
        Attribute = (1 - (np.log(attribute)/r))/(len(attribute)-1)
        
    return Attribute



                          

