class Solution:
    def isIsomorphic(self, str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            print(0)
        else:
            map1 = {}
            map2 = {}
            valid = True

            for c1, c2 in zip(str1, str2):
                if c1 in map1:
                    if map1[c1] != c2:
                        valid = False
                        break
                else:
                    map1[c1] = c2

                if c2 in map2:
                    if map2[c2] != c1:
                        valid = False
                        break
                else:
                    map2[c2] = c1

            return valid