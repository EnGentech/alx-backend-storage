-- triger an even when theres an update on an email

drop trigger if exists validate_email
delimiter $$
create trigger validate_email 
before update on users for each row
begin
if new.email <> old.email then
set new.valid_email = 1;
end if;
end $$
