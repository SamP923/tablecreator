# tablecreator

Script to generate markdown tables. Given a .csv file, add in the necessary characters to make it into a markdown table format. I made this for personal use in CTFs to automate making README tables. 


## Usage:
```bash
$ python tablecreator.py  [inputFile] [--alpha LIST]
                          [--ctfmode] [--delimiter "DELIM"] 
                          [--end NUM] [--output OUTPUTFILE] 
                          [--start NUM] [--writeups]
```

Command stacking (ie. `-cw`) is currently not supported.


**-a, --alpha**  
Specify how you want your list alphabetized in order of columns. Default goes in order of columns. CTFmode takes precedence over this command.  
`$ python tablecreator.py tables.csv --alpha 3,1,2 `


**-c, --ctfmode**  
Automatically organizes by 1, 2, 0 (organizes generic CTF results by Category, Point Value, Name of Chal). Adds links to any folders that match the challenge name (no delimiter in between words).  
`$ python tablecreator.py tables.csv --ctfmode`


**-d, --delimiter**  
Specify the delimiter used in your original file. Default is ','.  
`$ python tablecreator.py tables.csv --delimiter "."`


**-e, --end**  
Specify which column to end making the table at. Default is the last column in the file. Columns are selected in the range [i, j], with specified end column inclusive.  
`$ python tablecreator.py tables.csv --end 4 `


**-o, --output**  
Specify the name of the output file. Default is original file with .md extension.  
`$ python tablecreator.py tables.csv --output readme.md`


**-s, --start**  
Specify which column to start making the table at. Default is 0. Columns are selected in the range [i, j], with specified start column inclusive.  
`$ python tablecreator.py tables.csv --start 2`


**-w, --writeups**  
Must be used with CTF mode. Instead of linking to folders, link directly to file names (assumes .md ending)  
`$ python tablecreator.py tables.csv -w`


## How it works
1. Takes in the .csv file and creates a "header" row for column names and a "separator" row
2. Sorts rows alphabetically in order of columns. ctfmode assumes normal CTF format which is Challenge-Category-Value-Time and sorts by Category-Value-Challenge and strips the time column.
3. Adds in the pipe delimiter used in tables to each row, and writes all rows to the output file.


## Tasks

### Quality of Life improvements
1. Specify IO files when running the program, not in the script itself [DONE]
2. Automate adding links to files with the same name [DONE]
    - format is `[text](folder-to-find/)`
    - OR `[text](readme.md)`
3. Add support for arguments [DONE]
4. Add in column alphabetizing commands [DONE]
5. Finish CTF Mode [DONE]
6. Make alpha mode and column editing more compatible
7. Change alpha mode to use external function for sorting

### Formatting
1. Make the separators the same length as the column names [DONE]
2. When automating links, change the method so it removes any characters not in a specific alphabet (or characters) and changes spaces to dashes

