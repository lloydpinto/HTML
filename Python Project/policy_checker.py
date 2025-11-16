import os

# ---------------------------------------------
# 1. SETUP
# ---------------------------------------------

# Folder to check (change this if needed)
folder_path = "policies"

# Correct file extension
correct_extension = ".pdf"

# List of required policy files you expect to be present
required_files = [
    "Policy_HR_2024.pdf",
    "Policy_IT_2024.pdf",
    "Policy_Finance_2024.pdf"
]

# Create empty lists to store results
correct_files = []
incorrect_names = []
wrong_format = []
wrong_year = []
missing_files = []

# ---------------------------------------------
# 2. READ ALL FILES FROM THE FOLDER
# ---------------------------------------------

# Get all files available in the folder
files = os.listdir(folder_path)

print("\nChecking Policy Files...\n")

# ---------------------------------------------
# 3. CHECK EACH FILE
# ---------------------------------------------

for file in files:

    # Get full file path
    file_path = os.path.join(folder_path, file)

    # -----------------------
    # CHECK 1: Name starts with "Policy_"
    # -----------------------
    if not file.startswith("Policy_"):
        incorrect_names.append(file)
        print(f"❌ Incorrect name: {file}")
        continue  # Skip remaining checks for this file

    # -----------------------
    # CHECK 2: Correct extension (.pdf)
    # -----------------------
    if not file.endswith(correct_extension):
        wrong_format.append(file)
        print(f"❌ Wrong format: {file}")
        continue

    # -----------------------
    # CHECK 3: Correct year format (should be 4 digits)
    # Example: Policy_HR_2024.pdf → year = 2024
    # -----------------------
    try:
        # Split name by '_' → ["Policy", "HR", "2024.pdf"]
        parts = file.split("_")

        # Take the last part → "2024.pdf"
        # Remove ".pdf" → "2024"
        year = parts[-1].replace(".pdf", "")

        # Check if year is a digit AND is 4 digits
        if not year.isdigit() or len(year) != 4:
            wrong_year.append(file)
            print(f"❌ Wrong year format: {file}")
            continue

    except:
        wrong_year.append(file)
        print(f"❌ Unable to read year: {file}")
        continue

    # If all checks are correct, store it
    correct_files.append(file)
    print(f"✅ Correct file: {file}")

# ---------------------------------------------
# 4. CHECK MISSING FILES
# ---------------------------------------------

for required in required_files:
    if required not in files:
        missing_files.append(required)

# ---------------------------------------------
# 5. GENERATE REPORT FILE (report.txt)
# ---------------------------------------------

report_path = "report.txt"

with open(report_path, "w") as report:

    report.write("==== POLICY FILE VALIDATION REPORT ====\n\n")

    report.write("Correct Files:\n")
    for f in correct_files:
        report.write(f"  - {f}\n")

    report.write("\nIncorrect Names:\n")
    for f in incorrect_names:
        report.write(f"  - {f}\n")

    report.write("\nWrong Format (not PDF):\n")
    for f in wrong_format:
        report.write(f"  - {f}\n")

    report.write("\nWrong Year Format:\n")
    for f in wrong_year:
        report.write(f"  - {f}\n")

    report.write("\nMissing Required Files:\n")
    for f in missing_files:
        report.write(f"  - {f}\n")

print("\n📄 Report generated: report.txt")
print("✔ Script completed successfully!")
