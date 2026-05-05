import sqlite3

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    title TEXT,
    genre TEXT,
    image TEXT,
    year INTEGER,
    rating REAL,
    desc TEXT
)
""")

movies = [
("Inception","Sci-Fi,Thriller","inception.jpg",2010,8.8,"A thief who enters people's dreams to steal secrets gets a final chance at redemption."),
("Parasite","Drama,Thriller","parasite.jpg",2019,8.6,"A poor family schemes to infiltrate the lives of a wealthy household."),
("The Dark Knight","Action,Crime","dark_knight.jpg",2008,9.0,"Batman faces chaos when the Joker wreaks havoc on Gotham City."),
("Interstellar","Sci-Fi,Adventure","interstellar.jpg",2014,8.7,"Explorers travel through a wormhole to find a new home for humanity."),
("Joker","Drama,Crime","joker.jpg",2019,8.4,"A failed comedian descends into madness, inspiring a violent revolution."),
("Whiplash","Drama,Music","whiplash.jpg",2014,8.5,"A young drummer’s ambition collides with an abusive instructor’s perfectionism."),
("The Shawshank Redemption","Drama","shawshank.jpg",1994,9.3,"Two imprisoned men form an enduring friendship over years of confinement."),
("La La Land","Romance,Music","lalaland.jpg",2016,8.0,"A jazz musician and an aspiring actress chase dreams and love in LA."),
("Fight Club","Drama","fightclub.jpg",1999,8.8,"An office worker and a soap maker form an underground fight club."),
("The Godfather","Crime,Drama","godfather.jpg",1972,9.2,"An aging patriarch transfers control of his empire to his son."),
("The Social Network","Drama,Biography","social_network.jpg",2010,7.7,"The story behind Facebook’s creation."),
("Avengers: Endgame","Action,Adventure","endgame.jpg",2019,8.4,"The Avengers assemble to undo Thanos’ actions."),
("Get Out","Horror,Thriller","getout.jpg",2017,7.7,"A man uncovers disturbing secrets at his girlfriend’s home."),
("Coco","Animation,Family","coco.jpg",2017,8.4,"A boy enters the Land of the Dead."),
("Spirited Away","Animation,Fantasy","spirited_away.jpg",2001,8.6,"A girl enters a magical world of spirits."),
("The Grand Budapest Hotel","Comedy,Adventure","grand_budapest.jpg",2014,8.1,"A concierge gets entangled in a mystery."),
("Your Name","Animation,Romance","your_name.jpg",2016,8.4,"Two teenagers mysteriously swap bodies."),
("The Prestige","Mystery,Drama","prestige.jpg",2006,8.5,"Two rival magicians compete for fame."),
("The Matrix","Action,Sci-Fi","matrix.jpg",1999,8.7,"A hacker discovers reality is a simulation."),
("Her","Romance,Sci-Fi","her.jpg",2013,8.0,"A man falls in love with an AI."),
("Oppenheimer","Drama,History","oppenheimer.jpg",2023,8.6,"Story of the atomic bomb creator."),
("Little Women","Drama,Romance","little_women.jpg",2019,7.8,"Four sisters navigate life and love."),
("The Pianist","Drama,History","pianist.jpg",2002,8.5,"A pianist survives the Holocaust."),
("The Imitation Game","Biography,Drama","imitation_game.jpg",2014,8.0,"A mathematician cracks Nazi codes."),
("Black Swan","Drama,Thriller","black_swan.jpg",2010,8.0,"A ballerina loses herself in her role."),
("Arrival","Sci-Fi,Drama","arrival.jpg",2016,7.9,"A linguist communicates with aliens."),
("Good Will Hunting","Drama","good_will_hunting.jpg",1997,8.3,"A genius struggles to find direction."),
("Love, Rosie","Romance,Comedy","love_rosie.jpg",2014,7.2,"Friends deal with missed opportunities."),
("The Revenant","Adventure,Drama","revenant.jpg",2015,8.0,"A man seeks revenge in the wild."),
("The Wolf of Wall Street","Comedy,Biography","wolf_wallstreet.jpg",2013,8.2,"Rise and fall of a stockbroker."),
("Dune","Sci-Fi,Adventure","dune.jpg",2021,8.0,"Battle for desert planet Arrakis."),
("Mamma Mia!","Romance,Music,Comedy","mamma_mia.jpg",2008,6.5,"A bride invites three men to find her father."),
("Blade Runner 2049","Sci-Fi,Mystery","blade_runner.jpg",2017,8.0,"A blade runner uncovers secrets."),
("Mad Max: Fury Road","Action,Adventure","mad_max.jpg",2015,8.1,"A rebel escapes a tyrant."),
("The Green Mile","Drama,Fantasy","green_mile.jpg",1999,8.6,"A guard discovers supernatural powers."),
("Eternal Sunshine of the Spotless Mind","Romance,Sci-Fi","eternal_sunshine.jpg",2004,8.3,"A couple erases memories."),
("The Truman Show","Drama,Comedy","truman_show.jpg",1998,8.1,"A man discovers his life is a show."),
("Gone Girl","Thriller,Mystery","gone_girl.jpg",2014,8.1,"A husband becomes a suspect."),
("The Shape of Water","Romance,Fantasy","shape_water.jpg",2017,7.3,"A woman bonds with a creature."),
("Hereditary","Horror,Drama","hereditary.jpg",2018,7.3,"A family uncovers dark secrets."),
("Jojo Rabbit","War,History,Family,Comedy","jojo_rabbit.jpg",2019,7.9,"A boy in Nazi Germany changes perspective."),
("Once Upon a Time in Hollywood","Comedy,Drama","hollywood.jpg",2019,7.6,"An actor navigates Hollywood."),
("Inside Out","Animation,Family","inside_out.jpg",2015,8.1,"Emotions guide a girl."),
("Shutter Island","Thriller,Mystery","shutter_island.jpg",2010,8.2,"A marshal investigates a hospital."),
("Prisoners","Thriller,Crime","prisoners.jpg",2013,8.1,"A father searches for his daughter."),
("Knives Out","Mystery,Comedy","knives_out.jpg",2019,7.9,"A detective investigates a murder."),
("Schindler's List","War,History,Biography,Drama","schindlers_list.jpg",1993,9.0,"A man saves Jews during Holocaust."),
("The Sound of Music","Music,Family,Drama","sound_of_music.jpg",1965,8.0,"A governess brings joy to a family."),
("The Conjuring","Horror,Thriller","conjuring.jpg",2013,7.5,"Paranormal investigators help a family."),
("Hacksaw Ridge","War,Drama,Biography,History","hacksaw_ridge.jpg",2016,8.1,"A medic serves without weapons."),
("Maleficent","Fantasy,Adventure,Family,Action","maleficent.jpg",2014,7.0,"Story of a powerful fairy."),
("Paddington","Family,Comedy,Adventure","paddington.jpg",2014,7.3,"A lovable bear finds a new home in London."),
("The Lion King","Animation,Family,Drama","lion_king.jpg",1994,8.5,"A young lion prince flees his kingdom."),
("Frozen","Animation,Family,Fantasy","frozen.jpg",2013,7.4,"A princess sets out to find her sister with ice powers."),
("Harry Potter and the Sorcerer's Stone","Fantasy,Adventure,Family","harry_potter1.jpg",2001,7.6,"A young boy discovers he is a wizard."),
("Aladdin","Animation,Fantasy,Romance","aladdin.jpg",1992,8.0,"A street boy finds a magical lamp."),
("The Hangover","Comedy","hangover.jpg",2009,7.7,"Friends retrace a wild night in Las Vegas."),
("Home Alone","Comedy,Family","home_alone.jpg",1990,7.7,"A boy defends his home from burglars."),
("Encanto","Animation,Family,Fantasy","encanto.jpg",2021,7.2,"A magical family struggles with hidden tensions."),
("The Greatest Showman","Drama,Music","greatest_showman.jpg",2017,7.5,"A visionary creates a dazzling circus.")
]

cursor.executemany("INSERT INTO movies VALUES (?, ?, ?, ?, ?, ?)", movies)

conn.commit()
conn.close()