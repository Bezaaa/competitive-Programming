class Solution(object):
    def maximumTotalDamage(self, power):
        if not power:
            return 0

        count = Counter(power)
        unique_damages = sorted(count.keys())

        n = len(unique_damages)
        dp = [0] * n

        for i in range(n):
            damage = unique_damages[i]
            total = damage * count[damage]

           
            j = i - 1
            while j >= 0 and unique_damages[j] >= damage - 2:
                j -= 1

            include = total
            if j >= 0:
                include += dp[j]

            exclude = dp[i - 1] if i > 0 else 0

            dp[i] = max(include, exclude)

        return dp[-1]
            