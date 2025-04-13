import json


def extract_following(file_path):
    """
    Extract usernames from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        set: A set of usernames (str).
    """

    with open(file_path, "r") as file:
        data = json.load(file)

    usernames = set()

    for entry in data.get("relationships_following", []):
        entry_list = entry.get("string_list_data", [])
        if entry_list:
            usernames.add(entry_list[0].get("value"))
    return usernames


def extract_followers(file_path):
    """
    Extract usernames from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        set: A set of usernames (str).
    """
    with open(file_path, "r") as file:
        data = json.load(file)

    usernames = set()

    for entry in data:
        entry_list = entry.get("string_list_data", [])
        if entry_list:
            usernames.add(entry_list[0].get("value"))
    return usernames


if __name__ == "__main__":
    following_usernames = extract_following("following.json")
    followers_usernames = extract_followers("followers_1.json")

    not_following_back = following_usernames - followers_usernames
    you_dont_follow_back = followers_usernames - following_usernames

    print("\nPeople you follow who don't follow you back:")
    for user in sorted(not_following_back):
        print(f"- {user}")

    print("\nPeople who follow you but you don't follow back:")
    for user in sorted(you_dont_follow_back):
        print(f"- {user}")
