
 # File Manager Program

import os

# Function to list files
def list_files(directory):
  print("Files in", directory)
  for filename in os.listdir(directory):
    print(filename)

# Function to create a new file
def create_file(filename):
  open(filename, "w").close()
  print(filename, "created")

# Function to delete a file
def delete_file(filename):
  os.remove(filename)
  print(filename, "deleted")

# Function to rename a file
def rename_file(old_filename, new_filename):
  os.rename(old_filename, new_filename)
  print(old_filename, "renamed to", new_filename)

# Main program
while True:
  print("1. List Files")
  print("2. Create File")
  print("3. Delete File")
  print("4. Rename File")
  print("5. Exit")
  choice = input("Enter your choice: ")
  if choice == "1":
    directory = input("Enter directory: ")
    list_files(directory)
  elif choice == "2":
    filename = input("Enter filename: ")
    create_file(filename)
  elif choice == "3":
    filename = input("Enter filename: ")
    delete_file(filename)
  elif choice == "4":
    old_filename = input("Enter old filename: ")
    new_filename = input("Enter new filename: ")
    rename_file(old_filename, new_filename)
  elif choice == "5":
    break
  else:
    print("Invalid choice. Please try again.")


#This program allows users to:

#- List files in a directory
#- Create a new file
#- Delete a file
#- Rename a file