from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name="blog/blog.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
