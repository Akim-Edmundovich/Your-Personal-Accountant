from django.db import models
from django.core.validators import MinValueValidator

from account.models import CustomUser


class Type(models.Model):
    TRANSACTION_TYPES = (
        ('expense', 'Expense'),
        ('income', 'Income'),
    )
    name = models.CharField(max_length=7, choices=TRANSACTION_TYPES)

    def __str__(self):
        return self.name


class Category(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
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
                                   validators=[MinValueValidator(0.1)])
    quantity_type = models.CharField(max_length=4, choices=[
        ("шт", "шт"),
        ("кг", "кг"),
        ("л", "л"),
        ("см", "см"),
    ], null=True, blank=True)
    description = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.type} - {self.amount}"
