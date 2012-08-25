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

        self.dir = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        self.dir_str = ['N', 'S', 'E', 'W']

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
            if ok:
                break
            
            cur = q.pop()                        
            
            w,h = cur.width, cur.height
            p = cur.path

            cur_points = []
            for i in range(len(self.dir)):
                dw, dh = self.dir[i]
                dp = self.dir_str[i]
                cur_points.append(Point(w+dw, h+dh, p+dp))
                
            for i in range(len(cur_points)):
                cur_cand = cur_points[i]
                if(self.check(cur_cand, room_id)):
                    if(cur_room[cur_cand.height][cur_cand.width] == 'O' or
                       cur_room[cur_cand.height][cur_cand.width] == 'T'):
                        ok = True
                        self.add_path(cur_cand, room_id,
                                      len(self.rooms[room_id]), len(self.rooms[room_id][0]))
                        break
                    cur_room[cur_cand.height][cur_cand.width] = 'x'
                    q.push(cur_points[i])

        return ok
    
    def check(self, p, room_id):
        h = len(self.rooms[room_id])
        w = len(self.rooms[room_id][0])

        # out of map
        if p.width < 0 or p.height < 0 or p.width >= w or p.height >= h:
            return False 

        property = self.rooms[room_id][p.height][p.width]
        
        # if obstacle, entrance or visited, don't revisit
        if property == '@' or property == 'I' or property == 'x':
            return False

        return True;

    def add_path(self, p, room_id, h, w):
        if (room_id == self.room_num - 1):
            self.paths.append(p.path)
        elif(p.height == h-1):
            self.paths.append(p.path + "S")
        elif(p.height == 0):
            self.paths.append(p.path + "N")
        elif(p.width == 0):
            self.paths.append(p.path + "W")
        elif(p.width == w-1):
            self.paths.append(p.path + "E")
        else:
            print "Not expected!"

        

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
        print 'Escape failed.'
    else:
        michael.print_result()
    

if __name__ == "__main__":
    main()
