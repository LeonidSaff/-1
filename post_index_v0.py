import turtle as tt
tt.screensize(3700, 500)


Zero = [[100, 0], [0, 0], [100, 0], [100,200], [0,200], [0, 0]]
One = [[0, 200], [0, 0], [0, 200], [-100,100]]
Two = [[-100,0], [0, 0], [-100,0], [-100, 100], [0, 100], [0, 200], [-100, 200]]
Three = [[100, 100], [0, 0], [100, 100], [0, 100], [100, 200], [0, 200]]
Four = [[0, 200], [0, 0], [0, 200], [0, 100], [-100, 100], [-100, 200]]
Five = [[100, 0], [0, 0], [100, 0], [100, 100], [0, 100], [0, 200], [100, 200]]
Six = [[0, 200], [0, 0], [0, 200], [100, 200], [0, 200], [0, 100], [100, 100], [100, 0], [0, 0]]
Seven = [[0, 100], [0, 0], [0, 100], [100, 200], [0, 200]]
Eight = [[100, 0], [0, 0], [100, 0], [100,200], [0,200], [0, 0], [0, 100], [100,100]]
Nine = [[100,100], [0, 0], [100,100], [0, 100], [0, 200], [100, 200], [100,100]]

def run_num(numb):
   tt.speed(1)
   (x0, y0) = numb[0]
   tt.goto(x0, y0)
   tt.pendown()
   for i in range(1,len(numb)):
      (x, y) = numb[i]
      tt.goto(x, y)    
   tt.penup()

def run_pos(numb):
   for i in range(len(numb)):
      numb[i][0] += 200


AAA = list(input ('Введите индекс '))

for i in range(6):
   if AAA[i] == '0':
      run_num(Zero)
   elif AAA[i] == '1':
      run_num(One)
   elif AAA[i] == '2':
      run_num(Two)
   elif AAA[i] == '3':
      run_num(Three)
   elif AAA[i] == '4':
      run_num(Four)
   elif AAA[i] == '5':
      run_num(Five)
   elif AAA[i] == '6':
      run_num(Six)
   elif AAA[i] == '7':
      run_num(Seven)
   elif AAA[i] == '8':
      run_num(Eight)
   elif AAA[i] == '9':
      run_num(Nine)
   run_pos(Zero)
   run_pos(One)
   run_pos(Two)
   run_pos(Three)
   run_pos(Four)
   run_pos(Five)
   run_pos(Six)
   run_pos(Seven)
   run_pos(Eight)
   run_pos(Nine)



