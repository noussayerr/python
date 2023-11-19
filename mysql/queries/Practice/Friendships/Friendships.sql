INSERT INTO `friendships`.`users` (`id`, `first_name`, `last_name`, `created_at`, `updated_at`) VALUES ('1', 'noussayer', 'rahal', now(), now()) ,('2', 'Amy', 'Giver', now(), now()),('3', 'Eli', 'Byers', now(), now()),('4', 'Marky ', 'Mark', now(), now()),('5', 'Big', 'Bird', now(), now()),('6', 'Kermit', 'The Frog', now(), now());INSERT INTO `friendships`.`users` (`id`, `first_name`, `last_name`, `created_at`, `updated_at`) VALUES ('1', 'noussayer', 'rahal', now(), now()) ,('2', 'Amy', 'Giver', now(), now()),('3', 'Eli', 'Byers', now(), now()),('4', 'Marky ', 'Mark', now(), now()),('5', 'Big', 'Bird', now(), now()),('6', 'Kermit', 'The Frog', now(), now());

INSERT INTO friendships (`id`,`user_id`, `frind_id`, `created_at`, `updated_at`) VALUES ('1', '1', '2', now(), now()) ,('2', '1', '4', now(), now()),('3', '1', '6', now(), now());

INSERT INTO friendships (`id`,`user_id`, `frind_id`, `created_at`, `updated_at`) VALUES ('4', '2', '1', now(), now()) ,('5', '2', '3', now(), now()),('6', '2', '5', now(), now());

INSERT INTO friendships (`id`,`user_id`, `frind_id`, `created_at`, `updated_at`) VALUES ('7', '3', '2', now(), now()) ,('8', '3', '5', now(), now());

INSERT INTO friendships (`id`,`user_id`, `frind_id`, `created_at`, `updated_at`) VALUES ('9', '4', '3', now(), now());

INSERT INTO friendships (`id`,`user_id`, `frind_id`, `created_at`, `updated_at`) VALUES ('10', '5', '1', now(), now()),('11', '5', '6', now(), now());

INSERT INTO friendships (`id`,`user_id`, `frind_id`, `created_at`, `updated_at`) VALUES ('12', '6', '2', now(), now()),('13', '6', '3', now(), now());

SELECT users.first_name ,users.last_name,user2.first_name as friend_first_name,user2.last_name as friend_last_name from users
JOIN friendships ON friendships.user_id=users.id
LEFT JOIN users as user2 ON friendships.frind_id=user2.id;

SELECT 	user2.first_name as friend_first_name,user2.last_name as friend_last_name from users
JOIN friendships ON friendships.user_id=users.id
LEFT JOIN users as user2 ON friendships.frind_id=user2.id
where friendships.user_id=1;

SELECT count(id) FROM friendships;