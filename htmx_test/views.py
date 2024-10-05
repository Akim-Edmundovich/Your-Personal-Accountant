from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, render, redirect

from .forms import OperaForm
from .models import Opera


def opera_list(request):
    operas = Opera.objects.all()

    return render(request, 'operas/operas_list.html', {'operas': operas})


def create_opera(request):
    form = OperaForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            opera = form.save()
            return redirect('detail_opera', opera.id)

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
            return redirect('detail_opera', pk=opera.id)


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

    return HttpResponseNotAllowed(['POST'])


def create_opera_form(request):
    form = OperaForm()
    return render(request, 'partials/opera_form.html', {'form': form})
