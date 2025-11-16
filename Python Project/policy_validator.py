import os

# Path to the folder you want to check
folder_path = "policies"

# Expected extension
correct_extension = ".pdf"

# List all files in the folder
files = os.listdir(folder_path)

print("\nChecking Policy Files...\n")

#CHECK EACH FILE
for file in files:
    # Get full file path
    file_path = os.path.join(folder_path, file)
    
    # Check: file starts with "Policy_"
    if not file.startswith("Policy_"):
        print(f"❌ Incorrect name: {file}")
        continue
    
    # Check: correct extension
    if not file.endswith(correct_extension):
        print(f"❌ Wrong format: {file}")
        continue
    
    # If all checks pass
    print(f"✅ Correct file: {file}")
