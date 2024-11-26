#!/usr/bin/env python
# HSTK-dir-report.py
# Designed to be ran with chron 
# Generate directory usage reports in CSV format for Hammerspace shares.
# Ver 1.0
#   Initial Release, Variables for directory and output.
#

import subprocess
import csv

def run_directory_check_and_generate_csv():
    # VARIABLES
    """Run the command on the /hs directory and output data in CSV format to /tmp/hs-dir-stats.csv."""
    directory = "/hs"
    output_file = "/tmp/hs-dir-stats.csv"

    try:
        # HSTK command to run
        command = f"find {directory} -type d | xargs hs sum -e 'IS_FILE?{{1FILES/FILE,SPACE_USED/BYTES}}'"
        # Execute the command and capture its output
        result = subprocess.run(
            command, 
            shell=True, 
            universal_newlines=True,  # Ensures output is a string
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            check=True
        )
        
        # Process the command output
        data = []
        lines = result.stdout.splitlines()
        for i in range(0, len(lines), 2):
            directory = lines[i].strip()
            # Strip leading "####"
            if directory.startswith("#####"):
                directory = directory[5:].strip()
                
            file_info = lines[i + 1].strip()
            if file_info == "#EMPTY":
                file_info = "{0,0}"
            file_count, size_bytes = map(int, file_info.strip("{}").split(","))
            data.append([directory, file_count, size_bytes])
        
        # Write data to CSV
        with open(output_file, mode='w', newline='') as f:
            writer = csv.writer(f)
            # Write the header
            writer.writerow(["Directory", "File Count", "Size (Bytes)"])
            # Write the rows
            writer.writerows(data)
        
        print(f"Data successfully written to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error running the command: {e}")
        print(f"Command output: {e.output}")

# Run the function
if __name__ == "__main__":
    run_directory_check_and_generate_csv()
