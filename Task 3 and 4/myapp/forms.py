from django import forms


# class SignupPage(forms.Form):
#     username = forms.CharField(label='Enter Username:', max_length=100)
#     first_name = forms.CharField(label='Enter First name:', max_length=100)
#     last_name = forms.CharField(label='Enter Last name:', max_length=100)
#     email = forms.EmailField(label='Enter Email ID:', max_length=100)
#     phone_number = forms.IntegerField()
#     gender = forms.ChoiceField(choices=[(
#         'Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], widget=forms.RadioSelect)
#     password = forms.CharField(widget=forms.PasswordInput())
#     confirm_password = forms.CharField(widget=forms.PasswordInput())


# class Login(forms.Form):
#     email = forms.CharField(label='Email', max_length=100)
#     password = forms.CharField(label='Password', max_length=100)
