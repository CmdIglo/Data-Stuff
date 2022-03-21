"""
Author: Maxwell Leu
About: A script that converts data from a vcf file to a text file. This was my first time working with vcf files, so I can imagine
that this little piece of code isn't really suitable for other data science projects, but that wasn't really the intend of this 
project. I actually wrote it for my family, because we had to print out some contacts from a mobile phone and I was too lazy to
copy them by hand, so I wrote this code instead to fulfill that task automatically. By that you can probably already tell that this
code is very "file-specific" and not reliable to use with other files. But I like it, so I published it here :)
And by the way: This is all plain-python, "vanilla python" one might say, so you can get a little inspiration for your data science
projects...
"""

"""
vcf File-Structure of the used file:
BEGIN:VCARD
VERSION:SOME_NUMBERS
N:LASTNAMEFIRSTNAME
FN:FIRSTNAME LASTNAME
TEL:TELEPHONENUMBER
OTHERNUMBERS(not often used)
EMAIL:EMAIL(I was only supposed to copy the telephone numbers, but adding that feature shouldn't take too long I guess. Maybe I add it later)
END:VCARD
"""

# the file
# replace file.vcf with the filename of the file that is supposed to be converted
file = open('file.vcf', 'r')

# a local, list-like, version of the file
file = [line for line in file]

# the end product; structure: [{"Name": name, "Tel": tel}...]
contacts = []

# dictionary of contacts and their index in the file
contact_dict = {}

# number of context
num_contacts = 0

# finds out the index of the seperate contacts
for i in file:

    # new contacts begin with "BEGIN:VCARD" in vcf, so these are the entry-points to contacts
    if i != "BEGIN:VCARD\n":
        continue
    else:
        num_contacts += 1
        contact_dict[str(num_contacts)] = file.index(i)
        file.pop(file.index(i))

# variable declaration and initialization for the while loop
x = 1

while x < num_contacts:
    
    # creating a list for each contact. The list are the lines in the vcf file for the respective contact
    contact_snap = file[contact_dict[str(x)]:contact_dict[str(x+1)]]
    
    # List of the attributes of the contact
    contact = []
    for line in contact_snap:
        if line != "END:VCARD\n" and line != "BEGIN:VCARD\n":
            line = ''.join(i for i in line if i != "\n" and i != ";")
            contact.append(line)
    
    # the attributes get appended to the contacts list, where each contact is represented as a string
    contacts.append(contact)
    
    # you probably know what this does
    x += 1

# a new dictionary for the final product
contact_dict = []

# for each contact in the contacts file, the data gets cleaned up and the right structure, i.e. "Name": name, "Tel": tel. number,
# gets applied to the data
for contact in contacts:
    contact_file = {}
    
    # there were some file-transmission or similar mistakes in the file, so I had to make sure, that the name of the contact
    # was alphanumerical and displayed (saved) right. 
    
    #################################### example: FN:Max Mustermann ####################################                      
    name = "".join(i for i in contact[2][3:]) # -> Max Mustermann
    name = name.replace(" ", "")              # -> MaxMustermann

    if name.isalnum():                        # -> MaxMustermann.isalnum() => True; (Max Mustermann).isalnum() => False     
        contact_file["Name"] = "".join(i for i in contact[2][3:])
        contact_file["Tel"] = "".join(i for i in contact[3] if not i.isalpha() and i != ":" and i != "-")
    else:
        continue

    # now the cleaned up and structurized data of the contact will be added to the contact_dict file, where all contacts are stored
    contact_dict.append(contact_file)

# finally, the data gets written to the new "Kontakte.txt" (-> Kontakte = contacts) file, where it is stored in a very user-friendly
# and even better print-friendly format
with open("Kontakte.txt", "w") as f:
    
    # every contact
    for contact in contact_dict:
        ############ the contact ############
        #
        # Name: contact.name
        # Telefonnummer: contact.telnumber
        # 
        # ...
        f.writelines("\n")
        f.writelines("Name: " + contact["Name"] + "\n")
        f.writelines("Telefonnummer: " + contact["Tel"] + "\n")     
