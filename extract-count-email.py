#This script counts and extract sender's email from a text file.
    fname = input("Enter name of File: ")
    fhand = open (fname)
    count = 0
    for line in fhand:
            line = line.rstrip()
                if not line.startswith("From") or line.startswith("From:"):
                            continue #skipping to the beginning
                            #elif line.startswith("From:"):
                                #    continue
                                    else:
                                                count += 1
                                                    words = line.split() #the () is for empty spaces you can split with ; i.e. line.split(;)
                                                        email = words[1]
                                                            print(email)
                                                            print("There were", count, "lines in the file with From as the first word")

