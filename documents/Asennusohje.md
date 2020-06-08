## Sovelluksen käyttäminen paikallisesti

* Asenna tietokoneelle Python
* Lataa projekti, joko Cloonaamalla Repositori tai lataamalla se
* Pura zip-kansio 
* Terminaalin avulla luo projektinjuurikansioon venv-virtuaaliympäristö. Komento:
`
python3 -m venv venv
`
* Aktivoi virtuualiympäristö. Komento:
`
source venv/bin/activate
`
* Lataa projektin tarvitseman riippuvuudet. Komento:
`
pip install -r requirements.txt
`
* Käynnistä sovellus projektinjuurikansiosta. Komento:
`
python3 run.py
`
* Mene selaimella osoittee: http://localhost:5000/

