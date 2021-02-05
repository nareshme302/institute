from django import forms
from college.models import Branch, Student, Staff
import re


class StaffForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=10)

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']
        num = re.findall('\d+', data)
        if num[0][0] in '6789' and len(num[0]) == 10:
            return data
        else:
            raise forms.ValidationError("enter correct phone number")

    class Meta:
        model = Staff
        fields = ['name', 'branch', 'dob', "phone_number",'email', 'photo', 'file']


class StudentForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=10)

    def clean_phone_number(self):
        # breakpoint()
        data = self.cleaned_data['phone_number']
        num = re.findall('\d+', data)
        if num[0][0] in '6789' and len(num[0]) == 10:
            return data
        else:
            raise forms.ValidationError("enter correct phone number")

    class Meta:
        model = Student
        fields = ['name', 'branch', 'dob', 'email', 'photo', 'file', 'phone_number']


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'
