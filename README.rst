pykaban
========================================
* 使用Python执行阿兹卡班的AJAX接口
* 使用Python创建阿兹卡班任务流程
* 使用Python管理阿兹卡班流程调度


A Python client for Azkaban AJAX API
----------------------------------------
目前已经完成如下接口
* 验证接口 ``api-authenticate``
* 创建项目接口 ``api-create-a-project``
* 删除项目接口 ``api-delete-a-project``
* 上传项目Zip包接口 ``api-upload-a-project-zip``
* 使用Cron灵活调度接口 ``api-flexible-schedule``

Create Flow with Pythonic API
----------------------------------------
规划中

Customized Account Support
----------------------------------------
* 用户账户在``$HOME/.pykabanrc``下可以配置

Flow Schedule Support
----------------------------------------
* 自动解析工程目录下的 schedule.txt 文件，格式``flowname: 0 15 8 * * ? *``，并配置作业调度
