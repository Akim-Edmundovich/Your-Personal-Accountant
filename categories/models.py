from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return self.name


class Expenses(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory,
                                    on_delete=models.CASCADE,
                                    null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.category}; {self.amount}; {self.description}'


class Income(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory,
                                    on_delete=models.CASCADE,
                                    null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.category}; {self.amount}; {self.description}'
