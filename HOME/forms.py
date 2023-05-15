from django import forms
# register_style= (
#     "color":"white",
#     "display":
# )

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label="password",widget=forms.PasswordInput)
class RegisterForm(forms.Form):
    # must be unique username
    username = forms.CharField(label='Username')
    # both password fields should matchc
    password = forms.CharField(label="Password",widget = forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password",widget = forms.PasswordInput)
    first_name = forms.CharField(label="First Name")
    second_name = forms.CharField(label="Second Name")
    age = forms.CharField(label="Age",widget=forms.TextInput(attrs={
        "placeholder":"",
        "pattern":"[0-9]+",
        "font-family":"Font Awesome 5 Free",
    }))
    height = forms.CharField(label = "Height")
    weight = forms.CharField(label = "Weight")