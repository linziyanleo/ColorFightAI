# You need to import colorfight for all the APIs
import colorfight
import random

class ai:
    def __init__(self):
        self.g = colorfight.Game()    
        self.g.JoinGame('zero')


    def main(self):
        while True:
            attl = self.attack_which()
            d = random.choice(attl)
            print(self.g.AttackCell(d[0],d[1]))
            self.g.Refresh()
        

    def my_cell(self):
        mycell = []
        for x in range(self.g.width):
            for y in range(self.g.height):
                c = self.g.GetCell(x,y)
                if c.owner == self.g.uid:
                    loc = (str(x),str(y))
                    mycell.append(loc)
        return mycell

    def can_attack(self):
        #g = colorfight.Game()
        attack_list = []
        mycell = self.my_cell()
        #print('mycell:'+str(mycell))
        for cell in mycell:
            x = int(cell[0])
            y = int(cell[1])
            me = self.g.GetCell(x,y)
            temp = []
            for i in range(4):
                a = self.g.GetCell(x+1,y)
                b = self.g.GetCell(x-1,y)
                c = self.g.GetCell(x,y+1)
                d = self.g.GetCell(x,y-1)
                pointList = [a,b,c,d]
                deleteList = []
                for point in pointList:
                    '''
                    if (point in temp):
                        temp.remove(point)
                        deleteList.append((point.x,point.y))
                        print('pointList works')
                    else:
                        temp.append(point)
                    '''
                    temp.append(point)
                    #print(point.self.g.owner)
		for j in range(4):
            	    if temp[j] != None:
             	        if temp[j].isTaking == False:
                            if temp[j].owner != self.g.uid:
                                attack_list.append((temp[j].x,temp[j].y))
        print(deleteList)
        '''
        for p in attack_list:
            if p in deleteList:
                attack_list.pop((p.x,p.y))

                temp.append(a)
                temp.append(b)
                temp.append(c)
                temp.append(d)
        '''
        #print('attablelist:'+str(attack_list))
        return attack_list

    def fill_corner(self):
        #mycell = self.my_cell()
        cana = self.can_attack()
        fill_it = []
        i = 0
        for cell_1 in cana:
            i = i + 1
            for cell_2 in cana[i:]:
                if cell_1 == cell_2:
                    fill_it.append(cell_1)
                    
        return fill_it


    def protect(self):
        #g = colorfight.Game()
        time = []
        prot = []
        mycell = self.my_cell()
        for cell in mycell:
            x = int(cell[0])
            y = int(cell[1])
            me = self.g.GetCell(x,y)
            tempt = me.takeTime
            #print(str(tempt))
            if tempt <= 2.03:#(2+(100/(me.attackTime - me.occupyTime))):
                prot.append((me.x,me.y))
        #print('prolist:'+str(prot))
        return prot


    def attack_which(self):
        #pro = self.protect()
        cana = self.can_attack()
        corner = self.fill_corner()
        att = []
        '''
        for cell in pro:
            x = cell[0]
            y = cell[1]
            for acell in cana:
                if x == acell[0]:
                    if y == acell[1]:
                        att.append((acell[0],acell[1]))
        '''
        enemy = self.attack_enemy()
        if enemy == []:
            enemy = cana
        #print(str(att)+'12345')
        for cell_1 in corner:
            for cell_2 in enemy:
                if cell_1 == cell_2:
                    att.append(cell_1)
        return att


    def search_near_corner(self):
        mycell = self.my_cell()
        for cell in mycell:
            x = int(cell[0])
            y = int(cell[1])
            


    def attack_enemy(self):
        cana = self.can_attack()
        att = []
        for i in cana:
            info = self.g.GetCell(i[0],i[1])
            if info.owner:
                if info.takeTime <= 2.02:
                    att.append(i)
        if att ==[]:
            att = cana
        return att

a = ai()
a.main()
