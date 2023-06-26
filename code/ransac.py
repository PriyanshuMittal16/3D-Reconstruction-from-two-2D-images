from lse import least_squares_estimation
import numpy as np

def ransac_estimator(X1, X2, num_iterations=60000): #60000
    sample_size = 8

    eps = 10**-4

    best_num_inliers = -1
    best_inliers = None
    best_E = None
    # inliers =[]
    """ YOUR CODE HERE
    """

    for i in range(num_iterations):
        # permuted_indices = np.random.permutation(np.arange(X1.shape[0]))
        inliers=np.zeros((1,3))
        permuted_indices = np.random.RandomState(seed=(i*10)).permutation(np.arange(X1.shape[0]))
        sample_indices = permuted_indices[:sample_size]
        test_indices = permuted_indices[sample_size:]
        print(permuted_indices)
    

        for k in range (sample_size):
            # print(sample_size)
            j=sample_indices[k]
            a=X1[j]
            b=X2[j]
            
            if k==0:
                C=a
                D=b
            else:
                C=np.vstack((C,a))
                D=np.vstack((D,b))

        # print(C)
        # print(D)
        E=least_squares_estimation(C,D)
        e3=np.array([[0,-1,0], [1,0,0],[0,0,0]])
        # print(E)

        count=0
        inliers=sample_indices    #didn't knew to do, checked from piazza
        test_indices=np.array(test_indices)
        m=len(test_indices)
        # print(len(test_indices))
        count=0

        for lj in range (m):
            l=test_indices[lj]
            # print(l)
            xf1=X1[l,:]
            xf2=X2[l,:]
            # print(np.shape(xf1))
            # print(xf1)

            num1=np.matmul(xf2.T,np.matmul(E,xf1)) 
            num1p=np.power(num1,2)
            den1=np.matmul(e3, np.matmul(E, xf1))
            den1n=np.linalg.norm(den1)
            den1p=np.power(den1n,2)
            depx1=num1p/den1p
            # print(np.shape(depx1))


            num2=np.matmul(xf1.T,np.matmul(E.T,xf2)) 
            num2p=np.power(num2,2)
            den2=np.matmul(e3, np.matmul(E.T, xf2))
            den2n=np.linalg.norm(den2)
            den2p=np.power(den2n,2)
            depx2=num2p/den2p
            count+=1
            dsum =depx1+depx2
            # dsum = 10**-5
            # print(dsum)
            # print(count)
            
            if(dsum<eps):
                # inliers=np.append(inliers, l)
                inliers=np.hstack((inliers, l))
                
            # inliers = np.concatenate((sample_indices, inliers))
        

        """ END YOUR CODE
        """
        # print(np.shape(inliers))
        if inliers.shape[0] > best_num_inliers:
            best_num_inliers = inliers.shape[0]
            best_E = E
            best_inliers = inliers


    return best_E, best_inliers

if __name__ == "__main__":

    Pc=np.array([[0,1,3],[1,1,8],[1,0,10],[0,0,5], [0,2,3],[6,1,8],[1,9,10],[0,0,2], [8,1,3],[1,5,8],[7,0,10],[2,0,5], [0,1,3],[1,1,8],[1,0,10],[0,0,5], [0,2,3],[6,1,8],[1,9,10],[0,0,2], [8,1,3],[1,5,8],[7,0,10],[2,0,5]])
    Pw=np.array([[3,2,5],[2,1,6],[8,5,6],[7,8,3], [3,2,5],[8,1,6],[8,9,3],[7,7,7], [3,1,4],[5,9,6],[8,2,6],[7,8,5], [3,2,5],[2,1,6],[8,5,6],[7,8,3], [3,2,5],[8,1,6],[8,9,3],[7,7,7], [3,1,4],[5,9,6],[8,2,6],[7,8,5]])
    x= ransac_estimator(Pc,Pw)   