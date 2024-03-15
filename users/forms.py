from django import forms
from django.contrib.auth.forms import UserCreationForm

import re


class UserCreateForm(UserCreationForm):
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not re.match(r'^1[3456789]\d{9}$', phone_number):  # 1开头,3456789为第2个数字,然后跟9位数字
            raise forms.ValidationError("请输入有效的中国手机号码")
        return phone_number