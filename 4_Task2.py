data = input("Enter text to write to the file: ")
with open("output.txt", "w") as f:
    f.write(data + "\n")

more = input("Enter additional text to append: ")
with open("output.txt", "a") as f:
    f.write(more + "\n")

with open("output.txt", "r") as f:
    print("\nFinal content of output.txt:")
    print(f.read())