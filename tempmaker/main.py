
# Modification date: Sat Jan 22 00:02:36 2022

# Production date: Sun Sep  3 15:44:14 2023

filename = input("Enter file name: ")
filename = filename + ".txt"

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(12):
    temp = input(f"Enter the avg temp of {months[i]}: ")
    temp = temp + "\n"
    f = open(filename, "a")
    for j in range(month_days[i]):
        f.write(temp)
    f.close()
print("done!")