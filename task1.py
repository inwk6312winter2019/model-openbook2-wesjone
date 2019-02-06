fin = open('Street_Centrelines.csv')
def tuple_4():
  t = []
  list4 = []
  for line in fin:
    line = line.split(',')
    t.append((line[2],line[4],line[6],line[7]))
    print(t)
tuple_4()
