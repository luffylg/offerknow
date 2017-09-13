from django import forms

from offer.models import Offer


class OfferForm(forms.ModelForm):
    """
    表单类
    """
    company = forms.CharField(help_text='公司',
                              max_length=64,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    url = forms.CharField(help_text='网址',
                          max_length=256,
                          widget=forms.TextInput(attrs={'class': 'form-control'}))
    application_date = forms.DateField(help_text='申请日期',
                                       widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.CharField(help_text='状态',
                             max_length=32,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_interview_date = forms.DateField(help_text='最后更新时间',
                                          widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    application_method = forms.CharField(help_text='申请渠道',
                                         max_length=64,
                                         widget=forms.TextInput(attrs={'class': 'form-control'}))
    result = forms.CharField(help_text='结果',
                             max_length=64,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Offer
        fields = '__all__'
