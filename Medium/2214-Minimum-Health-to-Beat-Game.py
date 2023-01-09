class Solution:
    def minimumHealth(self, damage, armor: int) -> int:
        # total_damage = sum(damage)
        # max_damage = max(damage)
        # remaining_damage = total_damage - max_damage
        # damage_reduction = max(0, max_damage - armor)
        # return remaining_damage + damage_reduction + 1

        return sum(damage)-max(damage)+max(0,max(damage)-armor)+1