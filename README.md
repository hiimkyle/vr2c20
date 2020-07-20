# vr2c20

Notes) We're assuming you have python installed. If you do not, install it via the python website. Here's a link for the 64 bit python download. https://www.python.org/ftp/python/3.8.4/python-3.8.4-amd64.exe

1) From your Windows Desktop, open the command prompt by pressing "Windows+R". A run box should open up. Type "cmd" in the box and press "ok". A new window will pop up.

2) in the new window, type the following 
   ```pip3 install pyyaml```

3) once the pyyaml installs, install the python irsdk
   ```pip3 install pyirsdk```
   
3b) install the requests library by typing the following in the command line
   ```pip3 install requests```

4) Download the folder titled "YOUR_NAME_iracing_telemetry" from this github repo by clicking clicking on the corresponding .zip file above. You will be directed to a new screen. From there, push the download button in the lower right corner of the screen. After the .zip file has downloaded, unzip it and follow the next step.

5) From your Windows Desktop, open the command prompt by pressing "Windows+R". A run box should open up. Type ```"C:\"``` in the box and press "ok". A new window will pop up.

6) Drag and drop the "iracing_telemetry" folder into the C:\ window and double click on it.

7) From your Windows Desktop, open the command prompt by pressing "Windows+R". A run box should open up. Type "shell:startup" in the box and press "ok". A new window will pop up.

8) In the "shell:startup" window that appears, drag and drop the "collect_iracing - Shortcut" into the "shell:startup" window. From there reboot your computer and start iracing.

9) We can verify in Splunk if it is connected. From here you are good to go with iRacing Telemetry setup.
