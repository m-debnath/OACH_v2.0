/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/ oach_db /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE oach_db;

DROP TABLE IF EXISTS auth_group;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS auth_group_permissions;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS auth_permission;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS auth_user;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS auth_user_groups;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS auth_user_user_permissions;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS authtoken_token;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS django_admin_log;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=87 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS django_content_type;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS django_migrations;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS django_session;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS oach_accounts_api_transaction;
CREATE TABLE `oach_accounts_api_transaction` (
  `id` int NOT NULL AUTO_INCREMENT,
  `TransactionName` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique accountstransactionname` (`TransactionName`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS oach_accounts_api_transactionparameter;
CREATE TABLE `oach_accounts_api_transactionparameter` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ParameterName` varchar(100) NOT NULL,
  `ParameterValue` varchar(250) DEFAULT NULL,
  `TransactionName_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique accountstransactionparameter` (`TransactionName_id`,`ParameterName`),
  CONSTRAINT `oach_accounts_api_tr_TransactionName_id_a5077f1b_fk_oach_acco` FOREIGN KEY (`TransactionName_id`) REFERENCES `oach_accounts_api_transaction` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS oach_activities_api_transaction;
CREATE TABLE `oach_activities_api_transaction` (
  `id` int NOT NULL AUTO_INCREMENT,
  `TransactionName` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique activitiestransactionname` (`TransactionName`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS oach_activities_api_transactionparameter;
CREATE TABLE `oach_activities_api_transactionparameter` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ParameterName` varchar(100) NOT NULL,
  `ParameterValue` varchar(250) DEFAULT NULL,
  `TransactionName_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique activitiestransactionparameter` (`TransactionName_id`,`ParameterName`),
  CONSTRAINT `oach_activities_api__TransactionName_id_bc92eae2_fk_oach_acti` FOREIGN KEY (`TransactionName_id`) REFERENCES `oach_activities_api_transaction` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS oach_assets_api_transaction;
CREATE TABLE `oach_assets_api_transaction` (
  `id` int NOT NULL AUTO_INCREMENT,
  `TransactionName` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique assetstransactionname` (`TransactionName`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS oach_assets_api_transactionparameter;
CREATE TABLE `oach_assets_api_transactionparameter` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ParameterName` varchar(100) NOT NULL,
  `ParameterValue` varchar(250) DEFAULT NULL,
  `TransactionName_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique assetstransactionparameter` (`TransactionName_id`,`ParameterName`),
  CONSTRAINT `oach_assets_api_tran_TransactionName_id_edcf83ab_fk_oach_asse` FOREIGN KEY (`TransactionName_id`) REFERENCES `oach_assets_api_transaction` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS oach_invoices_api_transaction;
CREATE TABLE `oach_invoices_api_transaction` (
  `id` int NOT NULL AUTO_INCREMENT,
  `TransactionName` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique invoicestransactionname` (`TransactionName`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS oach_invoices_api_transactionparameter;
CREATE TABLE `oach_invoices_api_transactionparameter` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ParameterName` varchar(100) NOT NULL,
  `ParameterValue` varchar(250) DEFAULT NULL,
  `TransactionName_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique invoicestransactionparameter` (`TransactionName_id`,`ParameterName`),
  CONSTRAINT `oach_invoices_api_tr_TransactionName_id_f24b584a_fk_oach_invo` FOREIGN KEY (`TransactionName_id`) REFERENCES `oach_invoices_api_transaction` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS oach_orders_api_transaction;
CREATE TABLE `oach_orders_api_transaction` (
  `id` int NOT NULL AUTO_INCREMENT,
  `TransactionName` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique orderstransactionname` (`TransactionName`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS oach_orders_api_transactionparameter;
CREATE TABLE `oach_orders_api_transactionparameter` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ParameterName` varchar(100) NOT NULL,
  `ParameterValue` varchar(250) DEFAULT NULL,
  `TransactionName_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique orderstransactionparameter` (`TransactionName_id`,`ParameterName`),
  CONSTRAINT `oach_orders_api_tran_TransactionName_id_201c0388_fk_oach_orde` FOREIGN KEY (`TransactionName_id`) REFERENCES `oach_orders_api_transaction` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS oach_service_requests_api_transaction;
CREATE TABLE `oach_service_requests_api_transaction` (
  `id` int NOT NULL AUTO_INCREMENT,
  `TransactionName` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique servicerequeststransactionname` (`TransactionName`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS oach_service_requests_api_transactionparameter;
CREATE TABLE `oach_service_requests_api_transactionparameter` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ParameterName` varchar(100) NOT NULL,
  `ParameterValue` varchar(250) DEFAULT NULL,
  `TransactionName_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique servicerequeststransactionparameter` (`TransactionName_id`,`ParameterName`),
  CONSTRAINT `oach_service_request_TransactionName_id_8fcefa4f_fk_oach_serv` FOREIGN KEY (`TransactionName_id`) REFERENCES `oach_service_requests_api_transaction` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;






INSERT INTO auth_permission(id,name,content_type_id,codename) VALUES(1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Token',7,'add_token'),(26,'Can change Token',7,'change_token'),(27,'Can delete Token',7,'delete_token'),(28,'Can view Token',7,'view_token'),(29,'Can add token',8,'add_tokenproxy'),(30,'Can change token',8,'change_tokenproxy'),(31,'Can delete token',8,'delete_tokenproxy'),(32,'Can view token',8,'view_tokenproxy'),(33,'Can add Accounts API Transaction',9,'add_transaction'),(34,'Can change Accounts API Transaction',9,'change_transaction'),(35,'Can delete Accounts API Transaction',9,'delete_transaction'),(36,'Can view Accounts API Transaction',9,'view_transaction'),(37,'Can add Accounts API Parameter',10,'add_transactionparameter'),(38,'Can change Accounts API Parameter',10,'change_transactionparameter'),(39,'Can delete Accounts API Parameter',10,'delete_transactionparameter'),(40,'Can view Accounts API Parameter',10,'view_transactionparameter'),(41,'Can add Assets API Transaction',11,'add_transaction'),(42,'Can change Assets API Transaction',11,'change_transaction'),(43,'Can delete Assets API Transaction',11,'delete_transaction'),(44,'Can view Assets API Transaction',11,'view_transaction'),(45,'Can add Assets API Parameter',12,'add_transactionparameter'),(46,'Can change Assets API Parameter',12,'change_transactionparameter'),(47,'Can delete Assets API Parameter',12,'delete_transactionparameter'),(48,'Can view Assets API Parameter',12,'view_transactionparameter'),(49,'Can add Orders API Transaction',13,'add_transaction'),(50,'Can change Orders API Transaction',13,'change_transaction'),(51,'Can delete Orders API Transaction',13,'delete_transaction'),(52,'Can view Orders API Transaction',13,'view_transaction'),(53,'Can add Orders API Parameter',14,'add_transactionparameter'),(54,'Can change Orders API Parameter',14,'change_transactionparameter'),(55,'Can delete Orders API Parameter',14,'delete_transactionparameter'),(56,'Can view Orders API Parameter',14,'view_transactionparameter'),(57,'Can add Invoices API Transaction',15,'add_transaction'),(58,'Can change Invoices API Transaction',15,'change_transaction'),(59,'Can delete Invoices API Transaction',15,'delete_transaction'),(60,'Can view Invoices API Transaction',15,'view_transaction'),(61,'Can add Invoices API Parameter',16,'add_transactionparameter'),(62,'Can change Invoices API Parameter',16,'change_transactionparameter'),(63,'Can delete Invoices API Parameter',16,'delete_transactionparameter'),(64,'Can view Invoices API Parameter',16,'view_transactionparameter'),(65,'Can add Invoices API Transaction',17,'add_transaction'),(66,'Can change Invoices API Transaction',17,'change_transaction'),(67,'Can delete Invoices API Transaction',17,'delete_transaction'),(68,'Can view Invoices API Transaction',17,'view_transaction'),(69,'Can add Invoices API Parameter',18,'add_transactionparameter'),(70,'Can change Invoices API Parameter',18,'change_transactionparameter'),(71,'Can delete Invoices API Parameter',18,'delete_transactionparameter'),(72,'Can view Invoices API Parameter',18,'view_transactionparameter'),(73,'Can add Activities API Transaction',19,'add_transaction'),(74,'Can change Activities API Transaction',19,'change_transaction'),(75,'Can delete Activities API Transaction',19,'delete_transaction'),(76,'Can view Activities API Transaction',19,'view_transaction'),(77,'Can add Activities API Parameter',20,'add_transactionparameter'),(78,'Can change Activities API Parameter',20,'change_transactionparameter'),(79,'Can delete Activities API Parameter',20,'delete_transactionparameter'),(80,'Can view Activities API Parameter',20,'view_transactionparameter');

INSERT INTO auth_user(id,password,last_login,is_superuser,username,first_name,last_name,email,is_staff,is_active,date_joined) VALUES(1,'pbkdf2_sha256$216000$shsFY5pEzCOp$gbuXH124RsFW2XJKsVYy5LnMzGuD39aH01xdj64VX58=','2021-04-18 22:47:50.599353',1,'oachadmin','','','oachadmin@tele2.com',1,1,'2021-04-16 20:04:47.445460'),(2,'pbkdf2_sha256$216000$N4dkTCg27QJ0$po1Uz6I8FW7rDvnvfSReRO3oPrGmF8HesdH8vc0oSv0=',NULL,1,'oachapiservice','','','oach@tele2.com',1,1,'2021-04-16 20:09:54.978767');



INSERT INTO authtoken_token(key,created,user_id) VALUES('2ff24a4d1792d8bf631538ebf73706e87e7df2c0','2021-04-16 20:13:56.154608',2);

INSERT INTO django_admin_log(id,action_time,object_id,object_repr,action_flag,change_message,content_type_id,user_id) VALUES(1,'2021-04-16 20:45:05.618678',X'31','Transaction - Get Account By Id',1,X'5b7b226164646564223a207b7d7d5d',9,1),(2,'2021-04-16 20:45:58.257973',X'31','Transaction - Get Account By Id Transaction Parameter - RequestURL',1,X'5b7b226164646564223a207b7d7d5d',10,1),(3,'2021-04-16 20:46:13.551364',X'32','Transaction - Get Account By Id Transaction Parameter - Authorization',1,X'5b7b226164646564223a207b7d7d5d',10,1),(4,'2021-04-16 21:35:39.826191',X'31','Transaction - Get Account By Id Transaction Parameter - RequestURL',2,X'5b7b226368616e676564223a207b226669656c6473223a205b22506172616d6574657256616c7565225d7d7d5d',10,1),(5,'2021-04-16 21:36:35.790333',X'31','Transaction - Get Account By Id Transaction Parameter - RequestURL',2,X'5b7b226368616e676564223a207b226669656c6473223a205b22506172616d6574657256616c7565225d7d7d5d',10,1),(6,'2021-04-16 21:42:30.979775',X'31','Transaction - Get Account By Id Transaction Parameter - RequestURL',2,X'5b7b226368616e676564223a207b226669656c6473223a205b22506172616d6574657256616c7565225d7d7d5d',10,1),(7,'2021-04-16 21:56:21.067723',X'31','Transaction - Get Account By Id Transaction Parameter - RequestURL',2,X'5b7b226368616e676564223a207b226669656c6473223a205b22506172616d6574657256616c7565225d7d7d5d',10,1),(8,'2021-04-16 21:57:06.659066',X'31','Transaction - Get Account By Id Transaction Parameter - RequestURL',2,X'5b7b226368616e676564223a207b226669656c6473223a205b22506172616d6574657256616c7565225d7d7d5d',10,1),(9,'2021-04-16 22:18:44.299033',X'31','Transaction - Get Account By Id Transaction Parameter - RequestURL',2,X'5b7b226368616e676564223a207b226669656c6473223a205b22506172616d6574657256616c7565225d7d7d5d',10,1),(10,'2021-04-16 22:28:14.836422',X'31','Transaction - Get Account By Id Transaction Parameter - RequestURL',2,X'5b7b226368616e676564223a207b226669656c6473223a205b22506172616d6574657256616c7565225d7d7d5d',10,1),(11,'2021-04-17 07:28:12.692928',X'32','Transaction - Update Account By Id',1,X'5b7b226164646564223a207b7d7d5d',9,1),(12,'2021-04-17 07:30:20.832679',X'33','Transaction - Update Account By Id Transaction Parameter - RequestURL',1,X'5b7b226164646564223a207b7d7d5d',10,1),(13,'2021-04-17 07:30:40.300114',X'34','Transaction - Update Account By Id Transaction Parameter - Authorization',1,X'5b7b226164646564223a207b7d7d5d',10,1),(14,'2021-04-17 08:09:24.025264',X'33','Transaction - Get Account Hierarchy By Id',1,X'5b7b226164646564223a207b7d7d5d',9,1),(15,'2021-04-17 08:10:13.865064',X'35','Transaction - Get Account Hierarchy By Id Transaction Parameter - RequestURL',1,X'5b7b226164646564223a207b7d7d5d',10,1),(16,'2021-04-17 08:10:29.387963',X'36','Transaction - Get Account Hierarchy By Id Transaction Parameter - Authorization',1,X'5b7b226164646564223a207b7d7d5d',10,1),(17,'2021-04-18 08:01:15.478434',X'31','Transaction - Get Assets By Account Id',1,X'5b7b226164646564223a207b7d7d5d',11,1),(18,'2021-04-18 08:01:50.654194',X'31','Transaction - Get Assets By Account Id Transaction Parameter - RequestURL',1,X'5b7b226164646564223a207b7d7d5d',12,1),(19,'2021-04-18 08:02:12.785812',X'32','Transaction - Get Assets By Account Id Transaction Parameter - Authorization',1,X'5b7b226164646564223a207b7d7d5d',12,1),(20,'2021-04-18 08:33:19.354579',X'31','Transaction - Get Assets By Account Id Transaction Parameter - RequestURL',2,X'5b7b226368616e676564223a207b226669656c6473223a205b22506172616d6574657256616c7565225d7d7d5d',12,1),(21,'2021-04-18 08:38:52.835603',X'32','Transaction - Get Assets By Account Id Transaction Parameter - Authorization',2,X'5b7b226368616e676564223a207b226669656c6473223a205b22506172616d6574657256616c7565225d7d7d5d',12,1),(22,'2021-04-18 08:42:39.199268',X'31','Transaction - Get Assets By Account Id Transaction Parameter - RequestURL',2,X'5b7b226368616e676564223a207b226669656c6473223a205b22506172616d6574657256616c7565225d7d7d5d',12,1),(23,'2021-04-18 16:10:14.396669',X'31','Transaction - Get Orders By Account Id',1,X'5b7b226164646564223a207b7d7d5d',13,1),(24,'2021-04-18 16:10:26.491598',X'31','Transaction - Get Orders By Account Id Transaction Parameter - RequestURL',1,X'5b7b226164646564223a207b7d7d5d',14,1),(25,'2021-04-18 16:10:51.573018',X'32','Transaction - Get Orders By Account Id Transaction Parameter - Authorization',1,X'5b7b226164646564223a207b7d7d5d',14,1),(26,'2021-04-18 16:18:30.300548',X'32','Transaction - Get Order Items By Account Id',1,X'5b7b226164646564223a207b7d7d5d',13,1),(27,'2021-04-18 16:18:48.273477',X'33','Transaction - Get Order Items By Account Id Transaction Parameter - RequestURL',1,X'5b7b226164646564223a207b7d7d5d',14,1),(28,'2021-04-18 16:19:16.835148',X'34','Transaction - Get Order Items By Account Id Transaction Parameter - Authorization',1,X'5b7b226164646564223a207b7d7d5d',14,1),(29,'2021-04-18 17:31:49.526916',X'31','Transaction - Get Invoice By Account Id',1,X'5b7b226164646564223a207b7d7d5d',15,1),(30,'2021-04-18 17:32:04.354198',X'31','Transaction - Get Invoice By Account Id Transaction Parameter - RequestURL',1,X'5b7b226164646564223a207b7d7d5d',16,1),(31,'2021-04-18 17:32:25.002433',X'32','Transaction - Get Invoice By Account Id Transaction Parameter - Authorization',1,X'5b7b226164646564223a207b7d7d5d',16,1),(32,'2021-04-18 17:35:59.747883',X'31','Transaction - Get Invoice By Billing Account Id',2,X'5b7b226368616e676564223a207b226669656c6473223a205b225472616e73616374696f6e4e616d65225d7d7d5d',15,1),(33,'2021-04-18 17:41:34.451693',X'32','Transaction - Get Payments By Invoice Id',1,X'5b7b226164646564223a207b7d7d5d',15,1),(34,'2021-04-18 17:42:18.473979',X'33','Transaction - Get Payments By Invoice Id Transaction Parameter - RequestURL',1,X'5b7b226164646564223a207b7d7d5d',16,1),(35,'2021-04-18 17:42:56.487787',X'34','Transaction - Get Payments By Invoice Id Transaction Parameter - Authorization',1,X'5b7b226164646564223a207b7d7d5d',16,1),(36,'2021-04-18 19:23:21.234858',X'34','Transaction - Get Treatment By Billing Account Id',1,X'5b7b226164646564223a207b7d7d5d',9,1),(37,'2021-04-18 19:23:50.659406',X'37','Transaction - Get Treatment By Billing Account Id Transaction Parameter - RequestURL',1,X'5b7b226164646564223a207b7d7d5d',10,1),(38,'2021-04-18 19:24:09.373489',X'38','Transaction - Get Treatment By Billing Account Id Transaction Parameter - Authorization',1,X'5b7b226164646564223a207b7d7d5d',10,1),(39,'2021-04-18 19:50:05.402225',X'31','Transaction - Get Service Request By Account Id',1,X'5b7b226164646564223a207b7d7d5d',17,1),(40,'2021-04-18 19:50:48.563704',X'31','Transaction - Get Service Request By Account Id Transaction Parameter - RequestURL',1,X'5b7b226164646564223a207b7d7d5d',18,1),(41,'2021-04-18 19:51:06.685394',X'32','Transaction - Get Service Request By Account Id Transaction Parameter - Authorization',1,X'5b7b226164646564223a207b7d7d5d',18,1),(42,'2021-04-18 19:54:20.093993',X'32','Transaction - Get Activities By Service Request Id',1,X'5b7b226164646564223a207b7d7d5d',17,1),(43,'2021-04-18 19:56:00.500111',X'33','Transaction - Get Activities By Service Request Id Transaction Parameter - RequestURL',1,X'5b7b226164646564223a207b7d7d5d',18,1),(44,'2021-04-18 19:56:16.578120',X'34','Transaction - Get Activities By Service Request Id Transaction Parameter - Authorization',1,X'5b7b226164646564223a207b7d7d5d',18,1),(45,'2021-04-18 20:26:20.821104',X'33','Transaction - Get Account By Id',1,X'5b7b226164646564223a207b7d7d5d',17,1),(46,'2021-04-18 20:27:08.544541',X'35','Transaction - Get Account By Id Transaction Parameter - RequestURL',1,X'5b7b226164646564223a207b7d7d5d',18,1),(47,'2021-04-18 20:27:28.791783',X'36','Transaction - Get Account By Id Transaction Parameter - Authorization',1,X'5b7b226164646564223a207b7d7d5d',18,1),(48,'2021-04-18 20:28:50.773538',X'34','Transaction - Get Invoice By Id',1,X'5b7b226164646564223a207b7d7d5d',17,1),(49,'2021-04-18 20:29:05.181431',X'37','Transaction - Get Invoice By Id Transaction Parameter - RequestURL',1,X'5b7b226164646564223a207b7d7d5d',18,1),(50,'2021-04-18 20:29:22.545803',X'38','Transaction - Get Invoice By Id Transaction Parameter - Authorization',1,X'5b7b226164646564223a207b7d7d5d',18,1),(51,'2021-04-18 20:30:10.213116',X'35','Transaction - Get Order By Id',1,X'5b7b226164646564223a207b7d7d5d',17,1),(52,'2021-04-18 20:30:16.842174',X'36','Transaction - Get Asset By Id',1,X'5b7b226164646564223a207b7d7d5d',17,1),(53,'2021-04-18 20:30:35.563888',X'39','Transaction - Get Order By Id Transaction Parameter - RequestURL',1,X'5b7b226164646564223a207b7d7d5d',18,1),(54,'2021-04-18 20:30:49.642207',X'3130','Transaction - Get Order By Id Transaction Parameter - Authorization',1,X'5b7b226164646564223a207b7d7d5d',18,1),(55,'2021-04-18 20:32:11.084521',X'3131','Transaction - Get Asset By Id Transaction Parameter - RequestURL',1,X'5b7b226164646564223a207b7d7d5d',18,1),(56,'2021-04-18 20:32:23.736697',X'3132','Transaction - Get Asset By Id Transaction Parameter - Authorization',1,X'5b7b226164646564223a207b7d7d5d',18,1),(57,'2021-04-18 21:35:45.137999',X'31','Transaction - Get Activities By Account Id',1,X'5b7b226164646564223a207b7d7d5d',19,1),(58,'2021-04-18 21:36:39.333069',X'31','Transaction - Get Activities By Account Id Transaction Parameter - RequestURL',1,X'5b7b226164646564223a207b7d7d5d',20,1),(59,'2021-04-18 21:37:40.655066',X'32','Transaction - Get Activities By Account Id Transaction Parameter - Authorization',1,X'5b7b226164646564223a207b7d7d5d',20,1),(60,'2021-04-18 21:41:56.930030',X'32','Transaction - Get Account By Id',1,X'5b7b226164646564223a207b7d7d5d',19,1),(61,'2021-04-18 21:42:04.073447',X'33','Transaction - Get Asset By Id',1,X'5b7b226164646564223a207b7d7d5d',19,1),(62,'2021-04-18 21:42:15.977982',X'34','Transaction - Get Order By Id',1,X'5b7b226164646564223a207b7d7d5d',19,1),(63,'2021-04-18 21:42:24.316532',X'35','Transaction - Get Invoice By Id',1,X'5b7b226164646564223a207b7d7d5d',19,1),(64,'2021-04-18 21:42:54.993077',X'36','Transaction - Get Service Request By Id',1,X'5b7b226164646564223a207b7d7d5d',19,1),(65,'2021-04-18 21:46:24.875506',X'33','Transaction - Get Account By Id Transaction Parameter - RequestURL',1,X'5b7b226164646564223a207b7d7d5d',20,1),(66,'2021-04-18 21:46:41.996771',X'34','Transaction - Get Account By Id Transaction Parameter - Authorization',1,X'5b7b226164646564223a207b7d7d5d',20,1),(67,'2021-04-18 21:47:03.074001',X'35','Transaction - Get Order By Id Transaction Parameter - RequestURL',1,X'5b7b226164646564223a207b7d7d5d',20,1),(68,'2021-04-18 21:47:33.464204',X'36','Transaction - Get Order By Id Transaction Parameter - Authorization',1,X'5b7b226164646564223a207b7d7d5d',20,1),(69,'2021-04-18 21:48:42.643849',X'37','Transaction - Get Asset By Id Transaction Parameter - RequestURL',1,X'5b7b226164646564223a207b7d7d5d',20,1),(70,'2021-04-18 21:49:08.231842',X'38','Transaction - Get Asset By Id Transaction Parameter - Authorization',1,X'5b7b226164646564223a207b7d7d5d',20,1),(71,'2021-04-18 21:49:31.984495',X'39','Transaction - Get Invoice By Id Transaction Parameter - RequestURL',1,X'5b7b226164646564223a207b7d7d5d',20,1),(72,'2021-04-18 21:49:54.151146',X'3130','Transaction - Get Invoice By Id Transaction Parameter - Authorization',1,X'5b7b226164646564223a207b7d7d5d',20,1),(73,'2021-04-18 21:50:09.891229',X'3131','Transaction - Get Service Request By Id Transaction Parameter - RequestURL',1,X'5b7b226164646564223a207b7d7d5d',20,1),(74,'2021-04-18 21:50:28.968996',X'3132','Transaction - Get Service Request By Id Transaction Parameter - Authorization',1,X'5b7b226164646564223a207b7d7d5d',20,1),(75,'2021-04-18 22:16:07.630841',X'37','Transaction - Create Activity',1,X'5b7b226164646564223a207b7d7d5d',19,1),(76,'2021-04-18 22:17:03.856617',X'3133','Transaction - Create Activity Transaction Parameter - RequestURL',1,X'5b7b226164646564223a207b7d7d5d',20,1),(77,'2021-04-18 22:17:20.871292',X'3134','Transaction - Create Activity Transaction Parameter - Authorization',1,X'5b7b226164646564223a207b7d7d5d',20,1),(78,'2021-04-18 22:17:37.765962',X'38','Transaction - Update Activity By Id',1,X'5b7b226164646564223a207b7d7d5d',19,1),(79,'2021-04-18 22:18:24.440151',X'3135','Transaction - Update Activity By Id Transaction Parameter - RequestURL',1,X'5b7b226164646564223a207b7d7d5d',20,1),(80,'2021-04-18 22:18:39.342260',X'3136','Transaction - Update Activity By Id Transaction Parameter - Authorization',1,X'5b7b226164646564223a207b7d7d5d',20,1),(81,'2021-04-18 22:48:06.438341',X'37','Transaction - Create Service Request',1,X'5b7b226164646564223a207b7d7d5d',17,1),(82,'2021-04-18 22:48:15.174714',X'38','Transaction - Update Service Request By Id',1,X'5b7b226164646564223a207b7d7d5d',17,1),(83,'2021-04-18 22:49:25.299640',X'3133','Transaction - Create Service Request Transaction Parameter - RequestURL',1,X'5b7b226164646564223a207b7d7d5d',18,1),(84,'2021-04-18 22:49:44.547581',X'3134','Transaction - Create Service Request Transaction Parameter - Authorization',1,X'5b7b226164646564223a207b7d7d5d',18,1),(85,'2021-04-18 22:49:59.021450',X'3135','Transaction - Update Service Request By Id Transaction Parameter - RequestURL',1,X'5b7b226164646564223a207b7d7d5d',18,1),(86,'2021-04-18 22:50:09.530404',X'3136','Transaction - Update Service Request By Id Transaction Parameter - Authorization',1,X'5b7b226164646564223a207b7d7d5d',18,1);

INSERT INTO django_content_type(id,app_label,model) VALUES(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(7,'authtoken','token'),(8,'authtoken','tokenproxy'),(5,'contenttypes','contenttype'),(9,'oach_accounts_api','transaction'),(10,'oach_accounts_api','transactionparameter'),(19,'oach_activities_api','transaction'),(20,'oach_activities_api','transactionparameter'),(11,'oach_assets_api','transaction'),(12,'oach_assets_api','transactionparameter'),(15,'oach_invoices_api','transaction'),(16,'oach_invoices_api','transactionparameter'),(13,'oach_orders_api','transaction'),(14,'oach_orders_api','transactionparameter'),(17,'oach_service_requests_api','transaction'),(18,'oach_service_requests_api','transactionparameter'),(6,'sessions','session');

INSERT INTO django_migrations(id,app,name,applied) VALUES(1,'contenttypes','0001_initial','2021-04-16 20:03:50.763477'),(2,'auth','0001_initial','2021-04-16 20:03:50.898240'),(3,'admin','0001_initial','2021-04-16 20:03:51.266208'),(4,'admin','0002_logentry_remove_auto_add','2021-04-16 20:03:51.363204'),(5,'admin','0003_logentry_add_action_flag_choices','2021-04-16 20:03:51.373137'),(6,'contenttypes','0002_remove_content_type_name','2021-04-16 20:03:51.472145'),(7,'auth','0002_alter_permission_name_max_length','2021-04-16 20:03:51.540285'),(8,'auth','0003_alter_user_email_max_length','2021-04-16 20:03:51.563664'),(9,'auth','0004_alter_user_username_opts','2021-04-16 20:03:51.573536'),(10,'auth','0005_alter_user_last_login_null','2021-04-16 20:03:51.620148'),(11,'auth','0006_require_contenttypes_0002','2021-04-16 20:03:51.624554'),(12,'auth','0007_alter_validators_add_error_messages','2021-04-16 20:03:51.633970'),(13,'auth','0008_alter_user_username_max_length','2021-04-16 20:03:51.690096'),(14,'auth','0009_alter_user_last_name_max_length','2021-04-16 20:03:51.745484'),(15,'auth','0010_alter_group_name_max_length','2021-04-16 20:03:51.764189'),(16,'auth','0011_update_proxy_permissions','2021-04-16 20:03:51.773226'),(17,'auth','0012_alter_user_first_name_max_length','2021-04-16 20:03:51.830941'),(18,'sessions','0001_initial','2021-04-16 20:03:51.854462'),(19,'authtoken','0001_initial','2021-04-16 20:09:25.786026'),(20,'authtoken','0002_auto_20160226_1747','2021-04-16 20:09:25.898323'),(21,'authtoken','0003_tokenproxy','2021-04-16 20:09:25.903472'),(22,'oach_accounts_api','0001_initial','2021-04-16 20:43:58.861123'),(23,'oach_assets_api','0001_initial','2021-04-18 07:18:30.375740'),(24,'oach_orders_api','0001_initial','2021-04-18 15:46:53.669723'),(25,'oach_invoices_api','0001_initial','2021-04-18 17:26:09.186039'),(26,'oach_service_requests_api','0001_initial','2021-04-18 19:46:57.064660'),(27,'oach_service_requests_api','0002_auto_20210418_1947','2021-04-18 19:47:55.037309'),(28,'oach_activities_api','0001_initial','2021-04-18 21:31:20.343424');

INSERT INTO django_session(session_key,session_data,expire_date) VALUES('pzqdg4u9o5smxhkp24p2acd4fdc6tq27',X'2e654a78566a4d734f7769415152662d4674534549444177753366734e5a48684a3155425332705878333232544c6e52377a7a6e337a547974535f5872794c4f66457275774d7a7639626f48694d37636470416531652d6578743257654174385666744442627a336c315f56775f7734716a6272564767674168436f5770455552554c714d416f734361625171456257524a5168704935715549473543444653796330595143736b2d58374f6c4e79493a316c5947436b3a3964784d2d686a553335364233594369666c6c47352d70324772614a5a30506a6355466150634872374f63','2021-05-02 22:47:50.604394');

INSERT INTO oach_accounts_api_transaction(id,TransactionName) VALUES(1,'Get Account By Id'),(3,'Get Account Hierarchy By Id'),(4,'Get Treatment By Billing Account Id'),(2,'Update Account By Id');

INSERT INTO oach_accounts_api_transactionparameter(id,ParameterName,ParameterValue,TransactionName_id) VALUES(1,'RequestURL','http://172.18.0.1:8010/api/accounts/<pk>',1),(2,'Authorization','Token 2a19f90280b234059b1f58e5a4c7965db9900128',1),(3,'RequestURL','http://172.18.0.1:8010/api/accounts/<pk>',2),(4,'Authorization','Token 2a19f90280b234059b1f58e5a4c7965db9900128',2),(5,'RequestURL','http://172.18.0.1:8010/api/accounts/search/?RootAccountId=<pk>',3),(6,'Authorization','Token 2a19f90280b234059b1f58e5a4c7965db9900128',3),(7,'RequestURL','http://172.18.0.1:8010/api/treatments/search/',4),(8,'Authorization','Token 2a19f90280b234059b1f58e5a4c7965db9900128',4);

INSERT INTO oach_activities_api_transaction(id,TransactionName) VALUES(7,'Create Activity'),(2,'Get Account By Id'),(1,'Get Activities By Account Id'),(3,'Get Asset By Id'),(5,'Get Invoice By Id'),(4,'Get Order By Id'),(6,'Get Service Request By Id'),(8,'Update Activity By Id');

INSERT INTO oach_activities_api_transactionparameter(id,ParameterName,ParameterValue,TransactionName_id) VALUES(1,'RequestURL','http://172.18.0.1:8010/api/activities/search/',1),(2,'Authorization','Token 2a19f90280b234059b1f58e5a4c7965db9900128',1),(3,'RequestURL','http://172.18.0.1:8010/api/accounts/<pk>',2),(4,'Authorization','Token 2a19f90280b234059b1f58e5a4c7965db9900128',2),(5,'RequestURL','http://172.18.0.1:8020/api/orders/<pk>',4),(6,'Authorization','Token 512125d89105537b3ed038c29f54c2bc7a7812ad',4),(7,'RequestURL','http://172.18.0.1:8020/api/assets/<pk>',3),(8,'Authorization','Token 512125d89105537b3ed038c29f54c2bc7a7812ad',3),(9,'RequestURL','http://172.18.0.1:8010/api/invoices/<pk>',5),(10,'Authorization','Token 2a19f90280b234059b1f58e5a4c7965db9900128',5),(11,'RequestURL','http://172.18.0.1:8010/api/service_requests/<pk>',6),(12,'Authorization','Token 2a19f90280b234059b1f58e5a4c7965db9900128',6),(13,'RequestURL','http://172.18.0.1:8010/api/activities',7),(14,'Authorization','Token 2a19f90280b234059b1f58e5a4c7965db9900128',7),(15,'RequestURL','http://172.18.0.1:8010/api/activities/<pk>',8),(16,'Authorization','Token 2a19f90280b234059b1f58e5a4c7965db9900128',8);

INSERT INTO oach_assets_api_transaction(id,TransactionName) VALUES(1,'Get Assets By Account Id');

INSERT INTO oach_assets_api_transactionparameter(id,ParameterName,ParameterValue,TransactionName_id) VALUES(1,'RequestURL','http://172.18.0.1:8020/api/assets/search/',1),(2,'Authorization','Token 512125d89105537b3ed038c29f54c2bc7a7812ad',1);

INSERT INTO oach_invoices_api_transaction(id,TransactionName) VALUES(1,'Get Invoice By Billing Account Id'),(2,'Get Payments By Invoice Id');

INSERT INTO oach_invoices_api_transactionparameter(id,ParameterName,ParameterValue,TransactionName_id) VALUES(1,'RequestURL','http://172.18.0.1:8010/api/invoices/search/',1),(2,'Authorization','Token 2a19f90280b234059b1f58e5a4c7965db9900128',1),(3,'RequestURL','http://172.18.0.1:8010/api/payments/search/',2),(4,'Authorization','Token 2a19f90280b234059b1f58e5a4c7965db9900128',2);

INSERT INTO oach_orders_api_transaction(id,TransactionName) VALUES(2,'Get Order Items By Account Id'),(1,'Get Orders By Account Id');

INSERT INTO oach_orders_api_transactionparameter(id,ParameterName,ParameterValue,TransactionName_id) VALUES(1,'RequestURL','http://172.18.0.1:8020/api/orders/search/',1),(2,'Authorization','Token 512125d89105537b3ed038c29f54c2bc7a7812ad',1),(3,'RequestURL','http://172.18.0.1:8020/api/order_items/search/',2),(4,'Authorization','Token 512125d89105537b3ed038c29f54c2bc7a7812ad',2);

INSERT INTO oach_service_requests_api_transaction(id,TransactionName) VALUES(7,'Create Service Request'),(3,'Get Account By Id'),(2,'Get Activities By Service Request Id'),(6,'Get Asset By Id'),(4,'Get Invoice By Id'),(5,'Get Order By Id'),(1,'Get Service Request By Account Id'),(8,'Update Service Request By Id');
INSERT INTO oach_service_requests_api_transactionparameter(id,ParameterName,ParameterValue,TransactionName_id) VALUES(1,'RequestURL','http://172.18.0.1:8010/api/service_requests/search/',1),(2,'Authorization','Token 2a19f90280b234059b1f58e5a4c7965db9900128',1),(3,'RequestURL','http://172.18.0.1:8010/api/activities/search/',2),(4,'Authorization','Token 2a19f90280b234059b1f58e5a4c7965db9900128',2),(5,'RequestURL','http://172.18.0.1:8010/api/accounts/<pk>',3),(6,'Authorization','Token 2a19f90280b234059b1f58e5a4c7965db9900128',3),(7,'RequestURL','http://172.18.0.1:8010/api/invoices/<pk>',4),(8,'Authorization','Token 2a19f90280b234059b1f58e5a4c7965db9900128',4),(9,'RequestURL','http://172.18.0.1:8020/api/orders/<pk>',5),(10,'Authorization','Token 512125d89105537b3ed038c29f54c2bc7a7812ad',5),(11,'RequestURL','http://172.18.0.1:8020/api/assets/<pk>',6),(12,'Authorization','Token 512125d89105537b3ed038c29f54c2bc7a7812ad',6),(13,'RequestURL','http://172.18.0.1:8010/api/service_requests',7),(14,'Authorization','Token 2a19f90280b234059b1f58e5a4c7965db9900128',7),(15,'RequestURL','http://172.18.0.1:8010/api/service_requests/<pk>',8),(16,'Authorization','Token 2a19f90280b234059b1f58e5a4c7965db9900128',8);







/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
