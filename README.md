# aws-lambda-local-demo
Running AWS Lambda locally using AWS RIE and Docker

# How to Configure the Lambda Function

## 1. Build the Docker Image
```sh
 docker build -t aws_lambda:latest .
```

## 2. Run the Docker Container
```sh
 docker run -p 9000:8080 aws_lambda:latest
```

## 3. Test the Docker Container
```sh
 curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{
  "path": "/",
  "httpMethod": "GET"
}'
```

## 4. Test the API Endpoints

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

