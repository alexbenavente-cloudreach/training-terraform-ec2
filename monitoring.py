import boto3

# GET SUBNET INFORMATION
def getPrivateSubnetId():
    ec2_client = boto3.client('ec2')
    subnets_info = ec2_client.describe_subnets()

    for subnet in subnets_info['Subnets']:
        if subnet["Tags"][0]["Value"] == "talent-academy-private-a":
            private_subnet = subnet["SubnetId"]
            return private_subnet

private_subnet = getPrivateSubnetId()

ec2 = boto3.resource('ec2')
    
for instance in ec2.instances.all():
    if instance.subnet_id == private_subnet:
        print(
            "Id: {0}\nType: {1}\nAMI: {2}\nState: {3}\nSubnet: {4}".format(
            instance.id, instance.instance_type, instance.image.id, instance.state, instance.subnet_id
            )
        )
