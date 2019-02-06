def count_maintenance():
  fin = open('Street_Centrelines.csv')
  fin.readline()
  d = {}
  l = []
  for line in fin:
    line = line.split(',')  # put all required street into l
    l.append(line[12])
  for i in l:
    if i not in d:    #count numbers it occurs
      d[i]=1
    else:
      d[i]+=1
  print(d)
count_maintenance()
