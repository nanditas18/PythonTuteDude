with open("sample.txt",'rt') as fh:
    try:  
        i = 1
        for line in fh:
            print("line", i, ":", line.strip())
            i += 1
    except FileNotFoundError:
        print(f"The file {fh} was not found. ")