#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#networkinterface

import boto3

client = boto3.client('ec2')

def lambda_handler(event, context):
    
    response = client.request_spot_instances(
        InstanceCount=1,
        LaunchSpecification={
            
            'ImageId': 'ami-0b69ea66ff7391e80',
            'InstanceType': 't2.micro',
            'KeyName': 'isengard-virginia-laptop',
            'Placement': {
                'AvailabilityZone': 'us-east-1a',
            },
            'SecurityGroupIds': [
                'sg-0c2077153d0e3c550',
            ],
        },
        SpotPrice='0.005',
        Type='one-time',
    )
    
    print(response)
    print("\nCongrats! Your Spot instance is launched")
