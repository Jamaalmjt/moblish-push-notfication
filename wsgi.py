import os 

from django .core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTING_MODULE", "django_sns_moblie_push_notfication.setting")

application = get_wsgi_application()
