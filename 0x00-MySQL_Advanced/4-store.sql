-- A trigger event to decrease the quantity of an item after adding a row
drop trigger if exists decrease_me;

delimiter $$
create trigger decrease_me after insert 
on orders
for each row 
BEGIN
    -- Decrease the quantity of the item associated with the new order
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.number;
END;