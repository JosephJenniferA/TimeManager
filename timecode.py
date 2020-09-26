#create a program that can calculate how long I should spend doing tasks in each respective category

print('What is your name?')
name = input()  # enter in name in the variable "name"

print('Hi ' + name + ' how many hours do you plan to spend daily to become a python developer?')

daily = input()  # enter in the daily amount of time to spent, in the form of an integer

hoursdaily = input('Great, so you plan to spend ' + daily + ' hours to become a python developer. Is that right ' + name + '?')

#explore if then statements futher to understand what to do when they give the wrong response, don't respond, or say no.

if hoursdaily.lower() == ('yes'):
    print("great to hear," + name + '!')
else:
    print ("sorry for asking")
    
#ok so since you plan on spending this number of hours daily to become a developer. That means we estimate that you will spend this amount of minutes coding. 1 hour = 60 minutes so input * 60 

print("ok great. that means you will spend " + str(float(daily) * 60) + " minutes coding")

total_minutes = float(daily) * 60

print('what percentage of the total time do you plan to spend actually coding?')

coding_time = input()  # read a single line and store it in the variable "coding_time"

#correct percentage format!!!VVV
#print("%.0f%%" % (float(coding_time)))

#correct decimal format!!!!VVVV
codespent = (float(coding_time)/100)
total_time_coding = (codespent * total_minutes)

print('Ok great, so you plan to spend ' + str(float(coding_time)) + ("% of the time coding. That means you'll spend ") + str(float(total_time_coding)) + (" minutes coding each day. That's great! "))
