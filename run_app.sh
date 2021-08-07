#!/bin/sh
export FLASK_APP=main.py 
flask run

# PUT IN README:
# for above code to be executed, need to run following once in terminal:
# $ chmod +x run_app.sh
# Then every time I want to run the local server, instead of writing "flask run", I will write:
# $ ./run_app.sh