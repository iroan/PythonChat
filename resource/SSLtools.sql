/*
Navicat MySQL Data Transfer

Source Server         : 用于SSLTools开发
Source Server Version : 80003
Source Host           : localhost:3306
Source Database       : ssltools

Target Server Type    : MYSQL
Target Server Version : 80003
File Encoding         : 65001

Date: 2018-01-28 02:38:39
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `messagehistory`
-- ----------------------------
DROP TABLE IF EXISTS `messagehistory`;
CREATE TABLE `messagehistory` (
  `id` int(11) NOT NULL,
  `nickNameSend` varchar(20) DEFAULT NULL,
  `nickNameRecv` varchar(20) DEFAULT NULL,
  `sendTime` datetime DEFAULT NULL,
  `message` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of messagehistory
-- ----------------------------

-- ----------------------------
-- Table structure for `singinhistory`
-- ----------------------------
DROP TABLE IF EXISTS `singinhistory`;
CREATE TABLE `singinhistory` (
  `id` int(11) NOT NULL,
  `nickName` varchar(20) DEFAULT NULL,
  `upLineIp` varchar(30) DEFAULT NULL,
  `upLineTime` datetime DEFAULT NULL,
  `offLineTime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of singinhistory
-- ----------------------------

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nickName` varchar(20) NOT NULL,
  `trueName` varchar(20) DEFAULT NULL,
  `gender` bit(1) DEFAULT NULL,
  `department` varchar(20) DEFAULT NULL,
  `position` varchar(20) DEFAULT NULL,
  `introduce` text,
  `isOnTheJob` bit(1) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `phone` char(11) DEFAULT NULL,
  `password` char(40) NOT NULL,
  `isOnline` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'iroan', '王凯旋', '', '技术部', '项目经理、架构师、程序员', '有所补位，才能有所为', '', '2654189525@qq.com', '17585984347', '1', '');
INSERT INTO `user` VALUES ('2', 'kaijun', '王凯军', '', '技术部', '前段工程师', '吃饭、睡觉、做闲事', '', null, null, '1', '');
INSERT INTO `user` VALUES ('3', 'rong', '陈刚容', '', '后勤部', '医生', '吃饭、睡觉、上班', '', '1573811240@qq.com', '18375203954', '1', '');
