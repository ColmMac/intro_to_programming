import datetime 

entry = input("Enter journal entry: ")

with open("journal.txt", "a") as f:
    f.write(f"\n{datetime.datetime.now()}: {entry}")

f.close()