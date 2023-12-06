-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- 主機： db
-- 產生時間： 2023 年 12 月 06 日 21:59
-- 伺服器版本： 10.2.9-MariaDB-10.2.9+maria~jessie
-- PHP 版本： 8.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `s350f_groupproject_gp50`
--

-- --------------------------------------------------------

--
-- 資料表結構 `AttendanceRecords`
--

CREATE TABLE `AttendanceRecords` (
  `ClassID` varchar(255) NOT NULL,
  `StudentID` int(11) NOT NULL,
  `Date` date NOT NULL,
  `Status` varchar(255) DEFAULT NULL,
  `Remarks` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 傾印資料表的資料 `AttendanceRecords`
--

INSERT INTO `AttendanceRecords` (`ClassID`, `StudentID`, `Date`, `Status`, `Remarks`) VALUES
('S350FSoftwareEngineering-2023-11-17-16:00', 12345678, '2023-11-17', NULL, 'QQQ'),
('S350FSoftwareEngineering-2023-11-17-16:00', 87654321, '2023-11-17', NULL, 'WWW'),
('S320FDataBaseManagement-2023-11-21-11:00', 12345678, '2023-11-21', 'Late', 'QWE'),
('S320FDataBaseManagement-2023-11-21-11:00', 87654321, '2023-11-21', 'Present', 'ASD'),
('S312FJavaApplication-2023-11-20-11:00', 12345678, '2023-11-20', 'Present', 'abcd'),
('S312FJavaApplication-2023-11-20-11:00', 87654321, '2023-11-20', 'Absent', 'TESTING');

-- --------------------------------------------------------

--
-- 資料表結構 `ClassSchedule`
--

CREATE TABLE `ClassSchedule` (
  `ClassID` varchar(255) NOT NULL,
  `CourseName` varchar(255) NOT NULL,
  `ClassType` varchar(255) NOT NULL,
  `ClassDate` date NOT NULL,
  `StartTime` varchar(255) NOT NULL,
  `EndTime` varchar(255) NOT NULL,
  `Venue` varchar(255) NOT NULL,
  `InstructorName` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 傾印資料表的資料 `ClassSchedule`
--

INSERT INTO `ClassSchedule` (`ClassID`, `CourseName`, `ClassType`, `ClassDate`, `StartTime`, `EndTime`, `Venue`, `InstructorName`) VALUES
('S312FJavaApplication-2023-11-20-11:00', 'S312FJavaApplication', 'Lecture', '2023-11-20', '11:00', '13:00', 'JCC_DC309', 'JeffAuYeung'),
('S320FDataBaseManagement-2023-11-21-11:00', 'S320FDataBaseManagement', 'Lecture', '2023-11-21', '11:00', '13:00', 'JCC_DC309', 'JeffAuYeung'),
('S350FSoftwareEngineering-2023-11-17-16:00', 'S350FSoftwareEngineering', 'Lecture', '2023-11-17', '16:00', '18:00', 'JCC_DC309', 'JeffAuYeung');

-- --------------------------------------------------------

--
-- 資料表結構 `studentrecords`
--

CREATE TABLE `studentrecords` (
  `StudentID` varchar(255) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `StudentEmail` varchar(255) NOT NULL,
  `Gender` char(1) NOT NULL,
  `BirthDate` varchar(255) DEFAULT NULL,
  `PhoneNumber` varchar(8) DEFAULT NULL,
  `Status` varchar(255) NOT NULL,
  `Major` varchar(255) NOT NULL,
  `Grade` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `studentrecords`
--

INSERT INTO `studentrecords` (`StudentID`, `Name`, `StudentEmail`, `Gender`, `BirthDate`, `PhoneNumber`, `Status`, `Major`, `Grade`) VALUES
('12345678', 'John', 's1234567@live.hkmu.edu.hk', 'M', '2000-01-01', '12345678', 'undergraduate', 'Computer Science', '[{\"CourseName\": \"S312FJavaApplication\", \"Grade\": \"B\"}, {\"CourseName\": \"S320FDataBaseManagement\", \"Grade\": \"N/A\"}, {\"CourseName\": \"S350FSoftwareEngineering\", \"Grade\": \"N/A\"}, {\"CourseName\": \"S381FServer-Side\", \"Grade\": \"N/A\"}]'),
('16842143', 'HelloWorld', 's1684214@live.hkmu.edu.hk', 'M', '2023-12-02', '99999999', 'undergraduate', 'Computer Science', '[{\"CourseName\": \"S312FJavaApplication\", \"Grade\": \"N/A\"}, {\"CourseName\": \"S320FDataBaseManagement\", \"Grade\": \"N/A\"}, {\"CourseName\": \"S350FSoftwareEngineering\", \"Grade\": \"N/A\"}, {\"CourseName\": \"S381FServer-Side\", \"Grade\": \"N/A\"}]'),
('23456789', 'Emily Davis', 's2345678@live.hkmu.edu.hk', 'F', '1997-03-10', '23456789', 'undergraduate', 'Computer Science', '[{\"CourseName\": \"S312FJavaApplication\",\"Grade\": \"A\"},{\"CourseName\": \"S320FDataBaseManagement\",\"Grade\": \"B\"},{\"CourseName\": \"S350FSoftwareEngineering\",\r\n\"Grade\": \"C\"},{\"CourseName\": \"S381FServer-Side\",\"Grade\": \"D\"}]'),
('26745713', 'ABC Kun', 's2674571@live.hkmu.edu.hk', 'M', '2023-12-01', '12431219', 'undergraduate', 'Computer Science', '[{\"CourseName\": \"S312FJavaApplication\", \"Grade\": \"N/A\"}, {\"CourseName\": \"S320FDataBaseManagement\", \"Grade\": \"N/A\"}, {\"CourseName\": \"S350FSoftwareEngineering\", \"Grade\": \"N/A\"}, {\"CourseName\": \"S381FServer-Side\", \"Grade\": \"N/A\"}]'),
('34567890', 'Michael Wilson', 's3456789@live.hkmu.edu.hk', 'M', '1996-08-27', '34567890', 'undergraduate', 'Computer Science', '[{\"CourseName\": \"S312FJavaApplication\",\"Grade\": \"A\"},{\"CourseName\": \"S320FDataBaseManagement\",\"Grade\": \"B\"},{\"CourseName\": \"S350FSoftwareEngineering\",\r\n\"Grade\": \"C\"},{\"CourseName\": \"S381FServer-Side\",\"Grade\": \"D\"}]'),
('48439282', 'Henry Lo', 's4843928@live.hkmu.edu.hk', 'M', '2002-01-06', '53181718', 'undergraduate', 'Computer Science', '[{\"CourseName\": \"S312FJavaApplication\", \"Grade\": \"N/A\"}, {\"CourseName\": \"S320FDataBaseManagement\", \"Grade\": \"N/A\"}, {\"CourseName\": \"S350FSoftwareEngineering\", \"Grade\": \"N/A\"}, {\"CourseName\": \"S381FServer-Side\", \"Grade\": \"N/A\"}]'),
('87654321', 'Jane Smith', 's8765432@live.hkmu.edu.hk', 'F', '1999-09-20', '87654321', 'undergraduate', 'Computer Science', '[{\"CourseName\": \"S312FJavaApplication\", \"Grade\": \"N/A\"}, {\"CourseName\": \"S320FDataBaseManagement\", \"Grade\": \"B\"}, {\"CourseName\": \"S350FSoftwareEngineering\", \"Grade\": \"C\"}, {\"CourseName\": \"S381FServer-Side\", \"Grade\": \"D\"}]'),
('98765432', 'Alex Johnson', 's9876543@live.hkmu.edu.hk', 'M', '2000-12-03', '98765432', 'undergraduate', 'Computer Science', '[{\"CourseName\": \"S312FJavaApplication\",\"Grade\": \"A\"},{\"CourseName\": \"S320FDataBaseManagement\",\"Grade\": \"B\"},{\"CourseName\": \"S350FSoftwareEngineering\",\r\n\"Grade\": \"C\"},{\"CourseName\": \"S381FServer-Side\",\"Grade\": \"D\"}]');

-- --------------------------------------------------------

--
-- 資料表結構 `teacherrecords`
--

CREATE TABLE `teacherrecords` (
  `TeacherID` varchar(255) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Gender` char(1) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `EmploymentDate` varchar(255) NOT NULL,
  `PhoneNumber` varchar(8) NOT NULL,
  `Department` varchar(255) NOT NULL,
  `Designation` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `teacherrecords`
--

INSERT INTO `teacherrecords` (`TeacherID`, `Name`, `Gender`, `Email`, `EmploymentDate`, `PhoneNumber`, `Department`, `Designation`) VALUES
('David20231107', 'David', 'M', 'david@gmail.com', '2023-11-07', '99992222', 'Computer Science', 'Associate Professor'),
('DEF Kun20231102', 'DEF Kun', 'M', 'def@gmail.com', '2023-11-02', '99991111', 'Computer Science', 'Professor'),
('demo20231102', 'demo', 'F', 'demo@example.com', '2023-11-02', '44442222', 'Computer Science', 'Program Leader'),
('Jeff', 'Jeffffff', 'M', 'jeff@example.com', '2023-11-01', '12312312', 'Computer Science', 'Program Leader'),
('Kelvin20231203', 'Kelvin', 'M', 'abc@gmail.com', '2023-12-03', '99990000', 'Computer Science', 'Associate Professor'),
('testing20231105', 'testing', 'F', 'test@gmail.com', '2023-11-05', '12341234', 'Computer Science', 'Professor');

-- --------------------------------------------------------

--
-- 資料表結構 `useraccount`
--

CREATE TABLE `useraccount` (
  `LoginID` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `UserRole` varchar(255) DEFAULT NULL,
  `Name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `useraccount`
--

INSERT INTO `useraccount` (`LoginID`, `password`, `UserRole`, `Name`) VALUES
('Admin', 'Admin', 'Admin', 'Admin'),
('Jeff', '123123', 'teacher', 'Jeffffff'),
('12345678', '123123', 'student', 'John Doe'),
('87654321', '123123', 'student', 'Jane Smith'),
('98765432', '123123', 'student', 'Alex Johnson'),
('23456789', '123123', 'student', 'Emily Davis'),
('34567890', '123123', 'student', 'Michael Wilson'),
('48439282', '123123', 'student', 'Henry Lo'),
('26745713', '123123', 'student', 'ABC Kun'),
('16842143', '123123', 'student', 'HelloWorld'),
('Kelvin20231203', '123123', 'teacher', 'Kelvin'),
('DEF Kun20231102', '123123', 'teacher', 'DEF Kun'),
('David20231107', '123123', 'teacher', 'David'),
('testing20231105', '123123', 'teacher', 'testing'),
('demo20231102', '123123', 'teacher', 'demo');

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `AttendanceRecords`
--
ALTER TABLE `AttendanceRecords`
  ADD KEY `ClassID` (`ClassID`) USING BTREE;

--
-- 資料表索引 `ClassSchedule`
--
ALTER TABLE `ClassSchedule`
  ADD PRIMARY KEY (`ClassID`);

--
-- 資料表索引 `studentrecords`
--
ALTER TABLE `studentrecords`
  ADD PRIMARY KEY (`StudentID`);

--
-- 資料表索引 `teacherrecords`
--
ALTER TABLE `teacherrecords`
  ADD PRIMARY KEY (`TeacherID`);

--
-- 已傾印資料表的限制式
--

--
-- 資料表的限制式 `AttendanceRecords`
--
ALTER TABLE `AttendanceRecords`
  ADD CONSTRAINT `attendancerecords_ibfk_1` FOREIGN KEY (`ClassID`) REFERENCES `ClassSchedule` (`ClassID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
