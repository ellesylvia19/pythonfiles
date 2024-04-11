    # Create a new text file named "my_file.txt" in write mode ('w')
    with open('my_file.txt', 'w') as file:
        # Write three lines of text to the file
        file.write("This is line 1.\n")
        file.write("12345\n")
        file.write("Hello, world!\n")

    print("File 'my_file.txt' created and text written successfully.")

    # Open the file in read mode ('r') and display its contents
    with open('my_file.txt', 'r') as file:
        contents = file.read()
        print("Contents of 'my_file.txt' (read mode):")
        print(contents)

    # Open the file in append mode ('a') and append three more lines of text
    with open('my_file.txt', 'a') as file:
        file.write("This is line 4 (appended).\n")
        file.write("54321 (appended)\n")
        file.write("Goodbye, world! (appended)\n")

    print("Text appended to 'my_file.txt'.")

except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied to access the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Execution completed.")
