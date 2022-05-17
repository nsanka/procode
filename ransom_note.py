from collections import defaultdict, Counter

class Solution(object):
   def canSpell(self, magazine, note):
      letters = defaultdict(int)
      for c in magazine:
         letters[c] += 1

      for c in note:
         if letters[c] <= 0:
            return False
         letters[c] -= 1

      return True

   # Alternate method using Counter
   def canSpell_alt(self, magazine, note):
      letters = Counter(magazine)

      for c in note:
         if letters[c] <= 0:
            return False
         letters[c] -= 1

      return True


print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
print(Solution().canSpell_alt(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
# True

print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'cat'))
print(Solution().canSpell_alt(['a', 'b', 'c', 'd', 'e', 'f'], 'cat'))
# False
