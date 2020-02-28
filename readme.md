# jak to rozjet?
1. nainstalovat venv, https://docs.python.org/3/library/venv.html
2. vytvorit virtualni prostredi v svinov2/venv napr.
3. aktivovat venv, source venv/bin/activate
4. pip install -r requirements.txt
5. ./manage.py migrate
6. ./manage.py syncdb, tady se vytvori uzivatel
7. ./manage.py runserver, pres v minulem kroku vytvoreneho uzivatele se prihlas na 
    localhost:8000/admin. tam v zalozce sekce vyvor sekci s nazvem index. je to potreba,
    aby to fungovalo
8. ted uz by to melo fungovat. akorat se mi tam neserviruje staticky content (vypada to hnusne).
    mozna zkusit ./manage.py collectstatic. jinak se to nechava jako domaci ukol :D