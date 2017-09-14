from django import forms

from offer.models import Offer


class OfferForm(forms.ModelForm):
    """
    表单类
    """

    def __init__(self, *args, **kwargs):
        super(OfferForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        self.fields['application_date'].widget.attrs['class'] += ' form_datetime'
        self.fields['last_interview_date'].widget.attrs['class'] += ' form_datetime'

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
