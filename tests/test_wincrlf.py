import os
import pprint
import unittest
import zipfile


class WincflfTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_readfile(self):
        realpath = 'canshu/wincflf.sh'
        f = open(realpath, 'r', encoding='utf-8')
        data = f.read()
        f.close()
        pprint.pprint(data)

    def test_zipfile(self):
        project_path = 'canshu'
        zipfile_realpath = project_path + '.zip'
        tmpfile = zipfile.ZipFile(zipfile_realpath, 'w')
        for writepath in os.listdir(project_path):
            realpath = os.path.join(project_path, writepath)
            import sys
            if sys.version_info[0] == 2:
                f = open(realpath, 'rb')
                data = f.read()
                data = data.decode('utf-8')
                f.close()
            else:
                f = open(realpath, 'r', encoding='utf-8')
                data = f.read()
                f.close()
            data_replaced = data.replace('\r\n', '\n')
            tmpfile.writestr(writepath, data_replaced)
