from django.db import models
from django.utils import timezone
from students.models import Student

class Billing(models.Model):
    PAYMENT_STATUS = [
        ('pending', 'Pendente'),
        ('paid', 'Pago'),
        ('late', 'Atrasado'),
        ('partial', 'Parcial'),
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='billings')
    reference_month = models.DateField(help_text="Mês de referência da mensalidade")
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateField(null=True, blank=True)
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='pending')
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.student.name} - {self.reference_month.strftime('%m/%Y')}"
    
    def save(self, *args, **kwargs):
        if self.amount_paid >= self.amount:
            self.status = 'paid'
        elif self.amount_paid > 0:
            self.status = 'partial'
        elif self.due_date < timezone.now().date() and self.status == 'pending':
            self.status = 'late'
            
        super().save(*args, **kwargs) #check