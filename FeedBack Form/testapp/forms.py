from django import forms
from django.core import validators



class FeedBackForm(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea,
                               validators=[validators.MaxLengthValidator(40), validators.MinLengthValidator(10)])

    def clean(self):
        print("Total form validation...")
        cleaned_data = super().clean()
        inputname=cleaned_data['name']
        if len(inputname)<10:
            raise forms.ValidationError("Name should contains minimum 10 characters")
        inputrollno= cleaned_data['rollno']
        if len(str(inputrollno)) != 3:
            raise forms.ValidationError('Roll no should contains only 3 digits')

    # def clean_name(self):  # this is the syntax -->clean_fieldName-->this should be compulsarily written in this form
    #     imputname = self.cleaned_data['name']
    #     print("validating name")
    #     if len(imputname) < 4:
    #         raise forms.ValidationError("The length of field should be greater than 4")
    #     return imputname
    #
    # def clean_rollno(self):
    #     inputrollno = self.cleaned_data['rollno']
    #     print("validating rollno")
    #     return inputrollno
    #
    # def clean_email(self):
    #     inputemail = self.cleaned_data['email']
    #     print("validating email")
    #     return inputemail
    #
    # def clean_feedback(self):
    #     inputfeedback = self.cleaned_data['feedback']
    #     print("validating feedback")
    #     return inputfeedback
