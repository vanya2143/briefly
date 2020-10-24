from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddUserLinkForm
from .models import Link


def home_page(request):
    return render(request, 'linkCutter/home_page.html', {'title': "Link Cutter"})


class UserLinks(LoginRequiredMixin, CreateView):

    def get(self, request, *args, **kwargs):

        links = Link.objects.filter(creator=self.request.user)

        page_content = {
            'title': "Ссылки",
            'form': AddUserLinkForm,
            'links': links
        }

        # print(links)
        return render(request, 'linkCutter/links_page.html', page_content)

    def post(self, request, *args, **kwargs):
        form = AddUserLinkForm(request.POST)

        if form.is_valid():
            form.instance.creator = self.request.user
            form.save()
            # slug = form.cleaned_data['slug']

            # Перенаправляем пользователя на только что созданный курс
            return redirect('links-page')

        return render(request, 'linkCutter/links_page.html', {'form': form})


def link_redirect(request, slug):
    a = Link.objects.filter(source_link=slug).values()[0]
    # print(a['destination_link'])

    return redirect(a['destination_link'])


def about_page(request):
    return render(request, 'linkCutter/about_page.html', {'title': "Про нас"})
