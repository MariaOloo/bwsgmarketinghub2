from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import QuoteForm
from .models import QuoteRequest
def index (request):
    return render(request, 'index.html')

def about (request):
    return render(request, 'about.html')

def products (request):
    return render(request, 'products.html')

def discoverycall (request):
    return render(request, 'discoverycall.html')

# def store (request):
#     return render(request, 'store.html')

def contacts (request):
    return render(request,'contacts.html')

def store(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            print("form is valid")
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            service = form.cleaned_data['service']
            time_period = form.cleaned_data['time_period']
            specify = form.cleaned_data['specify']

            # Save the form data to the database
            QuoteRequest.objects.create(
                name=name,
                email=email,
                service=service,
                time_period=time_period,
                specify=specify
            )

            # Send an automatic response (customize as needed)
            send_mail(
                'Thank you for your quote request',
                f'Thank you, {name}, for your quote request. We will get back to you soon!',
                'oloomaria18@gmail.com',  # Your email address
                [email],
                fail_silently=False,
            )

            return redirect ('quote_requests_list')  # Redirect to the quote_requests_list view

    else:
        form = QuoteForm()

    return render(request, 'store.html', {'form': form})

def quote_requests_list(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            # Process the form data and save to the database
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            service = form.cleaned_data['service']
            time_period = form.cleaned_data['time_period']
            specify = form.cleaned_data['specify']

            # Save the form data to the database
            QuoteRequest.objects.create(
                name=name,
                email=email,
                service=service,
                time_period=time_period,
                specify=specify
            )

            # Send email response, etc.
            # ...

            return HttpResponse('Thank you for your quote request! We will get back to you As Soon As Possible')

    else:
        form = QuoteForm()

    quote_requests = QuoteRequest.objects.all()
    return render(request, 'quote_requests_list.html', {'quote_requests': quote_requests, 'form': form})