from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseBadRequest  # Add this import
from django.urls import reverse  # Add this import
from django.contrib.auth.decorators import login_required  # Add this import
from .models import AccountInfo
from Password_Saver.forms import AccountInfoForm
from Password_Saver.encrypt_decrypt import encrypt

@login_required
def update_password(request):
    if request.method == "POST":
        password = request.POST.get("password")
        encrypted_password = encrypt(password)
        id = request.POST.get("id")
        
        if id:  # Ensure ID is not empty
            update_data_obj = AccountInfo.objects.filter(user_id=request.user.id, id=id)
            if update_data_obj.exists():
                update_data_obj.update(password=encrypted_password)
                messages.success(request, "Password updated successfully")
            else:
                messages.warning(request, "An error occurred while updating. Please try again.")
        else:
            messages.warning(request, "Invalid ID provided.")
        return HttpResponseRedirect(reverse("list"))

@login_required  
def delete_data(request):
    if request.method == "POST":
        id = request.POST.get("id")
        if not id:
            return HttpResponseBadRequest("Invalid ID")  # You can handle this case more gracefully

        delete_obj = get_object_or_404(AccountInfo, user=request.user, id=id)
        delete_obj.delete()
        messages.success(request, "An entry has been successfully deleted")
        return HttpResponseRedirect(reverse("list"))
