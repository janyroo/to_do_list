部署到pythonanywhere注意修改setting.py
git pull更新

ALLOWED_HOSTS = [u'janyroo.pythonanywhere.com']

MEDIA_ROOT = u'/home/janyroo/to_do_list/todolist/media'
MEDIA_URL = '/media/'
STATIC_ROOT = u'/home/janyroo/to_do_list/todolist/static'
STATIC_URL = '/static/'
