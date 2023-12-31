import numpy as np

def reconstruct3D( transform_candidates, calibrated_1, calibrated_2):
  """This functions selects (T,R) among the 4 candidates transform_candidates
  such that all triangulated points are in front of both cameras.
  """

  best_num_front = -1
  best_candidate = None
  best_lambdas = None
  for candidate in transform_candidates:
    R = candidate['R']
    T = candidate['T']
  
  # for i in range (4):
  #   T=np.array([0,1,3]).reshape(3,1)
  #   R=np.array([[0,1,3],[1,1,8],[1,0,10]])

    lambdas = np.zeros((2, calibrated_1.shape[0]))
    
    """ YOUR CODE HERE
    """
    # x1=calibrated_1
    # x2=calibrated_2

    for i in range (calibrated_1.shape[0]):
      x1=calibrated_1[i,:].reshape(3,1)
      x2=calibrated_2[i,:].reshape(3,1)

      Rx1=np.matmul(R,x1)

      P=np.hstack((x2, -Rx1))
      # print(np.shape(P))

      Pinv=np.linalg.pinv(P)
      # print(np.shape(Pinv))
      a=np.matmul(Pinv,T)

      lambdas[0][i]=a[0]
      lambdas[1][i]=a[1]


    # print(lambdas)
    """ END YOUR CODE
    """
    num_front = np.sum(np.logical_and(lambdas[0]>0, lambdas[1]>0))

    if num_front > best_num_front:
      best_num_front = num_front
      best_candidate = candidate
      best_lambdas = lambdas
      print("best", num_front, best_lambdas[0].shape)
    else:
      print("not best", num_front)


  P1 = best_lambdas[1].reshape(-1, 1) * calibrated_1
  P2 = best_lambdas[0].reshape(-1, 1) * calibrated_2
  T = best_candidate['T']
  R = best_candidate['R']
  return P1, P2, T, R


if __name__ == "__main__":

    Pc=np.array([[0,1,3],[1,1,8],[1,0,10],[0,0,5], [0,2,3],[6,1,8],[1,9,10],[0,0,2], [8,1,3],[1,5,8],[7,0,10],[2,0,5], [0,1,3],[1,1,8],[1,0,10],[0,0,5], [0,2,3],[6,1,8],[1,9,10],[0,0,2], [8,1,3],[1,5,8],[7,0,10],[2,0,5]])
    Pw=np.array([[3,2,5],[2,1,6],[8,5,6],[7,8,3], [3,2,5],[8,1,6],[8,9,3],[7,7,7], [3,1,4],[5,9,6],[8,2,6],[7,8,5], [3,2,5],[2,1,6],[8,5,6],[7,8,3], [3,2,5],[8,1,6],[8,9,3],[7,7,7], [3,1,4],[5,9,6],[8,2,6],[7,8,5]])
    T1=np.array([0,1,3]).reshape(3,1)
    T2=np.array([8,1,6]).reshape(3,1)
    T3=np.array([1,0,10]).reshape(3,1)
    T4=np.array([5,9,6]).reshape(3,1)

    R1=np.array([[0,1,3],[1,1,8],[1,0,10]])
    R2=np.array([[8,1,6],[8,9,3],[7,7,7]])
    R3=np.array([[3,2,5],[2,1,6],[8,5,6]])
    R4=np.array([[1,1,8],[1,0,10],[0,0,5]])

    transform_candidates = {}
    transform_candidates.setdefault('T', {})['T1']=T1
    transform_candidates.setdefault('T', {})['T2']=T2
    transform_candidates.setdefault('T', {})['T3']=T3
    transform_candidates.setdefault('T', {})['T4']=T4

    transform_candidates.setdefault('R', {})['R1']=R1
    transform_candidates.setdefault('R', {})['R2']=R2
    transform_candidates.setdefault('R', {})['R3']=R3
    transform_candidates.setdefault('R', {})['R4']=R4
    
    
    # transform_candidates = {'T':[T1, T2, T3, T4], 'R':[R1, R2, R3, R4]}

    x= reconstruct3D(transform_candidates,Pc,Pw)  