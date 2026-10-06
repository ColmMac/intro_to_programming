

#Add Contact, phone number and name
def createcontact():
    number = input("Enter contact number: ").strip()
    name = input("Enter contact name: ").strip()
    contact = {"Name": name, "Number": number}
    return contact

# #Edit contact, phone number and name
def editcontact(name):
    edit = True
    newname = ""
    newnumber = ""
    while edit == True:
        updatetype = input("Would you like to update " + name + "'s contact number or name: ").strip()
        if updatetype.lower() == "name":
            newname = input("Please enter new contact name: ").strip()
            edit = False
            return newname
        elif updatetype.lower() == "number":
            newnumber = input("Please enter new contact number: ").strip()
            edit = False
            return newnumber
        else:
            print("Please enter valid contact name:") 

def main():
    contacts = []
    newname = ""
    running = True
    while running == True:
        print(contacts)
        action = input("Hello, type C to create a contact, E to edit a contact or D to delete a contact.").lower()
        if action == "c":
            contacts.append(createcontact())
            cont = input("Would you like to return to the options? Type Y or N: ").upper()
            if cont == "N":
                running = False
        elif action == "e":
            name = input("Please enter the name of the contact whom you would like to edit: ")
            newname = editcontact(name)
            for item in contacts:
                if item["Name"].lower() == name.lower():
                    editcontact(item)
                    found = True
                    break
            if not found:
                print("No contact named", name, "was found.")
            print(contacts)
    return contacts
print(main())
# #Delete contact
# def deletecontact():
#Ask if they want to edit, delete or add content (could create gui)

#.update() dictionary and .values + rep in dic