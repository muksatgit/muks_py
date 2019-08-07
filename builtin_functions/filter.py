
def starts_with_m(friend):
    return friend.startswith('M')

friends = ['Mukesh', 'Nikki','Saurabh','Nikhil','Pradeep', "Raphael", 'Mats']

start_with_m = filter(starts_with_m, friends)
print(next(start_with_m))
print(next(start_with_m))
