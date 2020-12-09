# -*- coding: utf-8 -*-
from __future__ import absolute_import

kfrom django.apps import AppConfig


class CommonAppConfig(AppConfig):
    name = "common"

    def ready(self):
        import common.signals  # noqa: F401
