import os
import random
print('Powered by zmbxzrq@github.com')
cmd_init='type = user\ncount = 10\nspeed = 1.0\nstart data >>\nLaunchActivity(com.gn100.unlock,com.gn100.unlock.MainActivity)\nUserWait(500)\n'
location=[[169,255],[551,255],[950,255],
	   [169,610],[551,610],[950,610],
	   [169,970],[551,970],[950,970]]
cmd_location_initpress1='DispatchPointer(0,0,0,'
cmd_location_initpress2='DispatchPointer(0,0,1,'
cmd_location_initpress3='DispatchPointer(0,0,2,'
cmd_location_initpress4=',0,0,0,0,0,0,0)'
def random_location(max):
	if max==1 or max==0:
		randomseed=0
	else:
		randomseed=random.randint(0,max-1)
	return(randomseed)
def del_location(location,now):
	locationbuff=list(location)
	left=[now[0]-781,now[1]]
	right=[now[0]+781,now[1]]
	up=[now[0],now[1]-715]
	down=[now[0],now[1]+715]
	top_right_corner=[now[0]+781,now[1]-715]
	lower_right_corner=[now[0]+781,now[1]+715]
	top_left_corner=[now[0]-781,now[1]-715]
	lower_left_corner=[now[0]-781,now[1]+715]
	try:
		locationbuff.remove(left)
	except:
		pass
	try:
		locationbuff.remove(right)
	except:
		pass
	try:
		locationbuff.remove(up)
	except:
		pass
	try:
		locationbuff.remove(down)
	except:
		pass
	try:
		locationbuff.remove(top_left_corner)
	except:
		pass
	try:
		locationbuff.remove(top_right_corner)
	except:
		pass
	try:
		locationbuff.remove(lower_left_corner)
	except:
		pass
	try:
		locationbuff.remove(lower_right_corner)
	except:
		pass
	return locationbuff
def create_mks(cmd):
	with open('test.mks','w') as f:
		f.write(cmd)
def run_mks():
	os.system('.\\adb.exe push test.mks /sdcard/script')
	os.system('.\\adb.exe shell monkey -f /sdcard/script/test.mks -v 1')
def main():
	for i in range(0,9):
		if i==0: 	#First Press
			randomseed=random_location(9)
			now=location[randomseed]
			cmd=cmd_init+cmd_location_initpress1+str(location[randomseed][0])+','+str(location[randomseed][1])+cmd_location_initpress4+'\nUserWait(500)\n'
			del location[randomseed]
		else:
			
			locationbuff=del_location(location,now)
			if len(locationbuff)<1:  #There's nowhere to go.
				cmd=cmd+last+cmd_location_initpress4+'\nUserWait(500)\n'							
				exit()
			randomseed=random_location(len(locationbuff))
			now=locationbuff[randomseed]
			cmd=cmd+cmd_location_initpress3+str(locationbuff[randomseed][0])+','+str(locationbuff[randomseed][1])+cmd_location_initpress4+'\nUserWait(500)\n'			
			last=str(locationbuff[randomseed][0])+','+str(locationbuff[randomseed][1])
			if i==8:
				cmd=cmd+cmd_location_initpress2+last+cmd_location_initpress4+'\nUserWait(500)\n'							
			location.remove(locationbuff[randomseed])
	create_mks(cmd)
	run_mks()
main()
input('Arbitrary key exit!')