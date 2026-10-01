from proximity_exercise import get_distance

user = {
    "1001": {
        "lat": 12.9352,
        "long": 77.6245,
        "category": "Professional",
        "tags": ["startups", "running"],
    }
}

other_users = {
    "A": {
        "lat": 12.936547,
        "long": 77.624500,
        "category": "Professional",
        "tags": ["startups", "coffee"],
    },
    "B": {
        "lat": 12.935200,
        "long": 77.630031,
        "category": "Social",
        "tags": ["badminton"],
    },
}


def score_match(
    user_category: str,
    user_tags: list,
    candidate_category: str,
    candidate_tags: list,
    distance: float,
    max_distance: float,
) -> float:
    proximity_score = max_distance - distance
    category_bonus = 200 if user_category == candidate_category else 0
    tag_bonus = len(set(user_tags) & set(candidate_tags))
    return proximity_score + category_bonus + (tag_bonus * 50)


max_dis = 600.0
for value in other_users.values():
    dis = get_distance(
        user[next(iter(user))]["lat"],
        user[next(iter(user))]["long"],
        value["lat"],
        value["long"],
    )

    s = score_match(
        user[next(iter(user))]["category"],
        user[next(iter(user))]["tags"],
        value["category"],
        value["tags"],
        distance=dis,
        max_distance=max_dis,
    )
    print(s)
