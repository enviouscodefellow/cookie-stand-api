from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Cookie


class CookieListView(LoginRequiredMixin, ListView):
    template_name = "cookies/cookie_list.html"
    model = Cookie
    context_object_name = "cookie_stands"


class CookieDetailView(LoginRequiredMixin, DetailView):
    template_name = "cookies/cookie_detail.html"
    model = Cookie


class CookieUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "cookies/cookie_update.html"
    model = Cookie
    fields = "__all__"


class CookieCreateView(LoginRequiredMixin, CreateView):
    template_name = "cookies/cookie_create.html"
    model = Cookie
    fields = ["name", "rating", "reviewer"] # "__all__" for all of them


class CookieDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "cookies/cookie_delete.html"
    model = Cookie
    success_url = reverse_lazy("cookie_list")
