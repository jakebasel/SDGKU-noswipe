from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import CreateView
from .forms import CustomUserChangeForm, CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
