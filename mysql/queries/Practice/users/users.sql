insert into `users`.`user` values ('rahal','noussayer','noussayer.rahal.83@gmail.com',now(),now()),('rahal','hassen','hassen,.rahal.83@gmail.com',now(),now()),('dojo','ninja','ninja.dojo.83@gmail.com',now(),now());
delete from `users`.`user`;
insert into `users`.`user` values ('rahal','noussayer','noussayer.rahal.83@gmail.com',now(),now()),('rahal','hassen','hassen,.rahal.83@gmail.com',now(),now()),('dojo','ninja','ninja.dojo.83@gmail.com',now(),now());
select * from `users`.`user`where email='noussayer.rahal.83@gmail.com';
select * from `users`.`user`where id=3;
update `users`.`user` set first_name= 'Pancakes' where id=3;
delete from `users`.`user` where id=2;
select * from `users`.`user` order by (first_name);
select * from `users`.`user` order by (first_name) DESC; 
