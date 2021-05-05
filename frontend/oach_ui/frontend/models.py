from django.db import models
from django import forms

class EnvironmentData(models.Model):
    Name = models.CharField(max_length=255)
    Value = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Environment Data'
        verbose_name_plural = 'Environment Data'
        constraints = [
            models.UniqueConstraint(fields=['Name', 'Value'], name='unique oachfrontendenvironmentdata')
        ]

    def __str__(self):
        return f'Environment Data - {self.Name}:{self.Value}'

class LdapConfig(models.Model):
    host = models.CharField(max_length=100, verbose_name = 'LDAP Server')
    port = models.CharField(max_length=100, verbose_name = 'LDAP Port')
    base_dn = models.CharField(max_length=100, verbose_name = 'Base DN')
    search_field = models.CharField(max_length=100, verbose_name = 'Search Field')
    ldap_acc = models.CharField(max_length=100, verbose_name = 'Service Account')
    password = models.CharField(max_length=100, verbose_name = 'Password')
    
    class Meta:
        verbose_name = 'LDAP Configuration'
        verbose_name_plural = 'LDAP Configuration'

    def __str__(self):
        return f'LDAP Config for server {self.host}:{self.port}'

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'
        
class AppUser(models.Model):
    login = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    email_addr = models.EmailField(max_length = 254, verbose_name='Email')
    Department = models.ManyToManyField(Department)

    class Meta:
        verbose_name = 'OACH User'
        verbose_name_plural = 'OACH Users'
    
    def __str__(self):
        return f'{self.login}'

    def save(self, *args, **kwargs):
        self.login = self.login.lower()
        return super(AppUser, self).save(*args, **kwargs)

class Transaction(models.Model):
    TransactionName = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        verbose_name = 'OACH Transaction'
        verbose_name_plural = 'OACH Transactions'
        constraints = [
            models.UniqueConstraint(fields=['TransactionName'], name='unique oachtransactionname')
        ]

    def __str__(self):
        return f'Transaction - {self.TransactionName}'

class TransactionParameter(models.Model):
    ParameterName = models.CharField(max_length=100)
    ParameterValue = models.CharField(max_length=250, null=True, blank=True)
    TransactionName = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name="transaction", null=True)
    
    class Meta:
        verbose_name = 'OACH Parameter'
        verbose_name_plural = 'OACH Parameters'
        constraints = [
            models.UniqueConstraint(fields=['TransactionName', 'ParameterName'], name='unique oachtransactionparameter')
        ]

    def __str__(self):
        return f'{self.TransactionName} Transaction Parameter - {self.ParameterName}'