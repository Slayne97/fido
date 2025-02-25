FROM python:3.13-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install dependencies
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y libpq-dev

# Copy Scripts
COPY ./docker/django/entrypoint /entrypoint
COPY ./docker/django/start /start
RUN sed -i 's/\r$//g' /entrypoint
RUN sed -i 's/\r$//g' /start
RUN chmod +x /entrypoint
RUN chmod +x /start

# Set work directory and copy project
WORKDIR /backend
COPY . /backend
RUN pip install -r /backend/requirements.txt


# Keep the container up for debugging
# CMD ["tail", "-f", "/dev/null"]

# Run the entrypoint script
ENTRYPOINT ["sh", "/entrypoint"]