-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: 회원db
-- ------------------------------------------------------
-- Server version	8.0.36-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `상담내용`
--

DROP TABLE IF EXISTS `상담내용`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `상담내용` (
  `로그코드` int NOT NULL AUTO_INCREMENT,
  `회원코드` int NOT NULL,
  `회원상담내용` varchar(5000) DEFAULT NULL,
  `욕설내용` varchar(10000) DEFAULT '없음',
  `횟수` int DEFAULT '0',
  PRIMARY KEY (`로그코드`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `상담내용`
--

LOCK TABLES `상담내용` WRITE;
/*!40000 ALTER TABLE `상담내용` DISABLE KEYS */;
INSERT INTO `상담내용` VALUES (1,1098,'너 병신이냐','병신',32),(2,1121,'아니 씨발 좆같은게 다 지랄이야','씨발, 좆, 지랄',3),(3,2345,'윤석열 국민의힘 존나 할말이 없네','윤석열, 존나, 국민의힘',23),(4,3141,'상품 배송이 너무 느린데 무슨일 있는건가요?','없음',0),(5,5161,'제가 실수로 잘못된 상품을 주문했어요. 어떻게 해야하죠?','없음',0),(6,5678,'조선족도 아니고 왜 못알아듣는데? 간첩새끼도아니고','조선족, 간첩새끼',2),(7,5812,'잘못걸었습니다','없음',0),(8,6171,'별의별 미친놈들이 다있네 내가 그런거 아니라고 말했잖아 병신아 못알아들어?','미친놈, 병신',2),(9,7181,'상품을 받았는데 파손되어 있네요. 교환해주실 수 있나요?','없음',0),(10,7463,'안녕하세요 회원탈퇴 후 재가입하려고 하는데요','없음',0),(11,8191,'야이 개새끼야 니가 뭔데, 사장나오라고해','개새끼',1),(12,8912,'야 이년아 지랄하고 앉아있네 존나 싸가지없네','년, 지랄, 존나',15),(13,9101,'이번달 결제가 되지 않았는데 무슨 문제가 있는걸까요?','없음',0),(14,7463,'뭐 때문에 기분이 나빴는지 저한테 물어보 친구 아니에요 이 여자 거기 교육 좀 똑바로 시키세요. 그냥 없어지기 전에 짜증 나게 진짜 병신 같은 게 무슨 매니저라고 거기 한 잔이냐 진짜.','병신',1),(15,5161,'또라이 새끼를 봤나? 이씨 야 이 존만한 새끼야 이분이 어떤 분이신 줄 알고 개소리를 하고 잡혀 있어. 이 씨발 저런 새끼야 확 우리 형님이 저런 똥간에서 바닥에 떨어진 싸구려 라이트나 죽고 다니는 그런 분으로 보여. 우리 형님이 거지 새끼야 이 새끼야 확 가뜩이나 요즘 가오 죽어서 민감하신데 이 씨발 저 새끼 분위기 파악해가면서 시브라 젖만 나 딱 닦고 그냥 확 어이구 이씨 꼬나봐 꼬나봐 확 눈깔을 파서 알다발 쳐라. 야 그만둬라. 지금 젖딴식에 신경 쓸 때가 아니다. 가자. 자.','개소리, 새끼, 또라이, 씨발, 똥, 젖, 죽어',21),(16,5161,'또라이 새끼를 봤나? 이씨 야 이 존만한 새끼야 이분이 어떤 분이신 줄 알고 개소리를 하고 잡혀 있어. 이 씨발 저런 새끼야 확 우리 형님이 저런 똥간에서 바닥에 떨어진 싸구려 라이트나 죽고 다니는 그런 분으로 보여. 우리 형님이 거지 새끼야 이 새끼야 확 가뜩이나 요즘 가오 죽어서 민감하신데 이 씨발 저 새끼 분위기 파악해가면서 시브라 젖만 나 딱 닦고 그냥 확 어이구 이씨 꼬나봐 꼬나봐 확 눈깔을 파서 알다발 쳐라. 야 그만둬라. 지금 젖딴식에 신경 쓸 때가 아니다. 가자. 자.','개소리, 새끼, 또라이, 씨발, 똥, 젖, 죽어',21),(17,3141,'또라이 새끼를 봤나? 이씨 야 이 존만한 새끼야 이분이 어떤 분이신 줄 알고 개소리를 하고 잡혀 있어. 이 씨발 저런 새끼야 확 우리 형님이 저런 똥간에서 바닥에 떨어진 싸구려 라이트나 죽고 다니는 그런 분으로 보여. 우리 형님이 거지 새끼야 이 새끼야 확 가뜩이나 요즘 가오 죽어서 민감하신데 이 씨발 저 새끼 분위기 파악해가면서 시브라 젖만 나 딱 닦고 그냥 확 어이구 이씨 꼬나봐 꼬나봐 확 눈깔을 파서 알다발 쳐라. 야 그만둬라. 지금 젖딴식에 신경 쓸 때가 아니다. 가자. 자.','개소리, 새끼, 또라이, 씨발, 똥, 젖, 죽어',21),(18,5812,'또라이 새끼를 봤나? 이씨 야 이 존만한 새끼야 이분이 어떤 분이신 줄 알고 개소리를 하고 잡혀 있어. 이 씨발 저런 새끼야 확 우리 형님이 저런 똥간에서 바닥에 떨어진 싸구려 라이트나 죽고 다니는 그런 분으로 보여. 우리 형님이 거지 새끼야 이 새끼야 확 가뜩이나 요즘 가오 죽어서 민감하신데 이 씨발 저 새끼 분위기 파악해가면서 시브라 젖만 나 딱 닦고 그냥 확 어이구 이씨 꼬나봐 꼬나봐 확 눈깔을 파서 알다발 쳐라. 야 그만둬라. 지금 젖딴식에 신경 쓸 때가 아니다. 가자. 자.','개소리, 새끼, 또라이, 씨발, 똥, 젖, 죽어',21),(19,5161,'또라이 새끼를 봤나? 이씨 야 이 존만한 새끼야 이분이 어떤 분이신 줄 알고 개소리를 하고 잡혀 있어. 이 씨발 저런 새끼야 확 우리 형님이 저런 똥간에서 바닥에 떨어진 싸구려 라이트나 죽고 다니는 그런 분으로 보여. 우리 형님이 거지 새끼야 이 새끼야 확 가뜩이나 요즘 가오 죽어서 민감하신데 이 씨발 저 새끼 분위기 파악해가면서 시브라 젖만 나 딱 닦고 그냥 확 어이구 이씨 꼬나봐 꼬나봐 확 눈깔을 파서 알다발 쳐라. 야 그만둬라. 지금 젖딴식에 신경 쓸 때가 아니다. 가자. 자.','개소리, 새끼, 또라이, 씨발, 똥, 젖, 죽어',21),(20,2345,'또라이 새끼를 봤나? 이씨 야 이 존만한 새끼야 이분이 어떤 분이신 줄 알고 개소리를 하고 잡혀 있어. 이 씨발 저런 새끼야 확 우리 형님이 저런 똥간에서 바닥에 떨어진 싸구려 라이트나 죽고 다니는 그런 분으로 보여. 우리 형님이 거지 새끼야 이 새끼야 확 가뜩이나 요즘 가오 죽어서 민감하신데 이 씨발 저 새끼 분위기 파악해가면서 시브라 젖만 나 딱 닦고 그냥 확 어이구 이씨 꼬나봐 꼬나봐 확 눈깔을 파서 알다발 쳐라. 야 그만둬라. 지금 젖딴식에 신경 쓸 때가 아니다. 가자. 자.','개소리, 새끼, 또라이, 씨발, 똥, 젖, 죽어',21),(21,1098,'또라이 새끼를 봤나? 이씨 야 이 존만한 새끼야 이분이 어떤 분이신 줄 알고 개소리를 하고 잡혀 있어. 이 씨발 저런 새끼야 확 우리 형님이 저런 똥간에서 바닥에 떨어진 싸구려 라이트나 죽고 다니는 그런 분으로 보여. 우리 형님이 거지 새끼야 이 새끼야 확 가뜩이나 요즘 가오 죽어서 민감하신데 이 씨발 저 새끼 분위기 파악해가면서 시브라 젖만 나 딱 닦고 그냥 확 어이구 이씨 꼬나봐 꼬나봐 확 눈깔을 파서 알다발 쳐라. 야 그만둬라. 지금 젖딴식에 신경 쓸 때가 아니다. 가자. 자.','개소리, 새끼, 또라이, 씨발, 똥, 젖, 죽어',21),(22,3141,'또라이 새끼를 봤나? 이씨 야 이 존만한 새끼야 이분이 어떤 분이신 줄 알고 개소리를 하고 잡혀 있어. 이 씨발 저런 새끼야 확 우리 형님이 저런 똥간에서 바닥에 떨어진 싸구려 라이트나 죽고 다니는 그런 분으로 보여. 우리 형님이 거지 새끼야 이 새끼야 확 가뜩이나 요즘 가오 죽어서 민감하신데 이 씨발 저 새끼 분위기 파악해가면서 시브라 젖만 나 딱 닦고 그냥 확 어이구 이씨 꼬나봐 꼬나봐 확 눈깔을 파서 알다발 쳐라. 야 그만둬라. 지금 젖딴식에 신경 쓸 때가 아니다. 가자. 자.','개소리, 새끼, 또라이, 씨발, 똥, 젖, 죽어',21),(23,6171,'또라이 새끼를 봤나? 이씨 야 이 존만한 새끼야 이분이 어떤 분이신 줄 알고 개소리를 하고 잡혀 있어. 이 씨발 저런 새끼야 확 우리 형님이 저런 똥간에서 바닥에 떨어진 싸구려 라이트나 죽고 다니는 그런 분으로 보여. 우리 형님이 거지 새끼야 이 새끼야 확 가뜩이나 요즘 가오 죽어서 민감하신데 이 씨발 저 새끼 분위기 파악해가면서 시브라 젖만 나 딱 닦고 그냥 확 어이구 이씨 꼬나봐 꼬나봐 확 눈깔을 파서 알다발 쳐라. 야 그만둬라. 지금 젖딴식에 신경 쓸 때가 아니다. 가자. 자.','개소리, 새끼, 또라이, 씨발, 똥, 젖, 죽어',21);
/*!40000 ALTER TABLE `상담내용` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `특별회원관리`
--

DROP TABLE IF EXISTS `특별회원관리`;
/*!50001 DROP VIEW IF EXISTS `특별회원관리`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `특별회원관리` AS SELECT 
 1 AS `회원코드`,
 1 AS `아이디`,
 1 AS `회원명`,
 1 AS `휴대폰번호`,
 1 AS `특별관리단계`,
 1 AS `회원상담내용`,
 1 AS `욕설내용`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `특별회원분류`
--

DROP TABLE IF EXISTS `특별회원분류`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `특별회원분류` (
  `분류코드` int NOT NULL,
  `특별관리단계` varchar(30) DEFAULT NULL,
  `기준횟수` varchar(45) NOT NULL,
  PRIMARY KEY (`분류코드`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `특별회원분류`
--

LOCK TABLES `특별회원분류` WRITE;
/*!40000 ALTER TABLE `특별회원분류` DISABLE KEYS */;
INSERT INTO `특별회원분류` VALUES (1,'상','30'),(2,'중','20'),(3,'하','10'),(4,'해당없음','0');
/*!40000 ALTER TABLE `특별회원분류` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `회원`
--

DROP TABLE IF EXISTS `회원`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `회원` (
  `회원코드` int NOT NULL,
  `아이디` varchar(30) DEFAULT NULL,
  `회원명` varchar(45) NOT NULL,
  `휴대폰번호` varchar(45) DEFAULT NULL,
  `분류코드` int DEFAULT NULL,
  PRIMARY KEY (`회원코드`),
  KEY `분류코드_idx` (`분류코드`),
  CONSTRAINT `분류코드` FOREIGN KEY (`분류코드`) REFERENCES `특별회원분류` (`분류코드`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `회원`
--

LOCK TABLES `회원` WRITE;
/*!40000 ALTER TABLE `회원` DISABLE KEYS */;
INSERT INTO `회원` VALUES (1098,'musiclover77','정서연','010-1234-5678',1),(1121,'newuser4','박민수','010-7777-8888',4),(1234,'newuser1','홍길동','010-1111-2222',1),(2345,'user123','김민지','010-1234-5677',2),(3141,'newuser5','정수빈','010-9999-0000',4),(4151,'user1234','이지은','010-1234-5679',1),(5161,'superman','김영호','010-9876-5432',2),(5678,'newuser2','김철수','010-3333-4444',2),(5812,'gaminmaster','최성민','010-2938-2922',4),(6171,'admin123','최승현','010-1111-3333',3),(7181,'awesome','장성우','010-7777-9999',4),(7463,'soccerfan99','박지영','010-2468-1357',4),(8191,'newuser6','이재현','010-8888-7777',4),(8912,'coolguy82','이준호','010-2293-8333',3),(9101,'newuser3','이영희','010-5555-6666',3);
/*!40000 ALTER TABLE `회원` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `특별회원관리`
--

/*!50001 DROP VIEW IF EXISTS `특별회원관리`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `특별회원관리` AS select `회원`.`회원코드` AS `회원코드`,`회원`.`아이디` AS `아이디`,`회원`.`회원명` AS `회원명`,`회원`.`휴대폰번호` AS `휴대폰번호`,`특별회원분류`.`특별관리단계` AS `특별관리단계`,`상담내용`.`회원상담내용` AS `회원상담내용`,`상담내용`.`욕설내용` AS `욕설내용` from ((`회원` join `상담내용` on((`회원`.`회원코드` = `상담내용`.`회원코드`))) join `특별회원분류` on((`회원`.`분류코드` = `특별회원분류`.`분류코드`))) */;
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

-- Dump completed on 2024-04-17 13:51:36
