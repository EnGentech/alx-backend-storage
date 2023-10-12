-- created a procedure with three argument 
describe projects;

delimiter $$
create procedure AddBonus(user_id int, project_name varchar(255), score int)
begin
	declare project_id int;
    
    select id into project_id 
    from projects
    where name = project_name;
    
     IF project_id IS NULL THEN
        -- Project doesn't exist, so create it
        INSERT INTO projects (name)
        VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- Insert the correction
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, project_id, score);
END $$
