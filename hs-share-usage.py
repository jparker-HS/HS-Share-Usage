import os
import subprocess

def select_directory(mount_point):
    # Get all directories in the specified mount point
    directories = [d for d in os.listdir(mount_point) if os.path.isdir(os.path.join(mount_point, d))]

    if not directories:
        print(f"No directories found in {mount_point}.")
        return None

    # Display the directories and ask the user to choose one
    print("Select a directory to analyze:")
    for i, directory in enumerate(directories, start=1):
        print(f"{i}: {directory}")

    # Validate the user's choice
    while True:
        try:
            selection = int(input("Enter the number of the directory you want to select: "))
            if 1 <= selection <= len(directories):
                break
            else:
                print(f"Invalid selection. Please enter a number between 1 and {len(directories)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    return os.path.join(mount_point, directories[selection - 1])

def main():
    while True:
        # Prompt for the mount point
        mount_point = input("Enter the mount point (e.g., Z:\\): ")

        # Ensure the mount point exists
        if not os.path.exists(mount_point):
            print(f"The mount point {mount_point} does not exist.")
            continue

        # Ask the user if they want to analyze the entire mount point or select a directory
        analyze_mount_point = input("Do you want to analyze the entire mount point? (Y/N): ").strip().lower()

        if analyze_mount_point == 'y':
            # Run the command on the mount point itself
            print(f"Running analysis on the entire mount point {mount_point}...")
            command = f"hs sum -e IS_FILE?{{FILE,SPACE_USED}} {mount_point}"
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
             print(result.stdout)
            else:
             print(f"Error executing command: {result.stderr}")
            
        else:
            # Select a directory within the mount point
            selected_directory = select_directory(mount_point)

            if selected_directory:
                # Run the command on the selected directory
                print(f"Running analysis on {selected_directory}...")
                command = f"hs sum -e IS_FILE?{{FILE,SPACE_USED}} {selected_directory}"
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                 print(result.stdout)
                else:
                 print(f"Error executing command: {result.stderr}")
                
        # Ask if the user wants to check another directory or mount point
        check_another = input("Would you like to check another directory or mount point? (Y/N): ").strip().lower()
        if check_another == 'n':
            break

if __name__ == "__main__":
    main()
