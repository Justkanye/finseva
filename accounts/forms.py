from django import forms
from django.contrib.auth import get_user_model, password_validation
from .models import Profile
from captcha.fields import ReCaptchaField

User = get_user_model()

STATE_CHOICES = (
        ("Andhra Pradesh", "Andhra Pradesh"),
        ("Andaman and Nicobar (UT)", "Andaman and Nicobar (UT)"),
        ("Arunachal Pradesh", "Arunachal Pradesh"),
        ("Assam", "Assam"),
        ("Bihar", "Bihar"),
        ("Chandigarh (UT)", "Chandigarh (UT)"),
        ("Chhattisgarh", "Chhattisgarh"),
        ("Dadra and Nagar Haveli (UT)", "Dadra and Nagar Haveli (UT)"),
        ("Daman and Diu (UT)", "Daman and Diu (UT)"),
        ("Delhi", "Delhi"),
        ("Goa", "Goa"),
        ("Gujarat", "Gujarat"),
        ("Haryana", "Haryana"),
        ("Himachal Pradesh", "Himachal Pradesh"),
        ("Jammu and Kashmir", "Jammu and Kashmir"),
        ("Jharkhand", "Jharkhand"),
        ("Karnataka", "Karnataka"),
        ("Kerala", "Kerala"),
        ("Lakshadweep (UT)", "Lakshadweep (UT)"),
        ("Madhya Pradesh", "Madhya Pradesh"),
        ("Maharashtra", "Maharashtra"),
        ("Manipur", "Manipur"),
        ("Meghalaya", "Meghalaya"),
        ("Mizoram", "Mizoram"),
        ("Nagaland", "Nagaland"),
        ("Orissa", "Orissa"),
        ("Puducherry (UT)", "Puducherry (UT)"),
        ("Punjab", "Punjab"),
        ("Rajasthan", "Rajasthan"),
        ("Sikkim", "Sikkim"),
        ("Tamil Nadu", "Tamil Nadu"),
        ("Telangana", "Telangana"),
        ("Tripura", "Tripura"),
        ("Uttar Pradesh", "Uttar Pradesh"),
        ("Uttarakhand", "Uttarakhand"),
        ("West Bengal", "West Bengal"),
    )

class RegisterForm(forms.Form):
    register_email = forms.EmailField()
    register_password = forms.CharField(widget=forms.PasswordInput()) 
    business_name = forms.CharField(max_length=220)
    first_name = forms.CharField(max_length=220)
    mobile_number = forms.CharField(max_length=22)
    shop_address = forms.CharField(max_length=220)
    state = forms.ChoiceField(choices=STATE_CHOICES)
    pin_code = forms.CharField(max_length=225)
    district = forms.CharField(max_length=220)
    captcha = ReCaptchaField()
    fields = '__all__'

    def clean_register_email(self):
        register_email = self.cleaned_data.get('register_email')
        qs = User.objects.filter(email=register_email)
        if qs.exists():
            raise forms.ValidationError('This is email is already in use.')
        return register_email

    def clean_register_password(self):
        register_password = self.cleaned_data.get('register_password')
        if register_password:
            try:
                password_validation.validate_password(register_password, self.instance)
            except ValidationError as error:
                raise forms.ValidationError(error)

class LoginForm(forms.Form):
    login_email = forms.EmailField()
    login_password = forms.CharField(widget=forms.PasswordInput())
    login_captcha = ReCaptchaField()
    fields = '__all__'

    def clean_login_email(self):
        login_email = self.cleaned_data.get('login_email')
        qs = User.objects.filter(email=login_email)
        if not qs.exists():
            raise forms.ValidationError('Account does not exist')
        return login_email

    def clean_login_password(self):
        login_password = self.cleaned_data.get('login_password')
        if login_password:
            try:
                password_validation.validate_password(login_password, self.instance)
            except ValidationError as error:
                raise forms.ValidationError(error)