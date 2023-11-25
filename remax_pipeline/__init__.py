from . import _version

__version__ = _version.get_versions()["version"]

from remax_pipeline.celery_app import celery_app
