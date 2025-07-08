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
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = countS.get(s[i], 0) + 1
        countT[t[i]] = countT.get(t[i], 0) + 1

    for char in countS:
        if countS[char] != countT.get(char, 0):
            return False
    
    return True


def isAnagram_3(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

if __name__ == '__main__':
    print(isAnagram("baba", "abba"))
    print(isAnagram_2("baba", "abba"))
    print(isAnagram_3("baba", "abba"))