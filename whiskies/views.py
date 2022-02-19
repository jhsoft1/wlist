from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Whisky


class WhiskyListView(ListView):
    model = Whisky

    # template_name = "whiskies/whisky_list.html"  # default
    # context_object_name = "whiskies"  # default = object_list
    # queryset = Book.objects.filter(user=request.user)

    def get_queryset(self):
        # self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Whisky.objects.filter(user=self.request.user)


class WhiskyDetailView(DetailView):
    model = Whisky
    # template_name = "whiskies/whisky_detail.html"
    # context_object_name = "book"   # default = object


class WhiskyUpdateView(UpdateView):
    model = Whisky
    fields = ('title', 'user', 'status',)
    # template_name = "whiskies/book_update_old.html" # default = whiskies/whisky_form.html
    success_url = "/"  # book_list url


class WhiskyDeleteView(DeleteView):
    model = Whisky
    # template_name = "whiskies/whisky_confirm_delete.html" # default = whisky_confirm_delete.html
    success_url = reverse_lazy('whisky_list')


class WhiskyCreateView(CreateView):
    model = Whisky
    fields = ('title', 'user', 'status',)
    # template_name = "whiskies/whisky_form.html" # default = whiskies/whisky_form.html
    success_url = reverse_lazy('whisky_list')
