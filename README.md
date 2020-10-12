<div align="center">
<img src="https://github.com/boomernag/activity-challenges/blob/418d8596204ea5db894208500ffabe5b7d89b9a3/static/img/Landing%20Page%20%28all%20devices%29.png" target="_blank" rel="noopener" alt="Activity Challenges">
<h2>Activity Challenges</h2>
</div>
    This website is created to be a fun and easy source of inspiration for physical movement. Users can add challenges, find challenges and activate/complete challenges.
    Challenges are supposed to be short, concise and easy to perform ranging from 1 minute to maximum of 10 minutes.

#### You can access the platform [here.]<a href="https://activity-challenges.herokuapp.com//"target="_blank">activity-challenges.com</a>

## Table of Contents

1. [**UX**](#ux)
   - [**User Stories**](#user-stories)
     - [**As a user of this platform, I will be able to:**](#as-a-user-of-this-platform-i-will-be-able-to)
2. [**Design**](#design)
   - [**Typography**](#typography)
     - [**Colours**](#colours)
     - [**Icons**](#icons)
   - [**Wireframes**](#wireframes)
3. [**Features**](#features)
   - [**Existing Features**](#existing-features)
     - [**Base**](#base)
     - [**Challenges**](#challenges)
     - [**Add a new challenge**](#add-a-new-challenge)
     - [**Edit a challenge**](#update-a-challenge)
     - [**Delete a challenge**](#delete-a-challenge)
     - [**Error Page**](#error-page)
   - [**Features Left to Implement**](#features-left-to-implement)
4. [**Technologies Used**](#technologies-used)
   - [**Tools**](#tools)
   - [**Libraries**](#libraries)
   - [**Languages**](#languages)
5. [**Testing**](#testing)
   - [**Tools used for testing**](#tools-used-for-testing)
     - [**Validators**](#validators)
     - [**Responsiveness**](#responsiveness)
6. [**Deployment**](#deployment)
   - [**Local Deployment**](#local-deployment)
     - [**Instructions**](#instructions)
   - [**Remote Deployment**](#remote-deployment)
     - [**Instructions**](#instructions-1)
7. [**Credits**](#credits)
   - [**Content**](#content)
   - [**Media**](#media)
   - [**Images**](#images)
   - [**Code**](#code)
8. [**Acknowledgements**](#acknowledgements)

# UX

## User Stories

### As a user of this platform, I will be able to:

- Find challenges, activate them and mark them as completed.
- Create a challenge.
- Edit a challenge.
- Delete a challenge.
- See activated challenge.
- See how long time a challenge is supposed to need to be completed.
- See how many times a challenge has been completed.

## Design

This project was developed with an idea of keeping it simple, keeping the challenges and its content in focus.
Bold titles for the challenges to help them stick out, a cursive title in the navbar for the page to get the "active" feeling.
Hover-effect on "activate"-button to get the feeling that it is hanging in the air and when user clicks it is showtime.

### Typography

- The body font used is **Roboto**. Good readability and working well on smaller screens.
- The "Challenges"-title is a condensed version of **Roboto**. It keeps the feeling of simplicity while helping the tile be caught by the eye.

### Colours

<img src="https://github.com/boomernag/activity-challenges/blob/170137cdfa22204c2c7fd07d034948bcb8f86263/static/img/Color%20Scheme.png" target="_blank" rel="noopener" alt="Color Scheme">
- In the colour scheme, I used orange a base as it is an "active" color.
- In the navbar and footer, I used the darkgray-ish background with letters in white, giving a nice frame for the page and also easily readible letters.
- In the background, I kept it simple with white (after trying both dark and bright)
- The page title got the orange color that looks clean but still adds that color spark to make the page more visually attractive.
- Challenge-activate button got the "start"-lightseagreen color and the deactivate button got the "stop"-red color.

### Icons

The icons used in this project are provided by [Font Awesome 5.12.1](https://fontawesome.com/) and [Materialize_1.0.0](https://https://materializecss.com/icons.html).
They were used for displaying: challenge time and completions, search function aswell as challenge edit- and delete buttons.

## Wireframes

These wireframes were designed with Balsamiq Mockups 4.0.21

- Mobile displays [here](https://github.com/boomernag/activity-challenges/blob/386fb4dbc9d9cd0f488337b1f6e026dfa13d4ca6/user_stories/Mobile.png)
- Computer displays [here](https://github.com/boomernag/activity-challenges/blob/386fb4dbc9d9cd0f488337b1f6e026dfa13d4ca6/user_stories/Desktop.png)

# Features

## Existing Features

### Base

All pages have the navigation bar with the logo and all visible links and footer.

- **Landing page**
<div align="center">
<img src="https://github.com/boomernag/activity-challenges/blob/170137cdfa22204c2c7fd07d034948bcb8f86263/static/img/Landing%20Page%20%28all%20devices%29.png" target="_blank" rel="noopener" alt="Landing paage (all devices)">
</div>

The page does not have a login functionality, which is set for future feature. So for now if a challenge is activated, it is active for everyone. Same goes for deactivating/completing a challenge.

### Add a challenge

<div align="center">
<img src="https://github.com/boomernag/activity-challenges/blob/170137cdfa22204c2c7fd07d034948bcb8f86263/static/img/Add%20Challenge%20%28all%20devices%29.png" target="_blank" rel="noopener" width="400" alt="Add Challenge (add devices)>
</div>

**CRUD - CREATE**
When entering the "Add Challenge" page user is provided three(3) inputs - [Title, Description and Time].
It is required to provide a title and description of minimum five(5) letters each aswell as choosing a time alternative.

### Activated Challenges

<div align="center">
<img src="https://github.com/boomernag/activity-challenges/blob/25e19967e1a3c888cce5425a2f0d94398436ca72/static/img/Activated%20Challenges%20%28Home%29%20%28all%20devices%29.png" target="_blank" rel="noopener" width="400" alt="Active Challenges (all devices)">
</div>

**CRUD - READ**
User can easily see which challenges that are activated by going to "Home" button in navbar. As mentioned, future feature is that activated challenges will be personal.
User can also search for challenge by title or description.

### Edit challenge

<div align="center">
<img src="https://github.com/boomernag/activity-challenges/blob/25e19967e1a3c888cce5425a2f0d94398436ca72/static/img/Update%20Challenge%20%28all%20devices%29.png" target="_blank" rel="noopener" width="400" alt="Edit Challenge (all devices)">
</div>

**CRUD - UPDATE**
When a challenge is not activated it is possible to be edited. User will then face the current information when enter that challenge edit page.
If changing, the information will be overwritten by the new input and also the completions will be set to 0 (as there might be a different kind of challenge).

### Delete Challenge

<div align="center">
<img src="https://github.com/boomernag/activity-challenges/blob/25e19967e1a3c888cce5425a2f0d94398436ca72/static/img/Delete%20Challenge.gif" target="_blank" rel="noopener" width="450" alt="Delete Challenge (gif)">
</div>

**CRUD - DELETE**
When clicking the delete button the challenge will be deleted. Atm there is no validation or confirmation when the button is clicked but it is a future feature.

### Error Page

For 500 and 404 errors the user will be redirected to landing page and a flash message of "Challenge does not exist" will be displayed.

## Features Left to Implement

- The next steps are:
    - Implement feature to have a personal database to see only users own activated challenges, how many challenges user has completed and added.
    - Further develop the search index to be more flexible and also add filters that user can filter challenges by.
    - Implement a timer user can use when activating a challenge so that is automatically completes when the designated time for the challenge is up.
    - Be able to add challenges to a cluster that is activated after one another when the cluster is started.
    - Recommend challenges to other users.
    - Create a general feed to show who completed a challenge.
    - Possiblity to add other users as "friends" and see their feed.
    - Create a group of friends that can be included in a cluster of challenges, so when the cluster starts it starts for every one who is part of that group.
    - Add media to challenges to visually describe how the challenge is supposed to be performed.

# Technologies Used

## Tools

- [Visual Studio Code](https://code.visualstudio.com/)
  - IDE used for development of this project.
- [Balsamiq Mockups 3](https://balsamiq.com/)
  - Used to create the wireframes and planning this project.
- [Dev Tools](https://www.google.com/chrome/)
  - This project used the Dev Tools from 3 browsers: Chrome, Firefox and Safari. They were necessary to keep track and test the code during the development.
- [Heroku](https://www.heroku.com)
  - Used for app hosting and deploying.
- [GitHub](https://github.com/)
  - This project uses **GitHub** to store and share all project code remotely.
- [Git](https://git-scm.com/)
  - It is used for version control
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
  - It is the database used for this project.
- [Am I Responsive](https://ami.responsivedesign.is/)
  - Used to get images for the README in different screen sizes.
- [Ezgif](https://ezgif.com/video-to-gif/)
  - Used to get screenrecording from video to gif for README display.

## Libraries

- [Materialize](https://materializecss.com/)
  - This project uses **Materialize** for better responsiveness and organization. It was also used for some CSS attributes, icons and effects.
- [FontAwesome](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.12.1/css/all.min.css)
  - The project uses **Font Awesome** to provide some icons.
- [Google Fonts](https://fonts.google.com/)
  - The project uses **Google fonts** to provide 'Roboto' and 'Staaliche' font.
- [JQuery](https://jquery.com)
  - Used to simplify DOM manipulation.
- [Flask 1.1.2](http://flask.pocoo.org/)
  - Back-end Python microframework.
- [PyMongo 3.11.0](https://api.mongodb.com/python/current/) - Python API for MongoDB.
- [Jinja](https://jinja.palletsprojects.com/en/2.10.x/)
  - It is the default templating language for flask used for display data from the python application in Html templates.

## Languages

- In this project Is used **HTML5**, **CSS**, **JAVASCRIPT** and **PYTHON** as programming languages.

# Testing

- I have thorougly tested differents possibilities of breaking the code and created solutions for when it happened. 
    - One of those things were when a challenge title that didn't exist was inserted into the url search field. That was fixed by adding an errorhandler for 500 error.
    - If a random text is inserted into the url or is misspelled that creates a 404 error user is redirected to landing page and a flash message is displayed.
    - When a challenge is in edit mode in one tab and then deleted in another, edit function is unavailable and user is redirected to landing page and a flash message is displayed.
    - When a challenge is in edit mode in one tab and then activated in another, edit function is unavailable and user is redirected to landing page and a flash message is displayed.- 

### Tools used for testing

#### Validators

- HTML

  - [The W3C Markup Validation Service](https://validator.w3.org/)

- CSS

  - [The W3C Markup Validation Service](https://jigsaw.w3.org/css-validator)

- JavaScript

  - [JS Hint](https://jshint.com/)

- Python
  - [PEP8](http://pep8online.com/) - The Python scripts were checked with pep8online. almost all the errors were solved, the only ones that persisted were of lines longer than 79 characters in some cases, however, in most cases they are in MongoDB query lines.

#### Responsiveness

- The Chrome browser development tools were used to check for responsiveness and scaling issues on different screen sizes.

- This project was tested in Chrome in different simulated devices.

* Phones

  - Moto G4
  - Galaxy S5
  - Pixel 2
  - Pixel 2 XL
  - iPhone 5/SE
  - iPhone 6/7/8
  - iPhone 6/7/8 Plus
  - iPhone X
  - iPad
  - iPad Pro
  - Surface Duo
  - Galaxy Fold
  - MacBook Pro 13" (real device)

# Deployment

You will need the following tools:

- An account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

## Local Deployment

The following instructions are based on use on a Macbook Pro 13'. If your OS is different, the commands may be different, but the process, in general, remains the same.

#### Instructions

- Save a copy of the Github repository located at https://github.com/boomernag/activity-challenges.
  - Unzip the repo into the chosen folder.
- If you have Git installed on your system, you can clone the repository with the following command.

```
git clone https://github.com/boomernag/activity-challenges
```

- Install all required modules with the command:

```
pip install -r requirements.txt
```

- Create a `.env` file with your credentials:
  e.g

```
MONGO_URI="insert your mongo URI details here"
SECRET_KEY="insert your secret key here"
```

- Create a database in MongoDB Atlas called **challengedb** with a collection called **challenges**

- Run the application with the command

```
python3 app.py
```

## Remote Deployment

#### Instructions

To deploy this app to Heroku you need to follow the steps below:

- Create a **requirements.txt** file so that Heroku can install all the dependencies required to run the app.
  `pip freeze > requirements.txt`

- Create a **Procfile** with the command:
  `echo web: python app.py > Procfile`

- In this step, you have to create a free account on the [Heroku website](https://signup.heroku.com/).
- Login to the account, click on new and then create a new app. In the following screen, you need to give a name and choose the Europe region.
- In the menu access the **Deploy** option, after that click on Connect to Github. Just below provide the information from the app's repository on GitHub and select the option Enable Automatic Deploy.
- On the Dashboard of the APP, click on Settings and then click on the option **Reveal config Vars**.
- Now you need to add the following variables to **Reveal config Vars**:
  - **IP**: `0.0.0.0`
  - **PORT**: `5000`
  - **MONGO_URI**: `link to your Mongo DB`
  - **SECRET_KEY**: `your chosen secret key`
- You are now ready to access the deployed app on Heroku.

# Credits

## Content

The challenges are written by me.

## Media

#### Images

- The images in this project were created using [Am I Responsive](http://ami.responsivedesign.is/) to implement in this readme.

### Code

- The code for the hover effects on "activate" and "deactivate/complete" buttons are from [Hover.css](https://ianlunn.github.io/Hover/).
- Code for the @app.errorhandler was copied from [Flask Palletsproject](https://flask.palletsprojects.com/en/1.1.x/errorhandling/)
- For the code for "edit_challenge" to work correctly I owe a lot of thanks to [Code-Institute-Support-team].

## Acknowledgements

Very Special Thanks to:

- My mentor in Code Institute **Rohit Sharma**. Thank you for your patience and taking your time to teach me extra.
- To Code Institute Support team for all the help along the project.
- All of the Code Institute Slack community for the answers to questions when I felt stuck.
