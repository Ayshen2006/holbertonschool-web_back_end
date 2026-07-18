#!/usr/bin/env python3
"""Return schools matching a specific topic."""


def schools_by_topic(mongo_collection, topic):
    """Return a list of schools that teach the given topic."""
    return list(mongo_collection.find({"topics": topic}))
