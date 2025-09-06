# Let us take example of ['neet', 'code'] => we can join both together and say 'neetcode'
# Problem comes when we want to decode back, how do we remember the end of the first word and the begining of the second word
# Here we can use a delimeter and lets us say our answer is "neet#code"
# The problem is any word could contain that delimeter also which makes it example ['neet', 'c#de'] => "neet#c#de" now if we decode => ['neet', 'c', 'de']


# Optimized Solution
# This is the optimized solution with time of O(m) for each function
# space complexity of O(m + n) for each with m as number of strings and n is the total length of initial string 

def encode(strs: list[str]) -> str:
    result = "" # Initialize a string to serve as a container
    for s in strs:
        result += str(len(s)) + ";"  + s # strs = ["neet","code","love","you"] => "4;neet4;code4;love3;you"
    return result


def decode(s: str) -> list[str]:
    result, i = [], 0 # result a list of decoded strings from the encode function, i a pointer
    while i < len(s):
        j = i
        while s[j] != ";":
            j += 1
        length = int(s[i:j]) # get the length of the str in "4;neet" => 4
        result.append(s[j+1 : j+1+length]) # str[2:6] => neet result = ["neet"]
        i = j + 1 + length # i is updated to be the beginning of the next number that indicates the length of another string
    return result

if __name__ == '__main__':
    print(encode(["neet","code","love","you"]))
    print(decode("4;neet4;code4;love3;you"))