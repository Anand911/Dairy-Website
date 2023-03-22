from django import forms
from .models import Customer
choices_gender=(('Male','Male'),('Female','Female'),('Other','other'))

class CustomerForm(forms.ModelForm):
    sex=forms.ChoiceField(choices=choices_gender)
    class Meta():
        model=Customer
        fields='__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer_id'].widget.attrs["readonly"] = True

class CustomerUpdateForm(forms.ModelForm):
    sex=forms.ChoiceField(choices=choices_gender)
    class Meta():
        model=Customer
        fields='__all__'