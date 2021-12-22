ARG VARIANT=3.9
FROM python:${VARIANT}

# Headless installs
ENV DEBIAN_FRONTEND=noninteractive

# Configure the timezone
ENV TZ=Australia/Sydney

# Create user account with sudo rights
RUN useradd -u 1001 -m -d /home/developer -s /bin/bash developer \
    && echo "developer ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER developer

# Install Poetry
RUN pip install --upgrade pip
RUN pip install --user poetry
ENV PATH="/home/developer/.local/bin:$PATH"
RUN poetry config virtualenvs.in-project true
