
CREATE TABLE `Pricing` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Min` int NOT NULL,
  `Max` int NOT NULL,
  `Value` int NOT NULL,
  PRIMARY KEY (`Id`)
)

CREATE TABLE `Ticket` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Code` varchar(55) NOT NULL,
  `LicenseNumber` varchar(10) NOT NULL,
  `EntryDate` TIMESTAMP NOT NULL,
  `OutDate` TIMESTAMP NULL,
  `ParkingPlaceNumber` int NULL,
  `Paid` int NOT NULL,
  PRIMARY KEY (`Id`)
)

CREATE TABLE `ParkingPlace` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Number` int NOT NULL,
  `Available` bit NOT NULL,
  PRIMARY KEY (`Id`)
)


INSERT INTO PRICING 
(Min, Max, Value)
VALUES
(1, 59, 1000),
(60, 119, 1900),
(120, 179, 2700),
(180, 239, 3500)

INSERT INTO PARKINGPLACE 
(number, available)
VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 1),
(5, 1),
(6, 1),
(7, 1),
(8, 1),
(9, 1),
(10, 1),
(11, 1),
(12, 1)

