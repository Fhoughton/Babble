from shutil import copyfile
import datetime

now = str(datetime.datetime.now()).replace(":","")

copyfile("db.sqlite3", "backups/db {}.sqlite3".format(now))