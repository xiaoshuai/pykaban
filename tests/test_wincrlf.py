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

    def test_zipdir(self):
        project_path = 'canshu'
        zipfile_realpath = project_path + '.zip'
        tmpfile = zipfile.ZipFile(zipfile_realpath, 'w')

        def write2zipfile(realpath, writepath):
            need_win_patch = False
            if realpath.endswith('.sh'):
                need_win_patch = True
            if realpath.endswith('.job'):
                need_win_patch = True
            if need_win_patch:
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
                data_replaced = data.replace("\r\n", "\n")
                tmpfile.writestr(writepath, data_replaced)
            else:
                tmpfile.write(realpath, writepath)

        for basename_l1 in os.listdir(project_path):
            realpath_l1 = os.path.join(project_path, basename_l1)
            if os.path.isdir(realpath_l1):
                for basename_l2 in os.listdir(realpath_l1):
                    realpath_l2 = os.path.join(realpath_l1, basename_l2)
                    if basename_l2.endswith('pyc'):
                        continue
                    if os.path.isfile(realpath_l2):
                        write2zipfile(realpath_l2, basename_l1 + '/' + basename_l2)
            else:
                write2zipfile(realpath_l1, basename_l1)
        tmpfile.close()
