print('what is the password?')
password = input()

if password == '12345':
    print('what is your name?')
    myName = input()
    if myName == 'yingke':

        import datetime

        now = datetime.datetime.now()

        print(now.hour)

        print('WEEKENDS!!!!!!!!!!!!!!')
            
        if now.hour <= 8 and now.hour > 7 :
            print('Have breakfast ' + myName)

        if now.hour <= 10 and now.hour > 8:
            print('Do your homework ' + myName)

        if now.hour <= 11 and now.hour > 10:
            print('playtime!!! ' + myName)

        if now.hour <= 13 and now.hour > 11:
            print('lunch break ' + myName)

        if now.hour <= 15 and now.hour > 13:
            print('chores ' + myName)

        if now.hour <= 17 and now.hour > 15:
            print('More playtime ' + myName)

        if now.hour < 20 and now.hour > 17:
            print('dinner time ' + myName)
        if now.hour >= 20 or now.hour < 7:
            print('sleep time ' + myName)
    
