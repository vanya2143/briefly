from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
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
            'links': links,
        }
        # print(request.__dict__.get('META').get('REMOTE_ADDR'))

        # print(links)
        return render(request, 'linkCutter/links_page.html', page_content)

    def post(self, request, *args, **kwargs):
        form = AddUserLinkForm(request.POST)

        if form.is_valid():
            form.instance.creator = self.request.user
            form.save()

            # Перенаправляем пользователя на только что созданный курс
            return redirect('links-page')

        return render(request, 'linkCutter/links_page.html', {'form': form})


def link_redirect(request, slug):
    link = get_object_or_404(Link, source_link=slug)
    link.clicks += 1
    link.save()

    return redirect(link.destination_link)


def about_page(request):
    return render(request, 'linkCutter/about_page.html', {'title': "Про нас"})
