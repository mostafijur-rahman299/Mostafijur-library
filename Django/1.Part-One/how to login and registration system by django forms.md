# 1. How to login and registration system by django forms?


```python
1.project/apps/forms.py

from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class UserRegister(forms.Form):
    username = forms.CharField(max_length=104)
    email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput)
    password2 = forms.CharField(widget = forms.PasswordInput,label= "Confirm Password")

    def clean(self,*args,**kwargs):
        data = self.cleaned_data
        password= self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError("Password Must Match")
        return data

    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data.get('email')
        if not "gmail.com" in email:
            raise forms.ValidationError('Email must be gmail')
        return email


    def clean_username(self,*args,**kwargs):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Already have an account!")
        return username

    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email = email)
        if qs.exists():
            raise forms.ValidationError('This eamil already taken')
        return email

class UserLogin(forms.Form):
    username = forms.CharField(max_length=104)
    password = forms.CharField(widget=forms.PasswordInput)

```

```python
2.project/apps/views.py

from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model

from .forms import UserRegister,UserLogin
from django.contrib.auth import authenticate,login

User=get_user_model()

def register(request):
    if request.method == 'POST':
        form = UserRegister(data=request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            new_user=User.objects.create_user(username,email,password)
            return redirect('/login')
    else:
        form=UserRegister
    return render(request,'index.html',{'form':form})

def user_login(request):
    forms=UserLogin(data=request.POST)
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=authenticate(username=username,password=password)
    if user:
        login(request,user)
        return redirect('/')
    else:
        forms=UserLogin
    return render(request,'login.html',{'forms':forms})

```

```python
3. project/urls.py

from django.contrib import admin
from django.urls import path

from apps.views import register,user_login

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',register,name='regi'),
    path('login/',user_login)

]

```

```html
4.project/apps/templates

***registration.html***
<form   method="POST">
  {% csrf_token %}
  {{ form }}
  <input type="submit" name="registration" value="submit">
</form>

***********************************************

***login.html***
<form  method="post">
  {% csrf_token %}
  {{ forms }}
  <input type="submit" name="login" value="login">
</form>
```



> Please inbox **[me](https://www.facebook.com/mostafijur.rahman299)** if you've any questions.
