contents = ["Content for the doc file",
            "Content for the report file",
            "Content for the presentation file"]

filenames = ["doc.txt",
             "report.txt",
             "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(rf"files\{filename}", 'w')
    file.writelines(content)
    file.close()
