from django.db.transaction import commit
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import NewBlank, BlankContent
from .forms import BlankContentCreateForm, BlankContentUpdateForm

# Create your views here.
class BlankHome(TemplateView):
    template_name = 'blank_app/home.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('blank_list')
        return super().dispatch(request, *args, **kwargs)


class BlankList(LoginRequiredMixin, ListView):
    model = NewBlank
    template_name = 'blank_app/dashboard.html'
    context_object_name = 'blanks'
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

class BlankDetail(LoginRequiredMixin, DetailView):
    model = NewBlank
    template_name = 'blank_app/blank_detail.html'
    context_object_name = 'blank'
    
class BlankCreate(LoginRequiredMixin, CreateView):
    model = NewBlank
    fields = ('title', 'description')
    template_name = 'blank_app/new_blank_create.html'
    success_url = reverse_lazy('blank_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BlankUpdate(LoginRequiredMixin, UpdateView):
    model = NewBlank
    template_name = 'blank_app/blank_update.html'
    fields = ('title', 'description')
    success_url = reverse_lazy('blank_list')

class BlankUpdate2(LoginRequiredMixin, UpdateView):
    model = NewBlank
    template_name = 'blank_app/blank_update2.html'
    fields = ('blank_on_off',) # 한 개라면 뒤어 꼭 ,를 붙히자. 안 그러면 튜플이 아니라 문자로 인식한다.

    def get_success_url(self):
        return reverse_lazy('blank_detail', kwargs={'pk': self.object.pk})

class BlankDelete(LoginRequiredMixin, DeleteView):
    model = NewBlank
    context_object_name = 'blank'
    template_name = 'blank_app/blank_delete.html'
    success_url = reverse_lazy('blank_list')

class BlankLoginView(LoginView):
    template_name = 'blank_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

class BlankLogoutView(LogoutView):
    template_name = 'blank_app/logout.html'

class RegisterPage(FormView):
    template_name = 'blank_app/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('blank_list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

class BlankContentCreate(CreateView):
    model = BlankContent
    form_class = BlankContentCreateForm
    template_name = 'blank_app/new_blank_content_create.html'

    def get_initial(self):
        return {"new_blank": self.kwargs.get("pk")}

    def get_success_url(self):
        return reverse_lazy('blank_detail', kwargs={'pk': self.object.new_blank.pk})

class BlankContentDelete(DeleteView):
    model = BlankContent
    context_object_name = 'blank_content'
    template_name = 'blank_app/blank_content_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('blank_detail', kwargs={'pk': self.object.new_blank.pk})

class BlankContentupdate(UpdateView):
    model = BlankContent
    form_class = BlankContentUpdateForm
    context_object_name = 'blank_content'
    template_name = 'blank_app/blank_content_update.html'

    def get_success_url(self):
        return reverse_lazy('blank_detail', kwargs={'pk': self.object.new_blank.pk})
