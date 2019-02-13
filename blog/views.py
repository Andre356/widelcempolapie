from .models import Dish
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm


# Class Based Views
class HomePageView(ListView):
    model = Dish
    template_name = 'blog/home.html'
    paginate_by = 8
    ordering = 'added'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class DetailDishView(DetailView):
    model = Dish
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateDishView(CreateView):
    template_name = 'blog/create_dish.html'
    fields = (
        'name', 'portions', 'ingredients', 'description', 'added', 'photo0', 'photo1', 'photo2', 'rating', 'thermomix')
    model = Dish


class UpdateDishView(UpdateView):
    template_name = 'blog/create_dish.html'
    fields = (
        'name', 'portions', 'ingredients', 'description', 'added', 'photo0', 'photo1', 'photo2', 'rating', 'thermomix')
    model = Dish


class DeleteDishView(DeleteView):
    model = Dish
    success_url = reverse_lazy('home')


class UserFormView(View):
    form_class = UserForm   # define form from forms.py file
    template_name = 'blog/registration_form.html'

    # whenever User wants UserFormView class and it's a get method, it's going to call this function
    # and display a blank form
    def get(self, request):
        form = self.form_class(None)                    # None because it's going to be a blank form
        return render(request, self.template_name, {'form': form})

    # whenever User wants UserFormView class and it's a post method, it's going to call this function
    # process for data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)  # not upload to DB, but manage locally
            # clean (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)     # this function will change the password if needed in future
            user.save()                     # at this point data is saved to the DB

            # returns User objects if credentials are correct (in DB)
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')

        return render(request, self.template_name, {form: form})
