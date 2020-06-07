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

streaming_service = Streaming_Service(True)
print(streaming_service.checkStreamingService())
movie_on_demand_service = Movie_On_Demand_Service(True)
print(movie_on_demand_service.checkMovieOnDemandService())

streaming_container = Streaming_Movies_Container([streaming1,streaming2,streaming3],{streaming7:5,streaming8:2})
print(f'Live Streams: {streaming_container.getLiveStreams()}')
print(f'prwto stin lista live stream: {streaming_container.getLiveStreams()[0]}')
streaming_container.addLiveStream(streaming4)
streaming_container.addUpcomingStream(streaming9,10)
print(f'Live streams: {streaming_container.getLiveStreams()}')
print(f'Upcoming Stream: {streaming_container.getUpcomingStreams()}')
print(streaming_container.retrieveLiveStreams())
print(streaming_container.retrieveUpcomingStreams(3))
streaming3.setPeopleWatchingNow(33)
streaming3.updatePeopleWatchingNow()
streaming3.setMaxPeopleWatching(50)
print(f'Epeidi 34<50 tha epistrepsei true kai exw : {streaming_container.checkWatchingNow(streaming3)}')

movie1 = Movie('Logan','James Mangold','Action',['Hugh Jackman','Dafne Keen'])
movie2 = Movie('Wolf Of Wallstreet','Martin Scorsese','Comedy',['Leonardo DiCaprio','Margot Robbie'])
movie3 = Movie('Avatar','James Cameron','Sci-Fi',['Sam Worthington','Zoe Zaldana'])
movie4 = Movie('Dunkirk','Christopher Nolan','Action',['Harry Styles','Cillian Murphy'])
movie5 = Movie('Blade Runner','Denis Villeneuve','Sci-Fi',['Ryan Gosling','Ann De Armas'])
upcoming_movie1 = Movie('Killers of the flower Moon','Martin Scorsese','Drama',['Robert DeNiro','Leonardo DiCaprio'])
upcoming_movie2 = Movie('Avatar 2','James Cameron','Sci-Fi',['Sam Worthington','Zoe Zaldana'])
upcoming_movie3 = Movie('Anerxomeni3','Unknown','Action',['prwtos','deuteros'])

company = Company(1)

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

cinema1.setPeakHours(0,34) # 0 ennow stis5
cinema1.setPeakHours(1,70)
cinema1.setPeakHours(2,70)
cinema1.setPeakHours(3,62)
cinema1.setPeakHours(4,80)
cinema1.setPeakHours(5,115)
cinema1.setPeakHours(6,120)
cinema1.setPeakHours(7,100)
cinema1.setPeakHours(8,90)

cinema2.setPeakHours(0,52)
cinema2.setPeakHours(1,25)
cinema2.setPeakHours(2,80)
cinema2.setPeakHours(3,100)
cinema2.setPeakHours(4,150)
cinema2.setPeakHours(5,200)
cinema2.setPeakHours(6,20)
cinema2.setPeakHours(7,42)
cinema2.setPeakHours(8,30)

cinema6.setPeakHours(0,70)
cinema6.setPeakHours(1,85)
cinema6.setPeakHours(2,56)
cinema6.setPeakHours(3,90)
cinema6.setPeakHours(4,80)
cinema6.setPeakHours(5,60)
cinema6.setPeakHours(6,70)
cinema6.setPeakHours(7,45)
cinema6.setPeakHours(8,78)

cinema1.getScreeningHalls()[0].reserveSeats([[1,1],[1,2],[1,3]])
print(f'Gia na doume oti i thesi ontws kratithike : {cinema1.getScreeningHalls()[0].getSeats()[1].getTaken()}')

company.addPastMovie(movie1) # na valw pros=igoumenes tainies gia na ginei provlepsi
company.addPastMovie(movie2)
company.addPastMovie(movie3)
company.addPastMovie(movie4)
company.addPastMovie(movie5)
company.addPastMovie(movie6)
print(company.getPastMovies()[5].getTitle())
print(f'Anamenomena esoda upcoming_movie1(Killers of the flower moon) : {company.estimateMovieTickets(upcoming_movie1)}') #  na dwsw mia pou na exei koinouw prwtaginistes kai eidos
print(f'Anamenomena eisitiria upcoming_movie1(killers of the flower moon): {company.estimateMovieEarnings(upcoming_movie1)}') # i skinotheti mono idio klp
print(f'Anamenomena esoda upcoming_movie2 (Avatar 2){company.estimateMovieEarnings(upcoming_movie2)}')
print(f'Anamemonema eisitiria upcoming_movie2(avatar 2): {company.estimateMovieTickets(upcoming_movie2)}')

company.addCinema(cinema1)
company.addCinema(cinema2)
company.addCinema(cinema3)
company.addCinema(cinema4)
company.addCinema(cinema5)
company.addCinema(cinema6)
company.addCinema(cinema7)
print(f'Peak hours gia oli tin epixeirisi : {company.calculatePeakHours()}')
print(f'Plithos kosmou pou episkefthike to cinema1 ana wra: {cinema1.getPeakHours()}')
print(f'Peak Hours gia to cinema1:{cinema1.calculatePeak()}')

cinema1.updateEarnings(9230.)
cinema1.updateTickets(270)
cinema2.updateEarnings(8745.)
cinema2.updateTickets(300)
cinema3.updateEarnings(10423.)
cinema3.updateTickets(657)
cinema4.updateEarnings(3451)
cinema4.updateTickets(254)
print(f'Eisitiria gia kathe cinema kai athroistika: {company.retrieveCinemasTickets()}')
print(f'Esoda gia kathe cinema kai athroistika: {company.retrieveCinemasEarnings()}')

ratings = Ratings()
ratings.addClientToLog(client1)
ratings.addClientToLog(client2)
ratings.addClientToLog(client3)
ratings.addClientToLog(client4)

ratings.registerRating(client1,streaming1,9)
ratings.registerRating(client1,streaming2,7)
ratings.registerRating(client1,streaming3,8)
ratings.registerRating(client1,streaming4,9)
ratings.registerRating(client1,streaming5,8)
ratings.registerRating(client1,classic1,10)
ratings.registerRating(client1,classic2,10)
ratings.registerRating(client1,classic3,10)
ratings.registerRating(client1,classic4,10)
ratings.registerRating(client1,classic5,10)

ratings.registerRating(client2,classic2,8)
ratings.registerRating(client2,streaming1,6)
ratings.registerRating(client2,streaming5,8)
ratings.registerRating(client3,streaming7,10)
ratings.registerRating(client3,streaming8,6)
ratings.registerRating(client4,classic8,9)


print(f'H lista twn aksilogisewn einai {ratings.getRatingsLog()}')
print(f'Elegxos aksiologimenwn tainiwn tou client1 : {ratings.checkRatedMovies(client1)}')
print(f'Elegxos aksiologimenvn klasikwn tou client1: {ratings.checkRatedClassicMovies(client1)}')
print(f'Elegxos aksilogimwn tainiwn client2: {ratings.checkRatedClassicMovies(client2)}, client3: {ratings.checkRatedClassicMovies(client3)} kai client4: {ratings.checkRatedClassicMovies(client4)}')

print(f'Einai i kritiki ok?? -> {ratings.validateRatingAndCritique(8,"Τέλεια ταινία. Υπέροχη σκηνοθεσία και σενάριο")}')

classic1.setMeanRating(9.8)
classic2.setMeanRating(9.2)
classic3.setMeanRating(9)
classic4.setMeanRating(8.7)
classic5.setMeanRating(9.3)
classic6.setMeanRating(10)
omades = Omades()
omades.addClassic(classic1)
omades.addClassic(classic2)
omades.addClassic(classic3)
omades.addClassic(classic4)
omades.addClassic(classic5)
print(f'Oi Kaliteres klasikes taksinomimenes me vasi tin mesi vathmologia tous: {omades.retrieveBestClassics()}')
omades.addClassic(classic6)
print(f'Oi kaliteres klasikes taksinomimenes me vasi tin mesi vathmologia tous: {omades.retrieveBestClassics()}')

streaming1.setMeanRating(7.3)
streaming2.setMeanRating(8.7)
streaming3.setMeanRating(6.7)
streaming4.setMeanRating(9.2)
streaming5.setMeanRating(7.8)
mainstream1 = Mainstream_Movie('Panic Room','David Fincher','Thriller',['Jodie Foster','Forest Whitaker'],2002)
mainstream2 = Mainstream_Movie('Zodiac','David Fincher','Thriller',['Jake Gyllenhaal','Mark Ruffalo'],2007)
mainstream3 = Mainstream_Movie('The Hobbit: An unexpected Journey','Peter Jackson','Adventure',['Martin Freeman','Ian Mckellen'],2012)
mainstream1.setMeanRating(8.5)
mainstream2.setMeanRating(8.8)
mainstream3.setMeanRating(7.8)
omades.addMainstream(mainstream1)
omades.addMainstream(mainstream2)
omades.addMainstream(mainstream3)
print(f'Oi kalitera on demand movies taksinomimenes : {omades.retrieveBestMovies()}')

      
priority_queue = Priority_Queue()
priority_queue.insertToPriorityQueue(client1)
priority_queue.insertToPriorityQueue(client2)
print(f'Pelates se oura anamonis: {priority_queue.getOnHold()}')
# estw thelei kratisi gia tainia stis 22:30
print(f'Xronos pou apomenei mexri tin dinatotita kratisis: {priority_queue.calculateReservationTime(22,30,00)}')
