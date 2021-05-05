from django.db import models

class Order(models.Model):
    ExternalOrderNumber = models.CharField(max_length=50, null=True, blank=True)
    OrderNumber = models.CharField(max_length=15)
    CustomerAccountId = models.CharField(max_length=15)
    BillingAccountId = models.CharField(max_length=15)
    BillingAccountNumber = models.CharField(max_length=15)
    Type = models.CharField(max_length=30)
    Status = models.CharField(max_length=30)
    Source = models.CharField(max_length=30)
    SalesPartner = models.CharField(max_length=100, null=True, blank=True)
    ErrorMessage = models.CharField(max_length=255, null=True, blank=True)
    OrderDate = models.DateField()
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'Order # {self.OrderNumber} of Customer Account Id {self.CustomerAccountId}'
	
class OrderItem(models.Model):
    OrderItemOrderId = models.CharField(max_length=15)
    CustomerAccountId = models.CharField(max_length=15)
    BillingAccountId = models.CharField(max_length=15)
    CustomerAccountNumber = models.CharField(max_length=15)
    BillingAccountNumber = models.CharField(max_length=15)
    ParentOrderItemId = models.CharField(max_length=15, null=True, blank=True)
    RootOrderItemId = models.CharField(max_length=15)
    Product = models.CharField(max_length=50)
    PrimaryAttributeName = models.CharField(max_length=30, null=True, blank=True)
    PrimaryAttributeValue = models.CharField(max_length=30, null=True, blank=True)
    Status = models.CharField(max_length=30)
    SubStatus = models.CharField(max_length=30)
    Action = models.CharField(max_length=30, null=True, blank=True)
    ErrorMessage = models.CharField(max_length=255, null=True, blank=True)
    StatusDate = models.DateField()
    ContractStartDate = models.DateField(null=True, blank=True)
    ContractEndDate = models.DateField(null=True, blank=True)
    RegretEndDate = models.DateField(null=True, blank=True)
    PlannedDisconnectDate = models.DateField(null=True, blank=True)
    DisconnectDate = models.DateField(null=True, blank=True)
        
    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'

    def __str__(self):
        return f'{self.Product} Order Item of Order Id {self.OrderItemOrderId}'
	
class InstalledAsset(models.Model):
    AssetOrderId = models.CharField(max_length=15)
    AssetOrderItemId = models.CharField(max_length=15)
    CustomerAccountId = models.CharField(max_length=15)
    BillingAccountId = models.CharField(max_length=15)
    CustomerAccountNumber = models.CharField(max_length=15)
    BillingAccountNumber = models.CharField(max_length=15)
    ParentAssetId = models.CharField(max_length=15, null=True, blank=True)
    RootAssetId = models.CharField(max_length=15)
    Product = models.CharField(max_length=50)
    ProductType = models.CharField(max_length=50)
    PrimaryAttributeName = models.CharField(max_length=30, null=True, blank=True)
    PrimaryAttributeValue = models.CharField(max_length=30, null=True, blank=True)
    Status = models.CharField(max_length=30)
    ErrorMessage = models.CharField(max_length=255, null=True, blank=True)
    ActualStartDate = models.DateField()
    ContractStartDate = models.DateField(null=True, blank=True)
    ContractEndDate = models.DateField(null=True, blank=True)
    RegretEndDate = models.DateField(null=True, blank=True)
    PlannedDisconnectDate = models.DateField(null=True, blank=True)
    ActualEndDate = models.DateField(null=True, blank=True)
            
    class Meta:
        verbose_name = 'Installed Asset'
        verbose_name_plural = 'Installed Assets'

    def __str__(self):
        return f'{self.Product} Asset of Customer Account Id {self.CustomerAccountId}'