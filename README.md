<h1 align="center">Numbers Test Task</h1>
<h2>How start the project?</h2>
<h3>IMPORTANT: fill in the .env file by .env.example</h3>
<ul>
<li style="font-weight: bold">If you want start project with Docker</li>
<ul> 
    <li style="font-weight: bold; margin-top: 20px;">Inside the repository there is .env.example, you need to create .env according to the template .env.example</li>  
<li>
    
    Numbers/: docker-compose up --build
</li> 
<li>

    Numbers/: docker-compose run backend sh -c "./manage.py runscript add_default_superuser"
</li> 
</ul>
<li style="font-weight: bold">If you want start without Docker</li>
<ul>
<li>

    Numbers/backend: python3 -m venv venv
</li>
<li>

    Numbers/backend: pip install -r requirements.txt
</li>
<li>

    Numbers/backend: python manage.py runserver
</li> 
<li>

    Numbers/frontend: npm install
</li>
<li>

    Numbers/frontend: npm start
</li>
</ul>
</ul>