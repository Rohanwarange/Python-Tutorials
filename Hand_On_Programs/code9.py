# he program will recieve 3 English words inputs from STDIN

# These three words will be read one at a time, in three separate line
# The first word should be changed like all vowels should be replaced by %
# The second word should be changed like all consonants should be replaced by #
# The third word should be changed like all char should be converted to upper case
# Then concatenate the three words and print them
# Other than these concatenated word, no other characters/string should or message should be written to STDOUT

# For example if you print how are you then output should be h%wa#eYOU.

# You can assume that input of each word will not exceed more than 5 chars


a,b,c=input("Enter three Word : ").split(",")
d,e="",""
for j in a:
    if j=="a" or j=="i" or j=="o" or j=="u" or  j=="e":
       j="%"
       d+=j
    else:   
        d+=j
for j in b:
    if j=="a" or  j=="i" or  j=="o" or  j=="u" or  j=="e":
        e+=j
    else:
        j="#"
        e+=j
print(d+e+c.upper())        

            
