# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Gradio’s default port
EXPOSE 7860

# Run the Gradio app
CMD ["python", "app.py"]