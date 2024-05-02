from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount']
        labels = {'amount': 'Amount'}

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter payment amount'})
