import boto3
import datetime

def lambda_handler(event, context):
  ec2 = boto3.client('ec2')
  now = datetime.datetime.now()
  if now.hour == 9:
    ec2.start_instances(InstancesID=['i-122334445'])
    print("Start Instance")
  elif now.hour == 18:
    ec2.stop_instances(InstancesID=['i-122334445'])
    print("Stop Instance")
  return {
    'statuscode' = 200,
    'body' = 'Function Executed'
  }
