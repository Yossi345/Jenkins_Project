import boto3
ec2 = boto3.client('ec2')
response = ec2.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-code',
            'Values': ['80']
        },
#        {
#            'Name': 'tag:k8s.io/role/master',
#            'Values': ['1']
#        }
    ]
)

for each_reservation in response["Reservations"]: 
    for each_instance in each_reservation["Instances"]:
        print("Reserved_id:{}\tinstance_id:{}".format(
            each_instance["Value"],
            each_instance["InstanceId"])) 


if __name__ == '__main__':
    list_running_instances()
