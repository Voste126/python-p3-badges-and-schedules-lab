def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    badges = []
    for name in names:
         badge = f'Hello, my name is {name}.'
         badges.append(badge)
    return badges
        

def assign_rooms(names):
    rooms = []
    for index, name in enumerate(names, start=1):
        guest_msg = f"Hello, {name}! You'll be assigned to room {index}!"
        rooms.append(guest_msg)
    return rooms

def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)

    for badge in badges:
        print(badge)
    for room in rooms:
        print(room)
