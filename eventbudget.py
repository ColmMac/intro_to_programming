organiser_name = input("Enter the organiser's name: ").strip()
event_name = input("Enter the event name: ").strip()
venue = input("Enter the venue: ").strip()


attendees = 48
dietary_reqs = 7
# All attendees get £4 refreshment, all but those with
# dietary requirements get meals, at £12

def calculate_budget(attendees, dietary_reqs):
    refreshment_cost = attendees * 4
    meal_cost = (attendees - dietary_reqs) * 12
    total_cost = refreshment_cost + meal_cost
    return total_cost

cost = calculate_budget(attendees, dietary_reqs)
print("Event:", event_name.capitalize())
print("Organiser:", organiser_name.capitalize())
print("Venue:", venue.capitalize())
print("Total Budget: £" + str(cost)) 