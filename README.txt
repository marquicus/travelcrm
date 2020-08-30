
TravelCRM
========================

Basic setup instructions in 2020 to run this project with deprecated python 2

1. Create virtualenv
```
   mkvirtualenv -p python2 travelcrm
```
2. Install application
```
   python setup.py develop
```
3. Start DB instance (non persistent postgres container db called `travelcrm` with admin/secret credentials)
```
   docker run -it --rm --name travel-postgres -p 5432:5432 -e POSTGRES_DB=travelcrm -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=secret postgres:9.6-alpine
```
4. Load dump found in `sql/travelcrm.sql`
```
   psql -hlocalhost -p5432 -Uadmin -dtravelcrm -W  -f sql/travelcrm.sql
```
5. Run
```
   pserve development.ini
```

Seems thats all, must works :), now open browser in http://localhost:6543 with admin:adminadmin


Dependencies
---------------

- git >= 2 <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>
- python2 >= 2.7 <http://www.python.org/getit/>
- docker >= 1.12 <https://docs.docker.com/get-started/>
- postgresql >= 9.6 <https://www.postgresql.org/download/>

Reference
---------------

Take a look at the docs for more information.

* https://www.python.org/
* https://trypyramid.com/


