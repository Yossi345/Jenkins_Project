import boto3

# Create a connection to the EC2 service
ec2 = boto3.client('ec2')

# Define the filters for the query
filters = [
    {'Name': 'tag:k8s.io/role/master', 'Values': ['1']},
    {'Name': 'instance-state-code', 'Values': ['80']}
]

# Use the filters to get a list of instances
response = ec2.describe_instances(Filters=filters)

# Loop through the instances and print the instance ID and name
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        instance_name = ''
        for tag in instance['Tags']:
            if tag['Key'] == 'Name':
                instance_name = tag['Value']
                break
        print(f"Instance ID: {instance_id}\tInstance Name: {instance_name}")
