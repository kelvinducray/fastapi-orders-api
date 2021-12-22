ARG VARIANT
FROM python:${VARIANT}

# Headless installs
ENV DEBIAN_FRONTEND=noninteractive

# Configure the timezone
ENV TZ=Australia/Sydney

# Create user account with sudo rights and make it the owner of the project dir.
RUN useradd -u 1001 -m -d /home/developer -s /bin/bash developers \
    && echo "developers ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

RUN chown -R developer:developers /workspaces/${VARIANT} \
    && chmod -R ugo+rw /workspaces/${VARIANT}

USER developer

# Install Poetry
RUN pip install --upgrade pip && pip install poetry
RUN poetry config virtualenvs.in-project true

# Initalise virtual environment
CMD poetry shell
