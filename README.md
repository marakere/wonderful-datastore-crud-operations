# wonderful-datastore-crud-operations

AWS Services used in this project:
	- API Gateway
	- Lambda
	- RDS
	- IAM
	- Cloudwatch

#1. Create a new role to access S3 and lambda vpc access execution role
	- Under attach policy section, add AmazonS3ReadOnlyAccess and AWSLambdaVPCAccessExecutionRole
	- Edit the trust relationship as below
		{
		  "Version": "2012-10-17",
		  "Statement": [
		    {
		      "Effect": "Allow",
		      "Principal": {
		        "Service": "lambda.amazonaws.com"
		      },
		      "Action": "sts:AssumeRole"
		    }
		  ]
		}

#2. Create an RDS instance
	- Create a new Instance (MySQL 5.7.19)
	- Create a table tabledatastore with itemkey, itemvalue, itemstatus, itemts
	- Ensure Inbound and Outbound ports are enabled for your CIDR or Specific IP

#3. Clone the code 
	- Replace the rds_config.py values with the actual values from the step2

#4. Make file
	- Use the make file to generate the .zip files and upload to S3
	- Create 3 lambda functions and upload the approporate zip file for get, getbykey and post
	- Lambda handler should be changed to map the class file name
	- Test to ensure that Get and Post are working as expected

#5. API Gateway
	- Create a new API, resource
	- Add GET and POST methods
	- For getbykey, add the below json in Body Mapping templates
	{
    "itemkey": "$input.params('itemkey')"
	}