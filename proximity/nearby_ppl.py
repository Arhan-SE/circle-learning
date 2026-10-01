from proximity_exercise import get_distance

user = {"1001": {"lat": 12.9352, "long": 77.6245}}

other_users = {
    "A": {"lat": 12.936547, "long": 77.624500},  # ~150m away
    "B": {"lat": 12.935200, "long": 77.630031},  # ~600m away
    "C": {"lat": 12.954265, "long": 77.644057},  # ~3000m (3km) away
}


def find_nearby(user_coords: dict, other_users_coords: dict, max_distance: float):
    distances = []
    nearby_people = []
    for _keys, _value in other_users_coords.items():
        user_point = next(iter(user_coords.values()))
        distance = get_distance(
            user_point["lat"], user_point["long"], _value["lat"], _value["long"]
        )
        distances.append({_keys: distance})

    for i in distances:
        for key, value in i.items():
            if value <= max_distance:
                nearby_people.append({"id": key, "distance": value})

    return nearby_people
