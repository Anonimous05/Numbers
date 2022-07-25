<h1 align="center">Canal Service Test Task</h1>
<h2>How start the project?</h2>
<h3>IMPORTANT: fill in the .env file by .env.example</h3>
<ul>
<li style="font-weight: bold">If you want start project with Docker</li>
<ul> 
    <li style="font-weight: bold; margin-top: 20px;">Inside the repository there is .env.example, you need to create .env according to the template .env.example</li>  
<li>
    
    CanalService/: docker-compose up --build
</li> 
<li>

    CanalService/: docker-compose run backend sh -c "./manage.py runscript add_default_superuser"
</li> 
</ul>
<li style="font-weight: bold">If you want start without Docker</li>
<ul>
<li>

    CanalService/backend: python3 -m venv venv
</li>
<li>

    CanalService/backend: pip install -r requirements.txt
</li>
<li>

    CanalService/backend: python manage.py runserver
</li> 
<li>

    CanalService/frontend: npm install
</li>
<li>

    CanalService/frontend: npm start
</li>
</ul>
</ul>
