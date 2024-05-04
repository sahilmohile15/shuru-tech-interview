# Shuru Tech Interview Project

## Project Setup
download the project via git and follow the instructions given below

1. Initialize a env
   
    ``` python -m venv venv ```

2. Navigate to the project
   
    ``` cd django_boilerplate ```

3. Install the required dependencies and packages
   
    ``` pip install -r requirements.txt ```

4. Migrate the changes
   
    ``` python3 manage.py migrate ```

5. Run the django server
    
    ``` python3 manage.py runserver```


## Models
1. Matches
    - id (Automated field)
    - date_of_match (datetime field)
    - venue (string field)
    - player_of_match (string field)
    - teams (many field)
    - declared (boolean)

2. Teams
    - id (Automated field)
    - name (string field)
    - wins (integer field)
    - losses (integer field)

3. Players
    - id (Automated field)
    - name (string field)
    - team (foreign field)
