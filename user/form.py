from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm


from .models import User
from django.contrib.auth.hashers import check_password

class CreateUserForm(forms.Form):
    username = forms.CharField(
        error_messages={'required':"아이디를 입력하세요."},
        max_length=64, label = "아이디"
    )
    email = forms.EmailField(
        error_messages={'required':"이메일을 입력하세요."},
        max_length=254, label = "email"
    )
    password1 = forms.CharField(
        error_messages={'required' : "비밀번호를 입력하세요"},
        widget = forms.PasswordInput, label = "비밀번호"
    )
    password2 = forms.CharField(
        error_messages={'required' : "비밀번호를 입력하세요"},
        widget = forms.PasswordInput, label = "비밀번호 재입력"
    )
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2:
            if password1 != password2:
                self.add_error('password', '비밀번호가 서로 다릅니다.')
                self.add_error('re_password', '비밀번호가 서로 다릅니다.')
            else:
                user = User(
                email = email,
                password=password1,
                )
                user.save() # db저장
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):  # save메소드 오버라이
        user = super(CreateUserForm, self).save(commit=False) # 기존의 id와 pw를 저장. commit이 Flase인 이유는 2번 저장하는것 방지.
        user.email = self.cleaned_data["email"]               # user 객체에 email 값 추가.
        if commit:
            user.save()              # 객체에 대한 모든 정보를 DB에 저장.
        return user