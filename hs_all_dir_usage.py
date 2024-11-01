import os
import csv
import subprocess

# Prompt user for the mount point
mount_point = input("Enter the drive mount (e.g., 'Z:'): ").strip()

# Validate the mount point exists
if not os.path.exists(mount_point):
    print(f"The mount point {mount_point} does not exist.")
    exit(1)

# Prepare CSV file
output_file = "directory_analysis.csv"
with open(output_file, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Directory", "HS Output"])

    # Walk the directory tree
    for root, dirs, _ in os.walk(mount_point):
        for directory in dirs:
            selected_directory = os.path.join(root, directory)
            print(f"Processing: {selected_directory}")

            # Run the "hs sum" command on the selected directory
            try:
                result = subprocess.check_output(
                    ["hs", "sum", "-e", "IS_FILE?{FILE,SPACE_USED}", selected_directory],
                    stderr=subprocess.STDOUT,
                    text=True
                ).strip()
            except subprocess.CalledProcessError as e:
                result = f"Error: {e.output.strip()}"
                print(result)

            # Write the result to the CSV
            csv_writer.writerow([selected_directory, result])

print(f"Analysis complete. Results saved to {output_file}.")
