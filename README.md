clone repo "git clone https://github.com/Ruslan-Panenko/mobile_service.git"

run docker-compose "docker-compose up"

run migrations:

    enter in django container "docker exec -ti <container_id> bash"
    
    run command "python manage.py makemigrations"
    
    and "python manage.py migrate"
    
open '0.0.0.0:8000'




TimeSheet

------------------------
05.08.2022
10:00-12:00
- started project
- created models file
------------------------

------------------------
08.08.2022
14:00-17:00
- created auth app
- created logic for auth
------------------------


------------------------
09.08.2022
9:00-15:00
- created service app
- created logic for users
------------------------


------------------------
10.08.2022
10:00-12:30
- created logic for masters
- pushed project on github
------------------------
