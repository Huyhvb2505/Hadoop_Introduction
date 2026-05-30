#!/usr/bin/env python3
"""
Exercise 1: Basic HDFS Operations
Level: Beginner

Learning Objectives:
- Connect to HDFS using Python
- Create directories in HDFS
- Upload and download files
- List directory contents
- Get file information

Tasks:
1. Connect to the HDFS cluster
2. Create a directory structure /exercises/exercise1/
3. Upload the sample_employees.csv file to HDFS
4. List the contents of your directory
5. Download the file back to a different location
6. Display file information (size, replication factor, etc.)
"""

from certifi import contents
from hdfs import InsecureClient
import os

def exercise1():
    """Complete the basic HDFS operations"""
    
    # TODO: Task 1 - Connect to HDFS
    # Initialize HDFileSystem with namenode host and port
    hdfs = InsecureClient('http://namenode:9870')  # Replace with your connection
    
    

    # TODO: Task 2 - Create directory structure
    # Create /exercises/exercise1/ directory
    hdfs.makedirs('/exercises/exercise1/')
    print("Directory created: /exercises/exercise1/")


    
    # TODO: Task 3 - Upload file
    # Upload /data/sample_employees.csv to /exercises/exercise1/employees.csv
    hdfs.upload('/exercises/exercise1/employees.csv','/data/sample_employees.csv' , overwrite=True)
    print("File uploaded successfully")
    # TODO: Task 4 - List directory contents
    # List and print the contents of /exercises/exercise1/
    contents = hdfs.list('/exercises/exercise1/' , status=True)
    print("Directory contents:")
    for name,item in contents:
        path = f'/exercises/exercise1/{name}'
        print(f"  {path} - Size: {item['length']} bytes")
    # TODO: Task 5 - Download file
    # Download the file to /exercises/downloaded_employees.csv
    hdfs.download('/exercises/exercise1/employees.csv', '/exercises/downloaded_employees.csv' , overwrite=True)
    print("File downloaded successfully")

    # TODO: Task 6 - Display file information
    # Get and print file information for the uploaded file
    file_info = hdfs.status('/exercises/exercise1/employees.csv')

    print("File Info:")
    print("  Name: /exercises/exercise1/employees.csv")
    print(f"  Size: {file_info['length']} bytes")
    print(f"  Replication: {file_info['replication']}")
    print(f"  Block size: {file_info['blockSize']} bytes")

    print("Exercise 1 completed!")

if __name__ == "__main__":
    exercise1()

# Expected Output:
"""
Directory created: /exercises/exercise1/
File uploaded successfully
Directory contents:
  /exercises/exercise1/employees.csv - Size: XXX bytes
File downloaded successfully
File Info:
  Name: /exercises/exercise1/employees.csv
  Size: XXX bytes
  Replication: 2
  Block size: XXXXXXX bytes
Exercise 1 completed!
"""

# Hints:
"""
1. Use InsecureClient('http://namenode:9870') to connect
2. Use hdfs.makedirs(path) to create directories
3. Use hdfs.upload(hdfs_path, local_path) for uploads
4. Use hdfs.list(path, status=True) to list contents
5. Use hdfs.download(hdfs_path, local_path) for downloads
6. Use hdfs.status(path) to get file information
"""
