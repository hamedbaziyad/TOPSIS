weights = [0.2, 0.2, 0.2, 0.2, 0.2]

def Weight_Prod(Decision_Matrix, weights):
    if sum(weights) != 1:
        print("Shape of weights is not satisfied.weights must be equal 1")
    else:
        if Decision_Matrix.shape[1] != len(weights):
            print("Shape of weights is not satisfied.")
        else:
            for i in range (0, Decision_Matrix.shape[1]):
                Decision_Matrix.iloc[:, i] = Decision_Matrix.iloc[:, i]*weights[i]
                
        return Decision_Matrix

