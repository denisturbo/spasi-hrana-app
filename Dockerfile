FROM python:3.12-slim

# Set workdir
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    nodejs \
    npm \
    && apt-get clean

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install Tailwind dependencies
RUN python manage.py tailwind install

CMD ["gunicorn", "spasihrana.wsgi:application", "--bind", "0.0.0.0:8000"]