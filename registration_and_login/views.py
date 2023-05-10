from django.shortcuts import render

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth import login, get_user_model

from registration_and_login.form import UserRegisterForm

User = get_user_model()
class CustomLoginView(LoginView):
    template_name = 'registration_and_login/login.html'
    fields = '__all__'
    redirect_authenticated_user = True


    def get_success_url(self):
        return reverse_lazy('task_list')


class RegisterPage(FormView):
    template_name = 'registration_and_login/register.html'
    form_class = UserRegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('task_list')


    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
