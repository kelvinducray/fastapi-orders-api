ARG VARIANT=3.9
# ARG PROJECT_NAME=fastapi-orders-api
FROM python:${VARIANT}

# Headless installs
ENV DEBIAN_FRONTEND=noninteractive

# Configure the timezone
ENV TZ=Australia/Sydney

# Create user account with sudo rights and make it the owner of the project dir.
RUN useradd -u 1001 -m -d /home/developer -s /bin/bash developer \
    && echo "developer ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# RUN chown -R developer:developer /workspaces/${PROJECT_NAME} \
#     && chmod -R ugo+rw /workspaces/${PROJECT_NAME}

# Install Poetry
RUN pip install --upgrade pip
RUN pip install poetry
ENV PATH="/home/developer/.local/bin:$PATH"
RUN poetry config virtualenvs.in-project true
