FROM vercel/python

# Install Tesseract and other dependencies
RUN apt-get update && apt-get install -y tesseract-ocr

# Set the working directory
WORKDIR /vercel/workpath

# Copy your project files
COPY . .

# Set the entrypoint
CMD ["python", "app.py"]