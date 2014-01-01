"""Aggregate synthetic review ratings; no remote data collection."""


def summarize_reviews(data):
    if not isinstance(data, list) or len(data) > 10000:
        raise ValueError("Supply a list of at most 10000 reviews")
    groups = {}
    for row in data:
        if not isinstance(row, dict):
            raise ValueError("Review must be an object")
        key, rating = row.get("business_id"), row.get("rating")
        if type(key) is not int or key < 1:
            raise ValueError("business_id must be a positive integer")
        if type(rating) is not int or not 1 <= rating <= 5:
            raise ValueError("Rating must be a whole number from 1 to 5")
        bucket = groups.setdefault(key, [])
        bucket.append(rating)
    return [{"business_id": key, "count": len(ratings), "average": round(sum(ratings) / len(ratings), 2),
             "histogram": {str(star): ratings.count(star) for star in range(1, 6)}}
            for key, ratings in sorted(groups.items())]
