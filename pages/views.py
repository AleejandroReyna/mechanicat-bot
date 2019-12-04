from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView as AuthLogoutView
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages


class HomeView(TemplateView):
    template_name = 'pages/home.html'


class LoginView(AuthLoginView):
    template_name = 'pages/auth_form.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        messages.success(self.request, "Login successfully")
        return super(LoginView, self).get_success_url()

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data()
        context['action'] = 'Login'
        return context


class LogoutView(AuthLogoutView):
    next_page = reverse_lazy('pages:home')

    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, "Logout successfully")
        return super(LogoutView, self).dispatch(request, *args, **kwargs)


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'pages/auth_form.html'
    success_url = reverse_lazy('pages:login')

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data()
        context['action'] = 'Signup'
        return context

    def get_success_url(self):
        messages.success(self.request, "Your account has been created.")
        return super(SignUpView, self).get_success_url()
