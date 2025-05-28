from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ValidationError

from Services.models import ItemModel, ServiceModel
from Accounts.models import CustomUserModel

class CartItemModel(models.Model):
    userId = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    itemId = models.ForeignKey(ItemModel, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cartItems'


class CartServiceModel(models.Model):
    userId = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    serviceId = models.ForeignKey(ServiceModel, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateVisit = models.DateTimeField()

    class Meta:
        db_table = 'cartServices'


class PaymentModel(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_COMPLETED = 'completed'
    STATUS_FAILED = 'failed'
    STATUS_REFUNDED = 'refunded'
    
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Ожидает оплаты'),
        (STATUS_COMPLETED, 'Оплачено'),
        (STATUS_FAILED, 'Ошибка оплаты'),
        (STATUS_REFUNDED, 'Возврат'),
    ]
    
    METHOD_CARD = 'card'
    METHOD_CASH = 'cash'
    METHOD_OTHER = 'other'
    
    METHOD_CHOICES = [
        (METHOD_CARD, 'Карта'),
        (METHOD_CASH, 'Наличные'),
        (METHOD_OTHER, 'Другое'),
    ]
    
    userId = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='payments')
    itemsId = models.ManyToManyField(CartItemModel, blank=True, related_name='payments')
    servicesId = models.ManyToManyField(CartServiceModel, blank=True, related_name='payments')
    
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    paymentMethod = models.CharField(max_length=20, choices=METHOD_CHOICES)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    transactionId = models.CharField(max_length=100, blank=True, null=True)  # ID транзакции платежной системы
    
    class Meta:
        db_table = 'payments'
        ordering = ['-createdAt']
    
    def __str__(self):
        return f"Payment #{self.id} - {self.get_status_display()} - {self.total_amount}"
    
    def calculate_total(self):
        item_total = sum(item.price for item in self.items.all())
        service_total = sum(service.price for service in self.services.all())
        return item_total + service_total
    
    def clean(self):
        if not self.items.exists() and not self.services.exists():
            raise ValidationError("Платеж должен содержать хотя бы один товар или услугу")
        
        
@receiver(post_save, sender=PaymentModel)
def update_cart_status(sender, instance, created, **kwargs):
    if instance.status == PaymentModel.STATUS_COMPLETED:
        instance.items.all().update(is_purchased=True)
        instance.services.all().update(is_purchased=True)