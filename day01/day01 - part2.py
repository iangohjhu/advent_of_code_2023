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

def isValidDigit(c_pos,line):
    c = line[c_pos] # character at that position

    if (c >= '0' and c <= '9'):
        # is a number so return it
        return int(c)

    if (c == 'o') and (line[c_pos+1] == 'n') and (line[c_pos+2] == 'e'):
         return 1
         
    if (c == 't') and (line[c_pos+1] == 'w') and (line[c_pos+2] == 'o'):
         return 2

    if (c == 't') and (line[c_pos+1] == 'h') and (line[c_pos+2] == 'r') and (line[c_pos+3] == 'e') and (line[c_pos+4] == 'e'):
         return 3

    if (c == 'f') and (line[c_pos+1] == 'o') and (line[c_pos+2] == 'u') and (line[c_pos+3] == 'r'):
         return 4

    if (c == 'f') and (line[c_pos+1] == 'i') and (line[c_pos+2] == 'v') and (line[c_pos+3] == 'e'):
         return 5

    if (c == 's') and (line[c_pos+1] == 'i') and (line[c_pos+2] == 'x'):
         return 6

    if (c == 's') and (line[c_pos+1] == 'e') and (line[c_pos+2] == 'v') and (line[c_pos+3] == 'e') and (line[c_pos+4] == 'n'):
         return 7

    if (c == 'e') and (line[c_pos+1] == 'i') and (line[c_pos+2] == 'g') and (line[c_pos+3] == 'h') and (line[c_pos+4] == 't'):
         return 8

    if (c == 'n') and (line[c_pos+1] == 'i') and (line[c_pos+2] == 'n') and (line[c_pos+3] == 'e'):
         return 9

    # not a valid digit
    return -1

# process list
for line in list:

    line_count += 1
    print (line_count, line)
                     
    firstDigit = -1
    lastDigit = -1
    value = 0

    for c_pos in range(0, len(line)):
        # check if it's a valid digit
        validDigit = -1
        validDigit = isValidDigit(c_pos, line)
       
        if validDigit != -1:
            if (firstDigit == -1):
                firstDigit = validDigit
            lastDigit = validDigit
        
    # print (firstDigit,lastDigit)
    calibration_value = 10 * firstDigit + lastDigit
    print (calibration_value)

    sum_calibration_values += calibration_value
# output
 
print("Sum of all the calibration values", sum_calibration_values)

   
