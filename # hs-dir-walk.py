# hs-dir-walk.py
# ver 1
# Author: Jeff Parker
def parse_directory_data(input_file, output_file):
    output_lines = []
    
    with open(input_file, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines), 2):
            # Parse Line 1 (Directory)
            directory = lines[i].strip().lstrip('#').strip()
            # Parse Line 2 (File count and size)
            file_info = lines[i + 1].strip()
            file_count, size_bytes = map(int, file_info.strip("{}").split(","))
            
            # Format the output
            size_line = f'node_directory_size_bytes{{directory="{directory}"}} {size_bytes}'
            count_line = f'node_directory_file_count{{directory="{directory}"}} {file_count}'
            
            output_lines.append(size_line)
            output_lines.append(count_line)
    
    # Write to output file
    with open(output_file, 'w') as f:
        f.write("\n".join(output_lines))
    
    # Print to STDOUT
    print("\n".join(output_lines))

# Main script
if __name__ == "__main__":
    input_file = input("Enter the path to the input file: ").strip()
    output_file = input("Enter the path to the output file: ").strip()
    
    parse_directory_data(input_file, output_file)