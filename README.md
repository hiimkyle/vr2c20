# vr2c20

1) From your Windows Desktop, open the command prompt by pressing "Windows+R". A run box should open up. Type "cmd" in the box and press "ok". A new window will pop up.

2) in the new window, type the following 
   ```pip3 install pyyaml```

3) once the pyyaml installs, install the python irsdk
   ```pip3 install pyirsdk```

4) Download the folder titled "iracing_telemetry" from this github repo by <p><a href="https://github.com/hiimkyle/vr2c20/raw/master/iracing_telemetry.zip">clicking the link here.</a></p>

5) From your Windows Desktop, open the command prompt by pressing "Windows+R". A run box should open up. Type ```"C:\"``` in the box and press "ok". A new window will pop up.

6) Drag and drop the "iracing_telemetry" folder into the C:\ window and double click on it.

7) From your Windows Desktop, open the command prompt by pressing "Windows+R". A run box should open up. Type "shell:startup" in the box and press "ok". A new window will pop up.

8) In the "shell:startup" window that appears, drag and drop the "collect_iracing - Shortcut" into the "shell:startup" window. From there reboot your computer and start iracing.

9) We can verify in Splunk if it is connected. From here you are good to go with iRacing Telemetry setup.
