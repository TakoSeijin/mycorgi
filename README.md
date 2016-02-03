# mycorgi
Create your own [my.corgiorgy.com](http://my.corgiorgy.com)-style website

To run:
* Install the requirements in requirements.txt using pip
* Replace all instances of "corgiorgy.com" in the code (there are many) with a domain pointing to the IP of the machine you're installing on
* Install PostgreSQL
* Edit database.py with your DB settings
* Run "python setup.py"
* Run "uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi"

If you need any help you can reach me on Twitter [@labelmaker](https://twitter.com/labelmaker). Have fun!
