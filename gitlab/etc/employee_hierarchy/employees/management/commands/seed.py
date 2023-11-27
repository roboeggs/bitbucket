import random
from faker import Faker
from django.core.management.base import BaseCommand
from employees.models import Employee

fake = Faker()

class Command(BaseCommand):
    help = 'Seed database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Seeding database...'))

        # Создаем 10 сотрудников
        for _ in range(10):
            Employee.objects.create(
                full_name=fake.name(),
                position=fake.job(),
                hire_date=fake.date_between(start_date='-5y', end_date='today'),
                salary=random.uniform(30000, 80000),
                # Добавляем поле фотографии
                photo='employee_photos/point.png'  # Укажите путь к вашей тестовой фотографии
            )

        self.stdout.write(self.style.SUCCESS('Database seeding completed.'))
