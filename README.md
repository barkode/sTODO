# sTODO

sTODO is a program that allows you to keep a list of your tasks. You can easily
add, edit and save your cases.

![landing-page](./assets/docs/landing_screen.png)

You can [visit our site here.](https://stodo-766c69891344.herokuapp.com/)

# Contents

- [sTODO](#stodo)
- [Contents](#contents)
- [User Experience (UX)](#user-experience-ux)
  - [Initial Discussion](#initial-discussion)
    - [Key Information for the Site](#key-information-for-the-site)
  - [User Stories](#user-stories)
    - [Client Goals](#client-goals)
    - [Visitor Goals](#visitor-goals)
      - [First Time Visitor Goals](#first-time-visitor-goals)
      - [Returning Visitor Goals](#returning-visitor-goals)
  - [Design](#design)
  - [Flowchart](#flowchart)
- [Features](#features)
  - [Existing Features](#existing-features)
    - [Landing Page](#landing-page)
    - [New User](#new-user)
    - [Existing User](#existing-user)
    - [Menu of actions](#menu-of-actions)
    - [Add task](#add-task)
    - [Edit task](#edit-task)
    - [Delete task](#delete-task)
    - [Quit](#quit)
    - [App termination](#app-termination)
  - [Future Implementations](#future-implementations)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
- [Deployment](#deployment)
  - [Github](#github)
    - [Forking the GitHub Repository](#forking-the-github-repository)
    - [Making a Local Clone](#making-a-local-clone)
  - [Heroku](#heroku)
- [Testing](#testing)
- [Credits](#credits)
  - [Code Used](#code-used)
  - [Content](#content)
  - [Code \& Content](#code--content)
    - [Media](#media)
    - [Acknowledgment](#acknowledgment)

[Back to top](#stodo)

# User Experience (UX)

## Initial Discussion

sTODO is a tool that allows a user to create a to-do list. The app is designed
to be simple and intuitive, allowing the user to add, edit and delete completed
tasks.

### Key Information for the Site

- A new user to set up a new account
- An existing user to access their account
- Functions to:
  - Add task
  - Edit task
  - Delete task

## User Stories

### Client Goals

- A simple program that users will want to use
- An program that meets the user’s needs

### Visitor Goals

#### First Time Visitor Goals

- To be able to set up a new account
- To understand how to use the app
- To be able to choose their own username and password

#### Returning Visitor Goals

- For reliable storage of personal data
- To access an existing account
- To be able to add task
- To be able to edit an existing task
- To be able to delete a task
- A pleasant user experience

[Back to top](#contents)

## Design

A rich library was used to style messages. This improves the user experience and
allows the user to pay attention to important messages. The following color
scheme was chosen:

- Green: to display logo

  ![green-color](./assets/docs/logo_color_scheme.png)

- Cyan: to display app description and user menu

  ![cyan-color](./assets/docs/app_description_scheme.png)

  ![cyan-color](./assets/docs/user_menu_scheme.png)

- Yellow: to display questions and answer options

  ![yellow-color](./assets/docs/question_and_options_scheme.png)

  ![cyan-color](./assets/docs/user_menu_scheme.png)

- Orange: to display app terminate message

  ![orange-color](./assets/docs/bye_msg_scheme.png)

- Red: to display error messages

  ![red-color](./assets/docs/error_msg_scheme.png)

- Magenta: to display table header

  ![magenta-color](./assets/docs/table_header_scheme.png)

- Default terminal color: to display input messages, user inputs and table data

  ![default-color](./assets/docs/def_table_scheme.png)

  ![default-color](./assets/docs/def_input_scheme.png)

[Back to top](#contents)

## Flowchart

- The flowchart was created using [draw.io](https://app.diagrams.net/)

  ![flowchart](./assets/docs/flowchart.png)

[Back to top](#contents)

# Features

## Existing Features

### Landing Page

- The landing page is the page the user lands on when the app is first run
- The logo and the paragraph below explain to the user what the app does
- The user must enter N or Y to select whether they are a new or existing user
- The user can enter N or Y in upper or lower case
- If any other entry is entered, the user will see an error message and be
  prompted to enter the information again.

<details>

<summary>Landing page user input</summary>

![Landing page](./assets/docs/lp1.png)

![Landing page input other letter](./assets/docs/lp2.png)

![Landing page input number](./assets/docs/lp3.png)

</details>

[Back to top](#contents)

### New User

- If N or n is selected the page will clear and the user will see a welcome
  message.

![new user page 1](./assets/docs/new_user_page1.png)

- They will be asked to enter their login and shown the format in which it
  should be. The login does not match the login of an existing user. If such a
  login exists, an error message will be displayed.

![new user page 2](./assets/docs/new_user_page2.png)

- The user will see an error message if the login does not consist of letters or
  underscores.

![new user page 3](./assets/docs/new_user_page3.png)

- After the user enters a login, he will be prompted for a password. There are
  no restrictions on the length or characters entered when entering a password.
  During registration, the user can see the password.

![new user page 4](./assets/docs/new_user_page4.png)

- After registration, the user gets to the page with his tasks.

![new user page 5](./assets/docs/new_user_page5.png)

- The username, password, and name are added to the user sheet in Google Sheets.
  Password is encrypted before adding to prevent security breach

![new user page 6](./assets/docs/new_user_page6.png)

- A new sheet will be created for the user with the same name as the selected
  user login.

![new user page 7](./assets/docs/new_user_page7.png)
![new user page 8](./assets/docs/new_user_page8.png)

[Back to top](#contents)

### Existing User

- The user will be prompted to enter his login and password.
- For added security, the password will be displayed as hashes

![exist user page 1](./assets/docs/exist_user_page1.png)

- If the password does not match the stored username, the server will display an
  error message

![exist user page 2](./assets/docs/exist_user_page2.png)

- When the username and password are entered correctly, the screen will clear
  and the user will receive a welcome message and see their task table. The
  user's login will be shown in the greeting. A
  [menu of actions](#menu-of-actions) will be shown below the table.

![exist user page 3](./assets/docs/exist_user_page3.png)

[Back to top](#contents)

### Menu of actions

- The menu gives the user four options;
  - Add task
  - Edit task
  - Delete task
  - Quit
- The user must pick letter to choose an option. The letters to be entered are
  highlighted in yellow.

![menu page 1](./assets/docs/menu_page1.png)

- If the user entered an incorrect letter, an error message will be displayed.

![menu page 2](./assets/docs/menu_page2.png)

[Back to top](#contents)

### Add task

- When pressing the letter A, the user will be prompted to add a new task.

![add task page 1](./assets/docs/add_task_page1.png)

- There are no restrictions on entered characters. The user can enter any
  characters.
- I can see, with the help of the library
  [rich](https://rich.readthedocs.io/en/latest/index.html), the table changes
  its width depending on the width of the content.

![add task page 2](./assets/docs/add_task_page2.png)

[Back to top](#contents)

### Edit task

- When pressing the letter E, the user will be prompted to enter the task number

![edit task page 1](./assets/docs/edit_task_page1.png)

- If the user entered an incorrect task number, an error will be issued.
- After that, it will show the main screen with tasks and menus.

![edit task page 2](./assets/docs/edit_task_page2.png)

- If the user entered the correct task number, he will be prompted to enter a
  new text.

![edit task page 3](./assets/docs/edit_task_page3.png)

- After the user enters a new task text and presses enter, the task text will be
  changed

![edit task page 4](./assets/docs/edit_task_page4.png)

[Back to top](#contents)

### Delete task

- When pressing the letter D, the user will be prompted to enter task number.

![delete task page 1](./assets/docs/del_page1.png)

- If the user enters an incorrect number, an error will be displayed. But it
  will be shown on the main screen.

![delete task page 2](./assets/docs/del_page2.png)

- If the user enters letters instead of numbers, he will be shown an error
  message. But it will be shown on the main screen.

![delete task page 3](./assets/docs/del_page3.png)

- After the user has entered the correct number, the task will be deleted. The
  user is shown a list of tasks without the deleted one

![delete task page 4](./assets/docs/del_page4.png)

[Back to top](#contents)

### Quit

- When pressing the letter Q, the app will be terminated. A page with the user's
  logo and login will be displayed.

![quit page 1](./assets/docs/quit_page1.png)

[Back to top](#contents)

### App termination

User pressed ctrl + c on pc or command + c on mac.

- When pressing the letter ctrl + c (command + c on mac), the app will be
  terminated. A page with the user's logo and login will be displayed.

![ctrl+c page 1](./assets/docs/ctrl_c_page1.png)

- When pressing the letter ctrl + c (command + c on mac), the app will be
  terminated. If the user is not authorized, instead of the login, he will see
  Dear user

![ctrl+c page 2](./assets/docs/ctrl_c_page2.png)

[Back to top](#contents)

## Future Implementations

- If the user name exists in the system, give an opportunity to choose another
  name.
- Add confirmation of the password entered by the user during registration.
- Add a forgotten password function – possibly with password hints
- Two-time confirmation of the password during registration
- Allow the user to select a category for their task
- Allow adding their own category name
- Allow editing their own category name
- Add the status of the task and give the possibility to change this status
- Add the ability to exchange messages in the system between users
- Add user roles

[Back to top](#contents)

# Technologies Used

## Languages Used

This app was written in Python.

## Frameworks, Libraries and Programs Used

- VSCODE – To write the code
- Github - To save and store files
- Heroku - To deploy and run the live project
- Draw.io - to produce the flowcharts
- PEP8 - to validate the Python code, improving the readability and consistency

The Python libraries used are:

- gspread - an API for Google Sheets
- google.oauth2.service_account - allows the program to access data held in
  Google Sheets
- time - allows dates and times to be manipulated, use the sleep function to
  delay the page clearing and use for generate id.
- rich - to display the text in different colors
- maskpass - to display the inputted passwords as #
- os - to clear the page on the live program
- sys - used in the function to slowly print text to the screen
- hashlib - to store the password, in Google Sheets, encrypted

[Back to top](#contents)

# Deployment

## Github

### Forking the GitHub Repository

- By forking the GitHub Repository we make a copy of the original repository on
  our GitHub account to view and/or make changes without affecting the original
  repository by using the following steps
- Log in to GitHub and locate the GitHub Repository
- At the top of the Repository (not top of page) just above the "Settings"
  Button on the menu, locate the "Fork" Button.
- You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

- Log in to GitHub and locate the GitHub Repository
- Under the repository name, click "Clone or download".
- To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
- Open Git Bash
- Change the current working directory to the location where you want the cloned
  directory to be made
- Type git clone, and then paste the URL you copied in Step 3.
  - $ git clone <https://github.com/YOUR-USERNAME/YOUR-REPOSITORY>
- Press Enter. Your local clone will be created.

[Back to top](#contents)

## Heroku

This site is deployed using Heroku and following these steps:

1. Create a [Heroku](https://id.heroku.com/login) account or, if you already
   have one, sign in
2. Click the 'new' button and select 'create new app'
3. Enter a unique name for your app and choose the region you are in
4. Click 'create app'
5. Click 'settings' and scroll down to 'Config Vars'. Click 'reveal Config Vars'
6. In the box with the text 'KEY' type PORT and 8000 in the box with the text
   'VALUE'
7. Scroll to the next section, build packs and click 'add build pack'. Add
   Python and NodeJS, in that order. Click 'Add Build pack'
8. Scroll back to the top of the page and click 'Deploy'
9. Scroll to the Deployment method and choose Github
10. In the next section, Connect to Github, type in your repository name. If you
    press the search button it'll bring up all your repositories. Connect to the
    correct repository
11. Scroll down to the two sections for deployment (automatic deploys or manual
    deploys). The automatic deploys will update each time the 'git push' command
    is entered. For the manual deploy, this will deploy the branch specified, in
    it's current state, when the 'Deploy Branch' button is clicked.

[Back to top](#contents)

# Testing

[Back to top](#contents)

# Credits

## Code Used

The lines from 8 to 19 in gsheets_api.py were taken from the Code Institute
Essentials project:

```python
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('stodo')
```

[Back to top](#contents)

## Content

All content was written by Kostiantyn Krysenko

[Back to top](#contents)

## Code & Content

- [Google](https://google.com)
- [github](github.com)
- [W3 Schools](https://www.w3schools.com/)
- [geeksforgeeks](geeksforgeeks.org)
- [stackoverflow](stackoverflow.com)
- [discuss python](discuss.python.org)
- [docs python](docs.python.org)
- [youtube](youtube.com)
- [gspread docs](docs.gspread.org)
- [rich docs](https://rich.readthedocs.io/en/latest/index.html)
- [pypi](pypi.org)

[Back to top](#contents)

### Media

There was no media used in the app

[Back to top](#contents)

### Acknowledgment

- I want to thank my tutor [Marko Tot](https://github.com/tmarkec) for his daily
  care and help. For the desire to create a favorable atmosphere for learning
  and creativity.
- I would like to thank my mentor, Anthony Ugwu, for his helpful advice on
  writing the project.
- I would also like to thank the entire
  [Code Institute](https://codeinstitute.net/ie/) and
  [Kerry College](https://kerrycollege.ie/) for giving me the opportunity to
  study and participate in this project.

[Back to top](#contents)
