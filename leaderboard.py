print ("Top 5 players:")
print ()
print ()

with open ("{file location.txt}","r") as file:
    top5 = file.readlines()
names_and_scores = [(l.strip().split(",")[0], int(l.strip().split(",")[1])) for l in top5]

names_and_scores.sort(key=lambda x: x[1], reverse =True)
for line in names_and_scores[:5]:
    print(line)
