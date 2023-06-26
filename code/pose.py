import numpy as np

def pose_candidates_from_E(E):
  transform_candidates = []
  ##Note: each candidate in the above list should be a dictionary with keys "T", "R"
  """ YOUR CODE HERE
  """
  R90=np.array([[0,-1,0],[1,0,0],[0,0,1]])
  Rm90=np.array([[0,1,0],[-1,0,0],[0,0,1]])
  [U,S,VT]=np.linalg.svd(E)

  T1=U[:,2]
  R1=np.matmul(U, np.matmul(R90.T,VT))

  T2=U[:,2]
  R2=np.matmul(U, np.matmul(Rm90.T,VT))

  T3=-U[:,2]
  R3=np.matmul(U, np.matmul(R90.T,VT))

  T4=-U[:,2]
  R4=np.matmul(U, np.matmul(Rm90.T,VT))

  # transform_candidates = {'T':[T1, T2, T3, T4], 'R':[R1, R2, R3, R4]}
  canidatel = {}
  canidatel['T'] = T1
  canidatel['R'] = R1
  transform_candidates.append(canidatel)

  canidate2 = {}
  canidate2['T'] = T2
  canidate2['R'] = R2
  transform_candidates.append(canidate2)

  canidate3 = {}
  canidate3['T'] = T3
  canidate3['R'] = R3
  transform_candidates.append(canidate3)

  canidate4 = {}
  canidate4['T'] = T4
  canidate4['R'] = R4
  transform_candidates.append(canidate4)
  # print(transform_candidates)



  """ END YOUR CODE
  """
  return transform_candidates


if __name__ == "__main__":

    Pc=np.array([[0,1,3],[1,1,8],[1,0,10]])
    # Pw=np.array([[3,2,5],[2,1,6],[8,5,6],[7,8,3], [3,2,5],[8,1,6],[8,9,3],[7,7,7], [3,1,4],[5,9,6],[8,2,6],[7,8,5], [3,2,5],[2,1,6],[8,5,6],[7,8,3], [3,2,5],[8,1,6],[8,9,3],[7,7,7], [3,1,4],[5,9,6],[8,2,6],[7,8,5]])
    x= pose_candidates_from_E(Pc)  