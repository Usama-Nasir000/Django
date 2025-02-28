# FROM python:3.4

# RUN apt-get update \
# 	&& apt-get install -y --no-install-recommends \
# 		postgresql-client \
# 	&& rm -rf /var/lib/apt/lists/*

# WORKDIR /usr/src/app
# COPY requirements.txt ./
# RUN pip install -r requirements.txt
# COPY . .

# EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



# NEW: Use latest Python version
FROM python:3.12 

# Update apt repositories and install PostgreSQL client
RUN apt-get update && apt-get install -y \
    libdbus-1-dev \
    libdbus-glib-1-dev \
    python3-dev \
    python3-setuptools \
    python3-wheel \
    meson \
    && rm -rf /var/lib/apt/lists/*


# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

