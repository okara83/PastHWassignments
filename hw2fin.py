##########################
# Onur Kara              #
# HW2 Intro Programming  #
# Columbia Univ. 2010    #
##########################


import csv, sys, urllib

source = r"http://www1.cs.columbia.edu/~joshua/teaching/cs3101/simpsons_diet.csv"
simpson = urllib.urlopen(source).readlines()
readit = csv.reader(simpson, delimiter=',', quotechar='"')

f = open(sys.argv[1],"w")

f.write('<html>')
f.write('<body>')
f.write('<table>')
for char, meal, ate, quantity, comment in readit: 
    f.write('<tr>')
    f.write('<td>')
    f.write(char)
    f.write('</td>')
    f.write('<td>')    
    f.write(meal)
    f.write('</td>')
    f.write('<td>')    
    f.write(ate)
    f.write('</td>')
    f.write('<td>')    
    f.write(quantity)
    f.write('</td>')
    f.write('<td>')    
    f.write(comment)
    f.write('</td>')
    f.write('</tr>')

f.write('WHOOO HOO!')    
f.write('</table>')
f.write('</body>')
f.write('</html>')

##I know I could concatenate the stuff in the for loop into a few linea,
## but I am happy this works. If you want I can work on doing it a shorter way.
