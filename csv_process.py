# CSV Processing


# Creating lists from reference file
dataRaw = open("data.csv", 'r')
lists = [[], [], []]
for row in dataRaw.readlines():
  row = row[:-1].split(',')
  for n in range(3):
    lists[n].append(float(row[n]))
dataRaw.close()


# Analyzing lists
maxes = []
mins = []
averages = []
for l in lists:
  maxes.append(str(max(l)))
  mins.append(str(min(l)))
  averages.append(str(sum(l) / len(l)))


# Storing results in new file
dataNew = open("data_new.csv", 'w')
dataNew.write(",List 1,List 2,List 3\n")
dataNew.write("Max," + ','.join(maxes) + "\n")
dataNew.write("Min," + ','.join(mins) + "\n")
dataNew.write("Average," + ','.join(averages) + "\n")
dataNew.close()