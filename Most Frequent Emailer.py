# This program will read in a text file and
# count the number of emails from each sender
# It will then display the email counts for each sender
# and who sent the most emails


# Select file to open 
fname = input("Enter file name (or hit enter to use the default file): ")
# or open the default file (for testing)
if len(fname) < 1 : fname = "mbox.txt"
# Create Handle
fh = open(fname)

#####################Read in the file##################################
# Create a blank list to store all
# of the email addresses of email senders
addresses = list()

# Step thru the lines in the file
# Add each line as an item in a list named 'line'
for line in fh:
    line = line.strip()
    
    # Find the Lines with the correct starting text
    # In this case "From:"
    # Continue past lines that don't fit the desired pattern
    if not line.startswith('From:'):
        continue

 
    # Split all lines that
    # start with 'From: '
    # this will give us a list named fromlines
    # In this case the list will have 2 items
    # in it: the first will be 'From;'
    # the second will be the email address
    # of the sender.
    # since this is inside of the loop
    # we get another 2-item list
    # for each line starting with "From: "
    fromlines = line.split() 
    
 
    # We only want the email address at index 1, getting rid of 'From:'
    # and just leaving 'email@domain' 
    # these email address will be added to (appended to)
    # a list named 'addresses'
    # Again - we are still inside the loop
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

##############Find the most frequent###########################
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
        
############################################################

####################Display Results#########################
# Print the results to the screen
print ("Total emails for each sender:")
# Convert the key/value pairs into items in a list
emailers = histo_dict.items()
# Step thru the key/value pairs and print each on a seperate line
for sender in emailers:
    print(sender)
    
print("__________________________________________________________________________")
print ("The most frequent emailer was ",(biggest_word), " who emailed ",(biggest_count)," times.")
