#!/usr/bin/env python3
"""Returns all students sorted by average score."""


def top_students(mongo_collection):
    """Return students sorted by average score."""
    pipeline = [
        {
            "$project": {
                "name": 1,
                "topics": 1,
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]

    return list(mongo_collection.aggregate(pipeline))
