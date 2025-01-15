# TO-ADD on ReadMe

- List of group members with a short description (one sentence) of what each member was assigned to do, and what they actually did in terms of contributing to the final deliverable (we can use tasks assignment in github)
- the URL of your deployed application
- the username and password for the admin user
- the username and passwords of at least 5 of the test users

# Group 7

| Member                         | Assigned                                                                                 | Finished tasks                                                                                       |
| ------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Sai Sandeep Vemula (220224206) | Friendship models and views and front end, Friend Requests page (back end and front end) | Friendship model and views, log in and authentication, Friends Request and Find Friends Back-end     |
| Ilenia Maietta (220322742)     | UserHobby model and views, Hobby list (front end and back end)                           | UserHobby model and views, Hobby List front and back-end, Find Friends and Friends Request Front-End |
| Amy Anigboro (220476137)       | Hobby model and views, Update Profile and Password (front end and back end)              | Hobby model and views, Update Profile and Password, Front End Error messages                         |
| Mariam Thabti (2103028471)     | User model and views, authentication and heap for hobbies                                | User model and views, log in, sign up and authentication, maximum heap for hobbies                   |

# URL of Deployed Application

# Admin User Log In Details

- Username: admin@email.com
- Password: admin

# Login details for Test Users

1. User: **Ilenia**, username: `ec22792@qmul.ac.uk`, password: `helloworld123`
2. User: **Sandeep**, username: `ec22898@qmul.ac.uk`, password: `helloworld123`
3. User: **Mariam**, username: `ec22860@qmul.ac.uk`, password: `helloworld123`
4. User: **Amy**, username: `ec22496@qmul.ac.uk`, password: `helloworld123`
5. User: **Konrad**, username: `Konrad@gmail.com`, password: `helloworld123`
6. User: **Gabrielle**, username: `Gabrielle@gmail.com`, password: `helloworld123`
7. User: **Taylor**, username: `Taylor@gmail.com`, password: `helloworld123`
8. User: **Rahul**, username: `Rahul@gmail.com`, password: `helloworld123`
9. User: **Abdullah**, username: `Abdullah@gmail.com`, password: `helloworld123`
10. User: **Nora**, username: `Nora@gmail.com`, password: `helloworld123`
11. User: **Charles**, username: `CharlesLeclerc@gmail.com`, password: `helloworld123`
12. User: **LewisHamilton**, username: `LewisHamilton@gmail.com`, password: `helloworld123`
13. User: **OscarPiastri**, username: `OscarPiastri@gmail.com`, password: `helloworld123`
14. User: **FernandoAlonso**, username: `FernandoAlonso@gmail.com`, password: `helloworld123`
15. User: **LandoNorris**, username: `LandoNorris@gmail.com`, password: `helloworld123`
16. User: **Nico Hulkenberg**, username: `NicoHulk@gmail.com`, password: `helloworld123`
17. User: **Alexander Albon**, username: `AlexAlbon@gmail.com`, password: `helloworld123`
18. User: **Pierre Gasly**, username: `PierreGasly@gmail.com`, password: `helloworld123`
19. User: **Carlos**, username: `Chilli@gmail.com`, password: `helloworld123`
20. User: **Oliver**, username: `Ollie@gmail.com`, password: `helloworld123`
21. User: **Yuki**, username: `YukiTsu@gmail.com`, password: `helloworld123`
22. User: **Lance**, username: `LanceStrolled@gmail.com`, password: `helloworld123`
23. User: **Max**, username: `SuperMax@gmail.com`, password: `helloworld123`
24. User: **Liam**, username: `LiamLawson@gmail.com`, password: `helloworld123`
25. User: **George**, username: `GeorgeRussell@gmail.com`, password: `helloworld123`


# Template for ECS639U Group Coursework

This template should be used as the starting point for your group coursework in the module ECS639U Web Programming (at Queen Mary University of London). Use Git (github.qmul.ac.uk) to collaborate on the coursework with your group members. Module leader: Paulo Oliva <[p.oliva@qmul.ac.uk](mailto:p.oliva@qmul.ac.uk)>

## Local development

To run this project in your development machine, follow these steps:

1. Create and activate a conda environment

2. Download this repo as a zip and add the files to your own private repo.

3. Install Pyhton dependencies (main folder):

   ```console
   $ pip install -r requirements.txt
   ```

4. Create a development database:

   ```console
   $ python manage.py migrate
   ```

5. Install JavaScript dependencies (from 'frontend' folder):

   ```console
   $ npm install
   ```

6. If everything is alright, you should be able to start the Django development server from the main folder:

   ```console
   $ python manage.py runserver
   ```

7. and the Vue server from the 'frontend' sub-folder:

   ```console
   $ npm run dev
   ```

8. Open your browser and go to http://localhost:5173, you will be greeted with a template page.

## OpenShift deployment

Once your project is ready to be deployed you will need to 'build' the Vue app and place it in Django's static folder.

1. The build command in package.json and the vite.config.ts files have already been modified so that when running 'npm run build' the generated JavaScript and CSS files will be placed in the mainapp static folder, and the index.html file will be placed in the templates folder:

   ```console
   $ npm run build
   ```

2. You should then follow the instruction on QM+ on how to deploy your app on EECS's OpenShift live server.

## License

This code is dedicated to the public domain to the maximum extent permitted by applicable law, pursuant to [CC0](http://creativecommons.org/publicdomain/zero/1.0/).
