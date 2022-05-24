Projekt navn: Pris sammenligner for dagligvare.

Projektet webscraper for tre forskellige daglivare butikker, (Bilka, Føtex og Nemlig) og vurderer ud fra kiloprisen hvilken butik der har den største samlede besparelse. 

Liste af brugte teknologier:
Tesseract(image recognition)
Request_html(webscraping)
Numpy(Dataformatering)
Pandas(Data præsentation)
Matplotlib(Visuel præsentation af data)

Installations guide:
den nyeste versioner af notebooken fra github skal være buildet(docker-compose --build).

User guide:
først skal en bruge tage et billede af en inkøbsliste(fra pc eller telefon),
derefter skal billedet gemmes i Modules mappen, og billedets filnavn skal indsættes i img_to_list metoden på linje 122 i main.py filen.
hvorefter main.py skal køres fra konsollen.

Status:
billedgenkendelse og konvertiering til lister er færdigt dog ikke præcist nok til håndskrevet data.
webscraping af Bilka er færdigt, men kunne ikke løse timeout problemer ift. Nemlig og Føtex.
dataen bliver konverteret til dataset med numpy og analyseret ift. laveste pris pr. enhed.
inkøbslisten med priser bliver vist med pandas.
En visuel representation af dataen bliver vist med matplotlib.

List of challanges:
en udfordring var at arbejde med tesseract-ocr