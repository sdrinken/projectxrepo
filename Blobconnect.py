def get_blob_service_client_account_key(self):
    # TODO: Replace <storage-account-name> with your actual storage account name
    account_url = "https://aiaprojectxstorage.blob.core.windows.net"
    shared_access_key = "gtrbirx4XyTqmAU0Gu8YoFDJay8NHqWQqTLi+4LBnBWuqHY5mR1smotzRBx7ztjtj/xTB57N+lxm+AStBdydDg=="
    credential = shared_access_key

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient(account_url, credential=credential)

    return blob_service_client