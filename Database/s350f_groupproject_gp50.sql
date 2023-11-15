-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2023-11-15 03:23:47
-- 伺服器版本： 10.4.21-MariaDB
-- PHP 版本： 7.3.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫: `s350f_groupproject_gp50`
--

-- --------------------------------------------------------

--
-- 資料表結構 `studentrecords`
--

CREATE TABLE `studentrecords` (
  `StudentID` varchar(255) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `StudentEmail` varchar(255) NOT NULL,
  `Gender` char(1) NOT NULL,
  `BirthDate` date DEFAULT NULL,
  `PhoneNumber` varchar(8) DEFAULT NULL,
  `Status` varchar(255) NOT NULL,
  `Major` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `studentrecords`
--

INSERT INTO `studentrecords` (`StudentID`, `Name`, `StudentEmail`, `Gender`, `BirthDate`, `PhoneNumber`, `Status`, `Major`) VALUES
('12345678', 'John Doe', 's1234567@live.hkmu.edu.hk', 'M', '1998-05-15', '12345678', 'undergraduate', 'Computer Science'),
('23456789', 'Emily Davis', 's2345678@live.hkmu.edu.hk', 'F', '1997-03-10', '23456789', 'undergraduate', 'Chinese Studies'),
('34567890', 'Michael Wilson', 's3456789@live.hkmu.edu.hk', 'M', '1996-08-27', '34567890', 'undergraduate', 'Computer Engineering'),
('87654321', 'Jane Smith', 's8765432@live.hkmu.edu.hk', 'F', '1999-09-20', '87654321', 'undergraduate', 'Computer Science'),
('98765432', 'Alex Johnson', 's9876543@live.hkmu.edu.hk', 'M', '2000-12-03', '98765432', 'undergraduate', 'Mathematics');

-- --------------------------------------------------------

--
-- 資料表結構 `teacherrecords`
--

CREATE TABLE `teacherrecords` (
  `TeacherID` varchar(255) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Gender` char(1) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `EmploymentDate` date NOT NULL,
  `PhoneNumber` varchar(8) NOT NULL,
  `Department` varchar(255) NOT NULL,
  `Designation` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `teacherrecords`
--

INSERT INTO `teacherrecords` (`TeacherID`, `Name`, `Gender`, `Email`, `EmploymentDate`, `PhoneNumber`, `Department`, `Designation`) VALUES
('Jeff20231101', 'Jeff', 'M', 'jeff@example.com', '2023-11-01', '12312312', 'Computer Science', 'Program Leader'),
('Jennifer20230801', 'Jennifer Chen', 'F', 'jenniferchen@example.com', '2023-08-01', '87654612', 'Economics', 'Associate Professor'),
('Jessica20231001', 'Jessica Wong', 'F', 'jessicawong@example.com', '2023-10-01', '76213210', 'Sociology', 'Assistant Professor'),
('Sarah20230601', 'Sarah Johnson', 'F', 'sarahjohnson@example.com', '2023-06-01', '98765455', 'Biology', 'Assistant Professor');

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
('Jeff', '123123', 'teacher', 'JeffAuYeung'),
('12345678', '123123', 'student', 'John Doe'),
('87654321', '123123', 'student', 'Jane Smith'),
('98765432', '123123', 'student', 'Alex Johnson'),
('23456789', '123123', 'student', 'Emily Davis'),
('34567890', '123123', 'student', 'Michael Wilson'),
('Jeff20231101', '123123', 'teacher', 'Jeff');

--
-- 已傾印資料表的索引
--

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
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
