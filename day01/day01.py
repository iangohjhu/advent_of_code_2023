# input_file = "sample_input.txt"
input_file = "puzzle_input.txt"

# open files in read mode
file = open(input_file, 'r')

# read lines in file
data = file.readlines()

# make it a list
list = list(data)

# last line
last_line = len(list)

# close file
file.close()

sum_calibration_values = 0
line_count = 0

# process list
for line in list:

    line_count += 1
    print (line_count, line)

    firstDigit = -1
    lastDigit = -1
    value = 0

    for c in line:
        if (c >= '0' and c <= '9'):
            # print (c, "is num")
            if (firstDigit == -1):
                    firstDigit = int(c)
            lastDigit = int(c)

    # print (firstDigit,lastDigit)
    calibration_value = 10 * firstDigit + lastDigit
    print (calibration_value)

    sum_calibration_values += calibration_value
# output
 
print("Sum of all the calibration values", sum_calibration_values)

   
