filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for idx, filename in enumerate(filenames):
    file = open(f"files/{filenames[idx]}", 'w')
    file.writelines("Hello")
    file.close()
