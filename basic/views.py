from django.shortcuts import render, redirect
from django.contrib import messages
from basic.forms import *
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    context = dict()
    return render(request, "basic/home.html", context)



def about(request):
    context = dict()
    return render(request, "basic/about.html", context)


def services(request):
    context = dict()
    return render(request, "basic/services.html", context)



def contact(request):
    context = dict()
    context = {
        "title":"Contact"
    }
   
    if request.method == 'POST':
        
        form = ContactForm(request.POST)
       
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            form.save()
            messages.success(request, 'Your information has been submitted')
            # return redirect('account:form_submitted')
            # subject = "Femme Fan Platform"
            # to = ['crn96m@gmail.com']
            # from_email = settings.DEFAULT_FROM_EMAIL
            # contact_link = request.scheme + "://" + request.META['HTTP_HOST'] + "/admin"
            # w_link = request.scheme + "://" + request.META['HTTP_HOST']
            # # print(contact_link)

            # ctx = {
            #     'c_link':contact_link,
            #     'w_link':w_link,
            #     'email': email, 
            #     'subject': subject, 
            #     'name': name, 
            #     'message': message, 
            # }

            # message = get_template('email/contact_email.html').render(ctx)
            # # message = get_template('all/email.html').render(Context(ctx))
            # msg = EmailMessage(subject, message, to=to, from_email=from_email)
            # msg.content_subtype = 'html'
            # msg.send()
            return redirect('contact')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            # messages.error(request, "Your information was not submitted!.")
        
   
    else:
        form = ContactForm()
    context["form"] = form
    return render(request, "basic/contact.html", context)

def team(request):
    context = dict()
    return render(request, "basic/team.html", context)


def portfolio(request):
    context = dict()
    return render(request, "basic/portfolio.html", context)


def faq(request):
    context = dict()
    return render(request, "basic/faq.html", context)



def subcribe(request):
    context = {"title":"Subscribe" }
    form = SubscribeForm()
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            p = form.save()
            messages.success(request, "You have successfully subscribed to our newsletters!.")
            return redirect("home")
        else:
            messages.error(request, "Email address already taken, please use a different one!.")
            

    context['form'] = form
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



@login_required(login_url='login')
def join_network(request):
    context = dict()
    context['title'] = 'Join F.A.N Club'
    form = NetworkForm()
    if request.method == "POST":
        form = NetworkForm(request.POST, instance=request.user)
        if form.is_valid():
            email = request.user.email
            # email = form.cleaned_data['email']
            identity = form.cleaned_data['identity']
            full_name = form.cleaned_data['full_name']
            contact = form.cleaned_data['contact']
            address = form.cleaned_data['address']
            age = form.cleaned_data['age']
            try: 
                # print(f"Network is there {request.user.network}")
                messages.info(request, f"You have already join F.A.N Club, your id number is {request.user.network.identity}")

            except:
                new_net = Network()
                new_net.user = request.user
                new_net.email = email
                new_net.full_name = full_name
                new_net.contact = contact
                new_net.identity = identity
                new_net.address = address
                new_net.age = age
                new_net.save()
                request.session['new_id'] = new_net.id
                messages.success(request, "You have successfully completed the first stage please proceed to fill out all the necessary question")
                return redirect("join_network_sc")
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)            

    context['form'] = form
    return render(request, 'basic/join_network.html',  context)

@login_required(login_url='login')
def join_network_sc(request):
    context = dict()
    context['title'] = 'Join F.A.N Club'
    form = NetworkForm2()
    if request.method == "POST":
        form = NetworkForm2(request.POST, instance=request.user)
        if form.is_valid():
            print(request.session['new_id'])
            city = form.cleaned_data['city']
            membership = form.cleaned_data['membership']
            best_calltime = form.cleaned_data['best_calltime']
            company_name = form.cleaned_data['company_name']
            registration_number = form.cleaned_data['registration_number']

            messages.success(request, "You have successfully subscribed to our newsletters!.")
            return redirect("join_network_th")
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            

    context['form'] = form
    return render(request, 'basic/join_network_sc.html',  context)

@login_required(login_url='login')
def join_network_th(request):
    context = dict()
    context['title'] = 'Join F.A.N Club'
    form = NetworkForm3()
    if request.method == "POST":
        form = NetworkForm3(request.POST, instance=request.user)
        if form.is_valid():
            # p = form.save()
            messages.success(request, "You have successfully subscribed to our newsletters!.")
            return redirect("join_network_ms")
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    context['form'] = form
    return render(request, 'basic/join_network_th.html',  context)

@login_required(login_url='login')
def join_network_ms(request):
    context = dict()
    context['title'] = 'Join F.A.N Club'
    return render(request, 'basic/join_network_ms.html',  context)

@login_required(login_url='login')
def update_network(request):
    context = dict()
    context['title'] = 'Join F.A.N Club | Update'
    
    try:
        network = request.user.network
        form = NetworkUpdateForm(instance=network)
        if request.method == "POST":
            form = NetworkUpdateForm(request.POST, instance=network)
            if form.is_valid():
                form.save()
                messages.success(request,f"Your account has been updated")
                return redirect("update_network")
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
        
        context['form'] = form
    except :
        context['form'] = form
    return render(request, 'basic/update_network.html',  context)


def autocomplete(request):
    if 'term' in request.GET:
        qs = ["Johannesburg", "Vereeniging", "Pietermaritzburg", "Pretoria", "Durban", "Cape Town", "Welkom", "East London", "Randburg", "Roodepoort", "Port Elizabeth", "Bloemfontein", "Centurion", "Springs", "Sandton", "Polokwane", "Klerksdorp", "Rustenburg", "Kimberley", "Bhisho", "Benoni", "George", "Middelburg", "Vryheid", "Potchefstroom", "Umtata", "Brits", "Alberton", "Upington", "Paarl", "Queenstown", "Mmabatho", "Kroonstad", "Uitenhage", "Bethal", "Worcester", "Vanderbijlpark", "Grahamstown", "Standerton", "Brakpan", "Thohoyandou", "Saldanha", "Tzaneen", "Graaff-Reinet", "Oudtshoorn", "Mossel Bay", "Port Shepstone", "Knysna", "Vryburg", "Ladysmith", "Kuilsrivier", "Beaufort West", "Aliwal North", "Volksrust", "Musina", "Vredenburg", "Malmesbury", "Lebowakgomo", "Cradock", "De Aar", "Ulundi", "Jeffrey's Bay", "Lichtenburg", "Hermanus", "Carletonville", "Mahikeng", "Nelspruit"]
        # qs = Product.objects.filter(title__icontains=request.GET.get('term'))
        titles = list()
        for product in qs:
            if product.lower().__contains__(request.GET.get('term').lower()) or request.GET.get('term').strip() in product.lower():
                titles.append(product)
        # titles = [product.title for product in qs]
        return JsonResponse(titles, safe=False)
    return render(request, 'basic/home.html')