from datetime import datetime, time
d1 = datetime.strptime('2003-06-26 22:55:37', '%Y-%m-%d %H:%M:%S')
d2 = datetime.now()
x = d2 - d1
print(x.days * 24 * 3600 + x.seconds, "seconds")
