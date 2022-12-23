from django import forms

from basic_app.models import UploadDatas


class MyForm(forms.Form):
    link_for_that_site = forms.URLInput()
    login_for_that_site = forms.CharField(max_length=200)
    password_for_that_site = forms.CharField()
    link_for_that_site2 = forms.URLInput()
    login_for_that_site2 = forms.CharField()
    password_for_that_site2 = forms.CharField()


class MovieForm(forms.ModelForm):
    class Meta:
        model = UploadDatas
        fields = ('link_for_that_site', 'login_for_that_site', 'password_for_that_site', 'link_for_that_site2',
                  'login_for_that_site2', 'password_for_that_site2')
