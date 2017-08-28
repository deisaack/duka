from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from .forms import FavoriteCreateForm
from .models import Drink, Favorite
from braces.views import StaffuserRequiredMixin

class DrinkCreateView(StaffuserRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Drink
    fields = ('name',)
    success_message = 'The Drink Was added'

    def get_context_data(self, **kwargs):
        context = super(DrinkCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create a new Drink'
        return context


class DrinkDeleteView(StaffuserRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    success_url = reverse_lazy('favorites:drink_list')
    success_message = 'The drink was deleted'
    model = Drink

class DrinkDetailView(StaffuserRequiredMixin, generic.DetailView):
    model = Drink


class DrinkListView(StaffuserRequiredMixin, generic.ListView):
    model = Drink


class DrinkUpdateView(StaffuserRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Drink
    fields = ('name',)
    success_message = 'The Drink was successfully updated'

    def get_context_data(self, **kwargs):
        context = super(DrinkUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Update a drink'
        return context

class FavoriteCreateView(StaffuserRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Favorite
    form_class = FavoriteCreateForm
    success_message = 'The person\'s Favorite was successfully added'

    def get_context_data(self, **kwargs):
        context = super(FavoriteCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Person\'s Favorite'
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.collector = self.request.user.collector
        self.object.save()
        return super(FavoriteCreateView, self).form_valid(form)



class FavoriteDeleteView(StaffuserRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Favorite
    success_url = reverse_lazy('favorites:favorite_list')
    success_message = 'The favorite was deleted'


class FavoriteDetailView(StaffuserRequiredMixin, generic.DetailView):
    model = Favorite


class FavoriteListView(StaffuserRequiredMixin, generic.ListView):
    model = Favorite


class FavoriteUpdateView(StaffuserRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Favorite
    form_class = FavoriteCreateForm
    success_message = 'The Persons Favorite was successfully updated'

    def get_context_data(self, **kwargs):
        context = super(FavoriteUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Update Person\'s Favorite'
        return context
