fin = open('Street_Centrelines.csv')
def street_class():
  d = {} 
  class_list = []
  for line in fin:
    line = line.split(',')
    class_list.append(line[10])
    for i in class_list:
      if i not in d:
        d[i]=list(line[2])
      else:
        d[i].append(list(line[2]))
  print(d)
street_class()

