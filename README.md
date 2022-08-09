# Shoes-Blog

![shoes](https://user-images.githubusercontent.com/83575427/183703915-883c5ad1-6135-44a7-ac01-5ea94e303b59.JPG)
https://shoesblog.herokuapp.com/
# Project Overview

Shoes_blog is a website that aims to provide a blog-style trainers information website for various brands which user can view and interact with via comments and likes by signing up and creating an account or logging into and existing one. This site has been created as part of my Portfolio Project 4 for Code Institute.

#Project Goals
 *The main business goal for shoes kingdom is to provide users with a blog-style website with various Snikers shoes accessible for the user to view. The user can   create an account to be able to further interact with these blog posts via likes and adding comments.

 *The main target audience for this website are snikers shoes lover, sports, nfts, crypoti, in genral every public that love to rock from time to time some of the most spectacular shoes out there.
#User Stories
##Site User Goals:

 - As a Site User I can like or unlike a post so that I can interact with the content
 - As a Site User I can leave comments on a post so that I can be involved in the conversation
 - As a Site User I can register an account so that I can comment and like
 - As a Site User/Admin I can view comments on an individual post so that I can read the conversation
 - As a Site User/Admin I can view the number of likes on each post so that I can see which is the most popular or viral
 - As a Site User I can click on a post so that I can read the full text
 - As a Site User I can view a list of posts so that I can select one to read
 - As a Site User I can locate their social media accounts so I can receive updates and see their following and how well they are known and reliable
 - As a Site User I can navigate easily through the site and find the relevant information with ease
 - As a Site User I can learn more about the site the purpose of the web app
 - As a Site User I can search keywords for shoes
 - As a Site User I can contact the site owner regarding any feedback or queries

#Site Owner Goals:

 - As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments
 - As a Site Admin I can create draft posts so that I can finish writing the content later
 - As a Site Admin I can create, read, update and delete posts so that I can manage my blog content
 - As a Site User/Admin I can view comments on an individual post so that I can read the conversation
 - As a Site User/Admin I can view the number of likes on each post so that I can see which is the most popular or viral
 - As a Site Admin I can prevent unauthorised users from having access so that they cannot access admin content or other users' profiles

# Scope
## To achieve the strategy goals, I want to implement the following features:

- A navigation bar fixed at the top of the screen which will allow the user to easily navigate and find the relevant sections.
- A Home section which will allow the user to find out about the website and view posts.
- An About Us page to inform the user about this website.
- A Login page for existing users to access their account to allow to like and add comments.
- A Register/Signup page to allow new users to create an account.
- A New entry page to view the selected post in more detail about the shoes and add comments/like the post.
- A Search bar to allow users to enter specific keywords to be able to locate snikers shoes that you want.
- A Footer located at the bottom of the website which allows the user to access social media links.
- A fully responsive design that will work on different devices including desktop, tablets, and mobile devices, allowing users to access the site anytime and anywhere.
- An Error 404 Page to allow users to redirect back to Home page in case of any errors.
- Full CRUD functionality for Admin to allow to create, read, update and delete posts.

# Typography
The fonts were obtained from Google Fonts.

For my logo text I have used Pacifico.

For the heading text I have used Poppins.

For the main text I have selected Montserrat which complements the font used for my headings and logo.

I have avoided using overly stylised fonts, which can be difficult to read for users, therefore ensuring the website is more accessible to users with visual impairments.

In the event the font fails to load, I have used sans-serif as a back-up font.

## Imagery
Images are obtained from the google.

I have used imagery appropriate to the website’s content to provide a more visual experience to the user.

Please see further details in the Credits section for the specific images used within the project.

# Database
A relational database was used for this project.

During production SQLite/Postgres was used as the main database, and for deployment all data was migrated to Heroku Postgres.

Please note that for testing purposes SQLite database was used. In the settings.py code was added to allow for the databases to be swtiched between SQLite for testing and Postgres for regular production. When DEVELOPMENT = True, then the SQLite database will be used for testing, and when this is set to False, then the Postgres database will be in use.

# Current Features
- For this project I opted for a website with different pages accessed by clicking the nav links, this is fully responsive and consists of a header, footer and the following main sections; Home, About Us, New Entry, Sign Up, Login, Search and 404 error page.

## Navigation:

- This feature is present on all the pages/sections and is fixed to the top.
- The header section has a fully responsive navigation bar which consists of the logo, located on the left-hand side.
- The navigation buttons for Home, About Us, Sign Up, Login (located left-hand side after the logo) and a Search bar (located on the right-hand side).
- Style has been applied to the logo and buttons on the left-hand side so the user is able to hover over these to signify that the links can be clicked.
- The Search bar has placeholder text to indicate to the user that they can enter text in the box provided.
- Style has also been applied to the search button next to the input box to indicate to the user that this has been selected and can be clicked.
## Home:

- This is the default page displayed when the user accesses the website.
- This page can also be viewed by clicking the shoes kingdom logo or the home button from the navigation.
- An introductory message displayed to the user.
- Snikers shoes blog posts displayed (max of 6) per page.
- There is a 'Next' button that allows user to click and navigate to the next page to view more Snikers shoes.
- Alternatively 'Prev' button can be clicked to return a page back.
- Sniker shoes blog posts are displayed from most recent to oldest.
- Each post is displayed in a card style with an image, author, date, title and like count.
- Style has been applied so the user can hover over the text for the posts which will underline to indicate that this can be selected.
- Selecting the clickable text will take the user to the 'Blog Posts' page to display the full content of the recipe post.
## About:

- User can access this section by clicking the 'About' button from the navigation.
- User is able to scroll further down the page and access the text which provides more detail about the website and it's purpose.
- For new users, a sign up link is also within the text which will take them to the 'Sign Up' page and allow the user to create an account.
## Sign Up:

- Accessed from the navigation bar by selecting the 'Sign Up' button.
- Once selected, the user is taken to the 'Sign Up' page.
- New users are prompted to enter a username, email (optional), password and password again to confirm.
- All fields apart from the email (optional) are required for the user to be able to create an account, otherwise an error is displayed.
- Upon successful creation the user is then able to login to the account.
- Alert is displayed to indicate that the user has signed in.
- Existing users are provided with the sign in link to take them to the 'Login' page.

## New Entry:

- Accessed once the user selects a shoe post from the 'Home' or 'Search' page.
- sniker shoes title and image displayed at the top.
- Content is then followed by the ingredient list and method steps.
- Further below is the comment section which users can view even if not logged in.
- Comment section is available and displayed for logged in users who can submit a comment.
- This is then sent for approval which is a feature only the Admin can access.
- Alert is displayed to indicate the comment has been sent for approval.
- Approved comments can be viewed on the post.

## Login:

- Accessed from the navigation bar by selecting the 'Login' button.
- Once selected, the user is taken to the 'Login' page.
- Existing users can enter their username and password and click the login button.
- Upon successful login, user is taken to the 'Home' page.
- Alert is displayed to indicate that the user has signed in.
- Incorrect username and password will faily to log the user into their account and a message will be displayes on the 'Login' page to indicate this.
- New users are provided with the register link to take them to the 'Sign Up' page to create an account.
## Logout:

- Option only available to users who are currently logged in.
- Accessed from the navigation bar by selecting the 'Logout' button.
- Once selected, user will be taken to the 'Sign Out' page to confirm that they wish to sign out from their account.
- User can select the sign out button option which will successfully sign out the user from their account and return them to the home page.
- Alert added to indicate that the user has signed out.
## Search:

- Accessed from the navigation bar in the top right-hand corner.
- Placeholder text added to indicate to the user that text can be entered in the input box.
- User cannot submit an empty search and user has to enter a max of 2 characters otherwise an error is displayed.
- User is able to click the search button once the requirements are met (as stated above), this will take the user to the 'Search' page.
- User is able to scroll down and view the displayed results of the snikers shoes which match the keywords entered.
- Prior to the search results, the user is displayed with the keyword searched and below the results are displayed.
- For any successful matches display the sniker shoe (same as the ones on the 'Home' page), the user can click this and be taken to the sniker shoe page.
- For any unsuccessful matches, the user is displayed with a message to state that no results have been found for this keyword.
## Footer:

- This feature is present on all the pages/sections and is fixed to the top.
- Social media links can be accessed by the user.
- Hover style applied to signal to the user which link they are selecting and opening.
- Links open in a new tab so the user is not taken away from the main website and can easily return.

## 404 Error Page:

Only accessed when error occurs or invalid links are being accessed.
User is presented with the error message and provided with a link to direct back to the home page.
#Features Exclusive to Admin:

- Only the Admin can approve and delete user comments.
- Only the Admin can create, update and delete posts.

# Technologies Used
### For this project the main languages used are HTML5, CSS3, JavaScript, Python, Django and Heroku Postgres.

# I have also utilised the following frameworks, libraries, and tools:

- Bootstrap v5.1.3:
- Bootstrap has been used for overall responsiveness of the website and for the layout with the addition of select classes.
## GitPod:
- I used GitPod as the IDE for this project and Git has been used for Version Control.
## GitHub:
- GitHub has been used to create a repository to host the project and receive updated commits from GitPod.
## Google Fonts:
- I have used Google Fonts to import fonts for styling purposes for this project.
## Font Awesome:
- Font Awesome was used to apply icons in the Home, Exercises and Footer sections.
## Chrome Dev Tools:
- Chrome Dev Tools was used to test the site, assist with debugging issues and run reports from Lighthouse.
- W3C Markup Validation Service:
- The W3C Markup Validation Service was used to validate the HTML document for this project and to identify any issues with the code.
- W3C CSS Validation Service:
- The W3C CSS Validation Service was used to validate the CSS document for this project and to identify any issues with the code.
## JSHint Validation Service:
- The JSHint Validation Service was used to validate the JavaScript document for this project and to identify any issues with the code.
- PEP8 Online Validation Service:
- The PEP8 Online Validation Service was used to validate the Python document for this project and to identify any issues with the code.
## Heroku:
- Heroku has been used to create a repository to host the project and receive updated commits from GitPod.
## Django:
- Django was used as the main framework to build this project.
## Cloudinary:
- Cloudinary was used to store all media and static files for this project.
## Am I Responsive:
- Am I Responsive was used to create the header image for the README file.
# Python:
- Various Python modules were used to build this project as detailed below and as seen in the requirements.txt file.

# alidation Testing
## To test the HTML code, I used the W3C Markup Validation Service.


![apture](https://user-images.githubusercontent.com/83575427/183723488-30772a6f-d371-4ef3-8e49-0c0ee4e30bdb.JPG)


- Please note that the base.html has been validated as part of the above pages as the code was inclusive of the testing.

## To test the CSS code, I used the W3C CSS Validation Service.

##style.css:


- No errors were detected in the code.

To test the JavaScript code, I used the JSHint Validation Service.

##script.js:


#The following HTML files were tested with script code:

add_post.html
edit_post.html
No errors were detected in the code. Warnings were detected in the code however this was due to the use of the new ES6 syntax in the code.

To test the Python code, I used the PEP8 Online Validation Service.

All files passed through the validator and no issues were detected with the exception of the settings.py file. This was due to the rows in question being too long, however as these are auto generated by Django or the link name being too long these rows were not amended and left as they are.

I also used the Chrome Dev Tools Lighthouse Report to test both on desktop and mobile.

The score for the lighthouse report for desktop and mobile run across the different pages varied from 77 lowest to 100 highest. Further steps were taken to try to improve the score, however no major score changes could be achieved for the report.

## Home Page:
![front](https://user-images.githubusercontent.com/83575427/183722024-a51a44bc-fc17-4f0a-a43d-8a6b89da9561.JPG)


## About Page:

![Cure](https://user-images.githubusercontent.com/83575427/183722295-d8e5bcb9-9669-4136-9b13-e7287070a304.JPG)



## Sign Up Page:

![Captre](https://user-images.githubusercontent.com/83575427/183722513-b2a1bf4e-cc33-437f-b39b-398207f16a5b.JPG)


## Login Page:

![pture](https://user-images.githubusercontent.com/83575427/183722637-900fc317-6d34-499e-a757-8176153c5d74.JPG)


## Logout Page:
![log](https://user-images.githubusercontent.com/83575427/183722785-74696c4a-e2eb-4119-a8e1-c35148c3e1d5.JPG)


## Search Page:

![searcg](https://user-images.githubusercontent.com/83575427/183722887-21ee0895-ff19-4e4d-97a0-d2fccc3bae58.JPG)



## Post Detail Page:
![Screenshot 2022-08-09 155601](https://user-images.githubusercontent.com/83575427/183723136-62079427-2252-498b-8322-8a0b7f548a0d.png)

![addnw](https://user-images.githubusercontent.com/83575427/183722928-1530c8d3-3714-4698-9ef7-e963e5bb571c.JPG)


# admin:
![Cse](https://user-images.githubusercontent.com/83575427/183723312-69a0ec46-e6a4-4b77-aa75-a1c88fc49f61.JPG)

![Caure](https://user-images.githubusercontent.com/83575427/183723329-7e383578-ea52-43e1-8ded-3835791499fa.JPG)

![ure](https://user-images.githubusercontent.com/83575427/183723388-ee98e051-7ea9-4783-a2bc-1d037ed82476.JPG)

## Login
![re](https://user-images.githubusercontent.com/83575427/183723198-ae937433-6510-4426-8d0d-6b5c29d62491.JPG)
#This website was tested on the following browsers:

Google Chrome
Safari
Mozilla Firefox
This website was also tested on the following devices:

iPhone 11 Pro
iPhone 12 Pro
iPad Pro
MacBook Air
Android One Plus 8 Pro
Automated Testing
Further testing was completed importing the Django TestCase. The test files can be located in the blog > tests folder for the project, this consists of the following files:

test_forms.py
test_models.py
test_urls.py
test_views.py
Please note that for testing purposes SQLite database was used. In the settings.py code was added to allow for the databases to be swtiched between SQLite for testing and Postgres for regular production. When DEVELOPMENT = True, then the SQLite database will be used for testing, and when this is set to False, then the Postgres database will be in use.

The Coverage was used to assist with automated testing to check the percentage of the project code that was covered with automated testing. The test provided an overall coverage of 76%.

To generate your own coverage report:

Install the package using pip install coverage
Run coverage run manage.py test
Then coverage html to generate the report
The report can be viewed in a browser by opening the index.html file from inside the htmlcov folder
The remaining untested code was tested manually for this project as detailed in the above sections.

In addition to completing automated testing for this project, the Travis CI for Continuous Integration was used to further test. However, due to changes with the Travis CI policy the free package was no longer accessible, therefore full testing could not be completed as expected.

# Deployment
The project was developed using GitPod and was deployed via the GitHub repository to Heroku.

The following steps were followed to deploy this project:

From the Heroku dashboard, select 'New' in the top right-hand corner.
Click 'Create new app'.
Enter the app name and choose region as Europe.
Click 'Create app'.
Select the 'Settings' tab, and scroll down to 'Buildpacks'.
Add 'Python' and save changes.
Scroll down to 'Config Vars' section, and add the 'KEY' and 'VALUE' for the CLOUDINARY_URL, DATABASE_URL and SECRET_KEY to run the app.
At the top of the page, click on the 'Deploy' section.
Select Github as deployment method.
Select 'Connect to Github', and locate the repository name and click on 'Connect' to link my Heroku app to my Github repository code.
To add the Postgres Database, click on the 'Resources' tab.
Under Add-ons, search for 'Heroku Postgres', click on the search result for this.
Select the 'Hobby Dev-Free' option and click submit order form which will add this to the Add-ons section.
Scroll further down, select 'Enable Automatic Deploys' and then select 'Deploy Branch' to deploy project.
After it has successfully deployed a 'view' button appears on screen and when clicked opens the deployed application.
Run the command heroku login -i and login when prompted. Then run the following command: heroku git:remote -a your_app_name_here and replace your_app_name_here with the name of your Heroku app. This will link the app to your Gitpod terminal.
After linking your app to your workspace, you can then deploy new versions of the app by running the command git push heroku main and your app will be deployed to Heroku.

# Acknowledgements
I would like to thank my family and friends for their support throughout this project and for assisting with the testing stage and providing valuable feedback.
Big thanks to all the code institute tutors, great help.
