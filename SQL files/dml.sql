DELIMITER //
CREATE TRIGGER inventoryAddCheck BEFORE INSERT ON inventory
	for each row
    BEGIN
    declare one_value int;
    declare newinvnum int;	
    set one_value = 0;
    if new.gun_id is not null
		then set one_value = 1;
	end if;
	if new.shield is not null
		then
			if one_value = 0
				then set one_value = 1;
			else
				SIGNAL SQLSTATE '02000' SET MESSAGE_TEXT = 'Cannot have more than one item id per record';
			end if;
	end if;
	if new.class_mod is not null and one_value
		then
			if one_value = 0
				then set one_value = 1;
			else
				SIGNAL SQLSTATE '02000' SET MESSAGE_TEXT = 'Cannot have more than one item id per record';
			end if;
	end if;
	if new.relic is not null and one_value
		then
			if one_value = 0
				then set one_value = 1;
			else
				SIGNAL SQLSTATE '02000' SET MESSAGE_TEXT = 'Cannot have more than one item id per record';
			end if;
	end if;
	if new.grenade_mod is not null and one_value
		then
			if one_value = 0
				then set one_value = 1;
			else
				SIGNAL SQLSTATE '02000' SET MESSAGE_TEXT = 'Cannot have more than one item id per record';
			end if;
	end if;
	
    set newinvnum = (select max(inv_num) from inventory where user_id = new.user_id and hunter_id = new.hunter_id);
    if newinvnum is null
		then set newinvnum = 0;
	end if;
	set new.inv_num = newinvnum + 1;
    END//
DELIMITER ;

Create view allVaultHunters as Select * from vault_hunter;
Create view usersAndHunters as Select u.username, v.name, v.class, v.level from user u join vault_hunter v on u.user_id = v.user_id;
Create view allSeraphGuns as Select * from gun where rarity = 'Seraph';
Create view userAndBadassRank as Select u.username, b.level, b.max_health, b.shield_cap, b.sh_recharge_delay, 
b.sh_recharge_rate, b.melee_damage, b.grenade_damage, b.gun_accuracy, b.gun_damage, b.fire_rate, b.recoil_reduction, b.el_effect_chance, 
b.el_effect_damage, b.crit_hit_damage from user u join badass_rank b on u.user_id = b.user_id;
Create view huntersAndEquipped as Select v.name, v.class, e.gun_1, e.gun_2, e.gun_3, e.gun_4, e.grenade_mod, e.class_mod, e.shield, e.relic from vault_hunter v join equipped e on v.hunter_id = e.hunter_id;
Create view npcAndLocation as Select n.name, l.location_name from npc n join location l on n.location_id = l.location_id;

DELIMITER //
Create procedure userCharacterData(user_id_param int)
BEGIN
	Select v.name, v.class, e.gun_1, e.gun_2, e.gun_3, e.gun_4, e.grenade_mod, e.class_mod, e.shield, e.relic from vault_hunter v join equipped e on v.hunter_id = e.hunter_id where v.user_id = user_id_param;
END //
DELIMITER ;

DELIMITER //
Create procedure allSeraphGunsOwned(user_id_param int)
begin
	Select * from gun where rarity = 'Seraph' and gun_id in (Select gun_id from inventory where user_id = user_id_param);
end //
DELIMITER ;

DELIMITER //
create procedure avgCharacterLevel(user_id_param int)
begin
	Select avg(level) from vault_hunter where user_id = user_id_param;
end //
DELIMITER ;
