"""
"""

def canConstruct(self, ransomNote: str, magazine: str) -> bool:

    mag_dict = {}
    for letter in magazine:
        if letter in mag_dict:
            mag_dict[letter] += 1
        else:
            mag_dict[letter] = 1

    ran_dict = {}
    for letter in ransomNote:
        if letter in ran_dict:
            ran_dict[letter] += 1
        else:
            ran_dict[letter] = 1

    for letter in ransomNote:
        if letter not in mag_dict or mag_dict[letter] < ran_dict[letter]:
            return False

    return True
