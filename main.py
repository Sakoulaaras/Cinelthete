from Admin import Admin
from Cinema import Cinema
from Classic_Movie import Classic_Movie
from Client import Client
from Company import Company
from Credit_Card import Credit_Card
from Mainstream_Movie import Mainstream_Movie
from Movie_On_Demand_Service import Movie_On_Demand_Service
from Movie_On_Demand import Movie_On_Demand
from Movie import Movie
from Omades import Omades
from Prepaid_Card import Prepaid_Card
from Priority_Queue import Priority_Queue
from Ratings import Ratings
from Recommended_Movie import Recommended_Movie
from Screening_Hall import Screening_Hall
from Seat import Seat
from Streaming_Movie import Streaming_Movie
from Streaming_Movies_Container import Streaming_Movies_Container
from Streaming_Service import Streaming_Service
from Ticket import Ticket
from Trading_System import Trading_System





client1 = Client('kostis','Petrakis','kpetrakis@ceid.upatras.gr',25)
client2 = Client('Vaggelis','Petrakis','vpetrakis@ceid.upatras.gr',24)
client3 = Client('Petros','Eleutheriadis','peleutheriadis@ceid.upatras.gr',24)
client4 = Client('Antonis','Karvounis','akarvounis@ceid.upatras.gr',24)

classic1 = Classic_Movie('GoodFellas','Martin Scorsese','Gangster',['Robert DeNiro','Joe Pesci','Liotta'],1980)
classic2 = Classic_Movie('The Godfather','Francis Ford Coppola','Crime',['Marlon Brando','Al Pacino'],1976)
classic3 = Classic_Movie('Taxi Driver','Martin Scorsese','Drama',['Robert DeNiro','Jodie Foster','Harvey Keitel'],1976)
classic4 = Classic_Movie('2001: A Space Odyssey','Stanley Kubrick','Sci-Fi',['Richard Strauss','Gyorgi Ligeti'],1968)
classic5 = Classic_Movie('The Shining','Stanley Kubrick','Horror',['Jack Nicholson','Shelley Duvall'],1980)
classic6 = Classic_Movie('Citizen Kane','Orson Welles','Drama',['Orson Welles','Ruth Warrick'],1941)
classic7 = Classic_Movie('Vertigo','Alfred Hitchock','',['Kim Novak','James Stewart'],1958)
classic8 = Classic_Movie('Raging Bull','Martin Scorsese','Drama',['Robert DeNiro','Joe Pesci'],1980)
classic9 = Classic_Movie('Psycho','Alfred Hitchock','Horror',['Anthony Perkins','Janet Leigh'],1960)
classic10 = Classic_Movie("Schindler's List",'Steven Spielberg','War',['Liam Neeson','Ralph Fiennes','Ben Kingsley'],1993)

streaming1 = Streaming_Movie('The Irishman','Martin Scorsese','Drama',['Robert DeNiro','Al Pacino','Joe Pesci'])
streaming2 = Streaming_Movie('Endgame','Russo Brothers','Sci-Fi',['Robert Downey Jr','Chris Evans','Josh Brolin'])
streaming3 = Streaming_Movie('Joker','Todd Phillips','Drama',['Joaquin Phoenix','Robert DeNiro', 'Zazie Beetz'])
streaming4 = Streaming_Movie('Once Upon A Time in Hollywood','Quentin Tarantino','Comedy',['Leonardo DiCaprio','Bradd Pitt','Margot Robbie'])
streaming5 = Streaming_Movie('John Wick 3','Chad Stahelski','Action',['Keanu Reeves','Halle Barry'])
streaming6 = Streaming_Movie('1917','Sam Mendes','Action',['George MacKay','Dean Charles Chapman'])
streaming7 = Streaming_Movie('Ford v Ferrari','James Mangold','Action',['Christian Bale','Matt Damon'])
streaming8 = Streaming_Movie('The Lighthouse','Robert Eggers','Drama',['Robert Pattison','Williem Dafoe'])
streaming9 = Streaming_Movie('Infinity War','Russo Brothers','Sci-Fi',['Robert Downey Jr','Chris Evans','Josh Brolin'])

movie1 = Movie('Logan','James Mangold','Action',['Hugh Jackman','Dafne Keen'])
movie2 = Movie('Wolf Of Wallstreet','Martin Scorsese','Comedy',['Leonardo DiCaprio','Margot Robbie'])
movie3 = Movie('Avatar','James Cameron','Sci-Fi',['Sam Worthington','Zoe Zaldana'])
movie4 = Movie('Dunkirk','Christopher Nolan','Action',['Harry Styles','Cillian Murphy'])
movie5 = Movie('Blade Runner','Denis Villeneuve','Sci-Fi',['Ryan Gosling','Ann De Armas'])
upcoming_movie1 = Movie('Killers of the flower Moon','Martin Scorsese','Drama',['Robert DeNiro','Leonardo DiCaprio'])
upcoming_movie2 = Movie('Avatar 2','James Cameron','Sci-Fi',['Sam Worthington','Zoe Zaldana'])
upcoming_movie3 = Movie('Anerxomeni3','Unknown','Action',['prwtos','deuteros'])

cinema1 = Cinema('Athina',20)
cinema2 = Cinema('Thesaloniki',15)
cinema3 = Cinema('Volos',10)
cinema4 = Cinema('Xalkida',2)
cinema5 = Cinema('Larisa',10)
cinema6 = Cinema('Kifisia',15)
cinema7 = Cinema('Pireas',10)
cinema8 = Cinema('Xania',5)
cinema9 = Cinema('Ioannina',8)
cinema10 = Cinema('Alexandroupoli',3)
