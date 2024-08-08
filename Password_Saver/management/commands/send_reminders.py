# Password_Saver/management/commands/send_reminders.py
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from Password_Saver.models import AccountInfo
from Password_Saver_Using_Django.settings import EMAIL_HOST_USER

class Command(BaseCommand):
    help = 'Send email reminders for password changes'

    def handle(self, *args, **kwargs):
        today = timezone.now().date()
        accounts = AccountInfo.objects.filter(reminder_date=today)
        for account in accounts:
            send_mail(
                'Password Change Reminder',
                f'Please remember to change your password for {account.account_name}.',
                EMAIL_HOST_USER,
                [account.user.email],
                fail_silently=False,
            )
        self.stdout.write(self.style.SUCCESS('Successfully sent reminders'))
