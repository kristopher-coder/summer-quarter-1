print("Scenario #1: A resturant menu with prices for each item")
print("Best Structure: Dictionary; best to pair food with price in key/value")
menu = {
    "French Toast": 12,
    "Grand Slam": 12,
    "T-Bone Steak": 18,
    "Avocado Toast": 15
}
for key, item in menu.items():
    print(key, ": ", item)
print("Scenario #2: High scores to an arcade game")
print("Best Structure: List: Need a mutable structure to update in real time")
highScores = [
    100,
    105,
    110,
    99
]
for score in highScores:
    print(score)
print("Scenario #3: All of the months of the year")
print("Best Structure: Tuple: We need a collection that does not need to change")
monthsInYear = (
    "January"
    "February"
    "March"
    "April"
    "May"
    "June"
    "July"
    "August"
    "September"
    "October"
    "November"
    "December"
)
for month in monthsInYear:
    print(month)