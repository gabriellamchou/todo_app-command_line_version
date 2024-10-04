filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for idx, filename in enumerate(filenames):
    filenames[idx] = filename.replace('.', '-', 1)

print(filenames)
