# Brute force solution, by sorting each string and comparing them to see if equal
# Time complexity is O(nlogn)
def isAnagram(s: str, t: str) -> bool:
    s = ''.join(sorted(s))
    t = ''.join(sorted(t))

    if s == t :
        return True
    return False

# Second solution 
def isAnagram_2(s: str, t: str) -> bool:

if __name__ == '__main__':
    print(isAnagram("baba", "abba"))
    print(isAnagram("baba", "adda"))