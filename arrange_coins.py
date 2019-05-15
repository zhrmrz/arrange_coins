import math
class Sol:
    def arrange_coins(self,n):
        return int(((math.sqrt(8*n+1))-1)/2)
if __name__ == '__main__':
    p1=Sol()
    print(p1.arrange_coins(8))
