# Unlock_Android_Test
#This project is for an Android test of the app that unlocks the screen.
It mainly uses python and monkey script
##Code idea:
First install the app, find the abscissa and ordinate of 9 points
Write it to a list, then apply for two lists, one for the location (locationbuff) that can be used, and one for the remaining locations.
For the first time, choose a point arbitrarily and remove it in the location.
The second time, choose the location where you can go to the first point, put him into the function del_location, he returns a locationbuff, randomly selected One point, delete him in the location, in order to ensure that we will not use it next time
In this loop, of course, you must be aware that sometimes he can't finish 9 points (because I don't allow it to cross two points across the domain, just like connecting from the lower left corner to the upper right corner), but also need to use it in the last loop. Adb lifted him up
You can clearly see these in <a href="https://github.com/zmbxzrq/Unlock_Android_Test/blob/master/src/Unlock_Android_Test_DEBUG.py">Unlock_Android_Test_DEBUG.py</a>
##Use it
If you want to test him, first, download the project, install the app, put the code in the same directory as adb.exe, and then run it. Of course, I have packaged it into an exe file.
##What we should attenion
So, if I change the random test to a traversal test, I can completely crack some unlock apps, which is what we are worth noting!