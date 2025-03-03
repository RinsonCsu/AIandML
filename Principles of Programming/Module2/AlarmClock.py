from datetime import datetime

print('Alarm Clock')
print('============\n')

while True:
    try:
        current_time_in_hours = int(input('Enter Current Time in hours in a 24 hour format:\n'))
    except Exception as err:
        print("Format Error:", err)
        print("Current Time entered not is in the right format. Please try again.")
        continue
    if((current_time_in_hours < 0) or (current_time_in_hours > 24) ):
        print("Please enter value in the range 0 to 24")
        continue
        
    try:
        hours_to_wait_for_the_alarm = int(input('Hours to wait for the alarm:\n'))                        
    except Exception as err:
        print("Format Error:", err)
        print("Hours to wait for the alarm is not in the right format. Please try again.")
        continue  
    if(hours_to_wait_for_the_alarm < 0 ):
           print("Hours to wait for the alarm cannot be negative")
           continue

    time_at_which_alarm_will_go_off = int((current_time_in_hours + hours_to_wait_for_the_alarm)%24)
    print("Current Time in hours: {}".format(current_time_in_hours))
    print("Hours to wait for the alarm: {}".format(hours_to_wait_for_the_alarm))
    print("\nAlarm will go off at '{} hours'".format(time_at_which_alarm_will_go_off))
    break
         
print ('\nExiting Alarm.. Bye!')
