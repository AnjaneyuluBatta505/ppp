#!/usr/bin/env python
import os
import sys
import urllib2
if __name__ == "__main__":

    from django.core.management import execute_from_command_line
    # db = urllib2.urlopen("https://github.com/pycoder505/ppp/raw/production/db.sqlite3")
    # output = open('static/db.sqlite3', 'wb')
    # output.write(db.read())
    # # output.close()
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practiceplacementpapers.settings')

    execute_from_command_line(sys.argv)
