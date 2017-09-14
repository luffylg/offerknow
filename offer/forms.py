from django import forms

from offer.models import Offer


class OfferForm(forms.ModelForm):
    """
    表单类
    """
    RESULT_CHOICES = (
        ('unknown', '待定'),
        ('rejected', '回绝'),
        ('accepted', '收到 offer'),
    )

    company = forms.CharField(
        label='公司',
        max_length=64,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    url = forms.CharField(
        label='网址',
        help_text='以 http 开头',
        max_length=256,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    application_date = forms.DateField(
        label='申请日期',
        widget=forms.DateInput(attrs={'class': 'form-control form_datetime'}),
    )
    status = forms.CharField(
        label='状态',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    last_interview_date = forms.DateField(
        label='最后更新时间',
        widget=forms.TextInput(attrs={'class': 'form-control form_datetime'}),
    )
    application_method = forms.CharField(
        label='申请渠道',
        max_length=64,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    result = forms.CharField(
        label='结果',
        max_length=64,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    def clean(self):
        """
        对不以 http 开头的 URL 做处理
        :return:
        """
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http'):
            url = 'http://' + url
            cleaned_data['url'] = url
        return cleaned_data

    class Meta:
        model = Offer
        fields = '__all__'


class DeleteOfferForm(forms.ModelForm):
    """
    删除表单
    """

    class Meta:
        model = Offer
        fields = ()
