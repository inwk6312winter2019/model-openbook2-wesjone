fin = open('Street_Centrelines.csv')
def street_class():
  d = {}
  t = 0 
  class_list = []
  class_list2 = []
  for line in fin:
    line = line.split(',')
    class_list.append(line[10])
    class_list2.append(line[2])
  for i in class_list:
    if i not in d:
      d[i] =list( class_list2[t])
    else:
      d[i].append(list(class_list2[t]))
  t=t+1
  print(d)
street_class()

