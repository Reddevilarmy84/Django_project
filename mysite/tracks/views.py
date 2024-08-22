from django.shortcuts import render, redirect
from .models import Tracks
from .forms import TracksForm
from django.views.generic import DetailView
# Create your views here.
def tracks_home(request):
        track = Tracks.objects.order_by('id')
        return render(request, 'tracks/tracks.html', {'track': track})

class TracksDetailView(DetailView):
        model = Tracks
        template_name = 'tracks/tracks_detail.html'
        context_object_name = 'track_detail'

def add_note(request):
        error =''
        if request.method == 'POST':
                form = TracksForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('home')
                else:
                        error = 'Форма не корректная'


        form = TracksForm()

        data = {'form':form, 'error':error}



        return render(request, 'tracks/add_note.html', data)
