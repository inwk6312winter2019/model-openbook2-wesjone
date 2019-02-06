fin = open('Street_Centrelines.csv')
def list_of_own():
  list_own = []
  for line in fin:
    line = line.split(',')
    list_own.append(line[11])
  print(list_own)

list_of_own()
