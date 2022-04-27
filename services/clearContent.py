
# clear files content
def clearContent(files):
    for file in files:
        with open(file, 'wb') as file:
            file.truncate()
