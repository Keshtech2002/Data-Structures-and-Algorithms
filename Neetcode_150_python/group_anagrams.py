from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
        frequency = defaultdict(list) # {key : [values]} (key, count of every character in a particular string
                                    #e.g a1b2 is "abb": values contain a list of strings e.g ["abb", "bab"])
    
        for s in strs: # Iterate through the list strs to create the count of every character in the string 
            count = [0] * 26 # A list of 0s 26 times [0, 0, 0, 0, ....]

            for c in s: #Iterate through the string s 
                count[ord(c)-ord("a")]  += 1 # e.g if the character is a (count[97-97] += 1) index 0 of list has a value of 1

            frequency[tuple(count)].append(s) # The counted list "a1b2" is now the key and the value now appends the string s

        return list(frequency.values())


if __name__ == '__main__':
    print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))