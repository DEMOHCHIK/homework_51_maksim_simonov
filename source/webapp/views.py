from django.shortcuts import render, redirect
from .cat import Cat


cat = Cat()


def home(request):
    if request.method == 'POST':
        cat_name = request.POST.get('cat_name')
        cat.set_name(cat_name)
        return redirect('info')
    return render(request, 'home.html')


def info(request):
    cat.check_state()
    return render(request, 'cat_info.html', {'cat': cat})


def command(request):
    if request.method == 'POST':
        command = request.POST.get('command')
        if command == 'feed':
            cat.feed()
            cat.check_state()
        elif command == 'play':
            cat.play()
            cat.check_state()
        elif command == 'sleep':
            cat.sleep()
            cat.check_state()
    return redirect('info')