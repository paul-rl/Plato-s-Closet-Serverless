from datetime import datetime
import sqlite3 as sl3
from localMessagingConstants import DEFAULT_DATE


DB_NAME = 'phone.sqlite'

TABLE_NAME = 'phone_registry'


class Database:
    def __init__(self):
        self.DB_NAME = 'phone.sqlite'
        self.TABLE_NAME = 'phone_registry'
        self.connection: sl3.Connection
        self.__createTableINE()

    def __connect(self):
        self.connection = sl3.connect(DB_NAME)

    def __createTableINE(self):
        self.__connect()
        with self.connection:
            self.connection.execute(
                f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} (date TEXT, time TEXT, phoneNo INTEGER)"
            )

    def addEntry(self, phoneNo, dt=None):
        self.__connect()

        with self.connection:
            # Parse date and time
            date = ""
            time = ""
            if dt is not None:
                date = dt.strftime("%Y-%m-%d")
                time = dt.strftime("%H-%M-%S")
            else:
                date = "UNSENT"
                time = "UNSENT"

            # Prepare SQLite statement
            stmnt = "INSERT INTO " + TABLE_NAME + " VALUES (?, ?, ?)"
            entryTuple = (date, time, phoneNo)

            # Execute SQLite statement
            self.connection.cursor().execute(stmnt, entryTuple)
            self.connection.commit()

    def reportMessage(self, phoneNo, dt:datetime):
        print("Reporting message")
        # VERIFY THIS HAPPENS, ADDITIONALLY, CHECK TO SEE HOW WE CAN VERIFY WHETHER A MESSAGE WAS SENT OR NOT USING SID OF MESSAGE
        self.__connect()
        date = dt.strftime("%Y-%m-%d")
        time = dt.strftime("%H-%M-%S")
        with self.connection:
            queryRes = self.query(phoneNo=phoneNo)
            print(f"query:{queryRes}")
            if queryRes[0][0] == "UNSENT":
                stmnt = f"UPDATE {self.TABLE_NAME} SET date = ?, time = ?"
                condition = f"WHERE phoneNo = ? AND date = ?"
                stmnt += " " + condition
                print("Here!" + stmnt)
                self.connection.cursor().execute(
                stmnt, 
                (date, time, phoneNo, "UNSENT")
                )
                self.connection.commit()
            else:
                print("Adding entry")
                self.addEntry(phoneNo, dt)
            
    
    def query(self, fromDate=None, toDate=None, phoneNo=None):
        self.__connect()
        print(f"fDate {fromDate}")
        print(f"tDate {toDate}")
        print(f"phone {phoneNo}")
        
        if fromDate is not None:
            fromDate = fromDate.strftime("%Y-%m-%d")
        if toDate is not None:
            toDate = toDate.strftime("%Y-%m-%d")
        
        if fromDate == DEFAULT_DATE:
            print("set to none")
            fromDate = None
        if toDate == DEFAULT_DATE:
            print("set to none")
            toDate = None
        # Prepare SQLite statement
        conditions = []

        # First, create our condition based on our dates
        if fromDate is not None and toDate is not None:  # BETWEEN
            dateCondition = f"date BETWEEN '{fromDate}' AND '{toDate}'"
            conditions.append(dateCondition)
        elif fromDate is not None:  # >= From Date
            dateCondition = f"date >= {fromDate}"
            conditions.append(dateCondition)
        elif toDate is not None:  # <= To Date
            dateCondition = f"date <= {toDate}"
            conditions.append(dateCondition)
        # No date condition if both from and to date are none

        # Next, create our phone # condition
        # TODO: Validate this input to make sure its valid
        if phoneNo is not None and len(phoneNo) == 10:
            phoneCondition = "phoneNo = " + str(phoneNo)
            conditions.append(phoneCondition)

        # Construct our SQL statement and conditions
        stmnt = "SELECT date, time, phoneNo FROM " + TABLE_NAME
        if len(conditions) >= 1:
            combinedConditions = " AND ".join(conditions)
            stmnt += " WHERE " + combinedConditions

        print(stmnt)

        with self.connection:
            cursor = self.connection.cursor()
            output = cursor.execute(stmnt).fetchall()
            print(output)
            return output
