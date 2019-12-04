from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.10'
__uuid__ = "60cac28d-efe6-4a8d-802f-fa4fc94fa741"

__docformat__ = "restructuredtext en"

import unittest
import os
import sys

#from testdata.YapyData_testdata import mypath
from yapydata.datatree.datatree import DataTree



class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
 #       sys.path.insert(0, mypath) 
        self.maxDiff = None

    def testCase010(self):
        class ContainerOfD(object):
            D = 123

        class ContainerOfC(object):
            C = [
                    ContainerOfD
                ]

        B = ContainerOfC
        
        ContainerOfB = set([1, 2, 'a', B, 3])             

        _cap = DataTree(
                {
                    'A': ContainerOfB
                }
            )
        
        fordebug = _cap('A', B, 'C', 0, 'D', direction='down', pysyn=True)
        
        self.assertEqual(_cap('A', B, 'C', 0, 'D', direction='down', pysyn=True), 123)

#         fordebug = _cap('A', 'B', 'C', 0, 'D', direction='down', pysyn=True)
#         
#         self.assertEqual(_cap('A', 'B', 'C', 0, 'D', direction='down', pysyn=True), 123)

if __name__ == '__main__':
    unittest.main()
