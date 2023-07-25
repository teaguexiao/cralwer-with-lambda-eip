import boto3

INSTANCE_ID = 'i-0e60f8cbe4f80f53c'

client = boto3.client('ec2')

def lambda_handler(event, context):
    
    try:
        #find the current EIP
        response = client.describe_addresses(
            Filters=[
                {
                    'Name': 'instance-id',
                    'Values': [
                        INSTANCE_ID,
                    ],
                },
            ],
        )
        INSTANCE_EIP = response["Addresses"][0]["AllocationId"]
        print("\nYour current EIP is " + INSTANCE_EIP + "  ,now releasting it")
        
        #release the current EIP
        response = client.release_address(
            AllocationId=INSTANCE_EIP,
        )
        print(response)
        print("\nReleased successed! Requesting new EIP now.") 
        
    except:
        print("there's no EIP previously assigned")
        
    #request new EIP address
    request_eip = client.allocate_address(
        Domain='vpc'
    )

    EIP = request_eip["PublicIp"]
    ALLOCATION_ID = request_eip["AllocationId"]
    
    #associate the EIP to the instance
    response = client.associate_address(
        AllocationId = ALLOCATION_ID,
        InstanceId = INSTANCE_ID,
        AllowReassociation = True,
    )
    
    print("\n")
    print(response)
    print("\n")
    print("You new EIP " + EIP + " has been assigned to instance " + INSTANCE_ID)
    print("\n")
