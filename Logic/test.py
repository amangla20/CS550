month = "March"
day = 21
fall = []
if month in ("January, February, March"):
   season = "Winter"
elif month in ("April, May, June"):
   season = "Spring"
elif month in ("July, August, September"):
   season = "Summer"
elif month in ("October, November, December"):
   season = "Fall"

if month == "March" and day>=21:
   season = "Spring"
if month == "June" and day>=21:
   season = "Summer"
if month == "September" and day>=21:
   season = "Fall"
if month == "December" and day>=21:
   season = "Winter"

print(season)
