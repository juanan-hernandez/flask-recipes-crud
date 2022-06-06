CREATE TYPE category AS ENUM ('STARTER', 'SIDE_DISH', 'MAIN_COURSE', 'DRINK', 'DESSERT');
CREATE TYPE country AS ENUM ('SPAIN', 'PORTUGAL', 'ITALY', 'FRANCE', 'GERMANY');
CREATE TYPE difficulty AS ENUM ('VERY_EASY', 'EASY', 'NORMAL', 'DIFFICULT', 'VERY_DIFFICULT');

CREATE TABLE IF NOT EXISTS recipe (
   id SERIAL PRIMARY KEY,
   name VARCHAR (50) NOT NULL UNIQUE,
   country country,
   category category,
   difficulty difficulty,
   url VARCHAR NOT NULL,
   time INTEGER
);

INSERT INTO recipe (name, country, category, difficulty, url, time)
VALUES 
   ('Sapnish omelette', 'SPAIN', 'MAIN_COURSE', 'VERY_DIFFICULT', 'https://spanishsabores.com/best-spanish-omelet-recipe/', 75),
   ('Pizza', 'ITALY', 'MAIN_COURSE', 'DIFFICULT', 'https://www.simplyrecipes.com/recipes/homemade_pizza/', 120),
   ('Gougères ', 'FRANCE', 'STARTER', 'DIFFICULT', 'https://www.foodandwine.com/recipes/alain-ducasses-gougeres', 45),
   ('Bacalhau a Bras', 'PORTUGAL', 'MAIN_COURSE', 'NORMAL', 'https://www.finedininglovers.com/recipes/main-course/bacalhau-bras-traditional-recipe', 40),
   ('Apple Strudel', 'GERMANY', 'DESSERT', 'NORMAL', 'https://platedcravings.com/apple-strudel-recipe/', 60);