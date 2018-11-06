CREATE TABLE Trucks (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    truckName VARCHAR(100),
    truckAddress VARCHAR(256),
    menu TEXT,
    latitude REAL,
    longitude REAL,
    hoursOfOp VARCHAR(100)
);