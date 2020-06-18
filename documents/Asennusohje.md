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

## Heroku

* Heroku CLI-työkalun ja tunnukset

* gunicorning asenneus 

`
pip install gunicorn
`

* Procfilen luominen

`
echo "web: gunicorn --preload --workers 1 hello:app" > Procfile
`

* Herokuun sovellukselle paikan luominen

`
heroku create "haluttu nimi"
`

* Paikalliseen versionhallintaan tieto Herokusta

`
git remote add heroku https://git.heroku.com/"haluttu nimi"
`

* Asetetaan Herokun HEROKU-ympäristömuuttujan arvoksi 1

`
heroku config:set HEROKU=1
`

* Lisätään Herokuun Postgre- tietokanta

`
heroku addons:add heroku-postgresql:hobby-dev
`


* Lähetetään Projekti Herokkun

`
git add .
git commit -m "viesti"
git push heroku master
`
