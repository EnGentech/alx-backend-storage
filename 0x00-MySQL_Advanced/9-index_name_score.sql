-- creating an index with a certain requirement 

CREATE INDEX idx_name_first_score ON names(name(1), score);