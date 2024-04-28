from django import forms

class PaymentForm(forms.ModelForm):
    name = forms.CharField(label='Your Name', max_length=100)
    product_name = forms.CharField(label='Product Name', max_length=100)
    technician_name = forms.CharField(label='Technician Name', max_length=100)
    # technician_id = forms.IntegerField(label='Technician ID')
    amount = forms.DecimalField(label='Amount')
