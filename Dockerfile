FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port from environment variable or default to 5000
ENV PORT=4321
EXPOSE $PORT

# Run the application
CMD ["sh", "-c", "python app.py --port=$PORT"]
