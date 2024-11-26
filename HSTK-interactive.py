#!/usr/bin/env python
# HSTK-interactive.py
# Designed to be ran with chron 
# Generate directory usage reports in CSV format for Hammerspace shares.
# Ver 1.0
#   Initial Release, Variables for directory and output.
#

import subprocess
import os
import csv

def run_hs_sum_and_format_output(directory, output_file):
    command = f"find {directory} -type d | xargs hs sum -e 'IS_FILE?{{1FILES/FILE,SPACE_USED/BYTES}}'"

    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        output, error = process.communicate()

        if error:
            print(f"Error 1  executing command: {error.decode()}")
        else:
            output_lines = output.decode().splitlines()

            with open(output_file, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                for line in output_lines:
                    parts = line.strip().split()
                    if len(parts) == 3:
                        csv_writer.writerow(parts)

    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

if __name__ == "__main__":
    directory = input("Enter the directory or mount point: ")
    output_file = input("Enter the output file path: ")

    run_hs_sum_and_format_output(directory, output_file)