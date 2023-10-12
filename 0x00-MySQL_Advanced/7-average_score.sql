-- A procedure to create an average

drop procedure if exists ComputeAverageScoreForUser;
delimiter $$
create procedure ComputeAverageScoreForUser(_id int)
begin
declare scores float;
select avg(score) into scores from corrections where user_id = _id;

update users
set average_score = scores
where id = _id;
end $$