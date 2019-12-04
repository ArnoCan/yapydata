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
import json

from yapydata.datatree.synjson import DataTreeJSON
from yapydata.datatree.synyaml import DataTreeYAML, YapyDataYAMLError



class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
#       sys.path.insert(0, mypath) 
        self.maxDiff = None

    def testCase010(self):
        _cap = DataTreeYAML()
        _cap.import_data(os.path.dirname(__file__) + os.sep + 'data')
        
        with open(os.path.dirname(__file__) + os.sep + 'data.json') as data_file:
            resx = json.load(data_file)

#         print("4TEST:_cap.data = <%s>" % (str(_cap.data)))
#         print("4TEST:resx      = <%s>" % (str(resx)))

        self.assertEqual(_cap.data, resx)


if __name__ == '__main__':
    unittest.main()

