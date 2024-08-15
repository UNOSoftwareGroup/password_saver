from django.core.management.base import BaseCommand
from django.utils import timezone
from Password_Saver.models import AccountInfo
from django.core.mail import send_mail

class Command(BaseCommand):
    help = 'Send reminder emails for passwords'

    def handle(self, *args, **kwargs):
        today = timezone.now().date()
        accounts = AccountInfo.objects.filter(reminder_date=today)
        
        for account in accounts:
            email_sent = send_mail(
                'Password Change Reminder',
                f'Remember to change your password for {account.account_name}.',
                'noreply@yourdomain.com',
                [account.user.email],
                fail_silently=False,
            )
            if email_sent:
                self.stdout.write(self.style.SUCCESS(f'Successfully sent reminder to {account.user.email}'))
            else:
                self.stdout.write(self.style.ERROR(f'Failed to send reminder to {account.user.email}'))
