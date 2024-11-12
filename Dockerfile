
# Use an official Python runtime as a parent image
FROM python:3.10-slim 

# Set the working directory in the container to /app
WORKDIR /app

# Copy the require,ents file into the container at /app
COPY requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . . 

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
