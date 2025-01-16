# Group 7

## READ.ME content

- URL of deployed application
- Member assigned and finished tasks
- Notes on E2E selenium-based testing
- Admin user log in details
- Log in details for test users
- Local development

# URL of Deployed Application

[https://group7-web-apps-ec22792.apps.a.comp-teach.qmul.ac.uk](https://group7-web-apps-ec22792.apps.a.comp-teach.qmul.ac.uk)

# Member assigned and finished tasks

| Member                         | Assigned                                                                               | Finished tasks                                                                                                                                              |
| ------------------------------ | -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sai Sandeep Vemula (220224206) | Friendship models and views and front end, Friend Requests page back-end and front-end | Friendship model and views, log in and authentication, Friends Request and Find Friends back-end, Authentication, Testing                                   |
| Ilenia Maietta (220322742)     | UserHobby model and views, Hobby list front-end and back-end                           | UserHobby model and views, Hobby List front-end and back-end, Find Friends and Friends Request front-end, Front-end Error messages, Authentication, Testing |
| Amy Anigboro (220476137)       | Hobby model and views, Update Profile and Password front-end and back-end              | Hobby model and views, Update Profile and Password front-end and back-end, Front-end Error messages, Testing                                                |
| Mariam Thabti (2103028471)     | User model and views, authentication and heap for hobbies                              | User model and views, log in, sign up and authentication, maximum heap for hobbies, Authentication, Testing                                                 |

# Note

## E2E selenium-based testing

The testing is set up to run continuously, as if a person was manually testing the website. We set up a series of helper functions, called in a class called test_new_user in the following order:

1. Account creation/ sign up a new user called 'New User', and then it logs out.
2. Log in: it logs in with the 'New User' credentials
3. Editing all the user's data on their profile page: it updates the password, first and last name ('UpdatedFirstName UpdatedLastNam'), email('updateduser@email.com') and date of birth ('02-11-2003').
4. It adds a new hobby that is not available in the dropdown (Biking), then adds every hobby from the dropdown list of hobbies. It then deletes a hobby.
5. It goes to the 'Find Friends' page and filters the users by age
6. It goes to the 'Find Friends' page and sends a friend request to the user with the most hobbies in common 'Other User'. It then logs out.
7. It logs in as the 'Other User' and goes to the 'Friend Requests' page and accepts the request. It then logs out.
8. It logs back in as the 'UpdatedFirstName UpdatedLastNam' and verifies 'Other User' and 'UpdatedFirstName UpdatedLastName' are friends.

Note: please do not scroll while running the tests and ensure to keep the header visible at all times, especially while deleting the hobby, and when filtering the users, because the redirection does not work if the header is not visible.

## Running the local version

Please run 'collectstatic' files beforehand, and use the [localhost:8000](localhost:8000) to run it.
The passwords for every user in the **local** version are 'helloworld123', while for the deployed version they are written below.

# Admin User Log In Details

- Username: admin@email.com
- Password: admin

# Login details for Test Users

| EMAIL                    | FIRST NAME  | LAST NAME  | PASSWORD            |
| ------------------------ | ----------- | ---------- | ------------------- |
| ec22792@qmul.ac.uk       | Ilenia      | Maietta    | Ilenia!Qz82$#1      |
| ec22898@qmul.ac.uk       | Sai Sandeep | Vemula     | Sandeep@Wm71\*&2    |
| ec22496@qmul.ac.uk       | Amy         | Anigboro   | Amy\*Lp48^@4        |
| ec22860@qmul.ac.uk       | Mariam      | Thabti     | Mariam#Rt93^%3      |
| Gabrielle@gmail.com      | Gabrielle   | G          | Gabrielle@Xn64$#6   |
| Taylor@gmail.com         | Taylor      | Dodd       | Taylor!Vm82@^7      |
| Konrad@gmail.com         | Konrad      | K          | Konrad#Qs56&!5      |
| Nora@gmail.com           | Nora        | H          | Nora@Wp39!@0        |
| LiamLawson@gmail.com     | Liam        | Lawson     | Lawson@Np83!$4      |
| Rahul@gmail.com          | Rahul Ray   | Lee        | Rahul#Yt93\*&8      |
| Abdullah@gmail.com       | Abdullah    | Zulfiqar   | Abdullah$Jk74#^9    |
| YukiTsu@gmail.com        | Yuki        | Tsunoda    | Yuki@Lp84&\*@1      |
| Ollie@gmail.com          | Oliver      | Bearman    | Oliver!Xp38^$0      |
| LanceStrolled@gmail.com  | Lance       | Stroll     | Strolled#Jm73!@2    |
| GeorgeRussell@gmail.com  | George      | Russell    | GeorgeT#Xm74&@5     |
| LandoNorris@gmail.com    | Lando       | Norris     | LandoNowins#Zt64&!5 |
| SuperMax@gmail.com       | Max         | Verstappen | SupaMax$Qw92^&3     |
| AlexAlbon@gmail.com      | Alexander   | Albon      | AlexAlbon!Ym74^&7   |
| PierreGasly@gmail.com    | Pierre      | Gasly      | Pierre@Wk82\*@8     |
| CharlesLeclerc@gmail.com | Charles     | Leclerc    | Leclerc^Tn82$#1     |
| NicoHulk@gmail.com       | Nico        | Hulkenberg | NicoHulk@Jp93$#6    |
| FernandoAlonso@gmail.com | Fernando    | Alonso     | NandoAlonso!Xp56^@4 |
| LewisHamilton@gmail.com  | Lewis       | Hamilton   | Ham@Vm73\*&2        |
| Chilli@gmail.com         | Carlos      | Sainz      | Carlos#Qs91&!9      |
| KimiRaik@gmail.com       | Kimi        | Räikkönen  | Kimi1@9Asw"2        |

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
