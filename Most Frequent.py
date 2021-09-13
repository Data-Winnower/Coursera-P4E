# This program will read in a text file and
# count the number of emails from each sender
# It will them tell who sent the most emails

# Select file to open 
fname = input("Enter file name: ")
# or open the default file (for testing)
if len(fname) < 1 : fname = "mbox-short.txt"
# Create Handle
fh = open(fname)

# Create a blank list to store all
# of the email addresses of email senders
addresses = list()

# Step thru the lines in the file
# Add each line as an item in a list named 'line'
for line in fh:
    line = line.strip()
    
    # Find the Lines with the correct starting text
    # In this case "From:"
    if not line.startswith('From:'):
        continue

    # Case Specific -> Get to the email address of each sender
    # (from each line)
    # In this case, the structure is 'From: email@domain'


    
    # Split all lines that
    # start with 'From: '
    # this will give us a list
    # In this case the list will have 2 items
    # in it: the first will be 'From;'
    # the second will be the email address
    # of the sender.
    fromlines = line.split() 
    
 
    # I only want the email address at index 1, getting rid of 'From:'
    # and just leaving 'email@domain' 
    # these email address will be added to (appended to)
    # a list named 'addresses'
    address = fromlines[1]
      
    addresses.append(address)  
    

    
#########Histogram Logic####################################
# Initialize a dictionary to collect address counts
histo_dict = dict()
# Step thru all the email address in the list 'addresses'
for address in addresses:
    # Add new addresses to histo_dict as a key
    # Initial value for each key will be
    # The default of zero plus 1
    # Existing words will have the value incremented by 1
    histo_dict[address] = histo_dict.get(address,0)+1


############################################################

# Initialize valiables for biggest so far count
# and associated key(word)
biggest_count = None
biggest_word = None       
# Step thru the pairs in histo_dict
for address,count in histo_dict.items():
    # Check to see if current item's value is the biggest so far
    if biggest_count is None or count > biggest_count:
        # Make the current item the biggest item so far
        biggest_count = count
        biggest_word = address
        

# Print the results to the screen
print("")
print ("Total emails for each sender:")
print(histo_dict)
print("")
print ("The most frequent emailer was ",(biggest_word), " who emailed ",(biggest_count)," times.")
