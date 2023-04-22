from django.core.management.base import BaseCommand
from faker import Faker
from api.models import UserManagement

class Command(BaseCommand):
    help = 'Populate UserManagement table with dummy data'

    def handle(self, *args, **options):
        fake = Faker()
        for i in range(50):
            username = fake.user_name()
            email = fake.email()
            mobile = fake.phone_number()
            user = UserManagement.objects.create(
                username=username,
                email=email,
                mobile=mobile,
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created user {user.id}: {username}'))
