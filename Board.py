class Board:
    def __init__(self, my_minions, enemies):
        self.my_minions = my_minions
        self.enemies = enemies

    def print_board(self):
        for i in self.enemies:
            print(f"({i.name}, {i.attack}, {i.health})", end='')
        print()
        for i in self.my_minions:
            print(f"({i.name}, {i.attack}, {i.health})", end='')
        print()
        print()

    def make_attack(self, attacker, attacked):
        attacker.health -= attacked.attack
        attacked.health -= attacker.attack
        attacker.has_attacker = True
        self.clean_body()

    def clean_body(self):
        body_count = 0
        for i in self.my_minions:
            if i.health <= 0:
                body_count += 1
                self.my_minions.remove(i)
        for j in self.enemies:
            if j.health <= 0:
                body_count += 1
                self.enemies.remove(j)
        return body_count

    def defile_data(self, if_print=False):
        health_list = []
        for i in self.my_minions:
            health_list.append(i.health)
        for i in self.enemies:
            health_list.append(i.health)
        health_list.sort()

        health_need = []
        for i in range(1, health_list[len(health_list) - 1]):
            if i not in health_list:
                health_need.append(i)

        available_health = []
        if len(health_need) > 0:
            for i in range(len(health_list) - 1):
                if health_list[i] == health_list[i + 1] or health_list[i] > health_need[0]:
                    available_health.append(health_list[i])




        if if_print:
            print(f"health_list:{health_list}")
            print(f"available_health:{available_health}")
            print(f"health_need:{health_need}")

        return ([health_need, available_health, health_list])

    def find_target(self, health_need, available_health):
        if len(health_need) == 0:
            return 0
        for i in self.my_minions:
            for j in self.enemies:
                if j.health - i.attack == health_need[0] and i.health in available_health:
                    self.make_attack(i, j)
                    print(f"action{i.name} attack {j.name}")
                    return 1
        return 0

    def prepare(self):
        n = 1
        while n == 1:
            l = self.defile_data()
            n = self.find_target(l[0], l[1])
