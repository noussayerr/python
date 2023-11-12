SELECT name FROM dojos_and_ninjas.dojos
JOIN dojos_and_ninjas.ninjas ON ninjas.dojo_id = dojos.id
where dojo_id=3;