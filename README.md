# jewelbi
与珠宝行业相关的人工智能服务项目
jewel目录下是一个用django运行的识别珠宝类型的项目。请安装python+django+tensorflow 1.0，在jewel目录下运行：nohup python manage.py runserver 0.0.0.0:80，访问请http://yourip:yourport/jewelsite/
我们有一个demo网站在http://www.siweirui.cn/jewelsite/
在cnnJewelType中也包含了训练代码，您可以将分类好的珠宝类型进行训练。目前的模型已经训练了形状维度，您也可以尝试训练一下比如颜色，光泽等图像特征比较明显的维度。
