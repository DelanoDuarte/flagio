# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /server

# Copy the current directory contents into the container at /app
COPY . /server

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Make the script executable
RUN flask db upgrade

# Run app.py when the container launches
CMD ["python", "run.py"]