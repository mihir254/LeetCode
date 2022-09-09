class Solution:
    def numberOfWeakCharacters(self, properties):
        properties.sort(key=lambda x:(-x[0], x[1]))
        ans, maxi = 0, -1
        for pro in properties:
            if pro[1] < maxi:
                ans += 1
            else:
                maxi = pro[1]
        return ans