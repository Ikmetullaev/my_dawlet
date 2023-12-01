from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django .forms import ModelForm  
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':"shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                                                                        'id' : 'username',
                                                                        'type' : 'text',
                                                                        'placeholder' : 'username'}))
                                                             
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : "shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline",
                                                            'id' : 'password',
                                                            'type' : 'text',
                                                            'placeholder' : 'password'}))

class UserRegistrationForm(UserCreationForm):
    # first_name = forms.CharField(widget=forms.TextInput(attrs={''
    #                                                          'class': 'bg-gray-200 pl-12 py-2 md:py-4 focus:outline-none w-full',
    #                                                          'type': 'text',
    #                                                          'placeholder': 'First Name',
    #                                                          'id': 'username'}))
    # last_name = forms.CharField(widget=forms.TextInput(attrs={''
    #                                                          'class': 'bg-gray-200 pl-12 py-2 md:py-4 focus:outline-none w-full',
    #                                                          'type': 'text',
    #                                                          'placeholder': 'Last Name',
    #                                                          'id': 'username'}))
    # username = forms.CharField(widget=forms.TextInput(attrs={''
    #                                                          'class': 'bg-gray-200 pl-12 py-2 md:py-4 focus:outline-none w-full',
    #                                                          'type': 'text',
    #                                                          'placeholder': 'username',
    #                                                          'id': 'username'}))
    first_name = forms.CharField(widget=forms.EmailInput(attrs={"class":"peer block min-h-[auto] w-full rounded border-0 bg-transparent px-3 py-[0.32rem] leading-[2.15] outline-none transition-all duration-200 ease-linear focus:placeholder:opacity-100 data-[te-input-state-active]:placeholder:opacity-100 motion-reduce:transition-none dark:text-neutral-200 dark:placeholder:text-neutral-200 [&:not([data-te-input-placeholder-active])]:placeholder:opacity-0",
                                                            "type":"text",
                                                            "id":"exampleFormControlInput2",
                                                            "placeholder":"Email address"}))
    last_name = forms.CharField(widget=forms.EmailInput(attrs={"class":"peer block min-h-[auto] w-full rounded border-0 bg-transparent px-3 py-[0.32rem] leading-[2.15] outline-none transition-all duration-200 ease-linear focus:placeholder:opacity-100 data-[te-input-state-active]:placeholder:opacity-100 motion-reduce:transition-none dark:text-neutral-200 dark:placeholder:text-neutral-200 [&:not([data-te-input-placeholder-active])]:placeholder:opacity-0",
                                                            "type":"text",
                                                            "id":"exampleFormControlInput2",
                                                            "placeholder":"Email address"}))
    username = forms.CharField(widget=forms.EmailInput(attrs={"class":"peer block min-h-[auto] w-full rounded border-0 bg-transparent px-3 py-[0.32rem] leading-[2.15] outline-none transition-all duration-200 ease-linear focus:placeholder:opacity-100 data-[te-input-state-active]:placeholder:opacity-100 motion-reduce:transition-none dark:text-neutral-200 dark:placeholder:text-neutral-200 [&:not([data-te-input-placeholder-active])]:placeholder:opacity-0",
                                                            "type":"text",
                                                            "id":"exampleFormControlInput2",
                                                            "placeholder":"Email address"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"peer block min-h-[auto] w-full rounded border-0 bg-transparent px-3 py-[0.32rem] leading-[2.15] outline-none transition-all duration-200 ease-linear focus:placeholder:opacity-100 data-[te-input-state-active]:placeholder:opacity-100 motion-reduce:transition-none dark:text-neutral-200 dark:placeholder:text-neutral-200 [&:not([data-te-input-placeholder-active])]:placeholder:opacity-0",
                                                            "type":"text",
                                                            "id":"exampleFormControlInput2",
                                                            "placeholder":"Email address"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"peer block min-h-[auto] w-full rounded border-0 bg-transparent px-3 py-[0.32rem] leading-[2.15] outline-none transition-all duration-200 ease-linear focus:placeholder:opacity-100 data-[te-input-state-active]:placeholder:opacity-100 motion-reduce:transition-none dark:text-neutral-200 dark:placeholder:text-neutral-200 [&:not([data-te-input-placeholder-active])]:placeholder:opacity-0",
                                                                  "type":"password",
                                                                    "id":"exampleFormControlInput22",
                                                                    "placeholder":"Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"peer block min-h-[auto] w-full rounded border-0 bg-transparent px-3 py-[0.32rem] leading-[2.15] outline-none transition-all duration-200 ease-linear focus:placeholder:opacity-100 data-[te-input-state-active]:placeholder:opacity-100 motion-reduce:transition-none dark:text-neutral-200 dark:placeholder:text-neutral-200 [&:not([data-te-input-placeholder-active])]:placeholder:opacity-0",
                                                                  "type":"password",
                                                                    "id":"exampleFormControlInput22",
                                                                    "placeholder":"Password"}))
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={''
    #                                                               'class': 'bg-gray-200 pl-12 py-2 md:py-4 focus:outline-none w-full',
    #                                                               'type': 'text',
    #                                                               'placeholder': 'password',
    #                                                               'id': 'username'}))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={''
    #                                                               'class': 'bg-gray-200 pl-12 py-2 md:py-4 focus:outline-none w-full',
    #                                                               'type': 'text',
    #                                                               'placeholder': 'Retype password',
    #                                                               'id': 'username'}))
class DawletForm(ModelForm):
  name = forms.CharField(max_length=45, widget=forms.TextInput(attrs={'type': 'text',
                                                         'id': 'name',
                                                         'name':'name',
                                                         'class': 'w-full bg-gray-800 rounded border border-gray-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}))
  text = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'id': 'name',
                                                                          'name':'name',
                                                                          'class':'w-full bg-gray-800 rounded border border-gray-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 h-32 text-base outline-none text-gray-100 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out'}))
  san = forms.IntegerField(widget=forms.TextInput(attrs={'type': 'number',
                                                         'id': 'name',
                                                         'name':'name',
                                                         'class': 'w-full bg-gray-800 rounded border border-gray-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}))
  image = forms.ImageField(widget=forms.FileInput(attrs={'class':'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400',
                                                         'id':'file_input',
                                                   'type':'file'}))
    


  class Meta:
     model = Dawlet
     fields = ('name', 'text', 'san', 'image')
    


class DawletchangeForm(ModelForm):
  name = forms.CharField(max_length=45, widget=forms.TextInput(attrs={'type': 'text',
                                                         'id': 'name',
                                                         'name':'name',
                                                         'class': 'w-full bg-gray-800 rounded border border-gray-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}))
  text = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'id': 'name',
                                                                          'name':'name',
                                                                          'class':'w-full bg-gray-800 rounded border border-gray-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 h-32 text-base outline-none text-gray-100 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out'}))
  san = forms.IntegerField(widget=forms.TextInput(attrs={'type': 'number',
                                                         'id': 'name',
                                                         'name':'name',
                                                         'class': 'w-full bg-gray-800 rounded border border-gray-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}))
  image = forms.ImageField(widget=forms.FileInput(attrs={'class':'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400',
                                                         'id':'file_input',
                                                   'type':'file'}))
  class Meta:
     model = Dawlet
     fields = ('name', 'text', 'san', 'image')
    