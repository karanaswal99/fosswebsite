# created by Chirath R, chirath.02@gmail.com
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from promotion.forms import JoinApplicationForm
from promotion.models import JoinApplication


class JoinApplicationListView(ListView):
    model = JoinApplication
    queryset = JoinApplication.objects.filter(is_approved=False)


class JoinApplicationDetailView(DetailView):
    model = JoinApplication


class JoinApplicationCreateView(CreateView):
    form_class = JoinApplicationForm
    template_name = 'base/form.html'


class JoinApplicationUpdateView(UpdateView):
    model = JoinApplication
    fields = ['is_approved']

    def get(self, **kwargs):
        return HttpResponse('This view accepts only post requests')

    def post(self, request, *args, **kwargs):
        if not (request.user.is_superuser or request.user == self.get_object().created_by):
            return redirect('permission_denied')
