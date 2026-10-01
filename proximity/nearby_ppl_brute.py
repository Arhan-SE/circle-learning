from proximity_exercise import get_distance

user = {"1001": {"lat": 2.5, "long": 2.5}}

other_users = {"1234": {"lat": 2, "long": 1}, "5678": {"lat": 3, "long": 2.75}}

# print(user)
# print(other_users)


nearest = ""


def nearest_person():
    global nearest
    distance_1_2 = get_distance(
        user["1001"]["lat"],
        user["1001"]["long"],
        other_users["1234"]["lat"],
        other_users["1234"]["long"],
    )
    distance_1_3 = get_distance(
        user["1001"]["lat"],
        user["1001"]["long"],
        other_users["5678"]["lat"],
        other_users["5678"]["long"],
    )
    if distance_1_2 > distance_1_3:
        nearest = other_users["5678"]
    else:
        nearest = other_users["1234"]
    return nearest


print(nearest_person())
