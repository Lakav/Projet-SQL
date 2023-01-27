BEGIN;

ATTACH DATABASE 'tpb2.db' AS tpb2;

INSERT INTO main.Game (IdGame, Name)
SELECT IdGame, name
FROM tpb2.game;

INSERT INTO main.Place (Name, Address, City)
SELECT Distinct placeName, address, city
FROM tpb2.tournament;


INSERT INTO main.Tournament (IdTournament, idGame, IdPlace, Date, Duration)
SELECT tpb2.tournament.IdTournament, main.Game.IdGame, main.Place.IdPlace, tpb2.tournament.date, tpb2.tournament.duration
FROM tpb2.tournament
INNER JOIN main.Game
    ON tpb2.tournament.IdGame = main.Game.IdGame
INNER JOIN main.Place
    ON tpb2.tournament.placeName = main.Place.Name;

INSERT INTO main.Employee_Data (Lastname, Firstname, Gender, Age, Wage)
SELECT lastname, firstname, gender, age, wage
FROM tpb2.staff;

INSERT INTO main.Employee_Data (Lastname, Firstname, Gender, Age, Wage)
SELECT  lastname, firstname, gender, age, wage
FROM tpb2.player;

INSERT INTO main.Employee_Data (Lastname, Firstname, Gender, Age, Wage)
SELECT  lastname, firstname, gender, age, wage
FROM tpb2.coach;
INSERT INTO main.Staff (IdStaff, IdEmployeeData)
SELECT tpb2.staff.idStaff, main.Employee_Data.IdEmployee
FROM tpb2.staff
INNER JOIN main.Employee_Data
    ON tpb2.staff.lastname = main.Employee_Data.Lastname
    AND tpb2.staff.firstname = main.Employee_Data.Firstname
    AND tpb2.staff.age = main.Employee_Data.Age;

INSERT INTO main.Player (IdPlayer, IdGame, Ranking, IdEmployeeData)
SELECT tpb2.player.idPlayer ,main.Game.IdGame, tpb2.player.ranking, main.Employee_Data.IdEmployee
FROM tpb2.player
INNER JOIN main.Game
    ON tpb2.player.IdGame = main.Game.IdGame
INNER JOIN main.Employee_Data
    ON tpb2.player.lastname = main.Employee_Data.Lastname
    AND tpb2.player.firstname = main.Employee_Data.Firstname
    AND tpb2.player.age = main.Employee_Data.Age;

INSERT INTO main.Coach (IdCoach, IdGame, LicenseDate, IdEmployeeData)
SELECT tpb2.coach.idCoach, main.Game.IdGame, tpb2.coach.licenseDate, main.Employee_Data.IdEmployee
FROM tpb2.coach
INNER JOIN main.Game
    ON tpb2.coach.IdGame = main.Game.IdGame
INNER JOIN main.Employee_Data
    ON tpb2.coach.lastname = main.Employee_Data.Lastname
    AND tpb2.coach.firstname = main.Employee_Data.Firstname
    AND tpb2.coach.age = main.Employee_Data.Age;

COMMIT;