import numpy as np

def least_squares_estimation(X1, X2):
  """ YOUR CODE HERE
  """

  p=X1[0:8,:]
  q=X2[0:8,:]   # Can interchange p and q
  m,d=np.shape(X1)
  A=np.zeros((m,9))
  # a0=np.matmul(q[0,:].T.reshape(3,1), p[0,:].reshape(1,3)).flatten()
  # a1=np.matmul(q[1,:].T.reshape(3,1), p[1,:].reshape(1,3)).flatten()
  # a2=np.matmul(q[2,:].T.reshape(3,1), p[2,:].reshape(1,3)).flatten()
  # a3=np.matmul(q[3,:].T.reshape(3,1), p[3,:].reshape(1,3)).flatten()
  # a4=np.matmul(q[4,:].T.reshape(3,1), p[4,:].reshape(1,3)).flatten()
  # a5=np.matmul(q[5,:].T.reshape(3,1), p[5,:].reshape(1,3)).flatten()
  # a6=np.matmul(q[6,:].T.reshape(3,1), p[6,:].reshape(1,3)).flatten()
  # a7=np.matmul(q[7,:].T.reshape(3,1), p[7,:].reshape(1,3)).flatten()

  for i in range (m):
     x=X1[i,0]*X2[i,:]
     y=X1[i,1]*X2[i,:]
     z=X1[i,2]*X2[i,:]
     A[i,:]=np.hstack((x,y,z))

  #I was doing by taking only the first 8 points as described in class
  # But actually we have to calculate A by taking into account all the points
  # So the size of A is mx9

  [u1, s1,v1] = np.linalg.svd(A)

  En= v1[8,:]
  E_Dash=np.array([[En[0],En[3],En[6]], [En[1],En[4],En[7]], [En[2],En[5],En[8]]])

  [u, s,v] = np.linalg.svd(E_Dash)

  sigma=np.array([[1,0,0],[0,1,0],[0,0,0]])

  E=np.matmul(u, np.matmul(sigma, v))
  print(s)
  

  return E
  




  """ END YOUR CODE
  """
  # return p

if __name__ == "__main__":

    Pc=np.array([[0,1,3],[1,1,8],[1,0,10],[0,0,5], [0,2,3],[6,1,8],[1,9,10],[0,0,2], [8,1,3],[1,5,8],[7,0,10],[2,0,5]])
    Pw=np.array([[3,2,5],[2,1,6],[8,5,6],[7,8,3], [3,2,5],[8,1,6],[8,9,3],[7,7,7], [3,1,4],[5,9,6],[8,2,6],[7,8,5]])
    x= least_squares_estimation(Pc,Pw)   
