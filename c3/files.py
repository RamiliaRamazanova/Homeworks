with open("journal", 'r') as journal:
    for line in journal:
        points = int(line.split()[-1])
        if points < 3:
            print(line.split()[:2])


