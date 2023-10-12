-- triger an even when theres an update on an email

drop trigger if exists validate_email
delimiter $$
create trigger validate_email 
before update on users for each row
begin
    if old.email <> new.email then
    set new.valid_email = 0;
end if;
end $$