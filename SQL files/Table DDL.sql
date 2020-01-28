CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

CREATE TABLE `badass_rank` (
  `user_id` int(11) NOT NULL,
  `level` int(11) DEFAULT NULL,
  `max_health` float(3,1) DEFAULT NULL,
  `shield_cap` float(3,1) DEFAULT NULL,
  `sh_recharge_delay` float(3,1) DEFAULT NULL,
  `sh_recharge_rate` float(3,1) DEFAULT NULL,
  `melee_damage` float(3,1) DEFAULT NULL,
  `grenade_damage` float(3,1) DEFAULT NULL,
  `gun_accuracy` float(3,1) DEFAULT NULL,
  `gun_damage` float(3,1) DEFAULT NULL,
  `fire_rate` float(3,1) DEFAULT NULL,
  `recoil_reduction` float(3,1) DEFAULT NULL,
  `reload_speed` float(3,1) DEFAULT NULL,
  `el_effect_chance` float(3,1) DEFAULT NULL,
  `el_effect_damage` float(3,1) DEFAULT NULL,
  `crit_hit_damage` float(3,1) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `badass_rank_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `inventory` (
  `user_id` int(11) NOT NULL,
  `hunter_id` int(11) NOT NULL,
  `inv_num` int(11) NOT NULL,
  `gun_id` int(11) DEFAULT NULL,
  `shield` int(11) DEFAULT NULL,
  `class_mod` int(11) DEFAULT NULL,
  `relic` int(11) DEFAULT NULL,
  `grenade_mod` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_id`,`hunter_id`,`inv_num`),
  KEY `gun_id` (`gun_id`),
  KEY `grenade_mod` (`grenade_mod`),
  KEY `class_mod` (`class_mod`),
  KEY `relic` (`relic`),
  KEY `shield` (`shield`),
  CONSTRAINT `inventory_ibfk_1` FOREIGN KEY (`user_id`, `hunter_id`) REFERENCES `vault_hunter` (`user_id`, `hunter_id`),
  CONSTRAINT `inventory_ibfk_2` FOREIGN KEY (`gun_id`) REFERENCES `gun` (`gun_id`),
  CONSTRAINT `inventory_ibfk_3` FOREIGN KEY (`grenade_mod`) REFERENCES `grenade` (`grenade_id`),
  CONSTRAINT `inventory_ibfk_4` FOREIGN KEY (`class_mod`) REFERENCES `class_mod` (`mod_id`),
  CONSTRAINT `inventory_ibfk_5` FOREIGN KEY (`relic`) REFERENCES `relic` (`relic_id`),
  CONSTRAINT `inventory_ibfk_6` FOREIGN KEY (`shield`) REFERENCES `shield` (`shield_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `location` (
  `location_id` int(11) NOT NULL AUTO_INCREMENT,
  `location_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`location_id`),
  UNIQUE KEY `location_name` (`location_name`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=latin1;

CREATE TABLE `manufacturer` (
  `manu_id` int(11) NOT NULL AUTO_INCREMENT,
  `manu_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`manu_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

CREATE TABLE `vault_hunter` (
  `hunter_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `class` varchar(10) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`user_id`,`hunter_id`),
  CONSTRAINT `vault_hunter_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `vechicle` (
  `vechicle_id` int(11) NOT NULL AUTO_INCREMENT,
  `vechicle_name` varchar(100) DEFAULT NULL,
  `vechicle_tye` varchar(50) DEFAULT NULL,
  `vechicle_crew` varchar(255) DEFAULT NULL,
  `vechicle_armaments` varchar(255) DEFAULT NULL,
  `location_id` int(11) DEFAULT NULL,
  `location_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`vechicle_id`),
  KEY `location_id` (`location_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

CREATE TABLE `currency` (
  `hunter_id` int(11) NOT NULL,
  `money` int(11) DEFAULT NULL,
  `eridium` int(11) DEFAULT NULL,
  `pistol_ammo` int(11) DEFAULT NULL,
  `sniper_ammo` int(11) DEFAULT NULL,
  `shotgun_ammo` int(11) DEFAULT NULL,
  `rifle_ammo` int(11) DEFAULT NULL,
  `submachine_ammo` int(11) DEFAULT NULL,
  `rocket_ammo` int(11) DEFAULT NULL,
  `grenades` int(11) DEFAULT NULL,
  `skeletonkeys` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`,`hunter_id`),
  CONSTRAINT `currency_ibfk_1` FOREIGN KEY (`user_id`, `hunter_id`) REFERENCES `vault_hunter` (`user_id`, `hunter_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `enemy` (
  `enemy_id` int(11) NOT NULL AUTO_INCREMENT,
  `location_id` int(11) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`enemy_id`),
  KEY `location_id` (`location_id`),
  CONSTRAINT `enemy_ibfk_1` FOREIGN KEY (`location_id`) REFERENCES `location` (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

CREATE TABLE `class_mod` (
  `mod_id` int(11) NOT NULL AUTO_INCREMENT,
  `manu_id` int(11) DEFAULT NULL,
  `location_id` int(11) DEFAULT NULL,
  `item_type` varchar(30) DEFAULT NULL,
  `mod_name` varchar(150) DEFAULT NULL,
  `mod_perk` varchar(255) DEFAULT NULL,
  `manufacturer` varchar(150) DEFAULT NULL,
  `location_name` varchar(200) DEFAULT NULL,
  `damage_type` varchar(200) DEFAULT NULL,
  `dropped_by` varchar(200) DEFAULT NULL,
  `minimum_task` varchar(200) DEFAULT NULL,
  `rarity` varchar(50) DEFAULT NULL,
  `dlc` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`mod_id`),
  KEY `manu_id` (`manu_id`),
  KEY `location_id` (`location_id`),
  CONSTRAINT `class_mod_ibfk_1` FOREIGN KEY (`manu_id`) REFERENCES `manufacturer` (`manu_id`),
  CONSTRAINT `class_mod_ibfk_2` FOREIGN KEY (`location_id`) REFERENCES `location` (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=latin1;

CREATE TABLE `grenade` (
  `grenade_id` int(11) NOT NULL AUTO_INCREMENT,
  `manu_id` int(11) DEFAULT NULL,
  `location_id` int(11) DEFAULT NULL,
  `item_type` varchar(30) DEFAULT NULL,
  `grenade_name` varchar(150) DEFAULT NULL,
  `grenade_perk` varchar(255) DEFAULT NULL,
  `manufacturer` varchar(150) DEFAULT NULL,
  `location_name` varchar(200) DEFAULT NULL,
  `damage_type` varchar(200) DEFAULT NULL,
  `dropped_by` varchar(200) DEFAULT NULL,
  `minimum_task` varchar(200) DEFAULT NULL,
  `rarity` varchar(50) DEFAULT NULL,
  `dlc` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`grenade_id`),
  KEY `manu_id` (`manu_id`),
  KEY `location_id` (`location_id`),
  CONSTRAINT `grenade_ibfk_1` FOREIGN KEY (`manu_id`) REFERENCES `manufacturer` (`manu_id`),
  CONSTRAINT `grenade_ibfk_2` FOREIGN KEY (`location_id`) REFERENCES `location` (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

CREATE TABLE `gun` (
  `gun_id` int(11) NOT NULL AUTO_INCREMENT,
  `manu_id` int(11) DEFAULT NULL,
  `gun_name` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `damage_type` varchar(255) DEFAULT NULL,
  `dropped_by` varchar(255) DEFAULT NULL,
  `minimum_task` varchar(255) DEFAULT NULL,
  `rarity` varchar(100) DEFAULT NULL,
  `manufacturer` varchar(200) DEFAULT NULL,
  `perk` varchar(255) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `dlc` varchar(255) DEFAULT NULL,
  `location_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`gun_id`),
  KEY `manu_id` (`manu_id`),
  KEY `location_id` (`location_id`),
  CONSTRAINT `gun_ibfk_1` FOREIGN KEY (`manu_id`) REFERENCES `manufacturer` (`manu_id`),
  CONSTRAINT `gun_ibfk_2` FOREIGN KEY (`location_id`) REFERENCES `location` (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=642 DEFAULT CHARSET=latin1;

CREATE TABLE `relic` (
  `relic_id` int(11) NOT NULL AUTO_INCREMENT,
  `manu_id` int(11) DEFAULT NULL,
  `location_id` int(11) DEFAULT NULL,
  `item_type` varchar(30) DEFAULT NULL,
  `relic_name` varchar(150) DEFAULT NULL,
  `relic_perk` varchar(255) DEFAULT NULL,
  `manufacturer` varchar(150) DEFAULT NULL,
  `location_name` varchar(200) DEFAULT NULL,
  `damage_type` varchar(200) DEFAULT NULL,
  `dropped_by` varchar(200) DEFAULT NULL,
  `minimum_task` varchar(200) DEFAULT NULL,
  `rarity` varchar(50) DEFAULT NULL,
  `dlc` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`relic_id`),
  KEY `manu_id` (`manu_id`),
  KEY `location_id` (`location_id`),
  CONSTRAINT `relic_ibfk_1` FOREIGN KEY (`manu_id`) REFERENCES `manufacturer` (`manu_id`),
  CONSTRAINT `relic_ibfk_2` FOREIGN KEY (`location_id`) REFERENCES `location` (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

CREATE TABLE `shield` (
  `shield_id` int(11) NOT NULL AUTO_INCREMENT,
  `manu_id` int(11) DEFAULT NULL,
  `location_id` int(11) DEFAULT NULL,
  `item_type` varchar(100) DEFAULT NULL,
  `shield_name` varchar(150) DEFAULT NULL,
  `shield_perk` varchar(255) DEFAULT NULL,
  `manufacturer` varchar(255) DEFAULT NULL,
  `location_name` varchar(255) DEFAULT NULL,
  `damage_type` varchar(255) DEFAULT NULL,
  `dropped_by` varchar(150) DEFAULT NULL,
  `minimum_task` varchar(255) DEFAULT NULL,
  `rarity` varchar(150) DEFAULT NULL,
  `dlc` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`shield_id`),
  KEY `manu_id` (`manu_id`),
  KEY `location_id` (`location_id`),
  CONSTRAINT `shield_ibfk_1` FOREIGN KEY (`manu_id`) REFERENCES `manufacturer` (`manu_id`),
  CONSTRAINT `shield_ibfk_2` FOREIGN KEY (`location_id`) REFERENCES `location` (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

CREATE TABLE `inventory` (
  `user_id` int(11) NOT NULL,
  `hunter_id` int(11) NOT NULL,
  `inv_num` int(11) NOT NULL,
  `gun_id` int(11) DEFAULT NULL,
  `shield` int(11) DEFAULT NULL,
  `class_mod` int(11) DEFAULT NULL,
  `relic` int(11) DEFAULT NULL,
  `grenade_mod` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_id`,`hunter_id`,`inv_num`),
  KEY `gun_id` (`gun_id`),
  KEY `grenade_mod` (`grenade_mod`),
  KEY `class_mod` (`class_mod`),
  KEY `relic` (`relic`),
  KEY `shield` (`shield`),
  CONSTRAINT `inventory_ibfk_1` FOREIGN KEY (`user_id`, `hunter_id`) REFERENCES `vault_hunter` (`user_id`, `hunter_id`),
  CONSTRAINT `inventory_ibfk_2` FOREIGN KEY (`gun_id`) REFERENCES `gun` (`gun_id`),
  CONSTRAINT `inventory_ibfk_3` FOREIGN KEY (`grenade_mod`) REFERENCES `grenade` (`grenade_id`),
  CONSTRAINT `inventory_ibfk_4` FOREIGN KEY (`class_mod`) REFERENCES `class_mod` (`mod_id`),
  CONSTRAINT `inventory_ibfk_5` FOREIGN KEY (`relic`) REFERENCES `relic` (`relic_id`),
  CONSTRAINT `inventory_ibfk_6` FOREIGN KEY (`shield`) REFERENCES `shield` (`shield_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `equipped` (
  `user_id` int(11) NOT NULL,
  `hunter_id` int(11) NOT NULL,
  `gun_1` int(11) DEFAULT NULL,
  `gun_2` int(11) DEFAULT NULL,
  `gun_3` int(11) DEFAULT NULL,
  `gun_4` int(11) DEFAULT NULL,
  `grenade_mod` int(11) DEFAULT NULL,
  `class_mod` int(11) DEFAULT NULL,
  `relic` int(11) DEFAULT NULL,
  `shield` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_id`,`hunter_id`),
  KEY `gun_1` (`gun_1`),
  KEY `gun_2` (`gun_2`),
  KEY `gun_3` (`gun_3`),
  KEY `gun_4` (`gun_4`),
  KEY `grenade_mod` (`grenade_mod`),
  KEY `class_mod` (`class_mod`),
  KEY `relic` (`relic`),
  KEY `shield` (`shield`),
  CONSTRAINT `equipped_ibfk_1` FOREIGN KEY (`user_id`, `hunter_id`) REFERENCES `vault_hunter` (`user_id`, `hunter_id`),
  CONSTRAINT `equipped_ibfk_2` FOREIGN KEY (`gun_1`) REFERENCES `gun` (`gun_id`),
  CONSTRAINT `equipped_ibfk_3` FOREIGN KEY (`gun_2`) REFERENCES `gun` (`gun_id`),
  CONSTRAINT `equipped_ibfk_4` FOREIGN KEY (`gun_3`) REFERENCES `gun` (`gun_id`),
  CONSTRAINT `equipped_ibfk_5` FOREIGN KEY (`gun_4`) REFERENCES `gun` (`gun_id`),
  CONSTRAINT `equipped_ibfk_6` FOREIGN KEY (`grenade_mod`) REFERENCES `grenade` (`grenade_id`),
  CONSTRAINT `equipped_ibfk_7` FOREIGN KEY (`class_mod`) REFERENCES `class_mod` (`mod_id`),
  CONSTRAINT `equipped_ibfk_8` FOREIGN KEY (`relic`) REFERENCES `relic` (`relic_id`),
  CONSTRAINT `equipped_ibfk_9` FOREIGN KEY (`shield`) REFERENCES `shield` (`shield_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

