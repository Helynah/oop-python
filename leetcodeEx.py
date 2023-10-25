"""
Leetcode Example.
"""


class RansomNote:
    """
    Ransom Note Class.
    """

    def can_construct(self, ransom_note, magazine):
        """
        Returns true if the ransome_note can be constructed
        from magazine.
        """
        char_freq = {}

        # Count characters in magazine
        for char in magazine:
            char_freq[char] = char_freq.get(char, 0) + 1

        # Check if ransom_note can be constructed
        for char in ransom_note:
            if char in char_freq and char_freq[char] > 0:
                char_freq[char] -= 1
            else:
                return False

        return True


note = RansomNote()
print(note.can_construct("a", "b"))  # false
print(note.can_construct("aa", "bb"))  # false
print(note.can_construct("aa", "aab"))  # true
print(note.can_construct("aa","aba"))# true