def lemonadeChange(self, bills: list[int]) -> bool:
        fives, tens, twentys = 0, 0, 0
        for i in bills:
            if(i == 5):
                fives += 1
            elif(i == 10):
                if(fives > 0):
                    tens += 1
                    fives -= 1
                else:
                    return False
            else:
                if(tens > 0 and fives > 0):
                    tens -= 1
                    fives -= 1
                    twentys += 1
                elif(tens == 0 and fives >= 3):
                    fives -= 3
                    twentys += 1
                else:
                    return False
        return True