from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

from account.models import CustomUser


class Category(models.Model):
    TRANSACTION_TYPES = (
        ('expense', 'Expense'),
        ('income', 'Income'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    type = models.CharField(max_length=7,
                            choices=TRANSACTION_TYPES,
                            null=False,
                            blank=False)
    name = models.CharField(max_length=50)

    class Meta:
        unique_together = ('type', 'name')
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)

    class Meta:
        unique_together = ('category', 'name')
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return self.name


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('expense', 'Expense'),
        ('income', 'Income'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    type = models.CharField(max_length=7,
                            choices=TRANSACTION_TYPES,
                            null=False,
                            blank=False)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 blank=False)
    subcategory = models.ForeignKey(Subcategory,
                                    on_delete=models.CASCADE,
                                    null=True,
                                    blank=True)
    amount = models.DecimalField(max_digits=10,
                                 decimal_places=1,
                                 blank=False,
                                 validators=[MinValueValidator(0.1)])
    quantity = models.DecimalField(max_digits=10,
                                   decimal_places=1,
                                   null=True,
                                   blank=True,
                                   default=0,
                                   validators=[MinValueValidator(0.1)])
    quantity_type = models.CharField(max_length=4, choices=[
        ("шт", "шт"),
        ("кг", "кг"),
        ("л", "л"),
        ("см", "см"),
    ], null=True, blank=True)
    description = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.type} - {self.amount}"
