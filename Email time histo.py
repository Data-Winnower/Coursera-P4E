#This program will count the occurances
#of emails sent during each hour
#using a text file of the contents of an email inbox.

#A default text file is provided if the
#user-requested file cannot be found

# Select file to open 
fname = input("Enter file name: ")
# or open the default file (for testing)
if len(fname) < 1 : fname = "mbox-short.txt"
# Create Handle
fh = open(fname)
words = list()
# Step thru the lines in the file
# Add each line as an item in a list named 'line'
for line in fh:
    line = line.strip()
    
    # Find the Lines with the correct starting text
    # In this case "From" without the colon
    if not line.startswith('From'):
        continue
    if line[4] == ":":
        continue
    # Add the lines of interest to a list named 'fromlines'
    # lines are split at the colon
    # thus I have 'From email@domain day date hour'
    # then 'minutes', 'seconds', 'year'
    
    fromlines = line.split(':')
    
    # Case Specific -> I just want the hours
    # which is included in the zero index
    # so I will delete all except the zero index
    del fromlines[1]
    del fromlines[1]
       
    for item in fromlines:
        line = item.split()
        words.append(line[5])
        
    print(fromlines)

#########Histogram Logic####################################
    # Initialize a dictionary to collect word counts
    histo_dict = dict()
    # Step thru all the email address in the list 'words'
    for word in words:
        # Add new words to histo_dict as a key
        # Initial value for each key will be
        # The default of zero plus 1
        # Existing words will have the value incremented by 1
        histo_dict[word] = histo_dict.get(word,0)+1
############################################################
temp_list =  (sorted([(k,v) for k,v in histo_dict.items()]))
for k,v in temp_list:
    print (k,v)



