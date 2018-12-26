#/usr/bin/env python
#__*__coding: utf-8 __*__

import random

dreams=["英格兰","法国","德国","巴西","阿根廷","西班牙","葡萄牙","比利时","瑞士","波兰"]
count=[0,0,0,0,0,0,0,0,0,0]
for i in range(365486):
	ran = int(random.random()*90)
	if ran <10:
		count[0]=count[0]+1
	elif ran <20:
		count[1]=count[1]+1
	elif ran <30:
		count[2]=count[2]+1
	elif ran <40:
		count[3]=count[3]+1
	elif ran <50:
		count[4]=count[4]+1
	elif ran <60:
		count[5]=count[5]+1
	elif ran <70:
		count[6]=count[6]+1
	elif ran <80:
		count[7]=count[7]+1
	elif ran <85:
		count[8]=count[8]+1
	elif ran <90:
		count[9]=count[9]+1
max =0
z=0
x=0
for y in count:
	if max <y:
		max=y
		z=x
	x=x+1 
print(count)
print(dreams[z])
