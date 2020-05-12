from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from users.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('the_counter:index')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'users/register.html', context)


def logout_view(request):
    """Ends an application session"""
    logout(request)
    return redirect('the_counter:index')


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('the_counter:index')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('the_counter:index')

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'users/login.html', context)


def account_view(request):
    if not request.user.is_authenticated:
        return redirect('users/login.html')

    context ={}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = AccountUpdateForm(
            initial={
                'email': request.user.email,
                'username': request.user.username,
            }
        )

    context['account_form'] = form
    return render(request, 'users/user.html', context)
