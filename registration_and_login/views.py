from django.shortcuts import render

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    template_name = 'registration_and_login/login.html'
    fields = '__all__'
    redirect_authenticated_user = True


    def get_success_url(self):
        return reverse_lazy('task_list')
