/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50553
Source Host           : localhost:3306
Source Database       : dnsdb

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2017-12-06 15:46:37
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for address
-- ----------------------------
DROP TABLE IF EXISTS `address`;
CREATE TABLE `address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `create_user` varchar(45) NOT NULL,
  `update_user` varchar(45) NOT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  `addr_ip_id` char(39) NOT NULL,
  `agentid_id` varchar(45) NOT NULL,
  `domain_id` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `address_addr_ip_id_13ecfd66_fk_ipinfo_ipaddress` (`addr_ip_id`),
  KEY `address_agentid_id_a2d88f46_fk_agent_agentid` (`agentid_id`),
  KEY `address_domain_id_d9beb7d8_fk_second_domain_domain` (`domain_id`),
  CONSTRAINT `address_addr_ip_id_13ecfd66_fk_ipinfo_ipaddress` FOREIGN KEY (`addr_ip_id`) REFERENCES `ipinfo` (`ipaddress`),
  CONSTRAINT `address_agentid_id_a2d88f46_fk_agent_agentid` FOREIGN KEY (`agentid_id`) REFERENCES `agent` (`agentid`),
  CONSTRAINT `address_domain_id_d9beb7d8_fk_second_domain_domain` FOREIGN KEY (`domain_id`) REFERENCES `second_domain` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of address
-- ----------------------------
INSERT INTO `address` VALUES ('1', '2017-11-25 15:53:33', '2017-11-25 15:53:33', 'admin', 'admin', '', '11010011000010110000111010101011', 'HK171125', 'tiejiang.org');

-- ----------------------------
-- Table structure for agent
-- ----------------------------
DROP TABLE IF EXISTS `agent`;
CREATE TABLE `agent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `agt_ip` varchar(39) NOT NULL,
  `agentid` varchar(45) NOT NULL,
  `agt_version` varchar(5) NOT NULL,
  `agt_state` int(11) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `create_user` varchar(30) NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  `token` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `agt_ip` (`agt_ip`),
  UNIQUE KEY `agentid` (`agentid`),
  UNIQUE KEY `agent_agt_ip_agt_version_agentid_5a484843_uniq` (`agt_ip`,`agt_version`,`agentid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of agent
-- ----------------------------
INSERT INTO `agent` VALUES ('1', '11000000101010000000001001100101', 'HK171125', '1.0.1', '0', '2017-11-25 10:37:05', '2017-11-25 10:37:05', 'admin', 'admin', '', null);
INSERT INTO `agent` VALUES ('2', '11000011011100001010110011100000', 'USA171125', '1.0.1', '0', '2017-11-25 10:39:33', '2017-11-25 10:39:33', 'admin', 'admin', '', null);

-- ----------------------------
-- Table structure for alias
-- ----------------------------
DROP TABLE IF EXISTS `alias`;
CREATE TABLE `alias` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `old_ip` char(39) DEFAULT NULL,
  `start_ip` char(39) DEFAULT NULL,
  `end_ip` char(39) DEFAULT NULL,
  `new_ip` char(39) NOT NULL,
  `ipmask` char(39) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `create_user` varchar(30) NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  `agentid_id` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `alias_new_ip_agentid_id_e0e393c8_uniq` (`new_ip`,`agentid_id`),
  KEY `alias_agentid_id_d2b88179_fk_agent_agentid` (`agentid_id`),
  CONSTRAINT `alias_agentid_id_d2b88179_fk_agent_agentid` FOREIGN KEY (`agentid_id`) REFERENCES `agent` (`agentid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of alias
-- ----------------------------
INSERT INTO `alias` VALUES ('2', null, '11001010000111101111011001100100', '11001010000111101111011011001000', '11001010000111101111011001111010', null, '2017-11-25 11:24:55', '2017-11-25 11:24:55', 'admin', 'admin', '', 'HK171125');

-- ----------------------------
-- Table structure for area
-- ----------------------------
DROP TABLE IF EXISTS `area`;
CREATE TABLE `area` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `areaname` varchar(45) NOT NULL,
  `machine_room` varchar(45) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `create_user` varchar(45) NOT NULL,
  `update_user` varchar(45) NOT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  `agentid_id` varchar(45) NOT NULL,
  `responsible_name` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `area_agentid_id_areaname_cdc72845_uniq` (`agentid_id`,`areaname`),
  KEY `area_responsible_name_ccf6c7d8_fk_dnsuser_id` (`responsible_name`),
  CONSTRAINT `area_agentid_id_2e5c3dae_fk_agent_agentid` FOREIGN KEY (`agentid_id`) REFERENCES `agent` (`agentid`),
  CONSTRAINT `area_responsible_name_ccf6c7d8_fk_dnsuser_id` FOREIGN KEY (`responsible_name`) REFERENCES `dnsuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of area
-- ----------------------------
INSERT INTO `area` VALUES ('1', '香港', '中信机房', '2017-11-25 10:42:13', '2017-11-25 10:42:13', 'admin', 'admin', '', 'HK171125', '1');
INSERT INTO `area` VALUES ('2', '美国', '硅谷', '2017-11-25 10:43:20', '2017-11-25 10:43:20', 'admin', 'admin', '', 'USA171125', '1');

-- ----------------------------
-- Table structure for authtoken_token
-- ----------------------------
DROP TABLE IF EXISTS `authtoken_token`;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_dnsuser_id` FOREIGN KEY (`user_id`) REFERENCES `dnsuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of authtoken_token
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add group', '2', 'add_group');
INSERT INTO `auth_permission` VALUES ('5', 'Can change group', '2', 'change_group');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete group', '2', 'delete_group');
INSERT INTO `auth_permission` VALUES ('7', 'Can add permission', '3', 'add_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can change permission', '3', 'change_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete permission', '3', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('10', 'Can add content type', '4', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('11', 'Can change content type', '4', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete content type', '4', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('13', 'Can add session', '5', 'add_session');
INSERT INTO `auth_permission` VALUES ('14', 'Can change session', '5', 'change_session');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete session', '5', 'delete_session');
INSERT INTO `auth_permission` VALUES ('16', 'Can add address', '6', 'add_address');
INSERT INTO `auth_permission` VALUES ('17', 'Can change address', '6', 'change_address');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete address', '6', 'delete_address');
INSERT INTO `auth_permission` VALUES ('19', 'Can add 区域', '7', 'add_area');
INSERT INTO `auth_permission` VALUES ('20', 'Can change 区域', '7', 'change_area');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete 区域', '7', 'delete_area');
INSERT INTO `auth_permission` VALUES ('22', 'Can add dns user profile', '8', 'add_dnsuserprofile');
INSERT INTO `auth_permission` VALUES ('23', 'Can change dns user profile', '8', 'change_dnsuserprofile');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete dns user profile', '8', 'delete_dnsuserprofile');
INSERT INTO `auth_permission` VALUES ('25', 'Can add 别名', '9', 'add_cname');
INSERT INTO `auth_permission` VALUES ('26', 'Can change 别名', '9', 'change_cname');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete 别名', '9', 'delete_cname');
INSERT INTO `auth_permission` VALUES ('28', 'Can add heartbeat', '10', 'add_heartbeat');
INSERT INTO `auth_permission` VALUES ('29', 'Can change heartbeat', '10', 'change_heartbeat');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete heartbeat', '10', 'delete_heartbeat');
INSERT INTO `auth_permission` VALUES ('31', 'Can add 域名', '11', 'add_seconddomain');
INSERT INTO `auth_permission` VALUES ('32', 'Can change 域名', '11', 'change_seconddomain');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete 域名', '11', 'delete_seconddomain');
INSERT INTO `auth_permission` VALUES ('34', 'Can add agent', '12', 'add_agent');
INSERT INTO `auth_permission` VALUES ('35', 'Can change agent', '12', 'change_agent');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete agent', '12', 'delete_agent');
INSERT INTO `auth_permission` VALUES ('37', 'Can add alias', '13', 'add_alias');
INSERT INTO `auth_permission` VALUES ('38', 'Can change alias', '13', 'change_alias');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete alias', '13', 'delete_alias');
INSERT INTO `auth_permission` VALUES ('40', 'Can add host', '14', 'add_host');
INSERT INTO `auth_permission` VALUES ('41', 'Can change host', '14', 'change_host');
INSERT INTO `auth_permission` VALUES ('42', 'Can delete host', '14', 'delete_host');
INSERT INTO `auth_permission` VALUES ('43', 'Can add i pinfo', '15', 'add_ipinfo');
INSERT INTO `auth_permission` VALUES ('44', 'Can change i pinfo', '15', 'change_ipinfo');
INSERT INTO `auth_permission` VALUES ('45', 'Can delete i pinfo', '15', 'delete_ipinfo');
INSERT INTO `auth_permission` VALUES ('46', 'Can add local', '16', 'add_local');
INSERT INTO `auth_permission` VALUES ('47', 'Can change local', '16', 'change_local');
INSERT INTO `auth_permission` VALUES ('48', 'Can delete local', '16', 'delete_local');
INSERT INTO `auth_permission` VALUES ('49', 'Can add loginfo', '17', 'add_loginfo');
INSERT INTO `auth_permission` VALUES ('50', 'Can change loginfo', '17', 'change_loginfo');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete loginfo', '17', 'delete_loginfo');
INSERT INTO `auth_permission` VALUES ('52', 'Can add mx', '18', 'add_mx');
INSERT INTO `auth_permission` VALUES ('53', 'Can change mx', '18', 'change_mx');
INSERT INTO `auth_permission` VALUES ('54', 'Can delete mx', '18', 'delete_mx');
INSERT INTO `auth_permission` VALUES ('55', 'Can add ptr', '19', 'add_ptr');
INSERT INTO `auth_permission` VALUES ('56', 'Can change ptr', '19', 'change_ptr');
INSERT INTO `auth_permission` VALUES ('57', 'Can delete ptr', '19', 'delete_ptr');
INSERT INTO `auth_permission` VALUES ('58', 'Can add resolv', '20', 'add_resolv');
INSERT INTO `auth_permission` VALUES ('59', 'Can change resolv', '20', 'change_resolv');
INSERT INTO `auth_permission` VALUES ('60', 'Can delete resolv', '20', 'delete_resolv');
INSERT INTO `auth_permission` VALUES ('61', 'Can add server', '21', 'add_server');
INSERT INTO `auth_permission` VALUES ('62', 'Can change server', '21', 'change_server');
INSERT INTO `auth_permission` VALUES ('63', 'Can delete server', '21', 'delete_server');
INSERT INTO `auth_permission` VALUES ('64', 'Can add srv', '22', 'add_srv');
INSERT INTO `auth_permission` VALUES ('65', 'Can change srv', '22', 'change_srv');
INSERT INTO `auth_permission` VALUES ('66', 'Can delete srv', '22', 'delete_srv');
INSERT INTO `auth_permission` VALUES ('67', 'Can add top domain', '23', 'add_topdomain');
INSERT INTO `auth_permission` VALUES ('68', 'Can change top domain', '23', 'change_topdomain');
INSERT INTO `auth_permission` VALUES ('69', 'Can delete top domain', '23', 'delete_topdomain');
INSERT INTO `auth_permission` VALUES ('70', 'Can add txt', '24', 'add_txt');
INSERT INTO `auth_permission` VALUES ('71', 'Can change txt', '24', 'change_txt');
INSERT INTO `auth_permission` VALUES ('72', 'Can delete txt', '24', 'delete_txt');
INSERT INTO `auth_permission` VALUES ('73', 'Can add Token', '25', 'add_token');
INSERT INTO `auth_permission` VALUES ('74', 'Can change Token', '25', 'change_token');
INSERT INTO `auth_permission` VALUES ('75', 'Can delete Token', '25', 'delete_token');

-- ----------------------------
-- Table structure for cname
-- ----------------------------
DROP TABLE IF EXISTS `cname`;
CREATE TABLE `cname` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cname` varchar(45) NOT NULL,
  `ttl` smallint(6) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `create_user` varchar(30) NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  `agentid_id` varchar(45) NOT NULL,
  `domain_id` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cname_cname_domain_id_569c701a_uniq` (`cname`,`domain_id`),
  KEY `cname_agentid_id_8fb0087f_fk_agent_agentid` (`agentid_id`),
  KEY `cname_domain_id_48400291_fk_second_domain_domain` (`domain_id`),
  CONSTRAINT `cname_agentid_id_8fb0087f_fk_agent_agentid` FOREIGN KEY (`agentid_id`) REFERENCES `agent` (`agentid`),
  CONSTRAINT `cname_domain_id_48400291_fk_second_domain_domain` FOREIGN KEY (`domain_id`) REFERENCES `second_domain` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of cname
-- ----------------------------
INSERT INTO `cname` VALUES ('1', '111.fdff.com', '600', '2017-11-25 16:30:12', '2017-11-28 11:21:11', 'admin', 'admin', '', 'HK171125', 'chuyiwei.com');

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
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
  KEY `django_admin_log_user_id_c564eba6_fk_dnsuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_dnsuser_id` FOREIGN KEY (`user_id`) REFERENCES `dnsuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('6', 'address', 'address');
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('12', 'agent', 'agent');
INSERT INTO `django_content_type` VALUES ('13', 'alias', 'alias');
INSERT INTO `django_content_type` VALUES ('7', 'area', 'area');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('25', 'authtoken', 'token');
INSERT INTO `django_content_type` VALUES ('9', 'cname', 'cname');
INSERT INTO `django_content_type` VALUES ('4', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('10', 'heartbeat', 'heartbeat');
INSERT INTO `django_content_type` VALUES ('14', 'host', 'host');
INSERT INTO `django_content_type` VALUES ('15', 'ipinfo', 'ipinfo');
INSERT INTO `django_content_type` VALUES ('16', 'local', 'local');
INSERT INTO `django_content_type` VALUES ('17', 'loginfo', 'loginfo');
INSERT INTO `django_content_type` VALUES ('18', 'mx', 'mx');
INSERT INTO `django_content_type` VALUES ('19', 'ptr', 'ptr');
INSERT INTO `django_content_type` VALUES ('20', 'resolv', 'resolv');
INSERT INTO `django_content_type` VALUES ('11', 'seconddomain', 'seconddomain');
INSERT INTO `django_content_type` VALUES ('21', 'server', 'server');
INSERT INTO `django_content_type` VALUES ('5', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('22', 'srv', 'srv');
INSERT INTO `django_content_type` VALUES ('23', 'topdomain', 'topdomain');
INSERT INTO `django_content_type` VALUES ('24', 'txt', 'txt');
INSERT INTO `django_content_type` VALUES ('8', 'users', 'dnsuserprofile');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'seconddomain', '0001_initial', '2017-11-25 10:01:37');
INSERT INTO `django_migrations` VALUES ('2', 'agent', '0001_initial', '2017-11-25 10:01:37');
INSERT INTO `django_migrations` VALUES ('3', 'ipinfo', '0001_initial', '2017-11-25 10:01:38');
INSERT INTO `django_migrations` VALUES ('4', 'address', '0001_initial', '2017-11-25 10:01:39');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0001_initial', '2017-11-25 10:01:39');
INSERT INTO `django_migrations` VALUES ('6', 'contenttypes', '0002_remove_content_type_name', '2017-11-25 10:01:40');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0001_initial', '2017-11-25 10:01:42');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0002_alter_permission_name_max_length', '2017-11-25 10:01:42');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0003_alter_user_email_max_length', '2017-11-25 10:01:42');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0004_alter_user_username_opts', '2017-11-25 10:01:42');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0005_alter_user_last_login_null', '2017-11-25 10:01:42');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0006_require_contenttypes_0002', '2017-11-25 10:01:42');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0007_alter_validators_add_error_messages', '2017-11-25 10:01:42');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0008_alter_user_username_max_length', '2017-11-25 10:01:43');
INSERT INTO `django_migrations` VALUES ('15', 'users', '0001_initial', '2017-11-25 10:01:45');
INSERT INTO `django_migrations` VALUES ('16', 'admin', '0001_initial', '2017-11-25 10:01:45');
INSERT INTO `django_migrations` VALUES ('17', 'admin', '0002_logentry_remove_auto_add', '2017-11-25 10:01:45');
INSERT INTO `django_migrations` VALUES ('18', 'alias', '0001_initial', '2017-11-25 10:01:46');
INSERT INTO `django_migrations` VALUES ('19', 'area', '0001_initial', '2017-11-25 10:01:47');
INSERT INTO `django_migrations` VALUES ('20', 'authtoken', '0001_initial', '2017-11-25 10:01:48');
INSERT INTO `django_migrations` VALUES ('21', 'authtoken', '0002_auto_20160226_1747', '2017-11-25 10:01:48');
INSERT INTO `django_migrations` VALUES ('22', 'cname', '0001_initial', '2017-11-25 10:01:49');
INSERT INTO `django_migrations` VALUES ('23', 'heartbeat', '0001_initial', '2017-11-25 10:01:50');
INSERT INTO `django_migrations` VALUES ('24', 'host', '0001_initial', '2017-11-25 10:01:51');
INSERT INTO `django_migrations` VALUES ('25', 'local', '0001_initial', '2017-11-25 10:01:52');
INSERT INTO `django_migrations` VALUES ('26', 'loginfo', '0001_initial', '2017-11-25 10:01:52');
INSERT INTO `django_migrations` VALUES ('27', 'mx', '0001_initial', '2017-11-25 10:01:53');
INSERT INTO `django_migrations` VALUES ('28', 'ptr', '0001_initial', '2017-11-25 10:01:55');
INSERT INTO `django_migrations` VALUES ('29', 'resolv', '0001_initial', '2017-11-25 10:01:56');
INSERT INTO `django_migrations` VALUES ('30', 'server', '0001_initial', '2017-11-25 10:01:57');
INSERT INTO `django_migrations` VALUES ('31', 'sessions', '0001_initial', '2017-11-25 10:01:58');
INSERT INTO `django_migrations` VALUES ('32', 'srv', '0001_initial', '2017-11-25 10:01:59');
INSERT INTO `django_migrations` VALUES ('33', 'topdomain', '0001_initial', '2017-11-25 10:01:59');
INSERT INTO `django_migrations` VALUES ('34', 'txt', '0001_initial', '2017-11-25 10:02:00');
INSERT INTO `django_migrations` VALUES ('35', 'cname', '0002_auto_20171128_1124', '2017-11-28 11:24:27');
INSERT INTO `django_migrations` VALUES ('36', 'agent', '0002_agent_token', '2017-11-29 13:14:59');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('uhwv18kh0udhszsim1jf77jun9xt5tyd', 'YTM5NzZhYjZjYzlhZDY4YzUxM2ViMWY4YjE4ODRhYTdhNzU5NDM5MTp7Il9hdXRoX3VzZXJfaGFzaCI6ImU0NjRjMzNjY2M4YmFjOTdmZjUyYmZhNzAwYjUwOGJjMDBlMzM1MDUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJ1c2Vycy52aWV3cy5DdXN0b21CYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEifQ==', '2017-12-14 15:18:16');

-- ----------------------------
-- Table structure for dnsuser
-- ----------------------------
DROP TABLE IF EXISTS `dnsuser`;
CREATE TABLE `dnsuser` (
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
  `name` varchar(30) DEFAULT NULL,
  `qq` varchar(11) DEFAULT NULL,
  `mobile` varchar(11) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `permission` int(11) NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `remarks` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of dnsuser
-- ----------------------------
INSERT INTO `dnsuser` VALUES ('1', 'pbkdf2_sha256$36000$Ni6BGrtKeQio$oy1KVlVaRJ7wLjw7AHRtlPJru8WjmVC61YWU9h1wOY0=', '2017-11-30 15:18:15', '0', 'admin', '', '', '584071227@qq.com', '0', '1', '2017-11-25 10:25:38', null, null, '15821111719', '2017-11-25 10:25:38', '2017-11-25 10:25:38', '1', '', null);
INSERT INTO `dnsuser` VALUES ('2', 'pbkdf2_sha256$36000$s5Q6mEXYLDaS$qZrSMj6aAv3UICWJ2pzqQsfeRkdn2OdG8OrvkvK8eys=', null, '0', 'chuyiwei', '', '', 'df829475@163.com', '0', '1', '2017-11-25 10:46:35', null, null, '15821111718', '2017-11-25 10:46:35', '2017-11-25 10:46:35', '1', '', null);
INSERT INTO `dnsuser` VALUES ('3', 'pbkdf2_sha256$36000$EYbs6FlFbsmu$ONKecMCn6CatjCU1sHkiOEwyeBySGPA678ZsfW88050=', null, '1', 'dufei', '', '', '', '1', '1', '2017-11-27 13:27:58', null, null, '', '2017-11-27 13:27:59', '2017-11-27 13:27:59', '1', '', null);
INSERT INTO `dnsuser` VALUES ('4', 'pbkdf2_sha256$36000$1CFcpoftHrOv$j5KF6rdUjqXpXK+/OO2kXC5tphHLuiG2c5m6sLxAsgE=', null, '0', '111', '', '', '18621609334@qq.com', '0', '1', '2017-11-29 11:31:55', null, null, '15821111712', '2017-11-29 11:31:55', '2017-11-29 11:31:55', '1', '', null);
INSERT INTO `dnsuser` VALUES ('5', 'pbkdf2_sha256$36000$GzVLzbWqprWD$jKxfXtofhpb6g0239gt2966gTkxWNdms4Bkwc4nNT+M=', null, '0', '2222', '', '', '584071226@qq.com', '0', '1', '2017-11-30 13:37:07', null, null, '15821111713', '2017-11-30 13:37:07', '2017-11-30 13:37:07', '1', '', null);
INSERT INTO `dnsuser` VALUES ('6', 'pbkdf2_sha256$36000$Hmf4IysAtBA5$2RYYe2X61ZlAI/dZYKo17nz+HYtBxoprkjz0hxiVMIA=', null, '0', '3333', '', '', '584071223@qq.com', '0', '1', '2017-11-30 14:31:39', null, null, '15821211719', '2017-11-30 14:31:39', '2017-11-30 14:31:39', '1', '', null);

-- ----------------------------
-- Table structure for dnsuser_groups
-- ----------------------------
DROP TABLE IF EXISTS `dnsuser_groups`;
CREATE TABLE `dnsuser_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dnsuserprofile_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `dnsuser_groups_dnsuserprofile_id_group_id_dcd10f3e_uniq` (`dnsuserprofile_id`,`group_id`),
  KEY `dnsuser_groups_group_id_66781b39_fk_auth_group_id` (`group_id`),
  CONSTRAINT `dnsuser_groups_dnsuserprofile_id_5963748d_fk_dnsuser_id` FOREIGN KEY (`dnsuserprofile_id`) REFERENCES `dnsuser` (`id`),
  CONSTRAINT `dnsuser_groups_group_id_66781b39_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of dnsuser_groups
-- ----------------------------

-- ----------------------------
-- Table structure for dnsuser_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `dnsuser_user_permissions`;
CREATE TABLE `dnsuser_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dnsuserprofile_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `dnsuser_user_permissions_dnsuserprofile_id_permis_1866821c_uniq` (`dnsuserprofile_id`,`permission_id`),
  KEY `dnsuser_user_permiss_permission_id_f55f41cf_fk_auth_perm` (`permission_id`),
  CONSTRAINT `dnsuser_user_permiss_dnsuserprofile_id_759c2bf9_fk_dnsuser_i` FOREIGN KEY (`dnsuserprofile_id`) REFERENCES `dnsuser` (`id`),
  CONSTRAINT `dnsuser_user_permiss_permission_id_f55f41cf_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of dnsuser_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for heartbeat
-- ----------------------------
DROP TABLE IF EXISTS `heartbeat`;
CREATE TABLE `heartbeat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` int(11) NOT NULL,
  `state` int(11) NOT NULL,
  `agent_version` varchar(5) NOT NULL,
  `message` varchar(100) DEFAULT NULL,
  `agentid_id` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `heartbeat_agentid_id_90993566_fk_agent_agentid` (`agentid_id`),
  CONSTRAINT `heartbeat_agentid_id_90993566_fk_agent_agentid` FOREIGN KEY (`agentid_id`) REFERENCES `agent` (`agentid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of heartbeat
-- ----------------------------

-- ----------------------------
-- Table structure for host
-- ----------------------------
DROP TABLE IF EXISTS `host`;
CREATE TABLE `host` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ttl` int(11) NOT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `create_user` varchar(30) NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `agentid_id` varchar(45) NOT NULL,
  `domain_id` varchar(45) NOT NULL,
  `host_ip_id` char(39) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `host_host_ip_id_domain_id_agentid_id_897fdf4c_uniq` (`host_ip_id`,`domain_id`,`agentid_id`),
  KEY `host_agentid_id_d4b1f897_fk_agent_agentid` (`agentid_id`),
  KEY `host_domain_id_e8a707ec_fk_second_domain_domain` (`domain_id`),
  CONSTRAINT `host_agentid_id_d4b1f897_fk_agent_agentid` FOREIGN KEY (`agentid_id`) REFERENCES `agent` (`agentid`),
  CONSTRAINT `host_domain_id_e8a707ec_fk_second_domain_domain` FOREIGN KEY (`domain_id`) REFERENCES `second_domain` (`domain`),
  CONSTRAINT `host_host_ip_id_5ea7265e_fk_ipinfo_ipaddress` FOREIGN KEY (`host_ip_id`) REFERENCES `ipinfo` (`ipaddress`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of host
-- ----------------------------
INSERT INTO `host` VALUES ('2', '600', '', '2017-11-25 10:59:36', '2017-11-25 10:59:36', 'admin', 'admin', 'HK171125', 'haojob.cn', '11010011000101001111011000011110');
INSERT INTO `host` VALUES ('3', '600', '', '2017-11-25 10:59:58', '2017-11-25 10:59:58', 'admin', 'admin', 'USA171125', 'hulian.top', '11001010000100000010001001110000');

-- ----------------------------
-- Table structure for ipinfo
-- ----------------------------
DROP TABLE IF EXISTS `ipinfo`;
CREATE TABLE `ipinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ipaddress` char(39) NOT NULL,
  `reverse_ip` varchar(30) NOT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `create_user` varchar(30) NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `agentid_id` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ipaddress` (`ipaddress`),
  UNIQUE KEY `reverse_ip` (`reverse_ip`),
  KEY `ipinfo_agentid_id_d4437af5_fk_agent_agentid` (`agentid_id`),
  CONSTRAINT `ipinfo_agentid_id_d4437af5_fk_agent_agentid` FOREIGN KEY (`agentid_id`) REFERENCES `agent` (`agentid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ipinfo
-- ----------------------------
INSERT INTO `ipinfo` VALUES ('1', '11010011000010110000111010101011', '171.14.11.211.in-addr.arpa.', '', '2017-11-25 10:55:18', '2017-11-25 10:55:18', 'admin', 'admin', 'HK171125');
INSERT INTO `ipinfo` VALUES ('2', '11001010000100000010001001110000', '112.34.16.202.in-addr.arpa.', '', '2017-11-25 10:55:33', '2017-11-25 10:55:33', 'admin', 'admin', 'USA171125');
INSERT INTO `ipinfo` VALUES ('4', '11010011000101001111011000011110', '30.246.20.211.in-addr.arpa.', '', '2017-11-25 10:56:13', '2017-11-25 10:56:13', 'admin', 'admin', 'HK171125');

-- ----------------------------
-- Table structure for local
-- ----------------------------
DROP TABLE IF EXISTS `local`;
CREATE TABLE `local` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `remarks` varchar(45) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `create_user` varchar(30) NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `agentid_id` varchar(45) NOT NULL,
  `domain_id` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `local_agentid_id_7e3a54af_fk_agent_agentid` (`agentid_id`),
  KEY `local_domain_id_91a32995_fk_second_domain_domain` (`domain_id`),
  CONSTRAINT `local_agentid_id_7e3a54af_fk_agent_agentid` FOREIGN KEY (`agentid_id`) REFERENCES `agent` (`agentid`),
  CONSTRAINT `local_domain_id_91a32995_fk_second_domain_domain` FOREIGN KEY (`domain_id`) REFERENCES `second_domain` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of local
-- ----------------------------
INSERT INTO `local` VALUES ('2', '', '2017-11-25 11:25:37', '2017-11-25 11:25:37', 'admin', 'admin', 'HK171125', 'chuyiwei.com');

-- ----------------------------
-- Table structure for loginfo
-- ----------------------------
DROP TABLE IF EXISTS `loginfo`;
CREATE TABLE `loginfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` int(11) NOT NULL,
  `state` int(11) NOT NULL,
  `message` varchar(100) DEFAULT NULL,
  `agentid_id` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `loginfo_agentid_id_da06f1fb_fk_agent_agentid` (`agentid_id`),
  CONSTRAINT `loginfo_agentid_id_da06f1fb_fk_agent_agentid` FOREIGN KEY (`agentid_id`) REFERENCES `agent` (`agentid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of loginfo
-- ----------------------------

-- ----------------------------
-- Table structure for mx
-- ----------------------------
DROP TABLE IF EXISTS `mx`;
CREATE TABLE `mx` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mxDomain` varchar(45) NOT NULL,
  `priority` int(11) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `create_user` varchar(30) NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  `agentid_id` varchar(45) NOT NULL,
  `domain_id` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mx_mxDomain_domain_id_agentid_id_0cab3c55_uniq` (`mxDomain`,`domain_id`,`agentid_id`),
  KEY `mx_agentid_id_3ee5d272_fk_agent_agentid` (`agentid_id`),
  KEY `mx_domain_id_d89aba58_fk_second_domain_domain` (`domain_id`),
  CONSTRAINT `mx_agentid_id_3ee5d272_fk_agent_agentid` FOREIGN KEY (`agentid_id`) REFERENCES `agent` (`agentid`),
  CONSTRAINT `mx_domain_id_d89aba58_fk_second_domain_domain` FOREIGN KEY (`domain_id`) REFERENCES `second_domain` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mx
-- ----------------------------
INSERT INTO `mx` VALUES ('1', 'mx.chuyiwei.com', '10', '2017-11-25 11:26:24', '2017-11-25 11:26:24', 'admin', 'admin', '', 'HK171125', 'chuyiwei.com');

-- ----------------------------
-- Table structure for ptr
-- ----------------------------
DROP TABLE IF EXISTS `ptr`;
CREATE TABLE `ptr` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `create_user` varchar(30) NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  `agentid_id` varchar(45) NOT NULL,
  `domain_id` varchar(45) NOT NULL,
  `ptr_ip_id` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ptr_domain_id_agentid_id_b50a0a0d_uniq` (`domain_id`,`agentid_id`),
  KEY `ptr_agentid_id_07c91bd3_fk_agent_agentid` (`agentid_id`),
  KEY `ptr_ptr_ip_id_2c1f8178_fk_ipinfo_reverse_ip` (`ptr_ip_id`),
  CONSTRAINT `ptr_agentid_id_07c91bd3_fk_agent_agentid` FOREIGN KEY (`agentid_id`) REFERENCES `agent` (`agentid`),
  CONSTRAINT `ptr_domain_id_eefa67e0_fk_second_domain_domain` FOREIGN KEY (`domain_id`) REFERENCES `second_domain` (`domain`),
  CONSTRAINT `ptr_ptr_ip_id_2c1f8178_fk_ipinfo_reverse_ip` FOREIGN KEY (`ptr_ip_id`) REFERENCES `ipinfo` (`reverse_ip`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ptr
-- ----------------------------
INSERT INTO `ptr` VALUES ('1', '2017-11-25 11:27:00', '2017-11-25 11:27:00', 'admin', 'admin', '', 'USA171125', 'haojob.cn', '171.14.11.211.in-addr.arpa.');
INSERT INTO `ptr` VALUES ('2', '2017-11-25 11:27:18', '2017-11-25 11:27:18', 'admin', 'admin', '', 'HK171125', 'chuyiwei.com', '30.246.20.211.in-addr.arpa.');

-- ----------------------------
-- Table structure for resolv
-- ----------------------------
DROP TABLE IF EXISTS `resolv`;
CREATE TABLE `resolv` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `remarks` varchar(45) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `create_user` varchar(30) NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `agentid_id` varchar(45) NOT NULL,
  `resolv_ip_id` char(39) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `resolv_resolv_ip_id_agentid_id_ff442aca_uniq` (`resolv_ip_id`,`agentid_id`),
  KEY `resolv_agentid_id_ae11ba4c_fk_agent_agentid` (`agentid_id`),
  CONSTRAINT `resolv_agentid_id_ae11ba4c_fk_agent_agentid` FOREIGN KEY (`agentid_id`) REFERENCES `agent` (`agentid`),
  CONSTRAINT `resolv_resolv_ip_id_40b6dd34_fk_ipinfo_ipaddress` FOREIGN KEY (`resolv_ip_id`) REFERENCES `ipinfo` (`ipaddress`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of resolv
-- ----------------------------
INSERT INTO `resolv` VALUES ('1', '', '2017-11-25 11:27:40', '2017-11-25 11:27:40', 'admin', 'admin', 'HK171125', '11010011000101001111011000011110');
INSERT INTO `resolv` VALUES ('2', '', '2017-11-25 11:27:52', '2017-11-25 11:27:52', 'admin', 'admin', 'USA171125', '11001010000100000010001001110000');

-- ----------------------------
-- Table structure for second_domain
-- ----------------------------
DROP TABLE IF EXISTS `second_domain`;
CREATE TABLE `second_domain` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(45) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `create_user` varchar(30) NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `domain` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of second_domain
-- ----------------------------
INSERT INTO `second_domain` VALUES ('1', 'tiejiang.org', '2017-11-25 10:49:40', '2017-11-25 10:49:40', 'admin', 'admin', '');
INSERT INTO `second_domain` VALUES ('2', 'chuyiwei.com', '2017-11-25 10:49:54', '2017-11-25 10:49:54', 'admin', 'admin', '');
INSERT INTO `second_domain` VALUES ('3', 'haojob.cn', '2017-11-25 10:50:03', '2017-11-25 10:50:03', 'admin', 'admin', '');
INSERT INTO `second_domain` VALUES ('4', 'hulian.top', '2017-11-25 10:50:38', '2017-11-25 10:50:38', 'admin', 'admin', '');

-- ----------------------------
-- Table structure for server
-- ----------------------------
DROP TABLE IF EXISTS `server`;
CREATE TABLE `server` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nameserver_port` int(11) NOT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `create_user` varchar(30) NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `agentid_id` varchar(45) NOT NULL,
  `domain_id` varchar(45) DEFAULT NULL,
  `namereverse_ip_id` varchar(30) DEFAULT NULL,
  `nameserver_ip_id` char(39) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `server_namereverse_ip_id_agentid_id_a2b98936_uniq` (`namereverse_ip_id`,`agentid_id`),
  KEY `server_agentid_id_50c8e320_fk_agent_agentid` (`agentid_id`),
  KEY `server_domain_id_43f2d1b2_fk_second_domain_domain` (`domain_id`),
  KEY `server_nameserver_ip_id_812ede81_fk_ipinfo_ipaddress` (`nameserver_ip_id`),
  CONSTRAINT `server_agentid_id_50c8e320_fk_agent_agentid` FOREIGN KEY (`agentid_id`) REFERENCES `agent` (`agentid`),
  CONSTRAINT `server_domain_id_43f2d1b2_fk_second_domain_domain` FOREIGN KEY (`domain_id`) REFERENCES `second_domain` (`domain`),
  CONSTRAINT `server_namereverse_ip_id_664cc3ae_fk_ipinfo_reverse_ip` FOREIGN KEY (`namereverse_ip_id`) REFERENCES `ipinfo` (`reverse_ip`),
  CONSTRAINT `server_nameserver_ip_id_812ede81_fk_ipinfo_ipaddress` FOREIGN KEY (`nameserver_ip_id`) REFERENCES `ipinfo` (`ipaddress`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of server
-- ----------------------------
INSERT INTO `server` VALUES ('2', '53', '', '2017-11-25 11:28:38', '2017-11-25 11:28:38', 'admin', 'admin', 'HK171125', 'chuyiwei.com', null, '11010011000101001111011000011110');

-- ----------------------------
-- Table structure for srv
-- ----------------------------
DROP TABLE IF EXISTS `srv`;
CREATE TABLE `srv` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `srv_domain` varchar(45) NOT NULL,
  `srv_port` int(11) NOT NULL,
  `priority` int(11) NOT NULL,
  `weight` int(11) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `create_user` varchar(30) NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  `agentid_id` varchar(45) NOT NULL,
  `domain_id` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `srv_srv_domain_agentid_id_6c92d3db_uniq` (`srv_domain`,`agentid_id`),
  KEY `srv_agentid_id_80ee68ba_fk_agent_agentid` (`agentid_id`),
  KEY `srv_domain_id_6b36e952_fk_second_domain_domain` (`domain_id`),
  CONSTRAINT `srv_agentid_id_80ee68ba_fk_agent_agentid` FOREIGN KEY (`agentid_id`) REFERENCES `agent` (`agentid`),
  CONSTRAINT `srv_domain_id_6b36e952_fk_second_domain_domain` FOREIGN KEY (`domain_id`) REFERENCES `second_domain` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of srv
-- ----------------------------
INSERT INTO `srv` VALUES ('1', 'www.chuyiwei.com', '0', '10', '10', '2017-11-25 11:34:48', '2017-11-25 11:34:48', 'admin', 'admin', '', 'HK171125', 'chuyiwei.com');

-- ----------------------------
-- Table structure for topdomain
-- ----------------------------
DROP TABLE IF EXISTS `topdomain`;
CREATE TABLE `topdomain` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `top_domain` varchar(45) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `create_user` varchar(30) NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `top_domain` (`top_domain`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of topdomain
-- ----------------------------
INSERT INTO `topdomain` VALUES ('1', '.cn', '2017-11-25 10:48:58', '2017-11-25 10:48:58', 'admin', 'admin', '');
INSERT INTO `topdomain` VALUES ('2', '.com', '2017-11-25 10:49:05', '2017-11-25 10:49:05', 'admin', 'admin', '');
INSERT INTO `topdomain` VALUES ('3', '.cc', '2017-11-25 10:49:09', '2017-11-25 10:49:09', 'admin', 'admin', '');
INSERT INTO `topdomain` VALUES ('4', '.org', '2017-11-25 10:49:15', '2017-11-25 10:49:15', 'admin', 'admin', '');
INSERT INTO `topdomain` VALUES ('5', '.top', '2017-11-25 10:49:18', '2017-11-25 10:49:18', 'admin', 'admin', '');

-- ----------------------------
-- Table structure for txt
-- ----------------------------
DROP TABLE IF EXISTS `txt`;
CREATE TABLE `txt` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `create_user` varchar(30) NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  `agentid_id` varchar(45) NOT NULL,
  `domain_id` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `txt_domain_id_agentid_id_b7f66082_uniq` (`domain_id`,`agentid_id`),
  KEY `txt_agentid_id_727d5d1b_fk_agent_agentid` (`agentid_id`),
  CONSTRAINT `txt_agentid_id_727d5d1b_fk_agent_agentid` FOREIGN KEY (`agentid_id`) REFERENCES `agent` (`agentid`),
  CONSTRAINT `txt_domain_id_3368babb_fk_second_domain_domain` FOREIGN KEY (`domain_id`) REFERENCES `second_domain` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of txt
-- ----------------------------
INSERT INTO `txt` VALUES ('1', 'v=spf1 include:aspmx.googlail. ~all', '2017-11-25 13:22:11', '2017-11-25 13:22:11', 'admin', 'admin', '', 'HK171125', 'chuyiwei.com');
INSERT INTO `txt` VALUES ('2', 'contact: jvnhvg@ml.tc', '2017-11-25 13:22:28', '2017-11-25 13:22:28', 'admin', 'admin', '', 'USA171125', 'haojob.cn');
SET FOREIGN_KEY_CHECKS=1;
