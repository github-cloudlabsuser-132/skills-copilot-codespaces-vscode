from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient

# Set variables
subscription_id = 'your-subscription-id'
resource_group_name = 'myResourceGroup'
storage_account_name = 'mystorageaccount'
location = 'westeurope'

# Authenticate with Azure
credential = DefaultAzureCredential()

# Initialize management clients
resource_client = ResourceManagementClient(credential, subscription_id)
storage_client = StorageManagementClient(credential, subscription_id)

# Create resource group
resource_client.resource_groups.create_or_update(resource_group_name, {'location': location})

# Create storage account
storage_async_operation = storage_client.storage_accounts.begin_create(
    resource_group_name,
    storage_account_name,
    {
        'sku': {'name': 'Standard_LRS'},
        'kind': 'StorageV2',
        'location': location
    }
)
storage_account = storage_async_operation.result()

print(f'Storage account {storage_account.name} created')