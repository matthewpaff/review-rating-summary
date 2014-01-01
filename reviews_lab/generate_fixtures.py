"""Original review examples; all businesses and ratings are generated."""


def make_case(index):
    key, kind = index + 1, index % 8
    if kind == 0:
        data, description = [{"business_id": key, "rating": 0}], "reject ratings below one star"
    elif kind == 1:
        data, description = [{"business_id": key, "rating": 6}], "reject ratings above five stars"
    elif kind == 2:
        data, description = [{"business_id": True, "rating": 3}], "reject boolean business identifiers"
    elif kind == 3:
        data, description = [{"business_id": key}], "reject reviews without a rating"
    elif kind == 4:
        data, expected, description = [], [], "summarize an empty review collection"
    else:
        first, second = 1 + index % 5, 1 + (index + 1) % 5
        data = [{"business_id": key + 10000, "rating": 5}, {"business_id": key, "rating": first}, {"business_id": key, "rating": second}]
        expected = [{"business_id": key, "count": 2, "average": (first + second) / 2,
                     "histogram": {str(star): int(star == first) + int(star == second) for star in range(1, 6)}},
                    {"business_id": key + 10000, "count": 1, "average": 5.0,
                     "histogram": {str(star): int(star == 5) for star in range(1, 6)}}]
        description = "group mixed ratings and emit deterministic business order"
    result = {"id": "reviews-{:04d}".format(index), "description": description, "input": data}
    result.update({"expected_error": True} if kind < 4 else {"expected": expected})
    return result
