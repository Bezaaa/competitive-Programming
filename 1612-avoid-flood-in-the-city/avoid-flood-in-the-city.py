class Solution(object):
    def avoidFlood(self, rains):
        n = len(rains)
        ans = [-1] * n  # Initialize output
        full_lakes = {}  # lake -> index when it was last rained on
        dry_days = []  # indexes where it's dry (rains[i] == 0)

        for i in range(n):
            lake = rains[i]

            if lake == 0:
                # It's a dry day — save the index for later use
                dry_days.append(i)
                ans[i] = 1  # will be replaced if needed

            else:
                # It's raining on a lake
                if lake in full_lakes:
                    # Lake is already full — need to find a dry day to dry it
                    found = False
                    for j in range(len(dry_days)):
                        dry_day_index = dry_days[j]
                        if dry_day_index > full_lakes[lake]:
                            # Use this dry day to dry the lake
                            ans[dry_day_index] = lake
                            dry_days.pop(j)  # remove used dry day
                            found = True
                            break

                    if not found:
                        # No dry day found → flood happens
                        return []

                # Mark this lake as full (update its last rain day)
                full_lakes[lake] = i
                ans[i] = -1  # it's a rain day

        return ans
