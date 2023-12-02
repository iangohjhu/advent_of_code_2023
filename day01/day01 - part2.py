# input_file = "sample_input_2.txt"
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

    c_pos = 0
    for c in line:
        validDigit = -1
        
        if (c >= '0' and c <= '9'):
            # print (c, "is num")
            validDigit = int(c)

        if (validDigit == -1) and (c == 'o') and (line[c_pos+1] == 'n') and (line[c_pos+2] == 'e'):
             validDigit = 1
             
        if (validDigit == -1) and (c == 't') and (line[c_pos+1] == 'w') and (line[c_pos+2] == 'o'):
             validDigit = 2

        if (validDigit == -1) and (c == 't') and (line[c_pos+1] == 'h') and (line[c_pos+2] == 'r') and (line[c_pos+3] == 'e') and (line[c_pos+4] == 'e'):
             validDigit = 3

        if (validDigit == -1) and (c == 'f') and (line[c_pos+1] == 'o') and (line[c_pos+2] == 'u') and (line[c_pos+3] == 'r'):
             validDigit = 4

        if (validDigit == -1) and (c == 'f') and (line[c_pos+1] == 'i') and (line[c_pos+2] == 'v') and (line[c_pos+3] == 'e'):
             validDigit = 5

        if (validDigit == -1) and (c == 's') and (line[c_pos+1] == 'i') and (line[c_pos+2] == 'x'):
             validDigit = 6

        if (validDigit == -1) and (c == 's') and (line[c_pos+1] == 'e') and (line[c_pos+2] == 'v') and (line[c_pos+3] == 'e') and (line[c_pos+4] == 'n'):
             validDigit = 7

        if (validDigit == -1) and (c == 'e') and (line[c_pos+1] == 'i') and (line[c_pos+2] == 'g') and (line[c_pos+3] == 'h') and (line[c_pos+4] == 't'):
             validDigit = 8

        if (validDigit == -1) and (c == 'n') and (line[c_pos+1] == 'i') and (line[c_pos+2] == 'n') and (line[c_pos+3] == 'e'):
             validDigit = 9
             
        if validDigit != -1:
            if (firstDigit == -1):
                firstDigit = validDigit
            lastDigit = validDigit
            
        c_pos += 1
        
    # print (firstDigit,lastDigit)
    calibration_value = 10 * firstDigit + lastDigit
    print (calibration_value)

    sum_calibration_values += calibration_value
# output
 
print("Sum of all the calibration values", sum_calibration_values)

   
