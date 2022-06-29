class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==0 : return 0
        a, i = 1, 0
        chars.append(" ")
        while chars[i] != " ":
            if chars[i] == chars[i+1]:
                a += 1
                i += 1
            else:
                if a > 1:
                    chars[i+2-a:i+1] = list(str(a))
                    i += 2 - a + len(list(str(a)))
                    a = 1
                else:
                    i += 1
        del chars[-1]
