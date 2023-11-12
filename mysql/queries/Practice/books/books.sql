insert into `books`.`users`(`name`,`created_at`,`updated_at`) values ('Jane Amsden',now(),now()),('Emily Dixon',now(),now()),('Theodore Dostoevsky',now(),now()),('William Shapiro',now(),now()),('Lao Xiu',now(),now());

insert into `books`.`books`(`id`,`title`,`created_at`,`updated_at`) values(1,'C Sharp',now(),now()),(2,'java',now(),now()),(3,'Python',now(),now()),(4,'php',now(),now()),(5,'ruby',now(),now());

update `books`.`books` set title='c #' where id=1;

update `books`.`users` set name='bill' where id=4;

insert into `books`.`favorites` (`user_id`,`book_id`)values (1,1),(1,2),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(3,4),(4,1),(4,2),(4,3),(4,4),(4,5);

select name from `books`.`users` 
join `books`.`favorites` on favorites.user_id=users.id
where favorites.book_id=3;

delete from `books`.`favorites` where user_id=2 and book_id=3;

insert into `books`.`favorites` (`user_id`,`book_id`)values(5,2);

select title from `books`.`books` 
join `books`.`favorites` on favorites.book_id=books.id
where user_id=3;

select name from `books`.`users` 
join `books`.`favorites` on favorites.user_id=users.id
where favorites.book_id=5;