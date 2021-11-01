o1 = open("src.txt",'w',encoding="utf-8")
o2 = open("tgt.txt",'w',encoding="utf-8")
with open("results.txt",'r',encoding="utf-8") as f:
	for line in f.readlines():
		part = line.strip().split("\t")
		if part[1][:5] == "Sorry":
			continue
		o1.write(part[0]+"\n")
		o2.write(part[1]+"\n")