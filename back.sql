-- MySQL dump 10.14  Distrib 5.5.56-MariaDB, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: hoteldb
-- ------------------------------------------------------
-- Server version	5.5.56-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add group',1,'add_group'),(2,'Can change group',1,'change_group'),(3,'Can delete group',1,'delete_group'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add room',5,'add_room'),(14,'Can change room',5,'change_room'),(15,'Can delete room',5,'delete_room'),(16,'Can add checkinfo',6,'add_checkinfo'),(17,'Can change checkinfo',6,'change_checkinfo'),(18,'Can delete checkinfo',6,'delete_checkinfo'),(19,'Can add bookinfo',7,'add_bookinfo'),(20,'Can change bookinfo',7,'change_bookinfo'),(21,'Can delete bookinfo',7,'delete_bookinfo'),(22,'Can add django migrations',8,'add_djangomigrations'),(23,'Can change django migrations',8,'change_djangomigrations'),(24,'Can delete django migrations',8,'delete_djangomigrations'),(25,'Can add staff',9,'add_staff'),(26,'Can change staff',9,'change_staff'),(27,'Can delete staff',9,'delete_staff'),(28,'Can add price',10,'add_price'),(29,'Can change price',10,'change_price'),(30,'Can delete price',10,'delete_price'),(31,'Can add customer',11,'add_customer'),(32,'Can change customer',11,'change_customer'),(33,'Can delete customer',11,'delete_customer'),(34,'Can add log entry',12,'add_logentry'),(35,'Can change log entry',12,'change_logentry'),(36,'Can delete log entry',12,'delete_logentry'),(37,'Can add session',13,'add_session'),(38,'Can change session',13,'change_session'),(39,'Can delete session',13,'delete_session'),(40,'Can add auth group',14,'add_authgroup'),(41,'Can change auth group',14,'change_authgroup'),(42,'Can delete auth group',14,'delete_authgroup'),(43,'Can add auth group permissions',15,'add_authgrouppermissions'),(44,'Can change auth group permissions',15,'change_authgrouppermissions'),(45,'Can delete auth group permissions',15,'delete_authgrouppermissions'),(46,'Can add auth permission',16,'add_authpermission'),(47,'Can change auth permission',16,'change_authpermission'),(48,'Can delete auth permission',16,'delete_authpermission'),(49,'Can add auth user',17,'add_authuser'),(50,'Can change auth user',17,'change_authuser'),(51,'Can delete auth user',17,'delete_authuser'),(52,'Can add auth user groups',18,'add_authusergroups'),(53,'Can change auth user groups',18,'change_authusergroups'),(54,'Can delete auth user groups',18,'delete_authusergroups'),(55,'Can add auth user user permissions',19,'add_authuseruserpermissions'),(56,'Can change auth user user permissions',19,'change_authuseruserpermissions'),(57,'Can delete auth user user permissions',19,'delete_authuseruserpermissions'),(58,'Can add django admin log',20,'add_djangoadminlog'),(59,'Can change django admin log',20,'change_djangoadminlog'),(60,'Can delete django admin log',20,'delete_djangoadminlog'),(61,'Can add django content type',21,'add_djangocontenttype'),(62,'Can change django content type',21,'change_djangocontenttype'),(63,'Can delete django content type',21,'delete_djangocontenttype'),(64,'Can add django session',22,'add_djangosession'),(65,'Can change django session',22,'change_djangosession'),(66,'Can delete django session',22,'delete_djangosession');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$36000$ChLIJvMpavmH$dpH6cFgmYD0Xwp8WUvl2SlTCcc0FPDtM0UbC9BaQvOc=','2017-12-07 08:24:52',1,'eather','','','eathertoo@gmail.com',1,1,'2017-12-07 08:23:06');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookinfo`
--

DROP TABLE IF EXISTS `bookinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bookinfo` (
  `book_id` int(11) NOT NULL AUTO_INCREMENT,
  `book_time` datetime DEFAULT NULL,
  `cus_id` int(11) DEFAULT NULL,
  `book_idnum` char(18) DEFAULT NULL,
  `book_phone` char(11) DEFAULT NULL,
  `book_num` int(11) DEFAULT NULL,
  `book_price` double DEFAULT NULL,
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookinfo`
--

LOCK TABLES `bookinfo` WRITE;
/*!40000 ALTER TABLE `bookinfo` DISABLE KEYS */;
INSERT INTO `bookinfo` VALUES (25,'2017-12-10 12:29:12',1,'','',2,300),(26,'2017-12-10 12:32:20',1,'','',3,700),(27,'2017-12-10 12:33:48',1,'','',3,660),(28,'2017-12-10 12:34:38',1,'','',4,800),(29,'2017-12-10 12:36:07',1,'','',5,1100),(30,'2017-12-10 13:17:39',1,'','',2,300),(31,'2017-12-11 01:03:06',4,'','',4,800),(32,'2017-12-11 01:08:02',1,'','',2,400),(33,'2017-12-11 02:49:42',1,'123456789012345678','11111111111',1,200);
/*!40000 ALTER TABLE `bookinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `checkinfo`
--

DROP TABLE IF EXISTS `checkinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `checkinfo` (
  `check_id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) DEFAULT NULL,
  `check_name` varchar(16) DEFAULT NULL,
  `check_idnum` char(18) DEFAULT NULL,
  `check_phone` char(11) DEFAULT NULL,
  `check_leavetime` date DEFAULT NULL,
  `check_checkInTime` date DEFAULT NULL,
  `check_statu` enum('pre','ing','after') DEFAULT NULL,
  `room_id` char(4) DEFAULT NULL,
  PRIMARY KEY (`check_id`)
) ENGINE=InnoDB AUTO_INCREMENT=74 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `checkinfo`
--

LOCK TABLES `checkinfo` WRITE;
/*!40000 ALTER TABLE `checkinfo` DISABLE KEYS */;
INSERT INTO `checkinfo` VALUES (51,25,NULL,NULL,'','2017-12-20','2017-12-10','pre','102'),(52,26,NULL,NULL,'','2017-12-11','2017-12-10','pre','105'),(53,27,NULL,NULL,'','2017-12-11','2017-12-10','pre','104'),(54,27,NULL,NULL,'','2017-12-11','2017-12-10','pre','107'),(55,27,NULL,NULL,'','2017-12-11','2017-12-10','pre','107'),(56,28,NULL,NULL,'','2017-12-30','2017-12-29','pre','101'),(57,28,NULL,NULL,'','2017-12-30','2017-12-29','pre','101'),(58,28,NULL,NULL,'','2017-12-30','2017-12-29','pre','103'),(59,28,NULL,NULL,'','2017-12-30','2017-12-29','pre','103'),(60,29,NULL,NULL,'','2018-01-02','2018-01-01','pre','101'),(61,29,NULL,NULL,'','2018-01-02','2018-01-01','pre','102'),(62,29,NULL,NULL,'','2018-01-02','2018-01-01','pre','105'),(63,29,NULL,NULL,'','2018-01-02','2018-01-01','pre','103'),(64,29,NULL,NULL,'','2018-01-02','2018-01-01','pre','106'),(65,30,NULL,NULL,'','2017-12-19','2017-12-16','pre','104'),(66,30,NULL,NULL,'','2017-12-19','2017-12-16','pre','105'),(67,31,NULL,NULL,'','2017-12-12','2017-12-11','pre','104'),(68,31,NULL,NULL,'','2017-12-12','2017-12-11','pre','117'),(69,31,NULL,NULL,'','2017-12-12','2017-12-11','pre','103'),(70,31,NULL,NULL,'','2017-12-12','2017-12-11','pre','106'),(71,32,NULL,NULL,'','2017-12-29','2017-12-20','pre','101'),(72,32,NULL,NULL,'','2017-12-29','2017-12-20','pre','103'),(73,33,NULL,NULL,'11111111111','2017-12-12','2017-12-11','pre','105');
/*!40000 ALTER TABLE `checkinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `cus_id` int(11) NOT NULL AUTO_INCREMENT,
  `cus_name` varchar(16) DEFAULT NULL,
  `id_num` char(18) DEFAULT NULL,
  `cus_phone` char(11) NOT NULL DEFAULT '',
  `cus_password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`cus_id`,`cus_phone`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Eather','123789469725796348','17804336173','pbkdf2_sha256$36000$iFFYSLCa8Fjl$P1+KMsjx5/D336u1kfZXh8Smihm1nTl5WMXvaseol70='),(2,NULL,NULL,'17869874876','pbkdf2_sha256$36000$susPjnRzuKww$O0OjzTk+Qiagh182VTKMKoA41VbV8EPuY1SPyMO1DJU='),(3,NULL,NULL,'17804331234','pbkdf2_sha256$36000$m8MCfPk7KmET$zoSKlkr7kua7T/igqDByNfd575lGTNH/NQbb6Mni/vA=');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (12,'admin','logentry'),(1,'auth','group'),(2,'auth','permission'),(3,'auth','user'),(4,'contenttypes','contenttype'),(14,'hotelmanager','authgroup'),(15,'hotelmanager','authgrouppermissions'),(16,'hotelmanager','authpermission'),(17,'hotelmanager','authuser'),(18,'hotelmanager','authusergroups'),(19,'hotelmanager','authuseruserpermissions'),(7,'hotelmanager','bookinfo'),(6,'hotelmanager','checkinfo'),(11,'hotelmanager','customer'),(20,'hotelmanager','djangoadminlog'),(21,'hotelmanager','djangocontenttype'),(8,'hotelmanager','djangomigrations'),(22,'hotelmanager','djangosession'),(10,'hotelmanager','price'),(5,'hotelmanager','room'),(9,'hotelmanager','staff'),(13,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'hotelmanager','0001_initial','2017-12-07 08:16:56'),(2,'contenttypes','0001_initial','2017-12-07 08:21:49'),(3,'auth','0001_initial','2017-12-07 08:21:51'),(4,'contenttypes','0002_remove_content_type_name','2017-12-07 08:21:51'),(5,'auth','0002_alter_permission_name_max_length','2017-12-07 08:21:51'),(6,'auth','0003_alter_user_email_max_length','2017-12-07 08:21:51'),(7,'auth','0004_alter_user_username_opts','2017-12-07 08:21:52'),(8,'auth','0005_alter_user_last_login_null','2017-12-07 08:21:52'),(9,'auth','0006_require_contenttypes_0002','2017-12-07 08:21:52'),(10,'auth','0007_alter_validators_add_error_messages','2017-12-07 08:21:52'),(11,'auth','0008_alter_user_username_max_length','2017-12-07 08:21:52'),(12,'admin','0001_initial','2017-12-07 08:23:24'),(13,'admin','0002_logentry_remove_auto_add','2017-12-07 08:23:24'),(14,'sessions','0001_initial','2017-12-07 08:23:58'),(15,'hotelmanager','0002_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions_django','2017-12-10 05:26:19');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('3rx2jubz95mlpvl3n8agdwajjw4nrmzl','ZGM4YjQ5MzQ4NzBiZWEwNGIxZTYzNTQ5NDNkMzQ1YWI4ZmM2ZTM5NTp7InVzZXIiOiIxNzgwNDMzNjE3MyIsImN1c19pZCI6MX0=','2017-12-25 01:07:13'),('a7ic2friteh10rwhbxdgcynrh2vry234','MjExZDM3ZTQ1NWZjOTUwMzIzZTAwZWQ3Zjg2ZTQ2OTNmOGI5ODgyNjp7Il9hdXRoX3VzZXJfaGFzaCI6ImI4ZmQ0ZWNlYzk3YTViYzhkMWY3ZjA2ZWNmY2VhZTExNjg1ZGU0MjQiLCJ1c2VyIjoiMTExMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEifQ==','2017-12-21 14:14:41'),('cihq8qgs3m5jb0r9rqfxjy5rxwioba3d','NGUyZDk1NTEyYjZlMGFkMThjYzViMTA0MzczNDE1M2RiNWRiM2UxMjp7ImN1c19pZCI6MSwidXNlciI6IjE3ODA0MzM2MTczIn0=','2018-01-02 11:56:39'),('pezx0ppcidmsdzvlnstl35ajm7cpn3ld','ZmRmM2YyZWFjZjQyYzViMWJkYjU5ODc1NTY3OWY1NjllOWM3NWYzYjp7InVzZXIiOiIxNzY0MzMwODY1NyJ9','2017-12-22 13:53:22'),('stftdsg8opgq1hbso8f6c0iekjuqbixf','ZWI0OWFjNmNiMjBiOTI4YWVlNThjOTNlYzI3MmE4ODM2MjQ4ZWQwNDp7ImN1c19pZCI6MywidXNlciI6IjE3ODA0MzMxMjM0In0=','2018-01-02 17:09:13'),('wwzherlfq940c8iu3zr2z5i2wp4tg0e7','NjI2ZDhhYzBiMzA0NWE4NTlkM2NlYTc3MzAyMzMwNGQzYTdhZTRhYzp7InVzZXIiOiIxMjM0NTY3ODkwMSJ9','2017-12-22 13:39:31');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `price`
--

DROP TABLE IF EXISTS `price`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `price` (
  `id` int(11) DEFAULT NULL,
  `room_level` enum('std_high','std_mid','std_low','double_high','double_mid','double_low') NOT NULL DEFAULT 'std_high',
  `room_price` double DEFAULT NULL,
  PRIMARY KEY (`room_level`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `price`
--

LOCK TABLES `price` WRITE;
/*!40000 ALTER TABLE `price` DISABLE KEYS */;
INSERT INTO `price` VALUES (NULL,'std_high',300),(NULL,'std_mid',200),(NULL,'std_low',100),(NULL,'double_high',580),(NULL,'double_mid',380),(NULL,'double_low',280);
/*!40000 ALTER TABLE `price` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `room`
--

DROP TABLE IF EXISTS `room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `room` (
  `room_id` char(4) NOT NULL,
  `room_level` enum('std_high','std_mid','std_low','double_high','double_mid','double_low') DEFAULT NULL,
  `room_pic` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`room_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room`
--

LOCK TABLES `room` WRITE;
/*!40000 ALTER TABLE `room` DISABLE KEYS */;
INSERT INTO `room` VALUES ('101','std_low',NULL),('102','std_mid','img/room/2.jpg'),('103','std_high','img/room/3.jpg'),('104','std_low','img/room/4.jpg'),('105','std_mid','img/room/5.jpg'),('106','std_high','img/room/6.jpg'),('107','double_low','img/room/7.jpg'),('108','double_mid','img/room/8.jpg'),('109','double_high','img/room/9.jpg'),('110','double_high','img/room/10.jpg'),('111','double_low','img/room/11.jpg'),('112','double_mid','img/room/12.jpg'),('113','double_mid','img/room/13.jpg'),('114','double_high','img/room/14.jpg'),('115','double_low','img/room/15.jpg'),('116','std_mid','img/room/16.jpg'),('117','std_low','img/room/17.jpg'),('118','std_high','img/room/18.jpg');
/*!40000 ALTER TABLE `room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `room_info`
--

DROP TABLE IF EXISTS `room_info`;
/*!50001 DROP VIEW IF EXISTS `room_info`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `room_info` (
  `room_id` tinyint NOT NULL,
  `check_name` tinyint NOT NULL,
  `check_phone` tinyint NOT NULL,
  `check_checkInTime` tinyint NOT NULL,
  `check_leavetime` tinyint NOT NULL,
  `check_id` tinyint NOT NULL,
  `book_id` tinyint NOT NULL,
  `check_statu` tinyint NOT NULL,
  `room_level` tinyint NOT NULL,
  `room_price` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `staff` (
  `sta_id` int(11) NOT NULL AUTO_INCREMENT,
  `sta_authority` enum('high','normal') DEFAULT NULL,
  `sta_passward` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`sta_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `room_info`
--

/*!50001 DROP TABLE IF EXISTS `room_info`*/;
/*!50001 DROP VIEW IF EXISTS `room_info`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `room_info` AS select `checkinfo`.`room_id` AS `room_id`,`checkinfo`.`check_name` AS `check_name`,`checkinfo`.`check_phone` AS `check_phone`,`checkinfo`.`check_checkInTime` AS `check_checkInTime`,`checkinfo`.`check_leavetime` AS `check_leavetime`,`checkinfo`.`check_id` AS `check_id`,`checkinfo`.`book_id` AS `book_id`,`checkinfo`.`check_statu` AS `check_statu`,`room`.`room_level` AS `room_level`,`price`.`room_price` AS `room_price` from ((`checkinfo` join `room`) join `price`) where ((`checkinfo`.`room_id` = `room`.`room_id`) and (`price`.`room_level` = `room`.`room_level`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-12-20 16:58:54
