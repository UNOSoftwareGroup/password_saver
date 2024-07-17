from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from Password_Saver.forms import RegistrationForm, LoginForm, AccountInfoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Password_Saver.models import AccountInfo
from Password_Saver.encrypt_decrypt import encrypt, decrypt
from django.contrib import messages

def index(request):
    registered = False
    reg_form = RegistrationForm()
    error = None
    if request.method == "POST":
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            reg = reg_form.save(commit=False)
            reg.set_password(reg.password)
            reg.save()
            registered = True
            reg_form = RegistrationForm()
        else:
            error = list(reg_form.errors.values())[0]
    return render(request, 'registration.html', {'reg_form': reg_form, 'registered': registered, 'error': error})

def login_page(request):
    login_form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('list')
            else:
                return HttpResponse("User is Inactive!")
        else:
            messages.error(request, "You entered an incorrect username or password")
    return render(request, 'login.html', {'login_form': login_form})

@login_required
def list_passwords(request):
    details = AccountInfo.objects.filter(user=request.user)
    for detail in details:
        detail.password = decrypt(detail.password)
    return render(request, 'home.html', {'details': details})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def add_acc_details(request):
    if request.method == "POST":
        add_details = AccountInfoForm(request.user, request.POST)
        if add_details.is_valid():
            account_info = add_details.save(commit=False)
            account_info.user = request.user
            account_info.save()
            return redirect('list')
    else:
        add_details = AccountInfoForm(request.user)
    return render(request, 'add_account.html', {'add_account': add_details})

@login_required
def update_password(request):
    if request.method == "POST":
        password = request.POST.get("password")
        id = request.POST.get("id")
        encrypted_password = encrypt(password)
        update_data_obj = AccountInfo.objects.filter(user=request.user, id=id)
        if not update_data_obj.exists():
            messages.warning(request, "An error occurred while updating. Please try again")
        else:
            update_data_obj.update(password=encrypted_password)
            messages.success(request, "Password updated successfully")
        return redirect('list')

@login_required
def delete_info(request):
    if request.method == "POST":
        id = request.POST.get("id")
        delete_obj = get_object_or_404(AccountInfo, user=request.user, id=id)
        delete_obj.delete()
        messages.success(request, "An entry has been successfully deleted")
        return redirect('list')
