from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView as AuthLogoutView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages


class HomeView(TemplateView):
    template_name = 'pages/home.html'


class LoginView(AuthLoginView):
    template_name = 'pages/login.html'
    redirect_authenticated_user = True
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        messages.success(self.request, "Login successfully")
        return super(LoginView, self).get_success_url()


class LogoutView(AuthLogoutView):
    next_page = reverse_lazy('pages:home')

    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, "Logout successfully")
        return super(LogoutView, self).dispatch(request, *args, **kwargs)
