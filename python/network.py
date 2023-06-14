import paramiko

# Define the SSH connection details
hostname = '34.227.150.197'
username = 'ubuntu'
password = 'ubuntu'

# Create an SSH client object
client = paramiko.SSHClient()

# Automatically add the host to the known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the remote machine
    client.connect(hostname=3.93.76.171, username=ec2-user, password=ec2-user)

    # Execute the command to retrieve networking details
    command = "ifconfig"
    stdin, stdout, stderr = client.exec_command(command)

    # Read the output of the command
    output = stdout.read().decode()

    # Print the networking details
    print(output)

finally:
    # Close the SSH connection
    client.close()
