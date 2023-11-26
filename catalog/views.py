from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        massage = request.POST.get('massage')
        print(f'{name} ({phone}):  {massage}')
    return render(request, 'catalog/contacts.html')
