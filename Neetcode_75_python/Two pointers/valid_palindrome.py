def isPalindrome(s: str) -> bool:
    """
    Problem:
      Given a string `s`, determine if it reads the same forwards and backwards
      when considering only alphanumeric characters and ignoring cases.

    Examples:
      s = "A man, a plan, a canal: Panama" -> True
      s = "race a car" -> False
      s = "" (empty string) -> True

    Approach:
      1. Iterate through each character in `s`.
      2. Build a new string containing only lowercase alphanumeric characters
         (i.e., letters and digits).
      3. Compare this cleaned string to its reverse.
      4. Return True if they’re the same, False otherwise.

    Time Complexity: O(n) for scanning + O(n) for reversing = O(n).
    Space Complexity: O(n) for the cleaned string.
    """

    # Step 1: Initialize an empty string to store only alphanumeric chars
    new_string = ""

    # Step 2: Loop through each character in the original string
    for c in s:
        # c.isalnum() returns True if c is a letter or a digit
        if c.isalnum():
            # Append lowercase version of c to new_string
            # (ignore case differences)
            new_string += c.lower()

    # Step 3: Compare cleaned string to its reverse
    # - new_string[::-1] creates a reversed copy
    # - if they’re equal, s is a palindrome under these rules
    return new_string == new_string[::-1]


def alphaNum(c):
    """
    Helper function to determine if a character is alphanumeric (letter or digit).

    Parameters:
      c (str): A single character.

    Returns:
      bool: True if c is a letter (A–Z or a–z) or a digit (0–9), False otherwise.

    How it works:
      - ord('A') returns the Unicode code point for 'A' (65)
      - ord('Z') = 90, ord('a') = 97, ord('z') = 122, ord('0') = 48, ord('9') = 57
      - We check if ord(c) falls into one of these ranges.
    """
    return (
        ord("A") <= ord(c) <= ord("Z") or  # uppercase A-Z
        ord("a") <= ord(c) <= ord("z") or  # lowercase a-z
        ord("0") <= ord(c) <= ord("9")     # digits 0-9
    )


def isPalindrome_2(s: str) -> bool:
    """
    Check if a string is a palindrome using the two-pointer technique.

    Problem:
      Determine if string `s` reads the same forwards and backwards
      when ignoring non-alphanumeric characters and case differences.

    Approach:
      - Use two pointers:
        * left (l) starting at the beginning of the string.
        * right (r) starting at the end of the string.
      - Move the pointers inward:
        * Skip any non-alphanumeric characters using alphaNum().
        * Compare the characters (converted to lowercase).
        * If mismatch → return False immediately.
      - If the entire loop finishes without mismatch → return True.

    Time Complexity: O(n) — each character is processed at most once.
    Space Complexity: O(1) — no extra string built, just pointers.

    Examples:
      "A man, a plan, a canal: Panama" → True
      "race a car" → False
      "" (empty string) → True
    """

    # Initialize two pointers at the start and end of the string
    l, r = 0, len(s) - 1

    # Loop while left pointer is before right pointer
    while l < r:
        # Move left pointer forward until it points to an alphanumeric character
        while l < r and not alphaNum(s[l]):
            l += 1
        # Move right pointer backward until it points to an alphanumeric character
        while r > l and not alphaNum(s[r]):
            r -= 1

        # Compare characters at l and r (lowercase for case-insensitivity)
        if s[l].lower() != s[r].lower():
            return False  # mismatch found, not a palindrome

        # Move both pointers inward for the next comparison
        l, r = l + 1, r - 1

    # If loop ends without mismatches, the string is a palindrome
    return True




if __name__ == '__main__':
    print(isPalindrome("Was it a car or a cat I saw?"))
    print(isPalindrome_2("Was it a car or a cat I saw?"))