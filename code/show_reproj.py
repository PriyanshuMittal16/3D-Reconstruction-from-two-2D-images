import numpy as np
import matplotlib.pyplot as plt

def show_reprojections(image1, image2, uncalibrated_1, uncalibrated_2, P1, P2, K, T, R, plot=True):

  """ YOUR CODE HERE
  """
  P1proj = []
  P2proj= []
  m=P2.shape[0]
  
  
  for i in range(m):
    A=np.matmul(K,(np.matmul(R, P1[i]))+T)
    P1proj.append(A)
    B=np.matmul(K, (np.matmul(R.T, P2[i]-T)))
    P2proj.append(B)
    P1proj = np.array(P1proj) 
    P2proj = np.array(P2proj)
  

  # P1proj = np.array(P1proj) 
  # P2proj = np.array(P2proj)
  # P1proj = []
  # P2proj= []
  # num_points = P2.shape[0]

  # for i in range (m):
  #   P1_temp = K @ (( R @ P1[i] ) + T)
  #   P1proj.append(P1_temp)
  #   P2_temp = K @ (R.T @ (P2[i] - T))
  #   P2proj.append(P2_temp)

  P1proj = np.array(P1proj) 
  P2proj = np.array(P2proj)

  
  
  # un1=np.hstack((P1, ones))
  # un2=np.hstack((P2,ones))


  # P=np.matmul(np.matmul(K,H),P1)
  # P1proj = np.matmul(k_inv, un1).T
  # P2proj = np.matmul(k_inv, un2).T


  
  """ END YOUR CODE
  """

  if (plot):
    plt.figure(figsize=(6.4*3, 4.8*3))
    ax = plt.subplot(1, 2, 1)
    ax.set_xlim([0, image1.shape[1]])
    ax.set_ylim([image1.shape[0], 0])
    plt.imshow(image1[:, :, ::-1])
    plt.plot(P2proj[:, 0] / P2proj[:, 2],
           P2proj[:, 1] / P2proj[:, 2], 'bs')
    plt.plot(uncalibrated_1[0, :], uncalibrated_1[1, :], 'ro')

    ax = plt.subplot(1, 2, 2)
    ax.set_xlim([0, image1.shape[1]])
    ax.set_ylim([image1.shape[0], 0])
    plt.imshow(image2[:, :, ::-1])
    plt.plot(P1proj[:, 0] / P1proj[:, 2],
           P1proj[:, 1] / P1proj[:, 2], 'bs')
    plt.plot(uncalibrated_2[0, :], uncalibrated_2[1, :], 'ro')
    
  else:
    return P1proj, P2proj