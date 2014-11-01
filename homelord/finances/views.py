from django.shortcuts import render


def finances(request):
    return render(request, 'finances.html')
