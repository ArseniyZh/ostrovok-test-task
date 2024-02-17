from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("admin:index")
    template_name = "user/register.html"

    def form_valid(self, form):
        # Делаем пользователя суперпользователем и авторизуем
        response = super().form_valid(form)
        user = self.object
        user.is_staff = True
        user.is_superuser = True
        user.save()
        login(self.request, user)
        return response
