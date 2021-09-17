from django.shortcuts import render


def home(request):
    return render(request, 'myapp/home.html')


def result(request):
    number = int(request.GET["number"])
    ans = [i for i in range(1, number+1)]
    context = {}
    context['ans'] = ans
    return render(request, 'myapp/display.html', context)
