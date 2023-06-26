import matplotlib
import matplotlib.pyplot as plt
import numpy as np 
import cv2

def plot_lines(lines, h, w):
    """ Utility function to plot lines
    """

    for i in range(lines.shape[1]):
        # plt.close('all')
        if abs(lines[0, i] / lines[1, i]) < 1:
            y0 = -lines[2, i] / lines[1, i]
            yw = y0 - w * lines[0, i] / lines[1, i]
            plt.plot([0, w], [y0, yw])
            # plt.clf()
            # plt.show()
            # plt.savefig(filename)
        else:
            x0 = -lines[2, i] / lines[0, i]
            xh = x0 - h * lines[1, i] / lines[0, i]
            plt.plot([x0, xh], [0, h])
            # plt.clf
            # plt.show()
            # plt.savefig(filename)


def plot_epipolar_lines(image1, image2, uncalibrated_1, uncalibrated_2, E, K, plot=True):
    """ Plots the epipolar lines on the images
    """

    """ YOUR CODE HERE
    """
    f=552,
    u0=307.5
    v0=205
    m,d=np.shape(uncalibrated_1)
    # print(m)
    # print(d)
    epipolar_lines_in_1=[]
    epipolar_lines_in_2=[]
    # K=np.array([[f,0,u0],[0,f,v0],[0,0,1]])
    u1=uncalibrated_1
    u2=uncalibrated_2
    K_inv=np.linalg.inv(K)
    F=np.matmul(K_inv.T, np.matmul(E,K_inv))
    
    for i in range(u1.shape[1]):
        
        ru1=[j[i] for j in u1]
        
        ru2=[j[i] for j in u2]
        epipolar_lines_in_1.append( np.dot(F.T, ru2))
        epipolar_lines_in_2.append( np.dot(F,ru1))

    #don't knwo why specifically we have to do like this
    
    epipolar_lines_in_1=np.transpose(epipolar_lines_in_1)
    epipolar_lines_in_2=np.transpose(epipolar_lines_in_2)
    
    """ END YOUR CODE
    """
    
    if(plot):

        plt.figure(figsize=(6.4*3, 4.8*3))
        ax = plt.subplot(1, 2, 1)
        ax.set_xlim([0, image1.shape[1]])
        ax.set_ylim([image1.shape[0], 0])
        plt.imshow(image1[:, :, ::-1])
        plot_lines(epipolar_lines_in_1, image1.shape[0], image1.shape[1])

        ax = plt.subplot(1, 2, 2)
        ax.set_xlim([0, image1.shape[1]])
        ax.set_ylim([image1.shape[0], 0])
        plt.imshow(image2[:, :, ::-1])
        plot_lines(epipolar_lines_in_2, image2.shape[0], image2.shape[1])
        
    else:
        return epipolar_lines_in_1, epipolar_lines_in_2
    


    