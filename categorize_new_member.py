"""
To be a senior, a member must be at least 55 years old and have a handicap
greater than 7. In this croquet club, handicaps range from -2 to +26; the better
the player the lower the handicap.

Input:
Input will consist of a list of pairs. Each pair contains information for a
single potential member. Information consists of an integer for the person's
age and an integer for the person's handicap.

Output:
Output will consist of a list of string values (in Haskell and C: Open or Senior)
stating whether the respective member is to be placed in the senior or open category.

Example:
input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]

CATEGORY: FUNDAMENTALS
"""
def open_or_senior(data):
    return ["Senior" if p[0]>=55 and p[1]>7 else "Open" for p in data]

# Other Solution
def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]
