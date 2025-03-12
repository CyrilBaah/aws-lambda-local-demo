# AWS Lambda Function 

This guide provides a step-by-step process to configure, build, and run an AWS Lambda function locally . The Lambda function can handle HTTP requests to return data such as countries, names, and todos.

---
## Prerequisites
Before you begin, ensure you have the following installed:

- Docker ([Install Docker](https://docs.docker.com/get-docker/))
- AWS CLI ([Install AWS CLI](https://aws.amazon.com/cli/))
- Python 3.x ([Install Python](https://www.python.org/downloads/))
- AWS Runtime Interface Emulator ([AWS RIE](https://github.com/aws/aws-lambda-runtime-interface-emulator))


---
## Building and Running the Dockerized Lambda Function

### 1. Build the Docker Image
Run the following command to build the Docker image for the Lambda function:
```sh
 docker build -t aws_lambda:latest .
```

### 2. Run the Docker Container
Start the container and expose it on port `9000`:
```sh
 docker run -p 9000:8080 aws_lambda:latest
```

### 3. Test the Lambda Function
To verify that the Lambda function is running, send a test request:
```sh
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{ "path": "/",
  "httpMethod": "GET"
}'
```

---
## API Endpoints
The Lambda function supports multiple endpoints. Use the following commands to test each endpoint:

### Get All Countries
```sh
 curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"httpMethod": "GET", "path": "/countries"}'
```

### Get All Names
```sh
 curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"httpMethod": "GET", "path": "/names"}'
```

### Get All Todos
```sh
 curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"httpMethod": "GET", "path": "/todos"}'
```

---
## Deployment to AWS Lambda
To deploy the Containerized Lambda function to AWS Lambda:

1. Authenticate with AWS:
   ```sh
    aws configure
   ```
2. Create an ECR repository:
   ```sh
    aws ecr create-repository --repository-name aws_lambda
   ```
3. Tag the Docker image:
   ```sh
    docker tag aws_lambda:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/aws_lambda:latest
   ```
4. Push the image to ECR:
   ```sh
    docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/aws_lambda:latest
   ```
5. Create a new Lambda function using the uploaded image:
   ```sh
    aws lambda create-function --function-name aws_lambda --package-type Image --code ImageUri=<aws_account_id>.dkr.ecr.<region>.amazonaws.com/aws_lambda:latest --role <execution_role_arn>
   ```


