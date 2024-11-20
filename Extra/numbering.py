import os

def rename_files_to_numbers(folder_path,file_name):
    try:
        # List all files in the folder
        files = os.listdir(folder_path)
        
        # Sort files to maintain order if required
        files.sort()

        # Loop through files and rename them with consecutive numbers
        for index, filename in enumerate(files, start=1):
            # Get the file extension
            file_extension = os.path.splitext(filename)[1]
            
            # Define new filename with a number and original extension
            new_filename = f"{file_name}{index}{file_extension}"
            
            # Construct the full paths
            original_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)
            
            # Rename the file
            os.rename(original_path, new_path)
        
        print(f"Files in '{folder_path}' have been renamed to numbers successfully.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the directory path
directory_path = "F:\projects\Fruit and vegtable website\Model\Data\\archive\\train"

# List to store folder names
folder_list = []

# Loop through the directory
for item in os.listdir(directory_path):
    # Check if the item is a folder
    if os.path.isdir(os.path.join(directory_path, item)):
        folder_list.append(item)
print(folder_list)
# # Example usage:
# for x in folder_list:
#     print(x)
#     folder_path = f"F:\projects\Fruit and vegtable website\Model\Data\\archive\\train\\{x}"  # Replace with your folder path
#     rename_files_to_numbers(folder_path,"3213151")
#     rename_files_to_numbers(folder_path,"image_")
#     folder_path = f"F:\projects\Fruit and vegtable website\Model\Data\\archive\\test\\{x}"  # Replace with your folder path
#     rename_files_to_numbers(folder_path,"3213151")
#     rename_files_to_numbers(folder_path,"image_")
#     folder_path = f"F:\projects\Fruit and vegtable website\Model\Data\\archive\\validation\\{x}"  # Replace with your folder path
#     rename_files_to_numbers(folder_path,"321315511")
#     rename_files_to_numbers(folder_path,"image_")
#     print("------------------------------------------------")
