import paramiko

# Define the SSH connection details for both machines
source_host = '34.227.150.197'
source_username = 'ubuntu'
source_password = 'ubuntu'

destination_host = '3.93.76.171'
destination_username = 'ec2-user'
destination_password = 'ec2-user'

# Define the source and destination file paths
source_path = '/opt/*'
destination_path = '/opt/'

# Create SSH client objects for both machines
source_client = paramiko.SSHClient()
destination_client = paramiko.SSHClient()

# Automatically add the source and destination hosts to the known hosts
source_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
destination_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the source machine
    source_client.connect(hostname=source_host, username=source_username, password=source_password)
    # Connect to the destination machine
    destination_client.connect(hostname=destination_host, username=destination_username, password=destination_password)

    # Create SFTP client objects for both machines
    source_sftp = source_client.open_sftp()
    destination_sftp = destination_client.open_sftp()

    # Copy the file from source to destination
    source_sftp.get(source_path, destination_path)

    print(f"File '{source_path}' copied successfully to '{destination_path}'.")

finally:
    # Close the SFTP and SSH connections
    source_sftp.close()
    destination_sftp.close()
    source_client.close()
    destination_client.close()
