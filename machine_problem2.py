text = input("Enter your text: ")

class Solution:
    def solve(self, s, k):
        def shift(c):
            i = ord(c) - ord('a')
            i += k
            i %= 26
            return chr(ord('a') + i)

        return "".join(map(shift, s))


ob = Solution()
print("The message", "'", text,  "'", "is encrypted to: ", (ob.solve(text, 3)))
