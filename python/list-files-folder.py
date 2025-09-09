import os

def list_files_in_folders(folder_path):
   try:
      files = os.listdir(folder_path)
      return files, None
   except FileNotFoundError:
      return None, "Folder not found"
   except PermissionError:
      return None, "Permission denied"
   
def main():
   folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
   
   for folder in folder_paths:
      files, error = list_files_in_folders(folder)
      if error:
         print(f"Error accessing folder '{folder}': {error} ")
      else:
            print(f"Files in folder '{folder}':")
            for file in files:
                print(file)
            #print()  

   
if __name__ == "__main__":
   main()   

