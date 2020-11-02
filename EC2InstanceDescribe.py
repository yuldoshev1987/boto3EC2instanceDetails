import boto3
import csv
client=boto3.client('ec2')
response=client.describe_instances()
# This function written by Rustam Yuldoshev
#You can get InstanceType,VpcId,SubnetId,AvailabilityZone,AccountNumber,Tags
#And write to CSV file to management purpose


def get_ec2_instanceDetails(fileName):
    client = boto3.client('ec2')
    response = client.describe_instances()
    Accoun='Acc-'
    with open(fileName,'w',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(['InstanceType','VpcId','SubnetId','AvailabilityZone','AccountNumber','TagTeamName'])
        for data in response.get('Reservations'):
            for data2 in data.get('Instances'):
                TeamName=''
                InstanceType=data2['InstanceType']
                VpcId = data2['VpcId']
                SubnetId = data2['SubnetId']
                AvailabilityZone=data2.get('Placement').get('AvailabilityZone')
                NetworkInterfaces = data2['NetworkInterfaces']
                for network in NetworkInterfaces:
                    OwnerId=Accoun+str((network['OwnerId']))
                    print(OwnerId)
                for tags in data2['Tags']:
                    TeamName = tags.get('Value')
                writer.writerow([InstanceType,VpcId,SubnetId,AvailabilityZone,OwnerId,TeamName])
get_ec2_instanceDetails('ec2instanceInfo.csv')