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
