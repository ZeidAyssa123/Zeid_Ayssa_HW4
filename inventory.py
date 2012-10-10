#!/usr/bin/env python
# Zeid Ayssa HW4
# Intro to Unix 
# ECE 2524


import argparse
import sys
import fileinput

parser = argparse.ArgumentParser(description='invenotry list')
parser.add_argument("-f, --data-file", action='store',  dest=  'InputFile',   help="path to the data file to read at startup")
args = parser.parse_args()

# declare my list

List = []


# defining different functions that will be used in this program


# Add function
def add_function(arg):
	#print "add items"
	item = []
	item = arg.split(':')
	# get footprint
	fprint = item[1].split(',')[0]
	fprint = fprint[2:len(fprint)-1]
	# get decription
	description = item[2].split(',')[0]
	description = description[2:len(description)-1]
	# get PartID
	PartID = item[3].split(',')[0]
	PartID = PartID[2:len(PartID)-1]
	# get Quantity
	Quantity = item[4].split(',')[0]
	Quantity = Quantity[1:len(Quantity)-1]
	# set up my own way of saving stuff 
	Item = PartID+'***'+description+'***'+fprint+'***'+Quantity+'\n'
	global List
	List.append(Item)
	print "Item was successfully added"
	

# Remove function
def delete_function(arg):
	command = arg.split('=')[0]
	request = arg.split('=')[1]
	global List
	if(command=='PartID'):
		# delete by part ID
		size = len(List)
		for i in range(size):
			item = List[i].split('***')[0]
			if(item == request):
				del List[i]
				print "Item(s) with PartID: "+request+" was removed"
	elif (command == 'Quantity'):
		# delete by quantity
		for i in range(1,len(List)-1):
			item = List[i].split('***')[3]
			if(int(item) == int(request)):
				del List[i]
				print "Item(s) with Quantity: "+request+" was removed"
	else:
		print "command was not found"



# set function implementation 
def set_function(arg):
	#set Quantity=5 for PartID=R67817
	global List
	request = arg.split(' ')[0]
	item = arg.split(' ')[2]
	change = request.split('=')[0]
	value = request.split('=')[1]
	part = item.split('=')[0]
	partvalue = item.split('=')[1]
	
	if(part == 'PartID'):
		if(change == 'Quantity'):
			for i in range(1,len(List)):
				Item = List[i].split('***')[0]
				if(Item == partvalue):
					Id = List[i].split('***')[0]
					desc = List[i].split('***')[1]
					footp = List[i].split('***')[2]
					quant = List[i].split('***')[3]
					newItem = Id+'***'+desc+'***'+footp+'***'+value
					# update list
					List[i] = newItem
					print "Quantity was updated for PartID:" + Id
			print "======================================================="
		else:
			print "Invalid Field Name: " + change
	
	
	
	
	
	#print "Invalid Field Name: " + change
	
def list_function(arg):
	global List
	command=[]
	command = arg.split(' ')
	size = len(command)
	
	# list all command
	if(size ==1):
		title = List[0]
		title = title.replace('***','\t\t\t')
		print title+'\n'
		for i in range(1,len(List)):
			Item = List[i]
			Id = List[i].split('***')[0]
			desc = List[i].split('***')[1]
			footp = List[i].split('***')[2]
			quant = List[i].split('***')[3]
			print '%-16s%-42s%-32s%-20s' % (Id , desc , footp , quant)
		print "======================================================="
	elif(size==3):
		com = arg.split(' ')[2]
		req = com.split('=')[1]
		comm = com.split('=')[0]
		
		# list by footprint
		if(comm == 'Footprint'):
			title = List[0]
			title = title.replace('***','\t\t\t')
			print title+'\n'
			for i in range(1,len(List)):
				Item = List[i].split('***')[2]
				if(Item == req):
					Id = List[i].split('***')[0]
					desc = List[i].split('***')[1]
					footp = List[i].split('***')[2]
					quant = List[i].split('***')[3]
					print '%-16s%-42s%-32s%-20s' % (Id , desc , footp , quant)
			print "======================================================="

		# list by Part ID
		elif (comm == 'PartID'):
			title = List[0]
			title = title.replace('***','\t\t\t')
			print title+'\n'
			for i in range(1,len(List)):
				Item = List[i].split('***')[0]
				if(Item == req):
					Id = List[i].split('***')[0]
					desc = List[i].split('***')[1]
					footp = List[i].split('***')[2]
					quant = List[i].split('***')[3]
					print '%-16s%-42s%-32s%-20s' % (Id , desc , footp , quant)
			print "======================================================="
		elif (comm == 'Quantity'):
			title = List[0]
			title = title.replace('***','\t\t\t')
			print title+'\n'
			for i in range(1,len(List)):
				Item = List[i].split('***')[3]
				if(Item == req):
					Id = List[i].split('***')[0]
					desc = List[i].split('***')[1]
					footp = List[i].split('***')[2]
					quant = List[i].split('***')[3]
					print '%-16s%-42s%-32s%-20s' % (Id , desc , footp , quant)
			print "======================================================="
		else:
			print "Invalid Command"
	# sorting function
	elif (size==4):
		command = arg.split(' ')[3]
		if(command == 'Footprint'):
			# sort by footprint
			# Bubble sort
			for i in range(1,len(List)-1):
				for j in range(1,len(List)-2):
					if(List[j].split('***')[2] > List[j+1].split('***')[2]):
						# swap
						temp = List[j]
						List[j] = List[j+1]
						List[j+1] = temp
			# print sorted List
			title = List[0]
			title = title.replace('***','\t\t\t')
			print title+'\n'
			for i in range(1,len(List)):
				Item = List[i]
				Id = List[i].split('***')[0]
				desc = List[i].split('***')[1]
				footp = List[i].split('***')[2]
				quant = List[i].split('***')[3]
				print '%-16s%-42s%-32s%-20s' % (Id , desc , footp , quant)
			print "======================================================="
		
		elif (command == 'PartID'):
			# sort by part ID
			for i in range(1,len(List)):
				for j in range(1,len(List)-1):
					if(List[j].split('***')[0] > List[j+1].split('***')[0]):
						# swap
						temp = List[j]
						List[j] = List[j+1]
						List[j+1] = temp
		# print sorted List
			title = List[0]
			title = title.replace('***','\t\t\t')
			print title+'\n'
			for i in range(1,len(List)):
				Item = List[i]
				Id = List[i].split('***')[0]
				desc = List[i].split('***')[1]
				footp = List[i].split('***')[2]
				quant = List[i].split('***')[3]
				print '%-16s%-42s%-32s%-20s' % (Id , desc , footp , quant)
			print "======================================================="
			
		elif (command == 'Quantity'):
			# sort by quantity
			for i in range(1,len(List)):
				for j in range(1,len(List)-1):
					if(int(List[j].split('***')[3]) > int(List[j+1].split('***')[3])):
						# swap
						temp = List[j]
						List[j] = List[j+1]
						List[j+1] = temp
			# print sorted List
			title = List[0]
			title = title.replace('***','\t\t\t')
			print title+'\n'
			for i in range(1,len(List)):
				Item = List[i]
				Id = List[i].split('***')[0]
				desc = List[i].split('***')[1]
				footp = List[i].split('***')[2]
				quant = List[i].split('***')[3]
				print '%-16s%-42s%-32s%-20s' % (Id , desc , footp , quant)
			print "======================================================="
			#print "quantity"
		else: 
			print "Invalid Command"
	else:
		print "Invalid Command"
		
	#print "list function"


 

# my delimeter is "***" just to be on the safe side 
#Read input file and save each line to List string array to manipulate later on
try:
	file = open(args.InputFile)
	while 1:
		line = file.readline()
		if not line:
			break
		pass # do something
		List.append(line)
		#print line 
    
except IOError as e:
    print "file: {} was not found".format(args.dataFile)
    sys.exit(1)
    
# process input commands  
for data in iter(sys.stdin.readline,  ''):
    caseDict = {'add': add_function,  'remove': delete_function,  'set':set_function,  'list': list_function}
    (prog,action,argv) = data.partition(" ")
    argv = argv.rstrip("\n")
    if argv:
		try:
			caseDict[prog](argv)
		except KeyError as e:
			print "invalid command {}".format(action)
	

# write changes back to the inputted file
try:
	fin = open(args.InputFile, "w")
	fin.truncate()
	# write back to file
	for i in range(len(List)):       
		fin.write(List[i])
	fin.close()
except IOError as e:
    print "file: {} was not found".format(args.dataFile)
    sys.exit(1)
 
