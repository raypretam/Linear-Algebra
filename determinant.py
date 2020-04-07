import numpy as np

'''
A=np.array([[2,3],[1,2]])
print(A[0,0]*A[1,1] - A[1,0]*A[0,1])
'''
def findDet(A,total=0):
    dim=A.shape[0]
    if dim==2:
        det=A[0,0]*A[1,1] - A[1,0]*A[0,1]
        return det
    else:
        A1=A.copy()
        #Delete the first rowValue
        A1=np.delete(A1,0,0)
        cols=A.shape[1]
        for i in range(cols):
            A2=np.delete(A1,i,1) #delete the corresponding column
            total+=(-1)**i * A[0,i] * findDet(A2)
        return total

A = np.random.normal(0,10,(3,3))
print("The determinant using numpy",np.linalg.det(A))

print("The determinant using hardcode recursion",findDet(A))
