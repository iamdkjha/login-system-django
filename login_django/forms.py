from django import forms

class PasswordResetForm(forms.Form):
    new_password = forms.CharField(max_length=200, widget=forms.PasswordInput)

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)