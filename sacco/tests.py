from django.test import TestCase
from .models import *

class Basictest(TestCase):
    def test_fields(self):
        setting = Setting()
        setting.SettingKey = "key"
        setting.SettingName = "contribution"
        setting.SettingValue = "Contribution Amount"
        setting.save()

        record = Setting.objects.get(pk=1)
        self.assertEqual(record, setting)
