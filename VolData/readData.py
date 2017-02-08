print("test")
import glob
fl = glob.glob("*.csv")
data = []
for i in fl:
    f = open(i,'r')
    d = f.readlines()
    data.append([j.rstrip("\n").split(",") for j in d])

        