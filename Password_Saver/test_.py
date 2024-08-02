# tests.py in Password_Saver folder
import pytest
from django.contrib.auth.models import User
from Password_Saver.models import AccountInfo, Folder
from Password_Saver.encrypt_decrypt import encrypt, decrypt

@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create_user(username='testuser', password='testpassword')
    assert user.username == 'testuser'

@pytest.mark.django_db
def test_account_info_creation():
    user = User.objects.create_user(username='testuser', password='testpassword')
    encrypted_password = encrypt('password123')
    account_info = AccountInfo.objects.create(user=user, account_name='test_account', user_name='test_user', password=encrypted_password)
    assert decrypt(account_info.password) == 'password123'

@pytest.mark.django_db
def test_folder_creation():
    user = User.objects.create_user(username='testuser', password='testpassword')
    folder = Folder.objects.create(user=user, name='test_folder')
    assert folder.name == 'test_folder'
