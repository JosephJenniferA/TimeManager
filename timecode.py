#create a program that can calculate how long I should spend doing tasks in each respective category
print('What is your name?')
name = input()  # read a single line and store it in the variable "name"
print('Hi ' + name + '!')
print('Ok ' + name + ' how many hours do you plan to spend daily to become a python developer?')
daily = input()  # read a single line and store it in the variable "daily"

hoursdaily = input('Great, so you plan to spend ' + daily + ' hours to become a python developer. Is that right ' + name + '?')
if hoursdaily.lower() == ('yes'):
    print("great to hear," + name + '!')
else:
    print ("sorry for asking")
    
#ok so since you plan on spending this number of hours daily to become a developer. That means we estimate that you will spend this amount of minutes coding 1 hour = 60 minutes so input * 60 

print("ok great. that means you will spend " + str(float(daily) * 60) + " minutes coding")

print('what percentage of time should be spent actually coding?')

coding_time = input()  # read a single line and store it in the variable "coding_time"

print('Ok great, so you plan to spend ' + str(float(coding_time)) + "% of the time coding. That's great " + name + '!')
#
print("the means you will spend" str(float(daily) * 60) ")
print(float(coding_time))
