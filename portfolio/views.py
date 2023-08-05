from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import *
from datetime import datetime
from .utlls import *


class PortfolioHome(DataMixin, ListView):
    model = Themes
    template_name = 'portfolio/index.html'
    context_object_name = 'themes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница',
                                      age=int((datetime.now() - datetime(2000, 5, 27)).days/365))

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Themes.objects.all().filter(is_published=True)


class PortfolioDetail(DataMixin, DetailView):
    model = Themes
    template_name = 'portfolio/work-details.html'
    context_object_name = 'some_theme'
    slug_url_kwarg = 'theme_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Детали работы')
        return dict(list(context.items()) + list(c_def.items()))


def page_not_found(request, exception):
    return HttpResponseNotFound(f"Страница не найдена!")
