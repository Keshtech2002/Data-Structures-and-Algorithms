# Brute force solution, by sorting each string and comparing them to see if equal
# Time complexity is O(nlogn)
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    s = ''.join(sorted(s))
    t = ''.join(sorted(t))

    if s == t :
        return True
    return False

# Second solution, two hashmaps with O(s+t) for time and space complexity
# While the time complexity is ok, the space complexity can be improved
def isAnagram_2(s: str, t: str) -> bool:
    if len(s) != len(t): # If they are not the same length they are not even anagrams of each other
        return False

    countS, countT = {}, {} # A hashmap for both strings

    for i in range(len(s)): # This iterates through the two strings together simultaneously and 
        countS[s[i]] = countS.get(s[i], 0) + 1 # attaches each letter to its number of counts e.g {s:1, p:1, g:1}
        countT[t[i]] = countT.get(t[i], 0) + 1 # default for every letter is {_:0} it checks if the letter is in the dictionary first before 
        # adding it with the get() method, if it is there it will increment the count

    for char in countS: #iterate through countS map now
        if countS[char] != countT.get(char, 0): # Checks each character and the value of its count in S and checks if it is present in t with the different value
            # then this triggers false immediately
            return False
    
    return True # if all are equal


def isAnagram_3(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

if __name__ == '__main__':
    print(isAnagram("baba", "abba"))
    print(isAnagram_2("baba", "abba"))
    print(isAnagram_3("baba", "abba"))