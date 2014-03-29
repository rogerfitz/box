-- MySQL dump 10.13  Distrib 5.5.34, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: box
-- ------------------------------------------------------
-- Server version	5.5.34-0ubuntu0.12.04.1

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
-- Table structure for table `attr_attr`
--

DROP TABLE IF EXISTS `attr_attr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `attr_attr` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(30) NOT NULL,
  `val` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attr_attr`
--

LOCK TABLES `attr_attr` WRITE;
/*!40000 ALTER TABLE `attr_attr` DISABLE KEYS */;
/*!40000 ALTER TABLE `attr_attr` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attr_attribute`
--

DROP TABLE IF EXISTS `attr_attribute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `attr_attribute` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(30) NOT NULL,
  `val` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attr_attribute`
--

LOCK TABLES `attr_attribute` WRITE;
/*!40000 ALTER TABLE `attr_attribute` DISABLE KEYS */;
/*!40000 ALTER TABLE `attr_attribute` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attr_boxattr`
--

DROP TABLE IF EXISTS `attr_boxattr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `attr_boxattr` (
  `attr_ptr_id` int(11) NOT NULL,
  `box_id` int(11) NOT NULL,
  PRIMARY KEY (`attr_ptr_id`),
  CONSTRAINT `attr_ptr_id_refs_id_0afe3963` FOREIGN KEY (`attr_ptr_id`) REFERENCES `attr_attr` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attr_boxattr`
--

LOCK TABLES `attr_boxattr` WRITE;
/*!40000 ALTER TABLE `attr_boxattr` DISABLE KEYS */;
/*!40000 ALTER TABLE `attr_boxattr` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attr_boxattribute`
--

DROP TABLE IF EXISTS `attr_boxattribute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `attr_boxattribute` (
  `attribute_ptr_id` int(11) NOT NULL,
  `box_id` int(11) NOT NULL,
  PRIMARY KEY (`attribute_ptr_id`),
  CONSTRAINT `attribute_ptr_id_refs_id_d121dfe3` FOREIGN KEY (`attribute_ptr_id`) REFERENCES `attr_attribute` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attr_boxattribute`
--

LOCK TABLES `attr_boxattribute` WRITE;
/*!40000 ALTER TABLE `attr_boxattribute` DISABLE KEYS */;
/*!40000 ALTER TABLE `attr_boxattribute` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attr_productattr`
--

DROP TABLE IF EXISTS `attr_productattr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `attr_productattr` (
  `attr_ptr_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`attr_ptr_id`),
  CONSTRAINT `attr_ptr_id_refs_id_4c6a2d4f` FOREIGN KEY (`attr_ptr_id`) REFERENCES `attr_attr` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attr_productattr`
--

LOCK TABLES `attr_productattr` WRITE;
/*!40000 ALTER TABLE `attr_productattr` DISABLE KEYS */;
/*!40000 ALTER TABLE `attr_productattr` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attr_profileattr`
--

DROP TABLE IF EXISTS `attr_profileattr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `attr_profileattr` (
  `attr_ptr_id` int(11) NOT NULL,
  `prof_id` int(11) NOT NULL,
  PRIMARY KEY (`attr_ptr_id`),
  CONSTRAINT `attr_ptr_id_refs_id_d6959dc2` FOREIGN KEY (`attr_ptr_id`) REFERENCES `attr_attr` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attr_profileattr`
--

LOCK TABLES `attr_profileattr` WRITE;
/*!40000 ALTER TABLE `attr_profileattr` DISABLE KEYS */;
/*!40000 ALTER TABLE `attr_profileattr` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attr_profileattribute`
--

DROP TABLE IF EXISTS `attr_profileattribute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `attr_profileattribute` (
  `attribute_ptr_id` int(11) NOT NULL,
  `prof_id` int(11) NOT NULL,
  PRIMARY KEY (`attribute_ptr_id`),
  CONSTRAINT `attribute_ptr_id_refs_id_61623678` FOREIGN KEY (`attribute_ptr_id`) REFERENCES `attr_attribute` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attr_profileattribute`
--

LOCK TABLES `attr_profileattribute` WRITE;
/*!40000 ALTER TABLE `attr_profileattribute` DISABLE KEYS */;
/*!40000 ALTER TABLE `attr_profileattribute` ENABLE KEYS */;
UNLOCK TABLES;

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
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
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
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=103 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add site',6,'add_site'),(17,'Can change site',6,'change_site'),(18,'Can delete site',6,'delete_site'),(19,'Can add product',7,'add_product'),(20,'Can change product',7,'change_product'),(21,'Can delete product',7,'delete_product'),(22,'Can add log entry',8,'add_logentry'),(23,'Can change log entry',8,'change_logentry'),(24,'Can delete log entry',8,'delete_logentry'),(28,'Can add box',10,'add_box'),(29,'Can change box',10,'change_box'),(30,'Can delete box',10,'delete_box'),(31,'Can add user',11,'add_user'),(32,'Can change user',11,'change_user'),(33,'Can delete user',11,'delete_user'),(34,'Can add migration history',12,'add_migrationhistory'),(35,'Can change migration history',12,'change_migrationhistory'),(36,'Can delete migration history',12,'delete_migrationhistory'),(37,'Can add product survey',13,'add_productsurvey'),(38,'Can change product survey',13,'change_productsurvey'),(39,'Can delete product survey',13,'delete_productsurvey'),(40,'Can add box survey',14,'add_boxsurvey'),(41,'Can change box survey',14,'change_boxsurvey'),(42,'Can delete box survey',14,'delete_boxsurvey'),(43,'Can add profile',15,'add_profile'),(44,'Can change profile',15,'change_profile'),(45,'Can delete profile',15,'delete_profile'),(46,'Can add event processing exception',16,'add_eventprocessingexception'),(47,'Can change event processing exception',16,'change_eventprocessingexception'),(48,'Can delete event processing exception',16,'delete_eventprocessingexception'),(49,'Can add event',17,'add_event'),(50,'Can change event',17,'change_event'),(51,'Can delete event',17,'delete_event'),(52,'Can add transfer',18,'add_transfer'),(53,'Can change transfer',18,'change_transfer'),(54,'Can delete transfer',18,'delete_transfer'),(55,'Can add transfer charge fee',19,'add_transferchargefee'),(56,'Can change transfer charge fee',19,'change_transferchargefee'),(57,'Can delete transfer charge fee',19,'delete_transferchargefee'),(58,'Can add customer',20,'add_customer'),(59,'Can change customer',20,'change_customer'),(60,'Can delete customer',20,'delete_customer'),(61,'Can add current subscription',21,'add_currentsubscription'),(62,'Can change current subscription',21,'change_currentsubscription'),(63,'Can delete current subscription',21,'delete_currentsubscription'),(64,'Can add invoice',22,'add_invoice'),(65,'Can change invoice',22,'change_invoice'),(66,'Can delete invoice',22,'delete_invoice'),(67,'Can add invoice item',23,'add_invoiceitem'),(68,'Can change invoice item',23,'change_invoiceitem'),(69,'Can delete invoice item',23,'delete_invoiceitem'),(70,'Can add charge',24,'add_charge'),(71,'Can change charge',24,'change_charge'),(72,'Can delete charge',24,'delete_charge'),(73,'Can add attribute',25,'add_attribute'),(74,'Can change attribute',25,'change_attribute'),(75,'Can delete attribute',25,'delete_attribute'),(85,'Can add attr',29,'add_attr'),(86,'Can change attr',29,'change_attr'),(87,'Can delete attr',29,'delete_attr'),(88,'Can add profile attr',30,'add_profileattr'),(89,'Can change profile attr',30,'change_profileattr'),(90,'Can delete profile attr',30,'delete_profileattr'),(91,'Can add box attr',31,'add_boxattr'),(92,'Can change box attr',31,'change_boxattr'),(93,'Can delete box attr',31,'delete_boxattr'),(94,'Can add captcha store',32,'add_captchastore'),(95,'Can change captcha store',32,'change_captchastore'),(96,'Can delete captcha store',32,'delete_captchastore'),(97,'Can add product attr',33,'add_productattr'),(98,'Can change product attr',33,'change_productattr'),(99,'Can delete product attr',33,'delete_productattr'),(100,'Can add box feedback',34,'add_boxfeedback'),(101,'Can change box feedback',34,'change_boxfeedback'),(102,'Can delete box feedback',34,'delete_boxfeedback');
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
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$10000$e0wrCJXNs5kI$2cDhQbkNoZbK/hJWlZur2RGXFyZcqofv6MyD9Wu2eGk=','2014-01-07 16:54:35',1,'root','','','minime@hochweb.com',1,1,'2014-01-07 16:54:35'),(2,'pbkdf2_sha256$10000$pAWZhTMhev7c$QF7inXHW1jWTNa+j1xduPSjTgnzuormkfImkXuKASUE=','2014-01-07 17:39:49',1,'matteo','','','minime@hochweb.com',1,1,'2014-01-07 17:24:59');
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
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
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
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
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
-- Table structure for table `boxes_box`
--

DROP TABLE IF EXISTS `boxes_box`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `boxes_box` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` decimal(5,2) DEFAULT NULL,
  `date_added` date NOT NULL,
  `date_modified` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `boxes_box`
--

LOCK TABLES `boxes_box` WRITE;
/*!40000 ALTER TABLE `boxes_box` DISABLE KEYS */;
INSERT INTO `boxes_box` VALUES (22,17.35,'2014-01-20','2014-01-20'),(43,16.02,'2014-01-25','2014-01-25'),(44,16.02,'2014-01-25','2014-01-25'),(45,16.02,'2014-01-28','2014-01-28');
/*!40000 ALTER TABLE `boxes_box` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `boxes_box_feedback`
--

DROP TABLE IF EXISTS `boxes_box_feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `boxes_box_feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `box_id` int(11) NOT NULL,
  `boxfeedback_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `boxes_box_feedback_box_id_9dec63c_uniq` (`box_id`,`boxfeedback_id`),
  KEY `boxes_box_feedback_cdd9e3d2` (`box_id`),
  KEY `boxes_box_feedback_6be3b8f3` (`boxfeedback_id`),
  CONSTRAINT `boxfeedback_id_refs_id_e22f51e5` FOREIGN KEY (`boxfeedback_id`) REFERENCES `boxes_boxfeedback` (`id`),
  CONSTRAINT `box_id_refs_id_466b2035` FOREIGN KEY (`box_id`) REFERENCES `boxes_box` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `boxes_box_feedback`
--

LOCK TABLES `boxes_box_feedback` WRITE;
/*!40000 ALTER TABLE `boxes_box_feedback` DISABLE KEYS */;
/*!40000 ALTER TABLE `boxes_box_feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `boxes_box_products`
--

DROP TABLE IF EXISTS `boxes_box_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `boxes_box_products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `box_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `box_id` (`box_id`,`product_id`),
  KEY `boxes_box_products_cdd9e3d2` (`box_id`),
  KEY `boxes_box_products_7f1b40ad` (`product_id`),
  CONSTRAINT `box_id_refs_id_bbca97c0` FOREIGN KEY (`box_id`) REFERENCES `boxes_box` (`id`),
  CONSTRAINT `product_id_refs_id_0f6d6070` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=134 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `boxes_box_products`
--

LOCK TABLES `boxes_box_products` WRITE;
/*!40000 ALTER TABLE `boxes_box_products` DISABLE KEYS */;
INSERT INTO `boxes_box_products` VALUES (51,22,3),(52,22,4),(53,22,10),(54,22,12),(55,22,13),(56,22,14),(57,22,15),(58,22,16),(113,43,3),(114,43,4),(115,43,10),(116,43,12),(117,43,13),(118,43,14),(119,43,16),(120,44,3),(121,44,4),(122,44,10),(123,44,12),(124,44,13),(125,44,14),(126,44,16),(127,45,3),(128,45,4),(129,45,10),(130,45,12),(131,45,13),(132,45,14),(133,45,16);
/*!40000 ALTER TABLE `boxes_box_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `boxes_boxfeedback`
--

DROP TABLE IF EXISTS `boxes_boxfeedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `boxes_boxfeedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `user_id_refs_id_9224c82d` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `boxes_boxfeedback`
--

LOCK TABLES `boxes_boxfeedback` WRITE;
/*!40000 ALTER TABLE `boxes_boxfeedback` DISABLE KEYS */;
/*!40000 ALTER TABLE `boxes_boxfeedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `captcha_captchastore`
--

DROP TABLE IF EXISTS `captcha_captchastore`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `captcha_captchastore` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `challenge` varchar(32) NOT NULL,
  `response` varchar(32) NOT NULL,
  `hashkey` varchar(40) NOT NULL,
  `expiration` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hashkey` (`hashkey`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `captcha_captchastore`
--

LOCK TABLES `captcha_captchastore` WRITE;
/*!40000 ALTER TABLE `captcha_captchastore` DISABLE KEYS */;
INSERT INTO `captcha_captchastore` VALUES (54,'KCYP','kcyp','1c78a53cc987e9126f4f90a1f432feaf02fa5acc','2014-01-29 04:58:39'),(55,'OOAQ','ooaq','c9c060f20dd857b83b6453895326a8fbc8cb8459','2014-01-29 04:58:51'),(56,'XKFG','xkfg','9410503911ac42b6957da16d312c9ec4ef2ae5ec','2014-01-29 04:58:59'),(57,'TYFB','tyfb','3dcce9462fc18aa4513ebcfec0f36bec9d1424cf','2014-01-29 04:59:07'),(58,'OFNX','ofnx','2fd7d8292d837b7b7a63d3dcbb95b554cad4b05b','2014-01-29 04:59:13'),(59,'XLDU','xldu','7b4c13c2073ca28ece3fa57c3a06c2ad0a5641fd','2014-01-29 04:59:44'),(60,'XCPY','xcpy','ac1e177ee4308c896c69dc5baf55683bca23cb34','2014-01-29 04:59:51'),(61,'RSSY','rssy','b71ea6dd7d561bd05ef101a08c362d79e1354ab1','2014-01-29 05:01:57');
/*!40000 ALTER TABLE `captcha_captchastore` ENABLE KEYS */;
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
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2014-01-07 17:29:01',2,7,'2','Product object',1,''),(2,'2014-01-07 17:31:56',2,7,'3','Product object',1,''),(3,'2014-01-07 17:48:51',2,7,'3','Product object',2,'Changed why_buy and image_url.'),(4,'2014-01-07 17:49:20',2,7,'2','Product object',2,'Changed why_buy and image_url.');
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
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'site','sites','site'),(7,'product','products','product'),(8,'log entry','admin','logentry'),(10,'box','boxes','box'),(11,'user','users','user'),(12,'migration history','south','migrationhistory'),(13,'product survey','surveys','productsurvey'),(14,'box survey','surveys','boxsurvey'),(15,'profile','users','profile'),(16,'event processing exception','payments','eventprocessingexception'),(17,'event','payments','event'),(18,'transfer','payments','transfer'),(19,'transfer charge fee','payments','transferchargefee'),(20,'customer','payments','customer'),(21,'current subscription','payments','currentsubscription'),(22,'invoice','payments','invoice'),(23,'invoice item','payments','invoiceitem'),(24,'charge','payments','charge'),(25,'attribute','users','attribute'),(29,'attr','attr','attr'),(30,'profile attr','attr','profileattr'),(31,'box attr','attr','boxattr'),(32,'captcha store','captcha','captchastore'),(33,'product attr','attr','productattr'),(34,'box feedback','boxes','boxfeedback');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
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
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('9ilzntyf0bfpsls3kljk0y2iqvo7dpyt','NjFiM2Q0YjU0ODQyNzlkZmNlZWNlN2IzZTA5YzI4NzkzOGZjYzE2MTp7fQ==','2014-02-12 04:59:25'),('aobiwvoux2jvwr52h69oqbbjl47f8ok9','ZjU2ZmU2MGZhMTllYmVkMGRhMWNhMzc5YzM1ZTI4NGFiY2M3ZTI3Yjp7fQ==','2014-02-01 03:52:13'),('nxodr2mjylj7q69il27ypk8p7rzpelaw','ZjU2ZmU2MGZhMTllYmVkMGRhMWNhMzc5YzM1ZTI4NGFiY2M3ZTI3Yjp7fQ==','2014-02-01 03:53:36'),('x3limm0slrchcbth8did0917aj9ypyy1','MzAzYzJlOTdiOTQ4MGY5ZWE5ZmU0MDE1ZThhOTc3MjI0ZDM2ZTkyZjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MTN9','2014-02-11 21:00:00'),('yivoz4xg4wmbp0rx2zvvm6cp2rfyt70e','ZjU2ZmU2MGZhMTllYmVkMGRhMWNhMzc5YzM1ZTI4NGFiY2M3ZTI3Yjp7fQ==','2014-02-01 03:52:55'),('zf4nm1i6ikgwidbnmvx06yj4ymdrgp5w','ZjU2ZmU2MGZhMTllYmVkMGRhMWNhMzc5YzM1ZTI4NGFiY2M3ZTI3Yjp7fQ==','2014-02-01 03:51:29');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_box`
--

DROP TABLE IF EXISTS `products_box`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_box` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_box`
--

LOCK TABLES `products_box` WRITE;
/*!40000 ALTER TABLE `products_box` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_box` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_box_products`
--

DROP TABLE IF EXISTS `products_box_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_box_products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `box_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `box_id` (`box_id`,`product_id`),
  KEY `products_box_products_cdd9e3d2` (`box_id`),
  KEY `products_box_products_7f1b40ad` (`product_id`),
  CONSTRAINT `box_id_refs_id_3caecbc2` FOREIGN KEY (`box_id`) REFERENCES `products_box` (`id`),
  CONSTRAINT `product_id_refs_id_69efd60a` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_box_products`
--

LOCK TABLES `products_box_products` WRITE;
/*!40000 ALTER TABLE `products_box_products` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_box_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_product`
--

DROP TABLE IF EXISTS `products_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `url` varchar(200) NOT NULL,
  `price` decimal(5,2) NOT NULL,
  `category` varchar(50) NOT NULL,
  `image_url` varchar(200) DEFAULT NULL,
  `duration_in_weeks` int(11) NOT NULL,
  `feedback` varchar(30),
  `item_count` int(11) NOT NULL,
  `items_per_box` int(11) NOT NULL,
  `items_per_purchase` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_product`
--

LOCK TABLES `products_product` WRITE;
/*!40000 ALTER TABLE `products_product` DISABLE KEYS */;
INSERT INTO `products_product` VALUES (3,'Bowties','http://www.amazon.com/dp/B006YEUD7G/',2.25,'party gear','http://ecx.images-amazon.com/images/I/61isMv5-h7L._SX522_.jpg',1,NULL,0,0,1),(4,'Hearos Ear Plugs Xtreme Protection','http://www.amazon.com/Hearos-Plugs-Xtreme-Protection-14-Pair/dp/B001EPQ86A',5.00,'ear plugs','http://ecx.images-amazon.com/images/I/513mdNTDOpL._SY450_.jpg',1,NULL,0,0,1),(10,'Bellagio Chocolate Truffle 3 of 25','http://www.amazon.com/Bellagio-Chocolate-Truffle-1-25-Ounce-Packets/dp/B000I200NW/',2.40,'hot chocolate','http://ecx.images-amazon.com/images/I/81brpZ16czL._SL1500_.jpg',1,NULL,0,0,1),(12,'Durex Pleasure Pack','http://www.amazon.com/Durex-Pleasure-Pack-Latex-Condoms/dp/B00B4E00G0/',0.96,'condoms, sex','http://ecx.images-amazon.com/images/I/71BVomyfI8L._SL1500_.jpg',1,NULL,0,0,1),(13,'Twix','http://www.amazon.com/Twix-Caramel-Chocolate-1-79-Ounce-Packages/dp/B0029JE7RC/',0.72,'candy bar, food','http://ecx.images-amazon.com/images/I/61t0gybPFBL._SL1500_.jpg',1,NULL,0,0,1),(14,'Chap Stick Variety','http://www.amazon.com/Variety-Assorted-Original-Strawberry-Moisturizer/dp/B00658MWUW/',1.20,'chap stick, winter','http://ecx.images-amazon.com/images/I/51waJrxFu%2BL.jpg',1,NULL,0,0,1),(15,'Chap Stick','http://www.amazon.com/Chapstick-Pack-classic-original-moisturizer/dp/B005KSY9QI/',1.33,'chap stick, winter','http://ecx.images-amazon.com/images/I/81e0NEXzjTL._SL1500_.jpg',1,NULL,0,0,1),(16,'Kikkerland Drunk Shot Glasses','http://www.amazon.com/Kikkerland-Drunk-Shot-Glasses-Set/dp/B003T1D1RG/',3.49,'drinking, glassware','http://ecx.images-amazon.com/images/I/31efEVNuVeL.jpg',1,NULL,0,0,1);
/*!40000 ALTER TABLE `products_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_product_attrs`
--

DROP TABLE IF EXISTS `products_product_attrs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_product_attrs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) NOT NULL,
  `productattr_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `products_product_attrs_product_id_22fb7660_uniq` (`product_id`,`productattr_id`),
  KEY `products_product_attrs_7f1b40ad` (`product_id`),
  KEY `products_product_attrs_6c3b5f8b` (`productattr_id`),
  CONSTRAINT `productattr_id_refs_attr_ptr_id_a4a95a19` FOREIGN KEY (`productattr_id`) REFERENCES `attr_productattr` (`attr_ptr_id`),
  CONSTRAINT `product_id_refs_id_9ba8c915` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_product_attrs`
--

LOCK TABLES `products_product_attrs` WRITE;
/*!40000 ALTER TABLE `products_product_attrs` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_product_attrs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `south_migrationhistory`
--

DROP TABLE IF EXISTS `south_migrationhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `south_migrationhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) NOT NULL,
  `migration` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `south_migrationhistory`
--

LOCK TABLES `south_migrationhistory` WRITE;
/*!40000 ALTER TABLE `south_migrationhistory` DISABLE KEYS */;
INSERT INTO `south_migrationhistory` VALUES (1,'users','0001_initial','2014-01-16 06:01:48'),(2,'users','0002_auto__add_field_profile_pa','2014-01-16 06:02:21'),(3,'users','0003_auto__del_field_profile_pa','2014-01-16 06:03:00'),(4,'users','0004_auto__del_field_profile_zipcode__del_field_profile_addr2__del_field_pr','2014-01-16 06:03:31'),(5,'users','0005_auto__add_field_profile_addr1__add_field_profile_addr2__add_field_prof','2014-01-16 06:03:51'),(6,'products','0001_initial','2014-01-16 17:02:08'),(8,'products','0002_initial','2014-01-16 17:08:11'),(9,'products','0003_auto__del_field_product_why_buy__add_field_product_prod_type__add_fiel','2014-01-16 17:09:10'),(10,'boxes','0001_initial','2014-01-16 17:16:33'),(11,'boxes','0002_auto__add_field_box_feedback','2014-01-16 17:17:08'),(12,'products','0004_auto__add_field_product_items_per_box','2014-01-16 18:48:42'),(13,'users','0006_auto__add_attribute__chg_field_profile_date_of_birth','2014-01-18 03:57:09'),(14,'users','0007_auto__chg_field_profile_city__chg_field_profile_zipcode__chg_field_pro','2014-01-18 18:03:30'),(15,'boxes','0003_auto__add_field_box_date_added__add_field_box_date_modified','2014-01-21 01:49:56'),(16,'captcha','0001_initial','2014-01-21 02:43:55'),(17,'users','0008_auto__del_attribute','2014-01-21 02:48:54'),(18,'products','0005_auto__del_field_product_prod_type__del_field_product_send_similar__chg','2014-01-26 01:59:33'),(19,'products','0006_auto__add_field_product_items_per_purchase','2014-01-26 02:01:38'),(20,'boxes','0004_auto__add_boxfeedback__del_field_box_feedback','2014-01-28 20:10:36'),(21,'users','0009_auto__add_field_profile_email','2014-01-28 23:09:18'),(22,'users','0010_auto__del_field_profile_email','2014-01-28 23:11:07');
/*!40000 ALTER TABLE `south_migrationhistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `surveys_boxsurvey`
--

DROP TABLE IF EXISTS `surveys_boxsurvey`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `surveys_boxsurvey` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rating` decimal(1,1) NOT NULL,
  `box_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `box_id` (`box_id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `box_id_refs_id_bbb9d434` FOREIGN KEY (`box_id`) REFERENCES `boxes_box` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `surveys_boxsurvey`
--

LOCK TABLES `surveys_boxsurvey` WRITE;
/*!40000 ALTER TABLE `surveys_boxsurvey` DISABLE KEYS */;
/*!40000 ALTER TABLE `surveys_boxsurvey` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `surveys_productsurvey`
--

DROP TABLE IF EXISTS `surveys_productsurvey`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `surveys_productsurvey` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rating` decimal(1,1) NOT NULL,
  `product_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_id` (`product_id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `product_id_refs_id_de09d0ba` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `surveys_productsurvey`
--

LOCK TABLES `surveys_productsurvey` WRITE;
/*!40000 ALTER TABLE `surveys_productsurvey` DISABLE KEYS */;
/*!40000 ALTER TABLE `surveys_productsurvey` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_profile`
--

DROP TABLE IF EXISTS `users_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `box_to_ship_id` int(11) DEFAULT NULL,
  `current_box_id` int(11) DEFAULT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `paid` tinyint(1) NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  `addr1` varchar(50) NOT NULL,
  `addr2` varchar(50) NOT NULL,
  `city` varchar(40) NOT NULL,
  `state` varchar(30) NOT NULL,
  `zipcode` varchar(15) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `users_profile_4e12ca24` (`box_to_ship_id`),
  KEY `users_profile_5f8a4558` (`current_box_id`),
  CONSTRAINT `box_to_ship_id_refs_id_d3e1180e` FOREIGN KEY (`box_to_ship_id`) REFERENCES `boxes_box` (`id`),
  CONSTRAINT `current_box_id_refs_id_d3e1180e` FOREIGN KEY (`current_box_id`) REFERENCES `boxes_box` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=497 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_profile`
--

LOCK TABLES `users_profile` WRITE;
/*!40000 ALTER TABLE `users_profile` DISABLE KEYS */;
INSERT INTO `users_profile` VALUES (486,NULL,45,'Matteo','Hoch',1,'1994-08-12','310 E Gregory Drive','','Champaign','IL','60527'),(490,NULL,NULL,'Bill','Ted',0,'1994-08-05','310 E Gregory Drive','','Champaign','IL','61820'),(492,NULL,NULL,'Bill','Ted',0,'2006-01-03','310 E Gregory Drive','','Champaign','IL','61820'),(495,NULL,NULL,'Test','Testy',1,'1991-02-03','310 E Gregory Drive','','Champaign','IL','61820'),(496,NULL,NULL,'Baa','Ted',0,'1992-01-03','310 E Gregory Drive','','Champaign','IL','61820');
/*!40000 ALTER TABLE `users_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_profile_boxes`
--

DROP TABLE IF EXISTS `users_profile_boxes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_profile_boxes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `profile_id` int(11) NOT NULL,
  `box_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_profile_boxes_profile_id_36a0d40f_uniq` (`profile_id`,`box_id`),
  KEY `users_profile_boxes_5948a8a3` (`profile_id`),
  KEY `users_profile_boxes_cdd9e3d2` (`box_id`),
  CONSTRAINT `box_id_refs_id_e906c726` FOREIGN KEY (`box_id`) REFERENCES `boxes_box` (`id`),
  CONSTRAINT `profile_id_refs_id_0b3a098e` FOREIGN KEY (`profile_id`) REFERENCES `users_profile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_profile_boxes`
--

LOCK TABLES `users_profile_boxes` WRITE;
/*!40000 ALTER TABLE `users_profile_boxes` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_profile_boxes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user`
--

DROP TABLE IF EXISTS `users_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  `profile_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `profile_id` (`profile_id`),
  CONSTRAINT `profile_id_refs_id_2248f7cc` FOREIGN KEY (`profile_id`) REFERENCES `users_profile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user`
--

LOCK TABLES `users_user` WRITE;
/*!40000 ALTER TABLE `users_user` DISABLE KEYS */;
INSERT INTO `users_user` VALUES (13,'','','pbkdf2_sha256$12000$qKZvwkDBb9lR$P57JrLir+BW56a8+xvT7vYYXHIOCpJg7M6eJwfXWdtE=','2014-01-29 04:38:01',1,'joshua','minime@hochweb.com',1,1,'2014-01-18 17:32:34',NULL),(21,'','','pbkdf2_sha256$12000$yZqw8xm2hRtN$dAreAmxuKmr44jVS982Fr+1bsieIu3MSEm/CEq/Jyjc=','2014-01-29 04:50:44',0,'mhoch2','',0,1,'2014-01-28 20:38:54',486),(25,'','','pbkdf2_sha256$12000$ZY5CjAKd6Ews$HdA4HBVkw3OVaY2c0CVEIFJLZAXPDObvTjf6PuorWS0=','2014-01-29 03:46:38',0,'bill','',0,1,'2014-01-29 03:46:37',490),(28,'','','pbkdf2_sha256$12000$Bas8FG6iDc6e$Zc+7m0Di+i85+/7GM5K+HKKMIze7l/XLMYYZGUNvnA4=','2014-01-29 04:05:29',0,'az','',0,1,'2014-01-29 04:05:28',NULL),(30,'','','pbkdf2_sha256$12000$DFFekmBeajUe$TE+Vr6qluiCJkQNQgkc//aTPQtpVooZu3rz1hDfJU2Q=','2014-01-29 04:50:51',0,'test','',0,1,'2014-01-29 04:21:30',495),(31,'','','pbkdf2_sha256$12000$vSHm4NlbXVM5$DSjJKGzIOfpfCbTpuB2gQYNHThtS913ExZFAoOTYEkc=','2014-01-29 04:58:03',0,'mhoch2@illinois.edu','',0,1,'2014-01-29 04:58:03',496);
/*!40000 ALTER TABLE `users_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_groups`
--

DROP TABLE IF EXISTS `users_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_groups_user_id_72323bc9_uniq` (`user_id`,`group_id`),
  KEY `users_user_groups_6340c63c` (`user_id`),
  KEY `users_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `group_id_refs_id_52d270a4` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_cbec8e88` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_groups`
--

LOCK TABLES `users_user_groups` WRITE;
/*!40000 ALTER TABLE `users_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_user_permissions`
--

DROP TABLE IF EXISTS `users_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_user_permissions_user_id_217af32e_uniq` (`user_id`,`permission_id`),
  KEY `users_user_user_permissions_6340c63c` (`user_id`),
  KEY `users_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_01625f6a` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_7d077e6f` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_user_permissions`
--

LOCK TABLES `users_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `users_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-01-28 23:45:22
