from django.db import models

class Student(models.Model):
    STATUS_CHOICES = [
        ('active', 'Ativo'),
        ('inactive', 'Inativo'),
    ]

    name = models.CharField(max_length=100)
    start_date = models.DateField()
    package = models.IntegerField(choices=[(4, '4 aulas'), (8, '8 aulas'), (12, '12 aulas'), (16, '16 aulas'), (20, '20 aulas')])
    payment_day = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    accumulated_classes = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    monthly_fee = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Valor da Mensalidade", default=0)

    def __str__(self):
        return self.name