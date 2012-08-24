import sys
from data_structure import Stack, Queue, Point

#  . open
#  @ obstacle
#  I entrance
#  O exit
#  T tunnel
#  x visited

class Michael:
    def __init__(self):
        print 'initializing...'
        self.rooms = []
        self.entrance = []
        self.paths = []

    def read_input(self):
        if sys.argv[1] == '--Stack':
            self.use_stack = True
        elif sys.argv[1] == '--Queue':
            self.use_stack = False
        
        self.filename = sys.argv[2]
        f = open(self.filename, 'r')
        self.read_room(f)

    def read_room(self, f):
        self.room_num = int(f.readline())
        
        for i in range(self.room_num):
            height, width = map(int, f.readline().split())
            cur_room = []
            for j in range(height):
                cur_row = []
                for k in range(width):
                    cur = f.read(1)
                    cur_row.append(cur)
                    if cur == 'I':
                        self.entrance.append(Point(k, j, ""))
                f.read(1)
                cur_room.append(cur_row)
            self.rooms.append(cur_room)
        self.print_room()
    
    def check_input(self):
        print 'idle'
                    

        
    def run(self):        
        for i in range(self.room_num):
            if(not self.escape_room(i)):
                print 'ERROR in ROOM #' + str(i)
                return False
        return True

    def escape_room(self, room_id):
        ok = False
        
        if self.use_stack:
            q = Stack()
        else:
            q = Queue()

        cur_ent = self.entrance[room_id]
        cur_room = self.rooms[room_id]
        q.push(cur_ent)

        while(not q.empty()):
            cur = q.pop()
#            print "Pop: " + cur.path
            
            if(cur_room[cur.height][cur.width] == 'O' or
               cur_room[cur.height][cur.width] == 'T'):
                ok = True
                self.paths.append(cur.path)
                break

            # mark as visited
            cur_room[cur.height][cur.width] = 'x'
            
            w,h = cur.width, cur.height
            p = cur.path
            
            N = Point(w, h-1, p+"N")
            S = Point(w, h+1, p+"S")
            E = Point(w+1, h, p+"E")
            W = Point(w-1, h, p+"W")


            # N,S,E,W

            if(self.check(N, room_id)):
#                print "Psh: " + N.path
                q.push(N)
            if(self.check(S, room_id)):
#                print "Psh: " + S.path
                q.push(S)
            if(self.check(E, room_id)):
#                print "Psh: " + E.path
                q.push(E)
            if(self.check(W, room_id)):
#                print "Psh: " + W.path
                q.push(W)

                
        return ok
         


    def check(self, p, room_id):
        h = len(self.rooms[room_id])
        w = len(self.rooms[room_id][0])

#        print "room#: " + str(room_id)
#        print "width: " + str(w)
#        print "height: " + str(h)
        
        # out of map
        if p.width < 0 or p.height < 0 or p.width >= w or p.height >= h:
            return False 

#       print "checking... " + str(p.height) + ", " + str(p.width)
        property = self.rooms[room_id][p.height][p.width]
        
        # if obstacle, entrance or visited, don't revisit
        if property == '@' or property == 'I' or property == 'x':
            return False

        return True;

        

    def print_room(self):
        for i in range(len(self.rooms)):
            room = self.rooms[i]
            for j in range(len(room)):
                row = room[j]
                for k in range(len(row)):
                    sys.stdout.write(row[k])
                sys.stdout.write('\n')
            sys.stdout.write('\n')

        for i in range(len(self.entrance)):
            cur_ent = self.entrance[i]
            sys.stdout.write(str(cur_ent.width))
            sys.stdout.write(' ')
            sys.stdout.write(str(cur_ent.height))
            sys.stdout.write('\n')

    def print_result(self):
        for i in range(len(self.paths)):
            print self.paths[i]

def main():
    michael = Michael()
    michael.read_input()
    ok = michael.run()
    if(not ok):
        print 'fail!'
    michael.print_result()
    

if __name__ == "__main__":
    main()
