class Party:
    fun = True
    def __init__(self, occasion, people_attending, location):
        self.occasion = occasion
        self.people_attending = people_attending
        self.location = location
            
    def __str__(self):
        return f"The {self.occasion} party is at {self.location}"

    def add_people(self, person):
        self.people_attending.append(PermissionError)
        
halloween = Party("Halloween", ["Fiona", "Mateo", "Rayo"], "Informatics Forum")
print(halloween)
halloween.add_people("Dom")
print("The people who are coming:")
for i in halloween.people_attending:
    print(i)