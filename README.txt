
TravelCRM
========================

Basic setup instructions in 2020 to run this project with deprecated python 2

1. Create virtualenv
```
   mkvirtualenv -p python2 travelcrm
```
2. Install dependencies
```
   make dependencies
```
3. Deploy once all the environment (will start and populate db)
```
   make deploy
```

Seems thats all, must works :), now open browser in http://localhost:6543 with admin:adminadmin

Other userful commands
```
   make run  # to run the application once the environment is up
   make stop  # to stop all environment
   make test  # will run tests (TODO)
   make build-docs  # build docs
```


Dependencies
---------------

- git >= 2 <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>
- make >= 4 <https://www.gnu.org/software/make/>
- python2 >= 2.7 <http://www.python.org/getit/>
- docker >= 1.12 <https://docs.docker.com/get-started/>
- postgresql >= 9.6 <https://www.postgresql.org/download/>

Reference
---------------

Take a look at the docs for more information.

* https://www.python.org/
* https://trypyramid.com/


