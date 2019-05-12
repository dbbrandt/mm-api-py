This is a light wrapper for mlmmapi to support web requests to correct_answer.

Setup:

1. sudo to precidix
2. cd srv
3. git clone https://[gitusername]@github.com/dbbrandt/mm-api-py.git
    * Provided password at prompt
4. Install python 3.6
    * Sudo yum install 3.6
    * yum install python36-devel. (For buing gcc packages like python-Levenshtein
5. Install pip
    * python3 -m pip install --user --upgrade pip
6. Setup venv
    * python3 -m pip install --user virtualenv
7. Create a virtual environment
    * python3 -m venv env
8. Attache to the venv
    * source env/bin/activate
9. Install the needed packages
    * fuzzywuzzy
    * python-Levenshtein  
    * numpy
    * pandas
    * scikit-learn version 0.20.3. (for the model dump).   Pip3 install scikit-learn==0.20.3
    * xgboost
    * Joblib
    * flask
    * mlmmapi
    * uwsgi
10. Update nginx config
    * Edit /etc/nginx/conf.d/mm-api_prodution.conf
    * Add the lines under the location @puma_mm-api_production used for the normal mm-api rails app.
    
           location /mm-api-py {
             include uwsgi_params;
             uwsgi_pass unix:/tmp/mm-api-py.sock;
           }
           
11. Run the uwsgi application
    * Got the /users/precidix/srv/mm-api-py directory
    * Run:
    * uwsgi —ini wsgi.ini &
12. Test and Restart nginx
    * sudo /etc/init.d/nginx configtest
    * sudo /etc/init.d/nginx restart
