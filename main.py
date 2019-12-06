import sqlite3
import os
from SQLiteInteracter import SQLiteInteracter
from GCPInteracter import GCPInteracter
from datetime import datetime

#DEFAULT_INTERACTER="local"
DEFAULT_INTERACTER="gcp"
interacter=None

# The main method
def main():
    try:
        env=os.environ['INTERACTER']
    except:
        env=DEFAULT_INTERACTER

    interacter = (SQLiteInteracter(),GCPInteracter())[env=="gcp"]
    interacter.InsertString("String -- "+getTime())





def getTime()->str:
    now = datetime.now() # current date and time
    time = now.strftime("%H:%M:%S")
    return "time: "+time


def InsertIntoRightDB(typeDB=DEFAULT_INTERACTER):
    # setting default value
    typeDB=(typeDB.lower(),DEFAULT_INTERACTER)[typeDB.lower() != "local" or typeDB.lower() != "gcp"]


main()