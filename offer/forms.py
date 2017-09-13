from django import forms

from offer.models import Offer


class OfferForm(forms.ModelForm):
    """
    表单类
    """
    company = forms.CharField(help_text='公司', max_length=64)
    url = forms.CharField(help_text='网址', max_length=256)
    application_date = forms.DateField(help_text='申请日期', widget=forms.DateTimeInput(attrs={'type': 'date'}))
    status = forms.CharField(help_text='状态', max_length=32)
    last_interview_date = forms.DateField(help_text='最后更新时间', widget=forms.DateTimeInput(attrs={'type': 'date'}))
    application_method = forms.CharField(help_text='申请渠道', max_length=64)
    result = forms.CharField(help_text='结果', max_length=64)

    class Meta():
        model = Offer
        fields = '__all__'
