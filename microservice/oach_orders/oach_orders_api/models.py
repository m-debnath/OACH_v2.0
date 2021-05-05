from django.db import models

class Transaction(models.Model):
    TransactionName = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Orders API Transaction'
        verbose_name_plural = 'Orders API Transactions'
        constraints = [
            models.UniqueConstraint(fields=['TransactionName'], name='unique orderstransactionname')
        ]

    def __str__(self):
        return f'Transaction - {self.TransactionName}'

class TransactionParameter(models.Model):
    ParameterName = models.CharField(max_length=100)
    ParameterValue = models.CharField(max_length=250, null=True, blank=True)
    TransactionName = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name="transaction", null=True)
    
    class Meta:
        verbose_name = 'Orders API Parameter'
        verbose_name_plural = 'Orders API Parameters'
        constraints = [
            models.UniqueConstraint(fields=['TransactionName', 'ParameterName'], name='unique orderstransactionparameter')
        ]

    def __str__(self):
        return f'{self.TransactionName} Transaction Parameter - {self.ParameterName}'