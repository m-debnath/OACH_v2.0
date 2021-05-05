from django.db import models

class Transaction(models.Model):
    TransactionName = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Service Requests API Transaction'
        verbose_name_plural = 'Service Requests API Transactions'
        constraints = [
            models.UniqueConstraint(fields=['TransactionName'], name='unique servicerequeststransactionname')
        ]

    def __str__(self):
        return f'Transaction - {self.TransactionName}'

class TransactionParameter(models.Model):
    ParameterName = models.CharField(max_length=100)
    ParameterValue = models.CharField(max_length=250, null=True, blank=True)
    TransactionName = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name="transaction", null=True)
    
    class Meta:
        verbose_name = 'Service Requests API Parameter'
        verbose_name_plural = 'Service Requests API Parameters'
        constraints = [
            models.UniqueConstraint(fields=['TransactionName', 'ParameterName'], name='unique servicerequeststransactionparameter')
        ]

    def __str__(self):
        return f'{self.TransactionName} Transaction Parameter - {self.ParameterName}'