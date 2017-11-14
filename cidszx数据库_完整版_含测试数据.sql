/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50558
Source Host           : localhost:3306
Source Database       : cidszx

Target Server Type    : MYSQL
Target Server Version : 50558
File Encoding         : 65001

Date: 2017-11-13 14:38:38
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for address
-- ----------------------------
DROP TABLE IF EXISTS `address`;
CREATE TABLE `address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(45) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `create_user` varchar(30) NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  `addr_ip_id` char(39) NOT NULL,
  `area_name_id` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `address_addr_ip_id_area_name_id_e386f3eb_uniq` (`addr_ip_id`,`area_name_id`),
  KEY `address_area_name_id_7facd8c0_fk_area_name` (`area_name_id`),
  CONSTRAINT `address_addr_ip_id_13ecfd66_fk_ipinfo_ipaddress` FOREIGN KEY (`addr_ip_id`) REFERENCES `ipinfo` (`ipaddress`),
  CONSTRAINT `address_area_name_id_7facd8c0_fk_area_name` FOREIGN KEY (`area_name_id`) REFERENCES `area` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of address
-- ----------------------------
INSERT INTO `address` VALUES ('1', 'address.domain.com', '2017-11-11 08:57:01', '2017-11-11 08:57:01', 'now user', 'now user', '', '1.1.1.1', 'cn');
INSERT INTO `address` VALUES ('2', 'address.domain.com', '2017-11-11 08:57:08', '2017-11-11 08:57:08', 'now user', 'now user', '', '1.1.1.2', 'cn');
INSERT INTO `address` VALUES ('3', 'address.domain.com', '2017-11-11 08:57:11', '2017-11-11 08:57:11', 'now user', 'now user', '', '1.1.1.2', 'us');

-- ----------------------------
-- Table structure for agent
-- ----------------------------
DROP TABLE IF EXISTS `agent`;
CREATE TABLE `agent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `agt_ip` char(39) NOT NULL,
  `agt_version` int(11) NOT NULL,
  `agt_states` int(11) NOT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `create_user` varchar(30) NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `area_name_id` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `agent_agt_ip_area_name_id_4cc34755_uniq` (`agt_ip`,`area_name_id`),
  KEY `agent_area_name_id_1a4c2b66_fk_area_name` (`area_name_id`),
  CONSTRAINT `agent_area_name_id_1a4c2b66_fk_area_name` FOREIGN KEY (`area_name_id`) REFERENCES `area` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of agent
-- ----------------------------
INSERT INTO `agent` VALUES ('1', '190.0.0.1', '1', '0', '', '2017-11-11 08:50:52', '2017-11-11 08:50:52', 'now user', 'now user', 'cn');
INSERT INTO `agent` VALUES ('2', '190.0.0.2', '1', '1', '', '2017-11-11 08:51:24', '2017-11-11 08:51:24', 'now user', 'now user', 'cn');
INSERT INTO `agent` VALUES ('3', '190.0.0.2', '1', '1', '', '2017-11-11 08:51:42', '2017-11-11 08:51:42', 'now user', 'now user', 'us');

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
  `ipmask` char(39) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `create_user` varchar(30) NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  `area_name_id` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `alias_new_ip_area_name_id_74bb4f15_uniq` (`new_ip`,`area_name_id`),
  KEY `alias_area_name_id_a5e30aa6_fk_area_name` (`area_name_id`),
  CONSTRAINT `alias_area_name_id_a5e30aa6_fk_area_name` FOREIGN KEY (`area_name_id`) REFERENCES `area` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of alias
-- ----------------------------
INSERT INTO `alias` VALUES ('1', '1.1.1.1', null, null, '2.2.2.2', '255.255.255.0', '2017-11-11 09:10:16', '2017-11-11 09:10:16', 'now user', 'now user', '', 'cn');
INSERT INTO `alias` VALUES ('2', '1.1.1.1', null, null, '2.2.2.1', '255.255.255.0', '2017-11-11 09:10:45', '2017-11-11 09:10:45', 'now user', 'now user', '', 'cn');

-- ----------------------------
-- Table structure for area
-- ----------------------------
DROP TABLE IF EXISTS `area`;
CREATE TABLE `area` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  `fullname` varchar(45) NOT NULL,
  `machine_name` varchar(45) NOT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `create_user` varchar(30) NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `responsible_id` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `fullname` (`fullname`),
  UNIQUE KEY `machine_name` (`machine_name`),
  KEY `area_responsible_id_cb3192c0_fk_dnsuser_username` (`responsible_id`),
  CONSTRAINT `area_responsible_id_cb3192c0_fk_dnsuser_username` FOREIGN KEY (`responsible_id`) REFERENCES `dnsuser` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of area
-- ----------------------------
INSERT INTO `area` VALUES ('1', 'cn', '中国', '湖北', '', '2017-11-11 08:50:01', '2017-11-11 08:50:01', 'now user', 'now user', '用户1');
INSERT INTO `area` VALUES ('2', 'us', '美国', '洛杉矶', '', '2017-11-11 08:50:26', '2017-11-11 08:50:26', 'now user', 'now user', '用户2');
INSERT INTO `area` VALUES ('3', 'uk', '英国', '伦敦', '', '2017-11-11 08:50:37', '2017-11-11 08:50:37', 'now user', 'now user', '用户2');

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
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add address', '7', 'add_address');
INSERT INTO `auth_permission` VALUES ('20', 'Can change address', '7', 'change_address');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete address', '7', 'delete_address');
INSERT INTO `auth_permission` VALUES ('22', 'Can add heartbeat', '8', 'add_heartbeat');
INSERT INTO `auth_permission` VALUES ('23', 'Can change heartbeat', '8', 'change_heartbeat');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete heartbeat', '8', 'delete_heartbeat');
INSERT INTO `auth_permission` VALUES ('25', 'Can add dns user', '9', 'add_dnsuser');
INSERT INTO `auth_permission` VALUES ('26', 'Can change dns user', '9', 'change_dnsuser');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete dns user', '9', 'delete_dnsuser');
INSERT INTO `auth_permission` VALUES ('28', 'Can add srv', '10', 'add_srv');
INSERT INTO `auth_permission` VALUES ('29', 'Can change srv', '10', 'change_srv');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete srv', '10', 'delete_srv');
INSERT INTO `auth_permission` VALUES ('31', 'Can add mx', '11', 'add_mx');
INSERT INTO `auth_permission` VALUES ('32', 'Can change mx', '11', 'change_mx');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete mx', '11', 'delete_mx');
INSERT INTO `auth_permission` VALUES ('34', 'Can add alias', '12', 'add_alias');
INSERT INTO `auth_permission` VALUES ('35', 'Can change alias', '12', 'change_alias');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete alias', '12', 'delete_alias');
INSERT INTO `auth_permission` VALUES ('37', 'Can add txt', '13', 'add_txt');
INSERT INTO `auth_permission` VALUES ('38', 'Can change txt', '13', 'change_txt');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete txt', '13', 'delete_txt');
INSERT INTO `auth_permission` VALUES ('40', 'Can add top domain', '14', 'add_topdomain');
INSERT INTO `auth_permission` VALUES ('41', 'Can change top domain', '14', 'change_topdomain');
INSERT INTO `auth_permission` VALUES ('42', 'Can delete top domain', '14', 'delete_topdomain');
INSERT INTO `auth_permission` VALUES ('43', 'Can add local', '15', 'add_local');
INSERT INTO `auth_permission` VALUES ('44', 'Can change local', '15', 'change_local');
INSERT INTO `auth_permission` VALUES ('45', 'Can delete local', '15', 'delete_local');
INSERT INTO `auth_permission` VALUES ('46', 'Can add agent', '16', 'add_agent');
INSERT INTO `auth_permission` VALUES ('47', 'Can change agent', '16', 'change_agent');
INSERT INTO `auth_permission` VALUES ('48', 'Can delete agent', '16', 'delete_agent');
INSERT INTO `auth_permission` VALUES ('49', 'Can add resolv', '17', 'add_resolv');
INSERT INTO `auth_permission` VALUES ('50', 'Can change resolv', '17', 'change_resolv');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete resolv', '17', 'delete_resolv');
INSERT INTO `auth_permission` VALUES ('52', 'Can add loginfo', '18', 'add_loginfo');
INSERT INTO `auth_permission` VALUES ('53', 'Can change loginfo', '18', 'change_loginfo');
INSERT INTO `auth_permission` VALUES ('54', 'Can delete loginfo', '18', 'delete_loginfo');
INSERT INTO `auth_permission` VALUES ('55', 'Can add area', '19', 'add_area');
INSERT INTO `auth_permission` VALUES ('56', 'Can change area', '19', 'change_area');
INSERT INTO `auth_permission` VALUES ('57', 'Can delete area', '19', 'delete_area');
INSERT INTO `auth_permission` VALUES ('58', 'Can add cname', '20', 'add_cname');
INSERT INTO `auth_permission` VALUES ('59', 'Can change cname', '20', 'change_cname');
INSERT INTO `auth_permission` VALUES ('60', 'Can delete cname', '20', 'delete_cname');
INSERT INTO `auth_permission` VALUES ('61', 'Can add i pinfo', '21', 'add_ipinfo');
INSERT INTO `auth_permission` VALUES ('62', 'Can change i pinfo', '21', 'change_ipinfo');
INSERT INTO `auth_permission` VALUES ('63', 'Can delete i pinfo', '21', 'delete_ipinfo');
INSERT INTO `auth_permission` VALUES ('64', 'Can add host', '22', 'add_host');
INSERT INTO `auth_permission` VALUES ('65', 'Can change host', '22', 'change_host');
INSERT INTO `auth_permission` VALUES ('66', 'Can delete host', '22', 'delete_host');
INSERT INTO `auth_permission` VALUES ('67', 'Can add second domain', '23', 'add_seconddomain');
INSERT INTO `auth_permission` VALUES ('68', 'Can change second domain', '23', 'change_seconddomain');
INSERT INTO `auth_permission` VALUES ('69', 'Can delete second domain', '23', 'delete_seconddomain');
INSERT INTO `auth_permission` VALUES ('70', 'Can add ptr', '24', 'add_ptr');
INSERT INTO `auth_permission` VALUES ('71', 'Can change ptr', '24', 'change_ptr');
INSERT INTO `auth_permission` VALUES ('72', 'Can delete ptr', '24', 'delete_ptr');
INSERT INTO `auth_permission` VALUES ('73', 'Can add server', '25', 'add_server');
INSERT INTO `auth_permission` VALUES ('74', 'Can change server', '25', 'change_server');
INSERT INTO `auth_permission` VALUES ('75', 'Can delete server', '25', 'delete_server');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$36000$SrHKvd8jiaoG$MMyYskBua4O3l6Tn1V9l8rBgjfm742KqXMgOGWcFELU=', '2017-11-11 08:49:12', '1', 'admin', '', '', '', '1', '1', '2017-11-11 08:46:58');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for cname
-- ----------------------------
DROP TABLE IF EXISTS `cname`;
CREATE TABLE `cname` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cname` varchar(100) NOT NULL,
  `ttl` int(11) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `create_user` varchar(30) NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  `area_name_id` varchar(10) NOT NULL,
  `domain_id` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cname_cname_area_name_id_80c552f6_uniq` (`cname`,`area_name_id`),
  KEY `cname_area_name_id_1f381dca_fk_area_name` (`area_name_id`),
  KEY `cname_domain_id_48400291_fk_second_domain_domain` (`domain_id`),
  CONSTRAINT `cname_area_name_id_1f381dca_fk_area_name` FOREIGN KEY (`area_name_id`) REFERENCES `area` (`name`),
  CONSTRAINT `cname_domain_id_48400291_fk_second_domain_domain` FOREIGN KEY (`domain_id`) REFERENCES `second_domain` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of cname
-- ----------------------------
INSERT INTO `cname` VALUES ('1', 'cname.qq.com', '10', '2017-11-11 09:07:22', '2017-11-11 09:07:22', 'now user', 'now user', '', 'cn', 'www.cn.com');
INSERT INTO `cname` VALUES ('3', 'cname.qq.com', '10', '2017-11-11 09:10:04', '2017-11-11 09:10:04', 'now user', 'now user', '', 'us', 'www.cn.com');

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
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
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
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('7', 'dnsmasq', 'address');
INSERT INTO `django_content_type` VALUES ('16', 'dnsmasq', 'agent');
INSERT INTO `django_content_type` VALUES ('12', 'dnsmasq', 'alias');
INSERT INTO `django_content_type` VALUES ('19', 'dnsmasq', 'area');
INSERT INTO `django_content_type` VALUES ('20', 'dnsmasq', 'cname');
INSERT INTO `django_content_type` VALUES ('9', 'dnsmasq', 'dnsuser');
INSERT INTO `django_content_type` VALUES ('8', 'dnsmasq', 'heartbeat');
INSERT INTO `django_content_type` VALUES ('22', 'dnsmasq', 'host');
INSERT INTO `django_content_type` VALUES ('21', 'dnsmasq', 'ipinfo');
INSERT INTO `django_content_type` VALUES ('15', 'dnsmasq', 'local');
INSERT INTO `django_content_type` VALUES ('18', 'dnsmasq', 'loginfo');
INSERT INTO `django_content_type` VALUES ('11', 'dnsmasq', 'mx');
INSERT INTO `django_content_type` VALUES ('24', 'dnsmasq', 'ptr');
INSERT INTO `django_content_type` VALUES ('17', 'dnsmasq', 'resolv');
INSERT INTO `django_content_type` VALUES ('23', 'dnsmasq', 'seconddomain');
INSERT INTO `django_content_type` VALUES ('25', 'dnsmasq', 'server');
INSERT INTO `django_content_type` VALUES ('10', 'dnsmasq', 'srv');
INSERT INTO `django_content_type` VALUES ('14', 'dnsmasq', 'topdomain');
INSERT INTO `django_content_type` VALUES ('13', 'dnsmasq', 'txt');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

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
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2017-11-11 08:42:48');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2017-11-11 08:42:51');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2017-11-11 08:42:52');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2017-11-11 08:42:52');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2017-11-11 08:42:53');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2017-11-11 08:42:53');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2017-11-11 08:42:53');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2017-11-11 08:42:53');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2017-11-11 08:42:53');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2017-11-11 08:42:53');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2017-11-11 08:42:53');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0008_alter_user_username_max_length', '2017-11-11 08:42:54');
INSERT INTO `django_migrations` VALUES ('13', 'dnsmasq', '0001_initial', '2017-11-11 08:43:05');
INSERT INTO `django_migrations` VALUES ('14', 'sessions', '0001_initial', '2017-11-11 08:43:06');
INSERT INTO `django_migrations` VALUES ('15', 'dnsmasq', '0002_auto_20171111_1709', '2017-11-11 09:09:55');
INSERT INTO `django_migrations` VALUES ('16', 'dnsmasq', '0003_auto_20171111_1714', '2017-11-11 09:15:37');

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
INSERT INTO `django_session` VALUES ('8enwepboe28f2f93biba1carnh6cz63e', 'MWMzZjZmOTQzMzc4MzI0YjQ0ZjA3MDA0Y2QzNjFjMjg2OTkwNjM4NDp7Il9hdXRoX3VzZXJfaGFzaCI6ImQwOTEyOTQ3YTczODAwZWFmYTdiYjBjM2VjNDE5ZmJlYjBiNDAzZjAiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2017-11-25 08:49:12');

-- ----------------------------
-- Table structure for dnsuser
-- ----------------------------
DROP TABLE IF EXISTS `dnsuser`;
CREATE TABLE `dnsuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `permission` int(11) NOT NULL,
  `email` varchar(30) NOT NULL,
  `qq` varchar(11) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of dnsuser
-- ----------------------------
INSERT INTO `dnsuser` VALUES ('1', '用户1', '0', 'test1@qq.com', '1111', '11111111111', '2017-11-11 08:49:31', '2017-11-11 08:49:31', 'now user', 'sadfasdf');
INSERT INTO `dnsuser` VALUES ('2', '用户2', '1', 'test2@qq.com', '222', '222222', '2017-11-11 08:49:48', '2017-11-11 08:49:48', 'now user', 'sadfasdf');

-- ----------------------------
-- Table structure for heartbeat
-- ----------------------------
DROP TABLE IF EXISTS `heartbeat`;
CREATE TABLE `heartbeat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` int(11) NOT NULL,
  `state` int(11) NOT NULL,
  `agent_ip` char(39) NOT NULL,
  `message` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Heartbeat_time_ff964635_uniq` (`time`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of heartbeat
-- ----------------------------
INSERT INTO `heartbeat` VALUES ('1', '23452345', '0', '3.3.3.5', '');

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
  `area_name_id` varchar(10) NOT NULL,
  `domain_id` varchar(45) NOT NULL,
  `host_ip_id` char(39) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `host_host_ip_id_domain_id_area_name_id_156f5c91_uniq` (`host_ip_id`,`domain_id`,`area_name_id`),
  KEY `host_area_name_id_754b253f_fk_area_name` (`area_name_id`),
  KEY `host_domain_id_e8a707ec_fk_second_domain_domain` (`domain_id`),
  CONSTRAINT `host_area_name_id_754b253f_fk_area_name` FOREIGN KEY (`area_name_id`) REFERENCES `area` (`name`),
  CONSTRAINT `host_domain_id_e8a707ec_fk_second_domain_domain` FOREIGN KEY (`domain_id`) REFERENCES `second_domain` (`domain`),
  CONSTRAINT `host_host_ip_id_5ea7265e_fk_ipinfo_ipaddress` FOREIGN KEY (`host_ip_id`) REFERENCES `ipinfo` (`ipaddress`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of host
-- ----------------------------
INSERT INTO `host` VALUES ('1', '600', '', '2017-11-11 08:56:08', '2017-11-11 08:56:08', 'now user', 'now user', 'cn', 'www.cn.com', '1.1.1.1');
INSERT INTO `host` VALUES ('2', '600', '', '2017-11-11 08:56:12', '2017-11-11 08:56:12', 'now user', 'now user', 'cn', 'www.cn.com', '1.1.1.2');
INSERT INTO `host` VALUES ('3', '600', '', '2017-11-11 08:56:17', '2017-11-11 08:56:17', 'now user', 'now user', 'us', 'www.cn.com', '1.1.1.1');
INSERT INTO `host` VALUES ('4', '600', '', '2017-11-11 08:56:21', '2017-11-11 08:56:21', 'now user', 'now user', 'us', 'www.uk.com', '1.1.1.1');

-- ----------------------------
-- Table structure for ipinfo
-- ----------------------------
DROP TABLE IF EXISTS `ipinfo`;
CREATE TABLE `ipinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ipaddress` char(39) NOT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `create_user` varchar(30) NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `area_name_id` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ipaddress` (`ipaddress`),
  KEY `ipinfo_area_name_id_d2c3e8bd_fk_area_name` (`area_name_id`),
  CONSTRAINT `ipinfo_area_name_id_d2c3e8bd_fk_area_name` FOREIGN KEY (`area_name_id`) REFERENCES `area` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ipinfo
-- ----------------------------
INSERT INTO `ipinfo` VALUES ('1', '1.1.1.1', '', '2017-11-11 08:51:55', '2017-11-11 08:51:55', 'now user', 'now user', 'cn');
INSERT INTO `ipinfo` VALUES ('2', '1.1.1.2', '', '2017-11-11 08:52:11', '2017-11-11 08:52:11', 'now user', 'now user', 'us');

-- ----------------------------
-- Table structure for local
-- ----------------------------
DROP TABLE IF EXISTS `local`;
CREATE TABLE `local` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(45) NOT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `create_user` varchar(30) NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `area_name_id` varchar(10) NOT NULL,
  `ipaddress_id` char(39) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `local_ipaddress_id_area_name_id_2e37d91a_uniq` (`ipaddress_id`,`area_name_id`),
  KEY `local_area_name_id_8a1a98fd_fk_area_name` (`area_name_id`),
  CONSTRAINT `local_area_name_id_8a1a98fd_fk_area_name` FOREIGN KEY (`area_name_id`) REFERENCES `area` (`name`),
  CONSTRAINT `local_ipaddress_id_50d8333f_fk_ipinfo_ipaddress` FOREIGN KEY (`ipaddress_id`) REFERENCES `ipinfo` (`ipaddress`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of local
-- ----------------------------
INSERT INTO `local` VALUES ('1', 'local.qq.com', '', '2017-11-11 08:56:33', '2017-11-11 08:56:33', 'now user', 'now user', 'cn', '1.1.1.1');
INSERT INTO `local` VALUES ('2', 'local.qq.com', '', '2017-11-11 08:56:38', '2017-11-11 08:56:38', 'now user', 'now user', 'cn', '1.1.1.2');
INSERT INTO `local` VALUES ('3', 'local.qq.com', '', '2017-11-11 08:56:44', '2017-11-11 08:56:44', 'now user', 'now user', 'us', '1.1.1.1');

-- ----------------------------
-- Table structure for loginfo
-- ----------------------------
DROP TABLE IF EXISTS `loginfo`;
CREATE TABLE `loginfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` int(11) NOT NULL,
  `state` int(11) NOT NULL,
  `agent_ip` char(39) NOT NULL,
  `message` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Loginfo_time_9646e35a_uniq` (`time`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of loginfo
-- ----------------------------
INSERT INTO `loginfo` VALUES ('1', '433452345', '0', '5.6.7.9', '1');

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
  `area_name_id` varchar(10) NOT NULL,
  `domain_id` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mx_mxDomain_area_name_id_5ad78f66_uniq` (`mxDomain`,`area_name_id`),
  KEY `mx_area_name_id_2febb400_fk_area_name` (`area_name_id`),
  KEY `mx_domain_id_d89aba58_fk_second_domain_domain` (`domain_id`),
  CONSTRAINT `mx_area_name_id_2febb400_fk_area_name` FOREIGN KEY (`area_name_id`) REFERENCES `area` (`name`),
  CONSTRAINT `mx_domain_id_d89aba58_fk_second_domain_domain` FOREIGN KEY (`domain_id`) REFERENCES `second_domain` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mx
-- ----------------------------
INSERT INTO `mx` VALUES ('1', 'mail@cyw.com', '10', '2017-11-11 09:06:14', '2017-11-11 09:06:14', 'now user', 'now user', '', 'cn', 'www.cn.com');
INSERT INTO `mx` VALUES ('2', 'mail@cywu.com', '10', '2017-11-11 09:06:44', '2017-11-11 09:06:44', 'now user', 'now user', '', 'cn', 'www.cn.com');

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
  `area_name_id` varchar(10) NOT NULL,
  `domain_id` varchar(45) NOT NULL,
  `ptr_ip_id` char(39) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ptr_domain_id_area_name_id_0cf5bf50_uniq` (`domain_id`,`area_name_id`),
  KEY `ptr_area_name_id_f707757e_fk_area_name` (`area_name_id`),
  KEY `ptr_ptr_ip_id_2c1f8178_fk_ipinfo_ipaddress` (`ptr_ip_id`),
  CONSTRAINT `ptr_area_name_id_f707757e_fk_area_name` FOREIGN KEY (`area_name_id`) REFERENCES `area` (`name`),
  CONSTRAINT `ptr_domain_id_eefa67e0_fk_second_domain_domain` FOREIGN KEY (`domain_id`) REFERENCES `second_domain` (`domain`),
  CONSTRAINT `ptr_ptr_ip_id_2c1f8178_fk_ipinfo_ipaddress` FOREIGN KEY (`ptr_ip_id`) REFERENCES `ipinfo` (`ipaddress`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ptr
-- ----------------------------
INSERT INTO `ptr` VALUES ('1', '2017-11-11 08:57:18', '2017-11-11 08:57:18', 'now user', 'now user', '', 'cn', 'www.cn.com', '1.1.1.1');
INSERT INTO `ptr` VALUES ('2', '2017-11-11 08:58:06', '2017-11-11 08:58:06', 'now user', 'now user', '', 'cn', 'www.uk.com', '1.1.1.1');
INSERT INTO `ptr` VALUES ('3', '2017-11-11 08:58:12', '2017-11-11 08:58:12', 'now user', 'now user', '', 'us', 'www.uk.com', '1.1.1.1');
INSERT INTO `ptr` VALUES ('4', '2017-11-11 08:58:15', '2017-11-11 08:58:15', 'now user', 'now user', '', 'uk', 'www.uk.com', '1.1.1.1');

-- ----------------------------
-- Table structure for resolv
-- ----------------------------
DROP TABLE IF EXISTS `resolv`;
CREATE TABLE `resolv` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `resolv_ip` char(39) NOT NULL,
  `resolv_port` int(11) DEFAULT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `create_user` varchar(30) NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `area_name_id` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `resolv_resolv_ip_area_name_id_495bd567_uniq` (`resolv_ip`,`area_name_id`),
  KEY `resolv_area_name_id_d5d23213_fk_area_name` (`area_name_id`),
  CONSTRAINT `resolv_area_name_id_d5d23213_fk_area_name` FOREIGN KEY (`area_name_id`) REFERENCES `area` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of resolv
-- ----------------------------
INSERT INTO `resolv` VALUES ('1', '3.2.1.2', null, '', '2017-11-11 09:11:28', '2017-11-11 09:11:28', 'now user', 'now user', 'cn');
INSERT INTO `resolv` VALUES ('2', '3.2.1.1', '2', '', '2017-11-11 09:11:38', '2017-11-11 09:11:38', 'now user', 'now user', 'cn');

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of second_domain
-- ----------------------------
INSERT INTO `second_domain` VALUES ('1', 'www.cn.com', '2017-11-11 08:55:53', '2017-11-11 08:55:53', 'now user', 'now user', '');
INSERT INTO `second_domain` VALUES ('2', 'www.uk.com', '2017-11-11 08:56:00', '2017-11-11 08:56:00', 'now user', 'now user', '');

-- ----------------------------
-- Table structure for server
-- ----------------------------
DROP TABLE IF EXISTS `server`;
CREATE TABLE `server` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reverse_ip` char(39) NOT NULL,
  `nameserver_ip` char(39) NOT NULL,
  `nameserver_port` int(11) NOT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `create_user` varchar(30) NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `area_name_id` varchar(10) NOT NULL,
  `domain_id` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `server_reverse_ip_area_name_id_c1313df1_uniq` (`reverse_ip`,`area_name_id`),
  KEY `server_area_name_id_4d0107be_fk_area_name` (`area_name_id`),
  KEY `server_domain_id_43f2d1b2_fk_second_domain_domain` (`domain_id`),
  CONSTRAINT `server_area_name_id_4d0107be_fk_area_name` FOREIGN KEY (`area_name_id`) REFERENCES `area` (`name`),
  CONSTRAINT `server_domain_id_43f2d1b2_fk_second_domain_domain` FOREIGN KEY (`domain_id`) REFERENCES `second_domain` (`domain`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of server
-- ----------------------------

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
  `area_name_id` varchar(10) NOT NULL,
  `domain_id` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `srv_srv_domain_area_name_id_1593bfbc_uniq` (`srv_domain`,`area_name_id`),
  KEY `srv_area_name_id_0ff4c009_fk_area_name` (`area_name_id`),
  KEY `srv_domain_id_6b36e952_fk_second_domain_domain` (`domain_id`),
  CONSTRAINT `srv_area_name_id_0ff4c009_fk_area_name` FOREIGN KEY (`area_name_id`) REFERENCES `area` (`name`),
  CONSTRAINT `srv_domain_id_6b36e952_fk_second_domain_domain` FOREIGN KEY (`domain_id`) REFERENCES `second_domain` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of srv
-- ----------------------------
INSERT INTO `srv` VALUES ('1', 'srv.domain.com', '22', '10', '10', '2017-11-11 09:01:11', '2017-11-11 09:01:11', 'now user', 'now user', '', 'cn', 'www.cn.com');
INSERT INTO `srv` VALUES ('2', 'srv.adomain.com', '22', '10', '10', '2017-11-11 09:01:21', '2017-11-11 09:01:21', 'now user', 'now user', '', 'cn', 'www.cn.com');
INSERT INTO `srv` VALUES ('5', 'srv.domain.clom', '22', '10', '10', '2017-11-11 09:04:49', '2017-11-11 09:04:49', 'now user', 'now user', '', 'cn', 'www.uk.com');

-- ----------------------------
-- Table structure for topdomain
-- ----------------------------
DROP TABLE IF EXISTS `topdomain`;
CREATE TABLE `topdomain` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `top_domain` varchar(45) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `delete_user` varchar(30) NOT NULL,
  `update_user` varchar(30) NOT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `top_domain` (`top_domain`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of topdomain
-- ----------------------------
INSERT INTO `topdomain` VALUES ('1', 'cn.com', '2017-11-11 08:55:26', '2017-11-11 08:55:26', 'now user', 'now user', '');
INSERT INTO `topdomain` VALUES ('2', 'uk.com', '2017-11-11 08:55:32', '2017-11-11 08:55:32', 'now user', 'now user', '');

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
  `area_name_id` varchar(10) NOT NULL,
  `domain_id` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `txt_domain_id_area_name_id_126055f1_uniq` (`domain_id`,`area_name_id`),
  KEY `txt_area_name_id_c478d24c_fk_area_name` (`area_name_id`),
  CONSTRAINT `txt_area_name_id_c478d24c_fk_area_name` FOREIGN KEY (`area_name_id`) REFERENCES `area` (`name`),
  CONSTRAINT `txt_domain_id_3368babb_fk_second_domain_domain` FOREIGN KEY (`domain_id`) REFERENCES `second_domain` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of txt
-- ----------------------------
INSERT INTO `txt` VALUES ('1', 'lll', '2017-11-11 09:06:59', '2017-11-11 09:06:59', 'now user', 'now user', '', 'cn', 'www.cn.com');
INSERT INTO `txt` VALUES ('2', 'lll', '2017-11-11 09:07:09', '2017-11-11 09:07:09', 'now user', 'now user', '', 'cn', 'www.uk.com');
SET FOREIGN_KEY_CHECKS=1;
