from celery import Celery

app = Celery("myapp", broker="pyamqp://guest@rabbitmq//")
