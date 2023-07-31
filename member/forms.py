from django import forms
from.models import UserData

class DateInput(forms.DateInput):
   input_type = 'date' 

class MemberForm(forms.ModelForm):

    class Meta:
        model = UserData
        fields = '__all__'

        widgets = {
            'date_of_expense': DateInput(),
        }
    
    def __init__(self, *args, **kwargs):
        super(MemberForm,self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select"
       
