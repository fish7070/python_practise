class biology:

    def __init__(self, hitPoint, attackPoint, defensePoint):
        self.hitPoint = hitPoint
        self.attackPoint = attackPoint
        self.defensePoint = defensePoint

class initiativeBiology(biology):

    def attack(self, biology):
        print("{} 攻擊 {} ".format(self.name, biology.name))
        damage = self.attackPoint - biology.defensePoint
        if damage < 0 : damage = 0
        biology.hitPoint = biology.hitPoint - damage
        print("{} 受到 {} 點傷害".format(biology.name, damage))
        print("{} 剩餘血量 {} ".format(biology.name, biology.hitPoint))



class human(initiativeBiology):
    def __init__(self, name,  hitPoint, attackPoint, defensePoint):
        self.name = name
        super().__init__(hitPoint, attackPoint, defensePoint)



class elf(initiativeBiology):
    def __init__(self, name,  hitPoint, attackPoint, defensePoint):
        self.name = name
        super().__init__(hitPoint, attackPoint, defensePoint)


class orc(initiativeBiology):
    def __init__(self, name,  hitPoint, attackPoint, defensePoint):
        self.name = name
        super().__init__(hitPoint, attackPoint, defensePoint)

    


def main():

    human1 = human("jack", 100, 10, 1)
    elf1 = elf("lilies", 100, 10, 1)
    orc1 = orc("bob", 100, 10, 1)

    human1.attack(elf1)
    orc1.attack(elf1)


    

main()