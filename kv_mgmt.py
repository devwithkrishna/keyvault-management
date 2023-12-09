import argparse
import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from dotenv import load_dotenv


def keyvault_url_from_kv_name(keyvault_name: str):
    """
    creating keyvault url from keyvault name
    :return:
    """
    keyvault_url = f"https://{keyvault_name.lower ()}.vault.azure.net"
    print (f"Key vault url is : , {keyvault_url}")
    return keyvault_url


def keyvault_management_operations(keyvault_name: str, operation: str, secret_name: str = "", secret_value: str = "", content: str = ""):
    credential = DefaultAzureCredential ()
    kv_url = keyvault_url_from_kv_name (keyvault_name)
    client = SecretClient (vault_url=kv_url, credential=credential)

    if operation == "set":
        print (f"Operation being performed is : Set on {keyvault_name}")
        client.set_secret (secret_name, secret_value)
        client.update_secret_properties(secret_name, content_type= content)
        print (f"Secret {secret_name} created on {keyvault_name}")

    elif operation == "list":
        print (f"Operation being performed is : List on {keyvault_name}")
        secrets_in_kv = client.list_properties_of_secrets ()
        print(f"Secrets in {keyvault_name} are : ")
        for secrets in secrets_in_kv:
            print(secrets.name)
        print (f"Secrets listed in {keyvault_name}")

    elif operation == "get":
        print (f"Operation being performed is : Get on {keyvault_name}")
        get_secret = client.get_secret(secret_name)
        print (f"secret value for {secret_name} is : {get_secret.value}")

    elif operation == "delete":
        print (f"Operation being performed is : Delete on {keyvault_name}")
        delete_secret = client.begin_delete_secret(secret_name).result ()
        print (f"deleting secret {secret_name} from {keyvault_name}")

    elif operation == "list_deleted_secrets":
        print (f"Operation being performed is : List deleted secrets on {keyvault_name}")
        list_deleted_secrets = client.list_deleted_secrets()
        print(f"Delted secrets in {keyvault_name} are : ")
        for secrets in list_deleted_secrets:
            print(f"Deleted secret name is : {secrets.name}")
            print(f"Deleted secret on : {secrets.deleted_date}")
            print(f"Deleted secret purge date is : {secrets.scheduled_purge_date}")
    elif operation == "recover":
        print(f"Operation being performed is : Recovery of secret on {keyvault_name}")
        recover_secret = client.begin_recover_deleted_secret(secret_name).result()
        print(f"Recovered secret {secret_name}")
    else:
        print (f"Invalid operation. Operation should be one among get, list, set, delete, list_deleted_secrets")



def main():
    """
    main function to test the script
    :return:
    """
    # Instatiate argparser
    parser = argparse.ArgumentParser (description='argumets for the function')
    parser.add_argument('--client_id',type=str, default= os.getenv('AZURE_CLIENT_ID'), help= 'azure client id for authentication')
    parser.add_argument('--client_secret', type=str, default=os.getenv('AZURE_CLIENT_SECRET'), help= 'azure client secret for authentication')
    parser.add_argument('--tenant_id', type=str, default=os.getenv('AZURE_TENANT_ID'), help= 'azure tenant id for authentication')
    parser.add_argument('--keyvault_name', type= str, required=True,help='Keyvault to authenticate and modify the secrets in it')
    parser.add_argument ('--operation', type= str,choices=['get', 'set', 'list', 'delete', 'list_deleted_secrets'],
                         required=True, help='get / set / list / delete / list_deleted_secrets / recover actions')
    parser.add_argument('--secret_name', type=str, help= 'secret name', default='')
    parser.add_argument('--secret_value', type=str, help = 'secret value to be modified in keyvault',default='')
    parser.add_argument('--content', type=str, help= 'content to add in secret metadata',default='')
    args = parser.parse_args()
    keyvault_name = args.keyvault_name
    operation = args.operation
    secret_name = args.secret_name
    secret_value = args.secret_value
    content =args.content

    keyvault_management_operations (keyvault_name = keyvault_name, operation = operation, secret_name = secret_name,
                                    secret_value = secret_value, content= content)



if __name__ == '__main__':
    main ()
