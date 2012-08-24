import sys

class Michael:
    def __init__(self):
        print 'initializing...'
        self.rooms = []

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
                    cur_row.append(f.read(1))
                f.read(1)
                cur_room.append(cur_row)
            self.rooms.append(cur_room)
        self.print_room()
    
    def check_input(self):
        print 'idle'
                    

        
    def run(self):
        print ''

    def escape_room(self, room_id):
        print ''

    def print_room(self):
        for i in range(len(self.rooms)):
            room = self.rooms[i]
            for j in range(len(room)):
                row = room[j]
                for k in range(len(row)):
                    sys.stdout.write(row[k])
                sys.stdout.write('\n')
            sys.stdout.write('\n')

def main():
    michael = Michael()
    michael.read_input()

if __name__ == "__main__":
    main()
