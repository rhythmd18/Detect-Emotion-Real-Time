# Base Image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements from host to container
COPY requirements.txt /app

# Install dependencies
RUN pip cache purge
RUN pip install -r requirements.txt
RUN pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cpu

# Copy all files from host to container
COPY . .

# Expose port
EXPOSE 5000

# Define default command
CMD ["python", "src/app.py"]