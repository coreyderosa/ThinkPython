'''ThinkPython book Exercise 1-4:
If you run a 10 kilometer race in 43 minutes 30 seconds, what is your average time per
mile? What is your average speed in miles per hour? (Hint: there are 1.61 kilometers in
a mile).'''
#need to convert 1 kilometer to 1 miles = 1.61km per mile
#need to convert how many miles in a km 1/1.61 = .62 miles per km
#need to convert 43 min 30 sec to hours 43.5/60 = .725 hours
#ran 10km in .725 hours.  That's 10 / .725 = 13.79km per hour
#If there is 1.61km in a mile and .62 miles in a km then 13.79 * .62 =  8.57 miles per hour


km = 10
raceTime = 43.5
milesTOkm = 1 / 1.61
minTOhours = raceTime / 60
kmPerHour = km / minTOhours
milesPerHour = milesTOkm * kmPerHour
print "The average mph for this runner is " + str(milesPerHour)
