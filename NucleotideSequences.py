import random
import time


# Setup

start_time = time.time()

population = [0,1,2,3] # 0 = A, 1 = T, 2 = C, 3 = G
pattern1 = [0,1,0,1,0,1,0,1] # ATATATAT
pattern2 = [0,1,3,2,3,3,1,2] # ATGCGGTC
trials = 10000 # Number of trials  
p1wins = 0
p2wins = 0


# Randomly hoose the nucleotides and check the patterns we see

for x in range(0,trials):
  nucleotidelist = []
  while nucleotidelist != pattern1 and nucleotidelist != pattern2:
     # Randomly choose a nucleotide, add it to the list, check against the patterns
     nucleotide = random.choice(population)
     nucleotidelist.append(nucleotide)
     nucleotidelist = nucleotidelist[-8:] # only keep the latest 8 nucleotides
  if nucleotidelist == pattern1:
    p1wins = p1wins + 1
  if nucleotidelist == pattern2:
    p2wins = p2wins + 1


# Summary information

p1percent = round(float(p1wins)/trials * 100,2)
p2percent = round(float(p2wins)/trials * 100,2)

print("Pattern 1 (ATATATAT) won", p1wins, "times. This is ", p1percent, "%")
print("Pattern 2 (ATGCGGTC) won", p2wins, "times. This is ", p2percent, "%")
print("--- %s seconds ---" % round(time.time() - start_time, 2))