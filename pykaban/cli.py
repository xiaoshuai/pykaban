# -*- coding: utf-8 -*-
from __future__ import print_function
import sys

if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding("utf-8")
import click
import os
import sys
import pykaban


@click.command()
@click.option('--server-url', default=None, help='The homepage of azkaban like "https://localhost:8443"')
@click.option('--username', default=None, help='The username of azkaban')
@click.option('--password', default=None, help='The password of azkaban')
@click.option('--project-path', prompt='Project path', help='The project path of azkaban.')
@click.option('--project-name', default=None, help='The project name of azkaban.')
def deploy(server_url, username, password, project_path, project_name):
    """部署程序到线上服务器"""
    import os
    rc_file = os.path.join(os.path.expanduser('~'), '.pykabanrc')
    if not os.path.isfile(rc_file):
        new_file = open(rc_file, 'w+')
        new_file.write("server_url = 'https://localhost:8443'\nusername = 'azkaban'\npassword = 'azkaban'\n")
        new_file.close()
    main_params = {}
    with open(rc_file) as f:
        exec(f.read(), main_params)  # pylint: disable=exec-used
    if not server_url:
        server_url = main_params['server_url']
    if not username:
        username = main_params['username']
    if not password:
        password = main_params['password']
    if project_path.endswith('/'):
        project_path = project_path[0:len(project_path) - 1]
    if not project_path.startswith('/'):
        project_path = os.path.join(os.getcwd(), project_path)
        project_path = os.path.realpath(project_path)
    click.echo('[pykaban][cli] finish init user ({username}) of azkaban({server_url}).'
               .format(username=username, server_url=server_url))
    # deploy
    click.echo('[pykaban][cli] deploy ({project_path}) to azkaban({server_url}) start.'
               .format(project_path=project_path, server_url=server_url))
    ajax_api = pykaban.AjaxAPI(server_url=server_url, username=username, password=password)
    ajax_api.authenticate()
    ajax_api.upload_project_zip(project_path=project_path, project_name=project_name)
    click.echo('[pykaban][cli] deploy ({project_path}) to azkaban({server_url}) success.'
               .format(project_path=project_path, server_url=server_url))

    # schedule
    click.echo('[pykaban][cli] schedule ({project_path}) to azkaban({server_url}) start.'
               .format(project_path=project_path, server_url=server_url))
    project_name, schedule_item_dict = ajax_api.upload_project_schedule(project_path=project_path,
                                                                        project_name=project_name)
    for (flow_name, cron_expression) in schedule_item_dict.items():
        ajax_api.flexible_schedule(project_name=project_name, flow_name=flow_name, cron_expression=cron_expression)
    click.echo('[pykaban][cli] schedule ({project_path}) to azkaban({server_url}) success.'
               .format(project_path=project_path, server_url=server_url))


if __name__ == '__main__':
    deploy()
