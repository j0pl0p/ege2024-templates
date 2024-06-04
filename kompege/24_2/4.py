line = open('data/4.txt').readline().strip()
line = line.replace('JBOSS', 'J*').replace('BOSSJ', '*J').replace('JBOSSJ', 'J*J')
print(line.count('BOSS'))