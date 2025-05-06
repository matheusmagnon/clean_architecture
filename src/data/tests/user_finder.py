from typing import Dict


class UserFinderSpy:
    def __init__(self):
        self.find_attributes = {}

    def find(self, first_name: str) -> Dict:
        self.find_attributes["first_name"] = first_name

        return {
            "type": "User",
            "count": 1,
            "attributes": [
                {"first_name": first_name, "last_name": "something"}
            ],
        }
