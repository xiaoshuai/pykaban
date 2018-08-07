import requests

from ._utils import parser_response_content as _parser


class AjaxAPI(object):
    def __init__(
            self,
            server_url='https://localhost:8443',
            username='azkaban',
            password='azkaban',
            **kwargs):
        self._server_url = server_url
        self._username = username
        self._password = password
        self._session_id = ''
        if 'expires' in kwargs:
            self._expires = kwargs['expires']
        else:
            self._expires = 5

    def authenticate(self, username=None, password=None):
        """
        验证
        :param username: The Azkaban username.
        :param password: The corresponding password.
        :return: error:	Return an error message if the login attempt fails.
        """
        self._username = username or self._username
        self._password = password or self._password
        try:
            response = requests.post(
                url=self._server_url + '/manager',
                headers={
                    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                },
                data={
                    "action": "login",
                    "username": self._username,
                    "password": self._password,
                },
            )
            assert response.status_code == 200
            resp = _parser(response.content)
            if 'session.id' in resp:
                self._session_id = resp['session.id']
                print('[authenticate] success session.id={session_id}.'.format(session_id=self._session_id))
        except requests.exceptions.RequestException:
            print('HTTP Request failed')

    def create_project(self, project_name, project_description):
        """
        创建项目
        """
        try:
            response = requests.post(
                url=self._server_url,
                headers={
                    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                },
                data={
                    "session.id": self._session_id,
                    "action": "create",
                    "name": project_name,
                    "description": project_description,
                },
            )
            assert response.status_code == 200
            resp = _parser(response.content)
            if 'status' in resp and resp['status'] == 'success':
                project_path = resp['path']
                print('[create_project] success path={project_path}.'.format(project_path=project_path))
                return project_path
        except requests.exceptions.RequestException:
            print('HTTP Request failed')

    def delete_project(self, project_name):
        """
        删除项目
        """
        try:
            response = requests.get(
                url=self._server_url + '/manager',
                params={
                    "session.id": self._session_id,
                    "delete": "true",
                    "project": project_name,
                },
                headers={
                    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                },
            )
            assert response.status_code == 200
            print('[delete_project] success project={project_name}.'.format(project_name=project_name))
        except requests.exceptions.RequestException:
            print('HTTP Request failed')

    def upload_project_zip(self, project_path, project_name=None):
        """
        上传项目Zip包
        """
        import os
        import zipfile
        if project_path.endswith('/'):
            project_path = project_path[0:len(project_path) - 1]
        if not project_name:
            project_name = os.path.basename(project_path)
        zipfile_realpath = project_path + '.zip'
        zipfile_basename = os.path.basename(zipfile_realpath)
        tmpfile = zipfile.ZipFile(zipfile_realpath, 'w')
        for basename_l1 in os.listdir(project_path):
            realpath_l1 = os.path.join(project_path, basename_l1)
            if os.path.isdir(realpath_l1):
                for basename_l2 in os.listdir(realpath_l1):
                    realpath_l2 = os.path.join(realpath_l1, basename_l2)
                    if basename_l2.endswith('pyc'):
                        continue
                    if os.path.isfile(realpath_l2):
                        tmpfile.write(realpath_l2, basename_l1 + '/' + basename_l2)
            else:
                tmpfile.write(realpath_l1, basename_l1)
        tmpfile.close()
        try:
            response = requests.post(
                url=self._server_url,
                files={
                    "file": (zipfile_basename, open(zipfile_realpath, 'rb'), 'application/zip', {'Expires': '5'}),
                },
                data={
                    "session.id": self._session_id,
                    "ajax": "upload",
                    "project": project_name,
                },
            )
            assert response.status_code == 200
            resp = _parser(response.content)
            os.remove(zipfile_realpath)
            if 'projectId' in resp and 'version' in resp:
                project_id = resp['projectId']
                project_version = resp['version']
                print('[upload_project_zip] success projectId={project_id} version={project_version}.'
                      .format(project_id=project_id, project_version=project_version))
                return project_id
        except requests.exceptions.RequestException:
            print('HTTP Request failed')
            os.remove(zipfile_realpath)

    def fetch_flows_of_project(self):
        """
        获取项目的流程
        """
        pass

    def fetch_jobs_of_flow(self):
        """
        获取流程的作业
        """
        pass

    def fetch_executions_of_flow(self):
        """
        获取流程的执行
        """
        pass

    def fetch_running_executions_of_flow(self):
        """
        获取正运行的执行
        """
        pass

    def execute_flow(self):
        """
        执行流程
        """
        pass

    def cancel_flow_execution(self):
        """
        取消流程执行
        """
        pass

    def schedule_flow(self):
        """
        调度期限流程（已废弃）
        """
        pass

    def flexible_schedule(self, project_name, flow_name, cron_expression):
        """
        使用Cron灵活调度
        :param project_name: The name of the project.
        :param flow_name: The name of the flow.
        :param cron_expression: A CRON expression is a string comprising 6 or 7 fields separated by white space that represents a set of times. In azkaban, we use Quartz Cron Format.
        :return:
        """
        try:
            response = requests.post(
                url=self._server_url + '/schedule',
                headers={
                    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                },
                data={
                    "session.id": self._session_id,
                    "ajax": "scheduleCronFlow",
                    "name": project_name,
                    "flow": flow_name,
                    "cronExpression": cron_expression,
                },
            )
            assert response.status_code == 200
            resp = _parser(response.content)

            if 'status' in resp and resp['status'] == 'success':
                schedule_id = resp['scheduleId']
                print('[create_project] success path={schedule_id}.'.format(schedule_id=schedule_id))
                return schedule_id
        except requests.exceptions.RequestException:
            print('HTTP Request failed')

    def fetch_schedule(self):
        """
        获取计划
        """
        pass

    def unschedule_flow(self):
        """
        取消调度流程
        """
        pass

    def set_sla(self):
        """
        设置SLA
        """
        pass

    def fetch_sla(self):
        """
        获取SLA
        """
        pass

    def pause_flow_execution(self):
        """
        暂停流程执行
        """
        pass

    def resume_flow_execution(self):
        """
        恢复流程执行
        """
        pass

    def fetch_flow_execution(self):
        """
        获取流程执行
        """
        pass

    def fetch_execution_job_logs(self):
        """
        获取执行作业日志
        """
        pass

    def fetch_flow_execution_updates(self):
        """
        获取流程执行更新
        """
        pass
