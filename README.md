# Group 7
## READ.ME content
- Member assigned and finished tasks
- URL of deployed application
- Admin user log in details
- Log in details for test users
- Notes on E2E selenium-based testing
- Instruction from original template repo
  
# Member assigned and finished tasks
| Member                         | Assigned                                                                                 | Finished tasks                                                                                       |
| ------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Sai Sandeep Vemula (220224206) | Friendship models and views and front end, Friend Requests page back-end and front-end | Friendship model and views, log in and authentication, Friends Request and Find Friends back-end, Authentication, Testing   |
| Ilenia Maietta (220322742)     | UserHobby model and views, Hobby list front-end and back-end                           | UserHobby model and views, Hobby List front-end and back-end, Find Friends and Friends Request front-end, Front-end Error messages, Authentication, Testing |
| Amy Anigboro (220476137)       | Hobby model and views, Update Profile and Password front-end and back-end            | Hobby model and views, Update Profile and Password front-end and back-end, Front-end Error messages, Testing                        |
| Mariam Thabti (2103028471)     | User model and views, authentication and heap for hobbies                                | User model and views, log in, sign up and authentication, maximum heap for hobbies, Authentication, Testing                  |

# URL of Deployed Application
[https://group7-web-apps-ec22792.apps.a.comp-teach.qmul.ac.uk](https://group7-web-apps-ec22792.apps.a.comp-teach.qmul.ac.uk)

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

# Notes on E2E selenium-based testing
The testing is set up to run continuously, as if a person was manually testing the website. We set up a series of helper functions, called in a class called test_new_user in the following order:
1. Account creation/ sign up a new user called 'New User', and then it logs out.
2. Log in: it logs in with the 'New User' credentials
3. Editing all the user's data on their profile page: it updates the password, first and last name ('UpdatedFirstName UpdatedLastNam'), email('updateduser@email.com') and date of birth ('02-11-2003').
4. It adds a new hobby that is not available in the dropdown (Biking), then adds every hobby from the dropdown list of hobbies.
5. It goes to the 'Find Friends' page and filters the users by age
6. It goes to the 'Find Friends' page and sends a friend request to the user with the most hobbies in common 'Other User'. It then logs out.
7. It logs in as the 'Other User' and goes to the 'Friend Requests' page and accepts the request. It then logs out.
8. It logs back in as the 'UpdatedFirstName UpdatedLastNam' and verifies 'Other User' and 'UpdatedFirstName UpdatedLastName' are friends.

**Note: sometimes the tests may seem to be stuck: they are not, the assertions are being checked.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
