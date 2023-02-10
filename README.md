# Welcome to our project for CEN4090L!

This repository contains all the files needed to run the React based web application that our group is creating for the software engineering capstone project. Our group members are Frankie Messina, Zach Porcoro, Raul Rodriguez, Andrew Stade, and Peter Vasiljev.

## Project description

In this project, we hope to overhaul the schedule assistant and the degree progress program provided
by FSU for computer science majors. The current iteration is disorganized and difficult to navigate.
This project will combine aspects from the schedule assistant along with new features and additions
to make course selection much easier and faster for computer science students.

## Project file structure
```
│   .gitignore
│   jsconfig.json
│   package-lock.json
│   package.json
│
├───public
│       favicon.ico
│       index.html
│       manifest.json
│       robots.txt
│
└───src
    │   firebase-config.js
    │   index.js
    │   setupTests.js
    │
    ├───APIs
    │       getUserData.js
    │       setUserData.js
    │
    ├───components
    │       AccountSettings.js
    │       AdditionalResources.js
    │       AppContainer.js
    │       CourseButton.js
    │       CourseDescription.js
    │       CourseFeedback.js
    │       CourseInfo.js
    │       CourseRecommendation.js
    │       CourseSelection.js
    │       DegreeProgress.js
    │       Home.js
    │       Login.js
    │       NavBar.js
    │       PageNotFound.js
    │       PasswordReset.js
    │       Register.js
    │
    ├───images
    │       404error.jpg
    │
    ├───models
    │       ClassInfo.js
    │       NameData.js
    │       UserData.js
    │
    ├───styles
    │       AccountSettings.css
    │       AdditionalResources.css
    │       CardButton.css
    │       CardList.css
    │       CourseSelection.css
    │       GlobalTheme.js
    │       NotFound.css
    │
    └───tests
            Navbar.test.js
```
