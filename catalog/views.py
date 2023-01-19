from django.shortcuts import render


def home(request):
    return render(request, 'home_page.html')


def contacts(request):
    if request.method == 'POST':
        print(request.POST.get('name'))
        print(request.POST.get('phone'))
        print(request.POST.get('message'))
    return render(request, 'contacts_page.html')
# Create your views here.