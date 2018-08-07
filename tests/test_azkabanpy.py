import pykaban
import json
import unittest


class pykabanTestCase(unittest.TestCase):
    def setUp(self):
        try:
            main_params = {}
            exec(open('../params.py').read(), main_params)  # pylint: disable=exec-used
            p_1 = main_params['server_url']
            p_2 = main_params['username']
            p_3 = main_params['password']
            self.ajax_api = pykaban.pykaban.AjaxAPI(server_url=p_1, username=p_2, password=p_3)
            self.ajax_api.authenticate()
        except KeyError:
            raise Exception("fail to init")

    def tearDown(self):
        pass

    def test_authenticate(self):
        pass
