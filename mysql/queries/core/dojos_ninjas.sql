INSERT INTO `dojos_and_ninjas`.`dojos` (`name`, `created_at`, `updated_at`) VALUES ('dojo1', now(),now());
INSERT INTO `dojos_and_ninjas`.`dojos` (`name`, `created_at`, `updated_at`) VALUES ('dojo2', now(),now());
INSERT INTO `dojos_and_ninjas`.`dojos` (`name`, `created_at`, `updated_at`) VALUES ('dojo3', now(),now());


delete  FROM dojos_and_ninjas.dojos;


INSERT INTO `dojos_and_ninjas`.`dojos` (`name`, `created_at`, `updated_at`) VALUES ('dojo1', now(),now());
INSERT INTO `dojos_and_ninjas`.`dojos` (`name`, `created_at`, `updated_at`) VALUES ('dojo2', now(),now());
INSERT INTO `dojos_and_ninjas`.`dojos` (`name`, `created_at`, `updated_at`) VALUES ('dojo3', now(),now());


INSERT INTO `dojos_and_ninjas`.`ninjas` (`id`,`first_name`, `last_name`, `age`, `created_at`, `updated_at`, `dojo_id`) VALUES   
(1,'ninja1/dojo1', 'cat', '10', now() ,now(), 1);
INSERT INTO `dojos_and_ninjas`.`ninjas` (`id`,`first_name`, `last_name`, `age`, `created_at`, `updated_at`, `dojo_id`) VALUES    
(2,'ninja2/dojo1', 'dog', '20', now() ,now(), 1);
INSERT INTO `dojos_and_ninjas`.`ninjas` (`id`,`first_name`, `last_name`, `age`, `created_at`, `updated_at`, `dojo_id`) VALUES   
(3,'ninja3/dojo1', 'cat', '30', now() ,now(), 1);

INSERT INTO `dojos_and_ninjas`.`ninjas` (`id`,`first_name`, `last_name`, `age`, `created_at`, `updated_at`, `dojo_id`) VALUES           
(4,'ninja1/dojo1', 'cat', '10', now() ,now(), 2);
INSERT INTO `dojos_and_ninjas`.`ninjas` (`id`,`first_name`, `last_name`, `age`, `created_at`, `updated_at`, `dojo_id`) VALUES    
(5,'ninja2/dojo1', 'dog', '20', now() ,now(), 2);
INSERT INTO `dojos_and_ninjas`.`ninjas` (`id`,`first_name`, `last_name`, `age`, `created_at`, `updated_at`, `dojo_id`) VALUES   
(6,'ninja3/dojo1', 'cat', '30', now() ,now(), 2);

INSERT INTO `dojos_and_ninjas`.`ninjas` (`id`,`first_name`, `last_name`, `age`, `created_at`, `updated_at`, `dojo_id`) VALUES           
(7,'ninja1/dojo1', 'cat', '10', now() ,now(), 3);
INSERT INTO `dojos_and_ninjas`.`ninjas` (`id`,`first_name`, `last_name`, `age`, `created_at`, `updated_at`, `dojo_id`) VALUES    
(8,'ninja2/dojo1', 'dog', '20', now() ,now(), 3);
INSERT INTO `dojos_and_ninjas`.`ninjas` (`id`,`first_name`, `last_name`, `age`, `created_at`, `updated_at`, `dojo_id`) VALUES   
(9,'ninja3/dojo1', 'cat', '30', now() ,now(), 3);   
	
SELECT * FROM dojos_and_ninjas.ninjas where dojo_id=1;

SELECT * FROM dojos_and_ninjas.ninjas where dojo_id=3;


SELECT name FROM dojos_and_ninjas.dojos
JOIN dojos_and_ninjas.ninjas ON ninjas.dojo_id = dojos.id
where dojo_id=3;