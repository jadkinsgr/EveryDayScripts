# Open the text file in read mode
with open('table.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Process each line as needed
        print(f"Create Table bronze.clarity.{line.strip()}")  # For example, print each line (stripped of leading/trailing whitespace)
