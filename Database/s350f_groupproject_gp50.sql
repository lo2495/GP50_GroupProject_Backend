-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2023-11-09 14:13:54
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
  `PhoneNumber` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `studentrecords`
--

INSERT INTO `studentrecords` (`StudentID`, `Name`, `StudentEmail`, `Gender`, `BirthDate`, `PhoneNumber`) VALUES
('12345678', 'John Doe', 's1234567@live.hkmu.edu.hk', 'M', '1998-05-15', '12345678'),
('87654321', 'Jane Smith', 's8765432@live.hkmu.edu.hk', 'F', '1999-09-20', '87654321'),
('98765432', 'Alex Johnson', 's98765432@live.hkmu.edu.hk', 'M', '2000-12-03', '98765432'),
('23456789', 'Emily Davis', 's2345678@live.hkmu.edu.hk', 'F', '1997-03-10', '23456789'),
('34567890', 'Michael Wilson', 's3456789@live.hkmu.edu.hk', 'M', '1996-08-27', '34567890');

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
('34567890', '123123', 'student', 'Michael Wilson');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;