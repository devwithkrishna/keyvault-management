# keyvault-management
keyvault management in azure using github workflow

## Parameters
* keyvault_name
* operation
    - get
    - set
    - list
    - delete
    - recover
    - list_deleted_secrets
        
```
usage: kv_mgmt.py [-h] [--client_id CLIENT_ID] [--client_secret CLIENT_SECRET]
                  [--tenant_id TENANT_ID] --keyvault_name KEYVAULT_NAME
                  --operation
                  {get,set,list,delete,list_deleted_secrets,recover}
                  [--secret_name SECRET_NAME] [--secret_value SECRET_VALUE]
                  [--content CONTENT]
```
## Table

|parameter name | mandatory values | optional | 
|---------------|------------------|----------|
|keyvault_name  | yes              |          |
|operation      | yes              |          |
|secret_name    |                  |  yes      |
|secret_value   |                  | yes       |
|content        |                  |  yes      |


## How program works

``` 
This python program leverages the azure sdks - azure identity and azure-keyvault-secrets.
Azure identity is used for authentication to azure and azure-keyvault-secrets to work with keyvault secrets.
```
* Azure Identity - uses DefaultAzureCredential method for authentication.
    - This uses the service principal app id, service principal secret and tenant id to do the authentication
      make sure you have the below.
    ```
    AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, AZURE_TENANT_ID are the environment variables it will be using
    ```
* I use the .env to supply the above vars and load them using python-dotenv package and use it. or you can pass it as 
    environment variable and use by os method.

The .env file will be of following 
```
AZURE_CLIENT_ID= "value"
AZURE_CLIENT_SECRET = "value"
AZURE_SUBSCRIPTION_ID = "value"
AZURE_TENANT_ID = "value"
```
replace the value with your original values.

AZURE_SUBSCRIPTION_ID - an optional parameter in .env file.

* The environment variables are passed in the github workflows in a differnt method.
    ```
    jobs:
        keyvault_management:
            runs-on: ubuntu-latest
            env:
            AZURE_CLIENT_ID: ${{ secrets.AZURE_CLIENT_ID }}
            AZURE_CLIENT_SECRET: ${{ secrets.AZURE_CLIENT_SECRET }}
            AZURE_TENANT_ID: ${{ secrets.AZURE_TENANT_ID }}
    ```
    * I have configued AZURE_CLIENT_ID, AZURE_CLIENT_SECRET and AZURE_TENANT_ID as repository secrets / organizational secrets.
    
