import pykaban
import json
import unittest


class AzkabanpyTestCase(unittest.TestCase):
    def setUp(self):
        try:
            main_params = {}
            with open('../params.py') as f:
                exec(f.read(), main_params)  # pylint: disable=exec-used
            p_1 = main_params['server_url']
            p_2 = main_params['username']
            p_3 = main_params['password']
            self.ajax_api = pykaban.AjaxAPI(server_url=p_1, username=p_2, password=p_3)
            self.ajax_api.authenticate()
        except KeyError:
            raise Exception("fail to init")

    def tearDown(self):
        pass

    def test_authenticate(self):
        pass

    def test_upload_project_zip(self):
        self.ajax_api.upload_project_zip(project_path='canshu', project_name='aaaa')

    def test_upload_project_schedule(self):
        schedule_item_dict = {}
        project_name, schedule_item_dict = self.ajax_api.upload_project_schedule(project_path='canshu',
                                                                                 project_name=None)
        print(project_name)
        print(schedule_item_dict)

    def test_upload_project_schedule(self):
        project_name, schedule_item_dict = self.ajax_api.upload_project_schedule(project_path='canshu', project_name='aaaa')
        for (flow_name, cron_expression) in schedule_item_dict.items():
            self.ajax_api.flexible_schedule(project_name=project_name,
                                            flow_name=flow_name, cron_expression=cron_expression)
