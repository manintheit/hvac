import hvac
import os
VAULT_ADDR=os.getenv("VAULT_ADDR","http://10.213.160.242:8200")
VAULT_TOKEN=os.getenv("VAULT_TOKEN","sometoken")
MOUNT_POINT=os.getenv("MOUNT_POINT","mysecret")

client = client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN,)

# The following path corresponds, when combined with the mount point, to a full Vault API route of "v1/secretz/hvac"

def read_secrets_kv_v1(path, mount_point):
    read_secret_result = client.secrets.kv.v1.read_secret(path=path,mount_point=mount_point,)
    return read_secret_result

user=read_secrets_kv_v1("infrastructre/ilo", "mysecret")['data']['username']
password=read_secrets_kv_v1("infrastructre/ilo", "mysecret")['data']['password']

print(user)






