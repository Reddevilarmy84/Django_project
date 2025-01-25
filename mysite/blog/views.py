from django.shortcuts import render, redirect
from .models import Artiсles
from .forms import ArticleForm
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView


class BlogUpdateView(UpdateView):
    model = Artiсles
    template_name = 'blog/create.html'

    form_class = ArticleForm

class BlogDetailView(DetailView):
    model = Artiсles
    template_name = 'blog/blog_detail.html'
    context_object_name = 'article'


class BlogDeleteView(DeleteView):
    model = Artiсles
    template_name = 'blog/blog_delete.html'
    success_url = '/blog'


def blog_home(request):
    #сортируем данные по дате, можно использовать срез
    blog = Artiсles.objects.order_by('-title')[0:50]
    return render(request, 'blog/blog_home.html', {'blog': blog})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_home')
        else:
            error = 'Form is not valid'

    form = ArticleForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'blog/create.html', data)