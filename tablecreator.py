from sys import argv
import csv, getopt

if len(argv) == 1:
    exit("Error - Could not open input file")

# declare default variables and flags
input_file_name = argv[1]
output_file_name = None
delim = ","
column_start = 0
column_end = None

custom_order = False
column_order = []
columns_changed = False
ctfmode = False
writeups = False

# arguments
arg_list = argv[1:]
short_options = "acdeosw:"
long_options = ["alpha", "ctfmode", "delimiter", "end", "output", "start", "writeups"]


try:
    arguments, values = getopt.getopt(arg_list, short_options, long_options)

    count = 0
    for val in values:
        if val in ("-a", "--alpha"):
            custom_order = True
            try:
               column_order = argv[count+2].split(',')
            except:
                exit("Please provide a list to alphabetize by. ex. 3,2,1")
        elif val in ("-c", "--ctfmode"):
            column_end = 2
            columns_changed = True
            ctfmode = True
        elif val in ("-d", "--delimiter"):
            try:
                delim = argv[count+2]
            except:
                exit("Please provide a delimiter.")
        elif val in ("-e", "--end"):
            try:
                column_end = int(argv[count+2])
            except:
                exit("Please provide a column to end at.")
            columns_changed = True
        elif val in ("-o", "--output"):
            try:
                output_file_name = argv[count+2]   
            except:
                exit("Please provide a file to output to.")
        elif val in ("-s", "--start"):
            try:
                column_start = int(argv[count+2])
            except:
                exit("Please provide a column to start at.")
            columns_changed = True
        elif val in ("-w", "--writeups"):
            ctfmode = True
            writeups = True
        count+=1
    
    # creates a default output file name if not specified
    if output_file_name == None:
        output_file_name = input_file_name.rsplit(".",1)[0] + '.md'
        print("No output file name given, defaulted to " + output_file_name)

except getopt.error as err:
    exit(str(err))

header = []
rows = []
separator = []

# read in the file contents with given delimiter
with open(input_file_name, 'r') as csv_file:
    file_delim = delim
    try:
        reader = csv.reader(csv_file, delimiter=file_delim)
    except:
        exit("Delimiter " + delim + " not found")

    # if end not provided
    if column_end == None:
        column_end = len(next(reader)) - 1
        csv_file.seek(0)

    # handles changing columns
    if columns_changed:
        reader1 = []
        
        # add columns in selected range
        for row in reader:
            placeholder = []
            for column in range(column_start, column_end + 1):
                placeholder.append(row[column])
            reader1.append(placeholder)

        reader = iter(reader1)
        del reader1

    header = next(reader, None)    
    
    # make the separator
    for h in header:
        separator.append('-' * len(h))

    # sort the list according to rows
    if ctfmode:
        # sorts by cat-val-name and adds links
        sorted_list = sorted(reader, key=lambda row:(row[1], int(row[2]), row[0]))
        for row in sorted_list:
            if writeups:
                fname = "(" + ''.join(filter(str.isalnum, row[0])) + ".md)"
            else:
               fname = "(" + ''.join(filter(str.isalnum,row[0])) + "/)"
            row[0] = "[" + row[0] + "]" + fname
    elif custom_order:
        sorted_list = sorted(reader, key=lambda row: int(column_order[0]))
        for i in column_order:
            if sorted_list[0][int(i)].isnumeric():
                print("Sorted Column " + header[int(i)] + " by int")
                sorted1 = sorted(sorted_list, key=lambda row: int(row[int(i)]))
            else:
                sorted1 = sorted(sorted_list, key=lambda row: row[int(i)])
            sorted_list = sorted1
    else:
        sorted_list = sorted(reader)

    # inserts header and separator separately
    sorted_list.insert(0, header)
    sorted_list.insert(1, separator)

    # adds pipes and creates output
    with open(output_file_name, 'w') as f:
        for row in sorted_list:
            f.write("| ")
            for item in row:
                f.write("%s | " % item)
            f.write("\n")
