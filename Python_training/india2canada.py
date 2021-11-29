print('enter the time in HH:MMST format')
time = input()

hh= time[0]+time[1]
mm= time[3]+time[4]
st= time[5]+time[6]
hh=int(hh)
mm=int(mm)



dif_h = 10 # hours and minutes to sub. 
dif_m = 30

temp_hh=0
out_min=0

# calculating total minutes
fm = mm-dif_m
if fm <= 0:
	fm = 60 + fm
	hh = hh-1
	out_min = fm

if fm >= 60:
	temp_hh=1
	out_min=fm-60 #final output of minutes
else:
	out_min = fm 

fh = hh-dif_h+temp_hh
if fh <= 0:
	fh = 12 +fh
	if st=='AM':
		st='PM' # final state
	else:
		st='AM'
	

out_hr=0

if fh>=12:
	re_hr = fh-12
	out_hr = re_hr #final hours
	
	if out_hr==0: # to avoid displyaing 0:30 
		out_hr=12
		
	if st=='AM':
		st='PM' # final state
	else:
		st='AM' #final state
else:
	out_hr = fh

out_hr = str(out_hr)
out_min = str(out_min)
out_time = ''
out_time_0 = out_hr+':'+'0'+out_min+st
out_time = out_time = out_hr+':'+out_min+st


if (out_min == '0'or out_min == '1'or out_min == '2'or out_min == '3'or out_min == '4'or out_min == '5'or out_min == '6'or out_min == '7'or out_min == '8'or out_min == '9'):
	print(out_time_0)
else:
	print(out_time)