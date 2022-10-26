"""
You probably know the "like" system from Facebook and other pages. People can 
"like" blog posts, pictures or other items. We want to create the text that should
be displayed next to such an item.

Implement the function which takes an array containing the names of people that
like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Note: For 4 or more names, the number in "and 2 others" simply increases.

CATEGORY: STRINGS | FUNDAMENTALS
"""
def likes(names):
    if not names:
        return "no one likes this"
    
    size = len(names)
    
    if size == 1:
        return "{} likes this".format(names[0])
    if size <= 2:
        return "{} and {} like this".format(names[0], names[1])
    if size <= 3:
        return "{}, {} and {} like this".format(names[0], names[1], names[2])
    if size >= 4:
        return "{}, {} and {} others like this".format(names[0], names[1], size-2)



# OTHER SOLUTION
def likes(names):
    count = len(names)

    output = {
        0 : "no one likes this",
        1 : "{} likes this",
        2 : "{} and {} like this",
        3 : "{}, {} and {} like this",
        4 : "{}, {} and {others} others like this",
    }
    return output[min(4,count)].format(*names[:3], others=count-2)


