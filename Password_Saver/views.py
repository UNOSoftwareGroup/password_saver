from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from Password_Saver.forms import RegistrationForm, LoginForm, AccountInfoForm, FolderForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Password_Saver.models import AccountInfo, Folder
from Password_Saver.encrypt_decrypt import encrypt, decrypt
from django.contrib import messages
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from Password_Saver_Using_Django.settings import EMAIL_HOST_USER
from django.http import JsonResponse
import random 
from datetime import datetime

@csrf_exempt
def index(request):
    registered = False
    reg_form = RegistrationForm()
    error = None
    if request.method == "POST":
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            email = request.POST.get("email")
            username = request.POST.get("username")
            password = request.POST.get('password1')
            otp = random.randint(100000, 999999)
            send_mail(
                "User Data: ",
                f"Verify your email by the OTP: {otp}",
                EMAIL_HOST_USER,
                [email],
                fail_silently=True
            )
            request.session['user_details'] = {
                'email': email,
                'username': username,
                'password': password,
                'otp': otp
            }
            return render(request, "otp.html", {"otp": otp, "email": email, "username": username, "password": password})
        else:
            error = list(reg_form.errors.values())[0]
            return render(request, 'registration.html', {'reg_form': reg_form, 'registered': registered, 'error': error})

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
                return HttpResponseRedirect("list")
            else:
                return HttpResponse("User is Inactive!")
        else:
            messages.error(request, "You entered an incorrect username or password")
    return render(request, 'login.html', {'login_form': login_form})

@csrf_exempt
def verify_otp(request):
    registered = False
    error = None
    success_message = None
    reg_form = RegistrationForm()
    if request.method == "POST":
        userotp = request.POST.get("otp")
        session_otp = request.session.get('user_details', {}).get('otp')
        if str(userotp) == str(session_otp):
            user_details = request.session.get('user_details')
            if user_details:
                reg_form = RegistrationForm({
                    'email': user_details['email'],
                    'username': user_details['username'],
                    'password1': user_details['password'],
                    'password2': user_details['password']
                })
                if reg_form.is_valid():
                    reg = reg_form.save(commit=False)
                    reg.set_password(user_details['password'])
                    reg.save()
                    success_message = "Your account has been created successfully!"
                    registered = True
                    del request.session['user_details']
                else:
                    error = list(reg_form.errors.values())[0]
            else:
                error = "Session expired. Please try again."
        else:
            error = "Invalid OTP. Please try again."
    return render(request, 'otp.html', {'registered': registered, 'error': error})

@login_required
def list_passwords(request):
    if request.user.is_authenticated:
        folders = Folder.objects.filter(user=request.user)
        details = AccountInfo.objects.filter(user=request.user).order_by('folder')
        for detail in details:
            try:
                detail.password = decrypt(detail.password)
            except:
                pass
        return render(request, 'home.html', {'details': details, 'folders': folders})

@login_required
def add_folder(request):
    if request.method == "POST":
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.user = request.user
            folder.save()
            return redirect('list')
    else:
        form = FolderForm()
    return render(request, 'add_folder.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

@login_required
def add_acc_details(request):
    if request.method == "POST":
        add_details = AccountInfoForm(request.user, request.POST)
        if add_details.is_valid():
            account_info = add_details.save(commit=False)
            account_info.user = request.user
            account_info.save()
            return HttpResponseRedirect(reverse("list"))
    else:
        add_details = AccountInfoForm(request.user)
    return render(request, 'add_account.html', {'add_account': add_details})

@login_required
def add_acc(request):
    if request.method == "POST":
        add_details = AccountInfoForm(request.user, request.POST)
        if add_details.is_valid():
            add_details.save(commit=False)
            add_details.instance.user = request.user
            add_details.save()
            messages.success(request, "Account details are added successfully!")
            return HttpResponseRedirect(reverse("list"))
        else:
            messages.warning(request, "This account info already exists!")
            return HttpResponseRedirect(reverse("list"))

@login_required
def update_password(request):
    if request.method == "POST":
        password = request.POST.get("password")
        folder_id = request.POST.get("folder")
        encrypted_password = encrypt(password)
        id = request.POST.get("id")
        update_data_obj = AccountInfo.objects.filter(user_id=request.user.id, id=id)
        if not update_data_obj.exists():
            messages.warning(request, "An error occurred while updating. Please try again")
        else:
            update_data_obj.update(password=encrypted_password, folder_id=folder_id)
            messages.success(request, "Password updated successfully")
        return HttpResponseRedirect(reverse("list"))


@login_required
def delete_info(request):
    if request.method == "POST":
        id = request.POST.get("id")
        delete_obj = get_object_or_404(AccountInfo, user=request.user, id=id)
        delete_obj.delete()
        messages.success(request, "An entry has been successfully deleted")
        return HttpResponseRedirect(reverse("list"))
