from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import Service, Image
from .forms import ContactForm


def evina(request):
    services = Service.objects.all()
    images = Image.objects.all()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Пробное сообщение'
            body = {'name':
                    form.cleaned_data['name'],
                    'email':
                    form.cleaned_data['email'],
                    'phone':
                    form.cleaned_data['phone'],
                    'message':
                    form.cleaned_data['message'],
                    }
            message = '\n'.join(body.values())
            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            print('Сообщение отправлено')

    form = ContactForm()
    context = {
        'services': services,
        'images': images,
        'form': form
    }

    return render(request, 'evina.html', context)


# def contact(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = 'Пробное сообщение'
#             body = {'name':
#                     form.cleaned_data['name'],
#                     'email':
#                     form.cleaned_data['email'],
#                     'phone':
#                     form.cleaned_data['phone'],
#                     'message':
#                     form.cleaned_data['message'],
#                     }
#             message = '\n'.join(body.values())
#             try:
#                 send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
#             except BadHeaderError:
#                 return HttpResponse('Найден некорректный заголовок')
#             print('Сообщение отправлено')
#
#     form = ContactForm()
#     return render(request, 'contact_form.html', {'form': form})
