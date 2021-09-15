#This program will count the occurances
#of emails sent during each hour
#using a text file of the contents of an email inbox.

#A default text file is provided if the
#user-requested file cannot be found
# or is not specified


#################Access the file########################################
# Select file to open 
fname = input("Enter file name (or hit enter to use the default): ")
# or open the default file (for testing)
if len(fname) < 1 : fname = "mbox.txt"
# Create Handle
fh = open(fname)

#####################Read in the file##################################
# Create a blank list to store all
# of the lines in the file that are of interest
hours = list()

# Step thru the lines in the file
# Add each line as an item in a list named 'line'
for line in fh:
    line = line.strip()
    
    # Find the Lines with the correct starting text
    # In this case "From" without the colon
    # Continue past lines that don't fit the desired pattern
    if not line.startswith('From'):
        continue
    if line[4] == ":":
        continue
    
    # Add the lines of interest to a list named 'fromlines'
    # The format of these lines is "From email@domain Day Month Date Hour:Min:Sec Year"
    # lines are split at the colons
    # this breaks each line into 3 parts
    # thus I have 'From email@domain Day Month Date Hour'
    # then 'Min', 'Sec Year'
    fromlines = line.split(':')
    
    # Case Specific -> I just want the hours
    # which is included in the zero index
    # so I will delete all except the zero index
    # We are inside the loop - so a new 3-item list is
    # Created and then cleaned up for each line of interest
    # Leaving a 1-item list for each line of interest
    del fromlines[1]
    del fromlines[1]

    # The 1-item list is then split on the spaces
    # This creates a 6-item list for each line of interest
    # The last item - index 5 -  is the Hour (what we want)
    # The Hours are then appended to the list named hours
    for item in fromlines:
        line = item.split()
        hours.append(line[5])
        
    
#########Histogram Logic####################################
    # Initialize a dictionary to collect word counts
    histo_dict = dict()
    # Step thru all the email address in the list 'words'
    for hour in hours:
        # Add new words to histo_dict as a key
        # Initial value for each key will be
        # The default of zero plus 1
        # Existing words will have the value incremented by 1
        histo_dict[hour] = histo_dict.get(hour,0)+1

##############Find the most frequent###########################
# Initialize valiables for biggest so far count
# and associated key(hour)
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

print ("Hour\tCount")
print ("------------")

# prepare the totals to print in order
# sort the dictionary by the hour
# store the sorted result in a list, named temp_list, of lists
temp_list =  (sorted([(k,v) for k,v in histo_dict.items()]))


for k,v in temp_list:
    print (k,"\t",v)
print("")
print ("In graphical histogram format:")
print ("Hour\tCount")
print ("------------")
for k,v in temp_list:
    print (k,"*"*v)

print("__________________________________________________________________________")
print ("The most emails were sent between ",(biggest_word),":00 and ",int(biggest_word) + 1, ":00.")
print ( "There were ",(biggest_count)," emails sent during that hour.")
