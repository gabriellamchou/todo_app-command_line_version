filenames = ["1.doc", "1.report", "1.presentation"]

filenames = [item.replace('.', '-', 1) + '.txt' for item in filenames]

print(filenames)
