"""
Created on January 12, 2016

@author: Cmunoz

This Module is a container of methods based on spicey 
"""

import logging
import numpy as np
# from spiceypy import wrapper as spi
import spiceypy as spi


class RefFrame(object):
    """ This class allows to ....
    """

    def __init__(self):
        pass

    def vecxyz2newRefFrame(self, vec, refTime, newRefFrame, currentRefFrame='J2000'):
        """ Translates vec in cartesian coordinate from currentRefFrame to newRefFrame
            input
            - vec
            ouput: 
            - vec in newRefFrame
        """

        logging.debug('inputVec={0}; refTime={1}; newRefFrame={2}; currentRefFrame={3}\n'.format(
            vec, refTime, newRefFrame, currentRefFrame))
        # vec = np.transpose(np.matrix(vec))
        mrot = np.matrix(spi.pxform(currentRefFrame, newRefFrame, refTime))
        vecNewRef = np.dot(mrot, vec).A1  # MROT*tVEC  and collapse vector for Matrix to 1D array format
        logging.debug('vecNewRef={0}'.format(vecNewRef))

        return vecNewRef

    def vecxyzList2newRefFrame(self, xL, yL, zL, timeL, newRefFrame, currentRefFrame='J2000'):
        """ Translates cartesian coordinate list from currentRefFrame to newRefFrame
        """

        (xL_inNewFrame, yL_inNewFrame, zL_inNewFrame) = ([], [], [])
        for i in range(len(timeL)):
            vec = self.vecxyz2newRefFrame([xL[i], yL[i], zL[i]], timeL[i], newRefFrame, currentRefFrame)
            xL_inNewFrame.append(vec[0])
            yL_inNewFrame.append(vec[1])
            zL_inNewFrame.append(vec[2])

        return (xL_inNewFrame, yL_inNewFrame, zL_inNewFrame)

    def vecposList2newRefFrame(self, posvecL, timeL, newRefFrame, currentRefFrame='J2000'):
        """ Translates position vector list in cartesian coordinates from currentRefFrame to newRefFrame
        """

        new_posvecL = []
        for i in range(len(timeL)):
            new_posvecL.append(self.vecxyz2newRefFrame(posvecL[i], timeL[i], newRefFrame, currentRefFrame))

        return new_posvecL

    def getKernelLoadedInfo(self):
        """ Returns the current list of kernel loaded in spice  
        """
        kInfo = []
        kcount = spi.ktotal('All')
        kInfo.append(kcount)
        for i in range(kcount):
            kInfo.append(spi.kdata(i, 'All', 256, 256, 256))

        return kInfo


if __name__ == '__main__':
    pass
