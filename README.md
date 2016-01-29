# mycorgi
Create your own corgiorgy.com-style website

To run:
-Install the requirements in requirements.txt
-Replace all instances of "corgiorgy.com" in the code with your own domain pointing to the IP of the machine you're running it on (there are a lot...)
-Install PosgreSQL and edit database.py with your DB settings
-Run setup.py
-Run "uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi"

If you need any help you can reach me on Twitter @labelmaker. Have fun!
