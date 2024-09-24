# Ruby Young 
# UWYO COSC 1010
# 09/29/2024
# Lab 03 
# Lab Section: 16
# Sources, people worked with, help given to: N/A 


#Part One 
print("Part One------------------------------------------------------------------------")
#Task One: Declare list containing elements: Wyoming, Colorado, Montana
states = ['Wyoming', 'Colorado', 'Montana']

#Task Two: Print entire list 
print(states)

#Task Three: Print first element in list 
print(states[0])

#Task Four: Print last element
print(states[-1])

#Task Five: Use F-string to print "COLORADO is south of WYOMING"
message = (f"{states[1].upper()} is south of {states[0].upper()}")
print(message)


#Part Two 
print("Part Two------------------------------------------------------------------------")

#Task Six: Append Washington, Oregon, California to list and print 
states.append('Washington')
states.append('Oregon')
states.append('California')
print(states)

#Task Seven: Overwrite the second last element to be Maine and print 
states[-2] ='Maine'
print(states)

#Task Eight: Insert Texas to be 3rd element & print 
states.insert(2, 'Texas')
print(states)

#Task Nine: Use 'del' & remove fourth item from the list & print  
del states[3]
print(states)

#Task Ten: Remove Texas using its value & print 
remove_texas = 'Texas'
states.remove(remove_texas)
print(states)


#Part Three
print("Part Three----------------------------------------------------------------------")

#Temporarily sort your list, print it both sorted and unsorted 
variable_sorted = sorted(states)
print(variable_sorted)
print(states)

#Permanently sort your list in reverse order, printing it out
states.sort(reverse = True)
print(states)

#Using the reverse method reverse the list and print it
states.reverse()
print(states)
