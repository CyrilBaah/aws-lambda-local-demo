# Define function directory
ARG FUNCTION_DIR="/function"

FROM python:buster as build-image

# Include global arg in this stage of the build
ARG FUNCTION_DIR

# Create function directory
RUN mkdir -p ${FUNCTION_DIR}
WORKDIR ${FUNCTION_DIR}

# update and upgrade image
RUN apt update && apt upgrade -y

# install python
RUN apt install python3 -y
RUN apt install python3-venv -y

# create and activate virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install the runtime interface client
RUN pip install --upgrade pip && \
    pip install awslambdaric --target ${FUNCTION_DIR}

# Copy function code
COPY . .
FROM python:buster

# Include global arg in this stage of the build
ARG FUNCTION_DIR

# Set working directory to function root directory
WORKDIR ${FUNCTION_DIR}

# Copy in the build image dependencies
COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}

# Add and execute script
RUN ["chmod","+x","/function/awscli-bundle/install"]
RUN ["/function/awscli-bundle/install","-i","/usr/local/aws","-b","/opt/aws"]

ADD aws-lambda-rie /usr/local/bin/aws-lambda-rie

RUN ["chmod", "+x", "/usr/local/bin/aws-lambda-rie"]
ENTRYPOINT ["sh", "/function/entry_script.sh" ]
CMD ["app.handler"]