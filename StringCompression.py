class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ''
        for char in chars:
            if chars.count(char) == 1:
                s += char
            else:
                s += char
                s += str(chatrs.count(char))
        return len(s)
