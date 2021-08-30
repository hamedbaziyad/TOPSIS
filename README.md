# TOPSIS implementation in Python
Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS)
CHING-LAI Hwang and Yoon introduced TOPSIS in 1981 in their Multiple Criteria Decision Making (MCDM) and Multiple Criteria Decision Analysis (MCDA) methods [1]. TOPSIS strives to minimize the distance between the positive ideal solution and the chosen alternative, as well as to maximize the distance between the negative ideal solution and the chosen alternative. [2]. TOPSIS, in a nutshell, aids researchers to rank alternative items by identifying some criteria. We present alternative information and the criteria for each in the following decision matrix:
![image](https://user-images.githubusercontent.com/44522286/131339802-c16bb37c-6479-40e5-b28f-b79471b9bb26.png)
It is possible that some criteria are more effective than others. Therefore, some weights are given to their importance. It is required that the summation of n weights equals one.

![image](https://user-images.githubusercontent.com/44522286/131339921-f9ef0065-ef39-4fd6-bd52-a3e27c51b0bb.png)

Jahanshahloo et al, (2006), explained the TOPSIS in six main phases as follows: 

## 1)	Normalized Decision Matrix
It is the first phase of TOPSIS to normalize the process. Researchers have proposed different types of normalization. In this section, we identify the most commonly used normalization methods. The criterion or attribute is divided into two categories, cost and benefit. There are two formulas for normalizing the decision matrix for each normalization method: one for benefit criteria and one for cost criteria. According to Vafaei et al (2018), some of these normalization methods include:

![image](https://user-images.githubusercontent.com/44522286/131340118-1f755eb0-ea87-4a06-acf1-24a86e25c910.png)

All of the above normalization methods were coded in Normalization.py. Also, there is another related file called Normalized_Decision_Matrix.py, implementing the normalization method on the decision matrix.  Now we have anormalized decision matrix as follows:

![image](https://user-images.githubusercontent.com/44522286/131340180-3ac3ae5e-45f9-4351-a880-10da0227b1ca.png)

## 2)	Weighted Normalized Decision Matrix
The Weighted Normalized Decision Matrix is calculated by multiplying the normalized decision matrix by the weights.

![image](https://user-images.githubusercontent.com/44522286/131340240-28dd0e6c-09db-4eef-a3c3-99c9ad0ac9ab.png)

 This multiplication is performed in the Weighted_Normalized_Decision_Matrix.py file. Now, we have a weighted normalized decision matrix as follows:
 
 ![image](https://user-images.githubusercontent.com/44522286/131340385-b783aa08-cbbe-4987-8ac1-7bfeb839b793.png)

## 3)	Ideal Solutions
As was mentioned, TOPSIS strives to minimize the distance between the positive ideal solution and the chosen alternative, as well as to maximize the distance between the negative ideal solution and the chosen alternative. But what are the positive and negative ideal solutions? 

If our attribute or criterion is profit-based, positive ideal solution (PIS) and negative ideal solution (NIS) are:

![image](https://user-images.githubusercontent.com/44522286/131340856-bcc7f6b3-a812-4b0a-8e1a-7f1c8345094f.png)

If our attribute or criterion is cost-based, positive ideal solution (PIS) and negative ideal solution (NIS) are:

![image](https://user-images.githubusercontent.com/44522286/131340875-ee1777de-cacf-4725-ac2d-2c9bb870e513.png)

In our code, ideal solutions are calculated in Ideal_Solution.py.

4)	Separation measures
It is necessary to introduce a measure that can measure how far alternatives are from the ideal solutions. Our measure comprise two main sections:
The separation of each alternative from the PIS is calculated as follows:

![image](https://user-images.githubusercontent.com/44522286/131340929-b68fa07a-1728-41ac-938b-da4fd0a74cd3.png)

Also, the separation of each alternative from the NIS is calculated as follows:

![image](https://user-images.githubusercontent.com/44522286/131340955-ce9e05d2-bfb4-4544-8d0b-609623881f5f.png)

5)	Closeness to the Ideal Solution
Now that the distance between ideal solutions and alternatives has been calculated, we rank our alternatives according to how close they are to ideal solutions. The distance measure is calculated by the following formula:

![image](https://user-images.githubusercontent.com/44522286/131340990-f18f6d58-93f1-419a-958e-281accd36cfa.png)

It is clear that :

![image](https://user-images.githubusercontent.com/44522286/131341036-7899bc44-4e7b-401b-8c3e-7e22fffd571d.png)

## 6)	Ranking
Now, alternatives are ranked in decreasing order based on closeness to the ideal solution. Both of (5) and (6) are calculated in Distance_Between_Ideal_and_Alternatives.py.
## 7)	TOPSIS
In this section, all of the previous .py files are employed and utilized in an integrated way.


## References
1.	 Hwang, C.L.; Yoon, K. (1981). Multiple Attribute Decision Making: Methods and Applications. New York: Springer-Verlag.: https://www.springer.com/gp/book/9783540105589
2.	 Assari, A., Mahesh, T., & Assari, E. (2012b). Role of public participation in sustainability of historical city: usage of TOPSIS method. Indian Journal of Science and Technology, 5(3), 2289-2294.
3.	Jahanshahloo, G.R., Lotfi, F.H. and Izadikhah, M., 2006. An algorithmic method to extend TOPSIS for decision-making problems with interval data. Applied mathematics and computation, 175(2), pp.1375-1384.
4.	Vafaei, N., Ribeiro, R.A. and Camarinha-Matos, L.M., 2018. Data normalization techniques in decision making: case study with TOPSIS method. International journal of information and decision sciences, 10(1), pp.19-38.
