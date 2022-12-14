# First semester test example program
# Written by AM on 14 Dec 22
# Please ONLY use this program and its code as example only and not in production project
# Comments will be include at every single line to get you to know more about Python, be sure to read it to understand what is going on

# The code will be separated into sections, each of it corresponds to one exercise of the test. Make sure you read the correct exercise you are working on

# Exercise 1: Insert 3 scores from 0 to 10 and calculate the average round it to the nearest ten-thousandth, checks whether the user passes the test or not.

# Part 1: Ask user for their score
score1 = float(input("Enter your first score: ")) # Prompt user to enter their first score, then save it as score1
score2 = float(input("Enter your second score: ")) # Prompt user to enter their second score, then save it as score2
score3 = float(input("Enter your third score: ")) # Prompt user to enter their third score, then save it as score3

# Part 2: Calculate the average
# You can use whatever module if you want, but we only focus on the most basic implementation of calculating the average, which is divide the sum by the number of scores, 3.
aver = (score1 + score2 + score3) / 3 # Calculate average and save as aver
aver = round(aver, 4) # And round to the nearest ten-thousandth

# Part 3: Return results
print("Diem trung binh la " + str(aver)) # Print average, you can use f-string if you want
if aver >= 5: # If average is higher or equal to 5
	print("Qua mon") # Passed
elif aver < 5: # If average is less than 5
	print("Khong qua mon") # Failed
else: # Other weird cases
	print("Undefined error") # Raise error
	
# Exercise 2: Double number
# Basically ask for a number, and then print out its double counterpart
num = int(input("Nhap gia tri n: ")) # Ask user for input of a number, save it as num
print("So gap doi: " + str(num * 2)) # Multiply it up and print it out

# Exercise 3: Calculate electricity bill
name = input("Ho va ten: ") # Ask user for their name
chiso1 = int(input("Nhap chi so thang truoc: ")) # Ask user for last month counter
chiso2 = int(input("Nhap chi so thang sau: ")) # Current one
diff = chiso2 - chiso1 # Calculate this month usage
print("Ho va ten: " + name) # Print out the name again, which is a requirement
if diff <= 60: # If used less than 60kWh
	print("Tien phai tra la: " + str(diff * 5))
elif diff > 60 and diff <= 160: # If used more than 60 but less than 160
	print("Tien phai tra la: " + str((diff - 60) * 8 + 60 * 5))
elif diff >= 160: # If used more than 160
  print("Tien phai tra la: " + str((diff - 160) * 10 + 60 * 5 + 100 * 8))
else: # If none of that is True
  print("Undefined Error")

# Exercise 4: Calculate (-) point
# Part 1: Ask for the rules
a = int(input("So diem bi tru trong mot truong hop khong deo the hoc sinh: "))
b = int(input("So diem bi tru trong mot truong hop noi truyen trong lop: "))
c = int(input("So diem bi tru trong mot truong hop di hoc muon: "))
t = int(input("So truong hop khong deo the duoc ghi nhan: "))
n = int(input("So truong hop noi truyen trong lop duoc ghi nhan: "))
m = int(input("So truong hop di hoc muon duoc ghi nhan: "))

# Part 2: Calculate the total (-) score
total = a * t + b * n + c * m
print(total) # Print out the total