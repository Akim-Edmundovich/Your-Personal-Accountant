from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, render, redirect

from .forms import OperaForm, SingerForm
from .models import Opera, Singer


def opera_list(request):
    operas = Opera.objects.all()

    return render(request, 'operas/operas.html', {'operas': operas})


def opera_clean_list(request):
    operas = Opera.objects.all()

    return render(request, 'operas/list_operas.html', {'operas': operas})


def create_opera(request):
    form = OperaForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('operas')

        else:
            return render(request, 'partials/opera_form.html',
                          {'form': form})

    return render(request, 'partials/opera_form.html', {'form': form})


def update_opera(request, pk):
    opera = Opera.objects.get(id=pk)
    form = OperaForm(request.POST or None, instance=opera)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('operas')

    context = {
        'form': form,
        'opera': opera
    }

    return render(request, 'partials/opera_form.html', context)


def detail_opera(request, pk):
    opera = Opera.objects.get(id=pk)

    return render(request, 'partials/opera_detail.html', {'opera': opera})


def delete_opera(request, pk):
    opera = get_object_or_404(Opera, id=pk)

    if request.method == 'POST':
        opera.delete()
        return HttpResponse('')

    return HttpResponseNotAllowed('NOT ALLOWED!')


def create_opera_form(request):
    form = OperaForm()
    return render(request, 'partials/opera_form.html', {'form': form})


def opera_singer_list(request, pk):
    opera = Opera.objects.get(id=pk)
    singers = Singer.objects.filter(opera=opera)

    return render(request,
                  'singers/list_singers.html',
                  {"singers": singers,
                   'opera': opera})


def opera_singer_create(request, pk):
    opera = Opera.objects.get(id=pk)
    form = SingerForm(request.POST or None, initial={'opera': opera})

    if request.method == "POST":
        if form.is_valid():
            singer = form.save(commit=False)
            singer.opera = form.cleaned_data['opera']
            singer.save()
            return redirect('opera_singer_list', opera.id)

        else:
            return render(request, 'singers/singer_form.html', {'form': form})

    context = {
        'opera': opera,
        'form': form
    }
    return render(request, 'singers/singer_form.html', context)


def create_singer_form(request):
    form = SingerForm()
    return render(request,
                  'singers/singer_form.html',
                  {'form': form})


def opera_singer_detail(request, pk):
    singer = Singer.objects.get(id=pk)
    context = {
        'singer': singer
    }

    return render(request, 'singers/singer_detail.html', context)


def opera_singer_update(request, pk):
    singer = get_object_or_404(Singer, id=pk)
    form = SingerForm(request.POST or None, instance=singer)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('opera_singer_list', pk=singer.opera.id)

    context = {
        'singer': singer,
        'form': form
    }
    return render(request, 'singers/singer_update.html', context)


def singer_delete(request, pk):
    singer = get_object_or_404(Singer, id=pk)

    if request.method == 'POST':
        singer.delete()
        return HttpResponse('')

    return HttpResponseNotAllowed('Not allowed delete.')
