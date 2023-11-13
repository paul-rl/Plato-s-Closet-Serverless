import sqlite3 as sl3


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
                "CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " (date TEXT, time TEXT, phoneNo INTEGER, orderNo TEXT)"
            )

    def addEntry(self, dt, phoneNo, orderNo):
        self.__connect()

        with self.connection:
            # Parse date and time
            date = dt.strftime("%Y-%m-%d")
            time = dt.strftime("%H-%M-%S")

            # Prepare SQLite statement
            stmnt = "INSERT INTO " + TABLE_NAME + " VALUES (?, ?, ?, ?)"
            entryTuple = (date, time, phoneNo, orderNo)

            # Execute SQLite statement
            self.connection.cursor().execute(stmnt, entryTuple)
            self.connection.commit()

    def query(self, fromDate=None, toDate=None, phoneNo=None, orderNo=None):
        self.__connect()
        # Prepare SQLite statement
        conditions = []

        # First, create our condition based on our dates
        if fromDate is not None and toDate is not None:  # BETWEEN
            fromDateStr = fromDate.strftime("%Y-%m-%d")
            toDateStr = toDate.strftime("%Y-%m-%d")
            dateCondition = "date BETWEEN '" + fromDateStr + "' AND '" + toDateStr + "'"
            conditions.append(dateCondition)
        elif fromDate is not None:  # >= From Date
            fromDateStr = fromDate.strftime("%Y-%m-%d")            
            dateCondition = "date >= " + fromDateStr
            conditions.append(dateCondition)
        elif toDate is not None:  # <= To Date
            toDateStr = toDate.strftime("%Y-%m-%d")
            dateCondition = "date <= " + toDateStr
            conditions.append(dateCondition)
        # No date condition if both from and to date are none

        # Next, create our phone # condition
        # TODO: Validate this input to make sure its valid
        if len(phoneNo) == 10:
            phoneCondition = "phoneNo = " + str(phoneNo)
            conditions.append(phoneCondition)

        # Last, create our order # condition
        if orderNo is not None:
            orderCondition = "orderNo = " + str(orderNo)
            conditions.append(orderCondition)

        # Construct our SQL statement and conditions
        stmnt = "SELECT date, time, phoneNo, orderNo FROM " + TABLE_NAME
        if len(conditions) >= 1:
            combinedConditions = " AND ".join(conditions)
            stmnt += " WHERE " + combinedConditions

        print(stmnt)

        with self.connection:
            cursor = self.connection.cursor()
            output = cursor.execute(stmnt).fetchall()
            print(output)
            return output

    def contains(self, phoneNo, orderNo):
        self.__connect()
        with self.connection:
            matchingRows = self.query(phoneNo=phoneNo, orderNo=orderNo)
            return len(matchingRows) >= 1
