# django_taska_v01
Task Management App

 ________________________________________________________________________
-好运-0☢0-----0☢0☠☠0☢0-----0☢0☠☠0☢0-----0☢0☠☠0☢0-----0☢0☠☠0☢0-----0☢0-好运-
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

Useful:
python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py runserver

To do:
- Build task list models
- Views/forms to handle file uploads for attachment
- Add validation (e.g., completed_date only set if completed=True)
- Remove references to taska.html
  - project urls.py
  - app views.py

- register task models to admin page
- build and style taska page

 ________________________________________________________________________
-好运-0☢0-----0☢0☠☠0☢0-----0☢0☠☠0☢0-----0☢0☠☠0☢0-----0☢0☠☠0☢0-----0☢0-好运-
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

__PROMPTS

Please create a responsive main screen for a web app.
The main container should be width 100vw, height 100vh - 105px, with a flex display.
The contents of the main container will change depending on the screen width.
When the screen width is greater than 650px, the main container will have two fixed components. A sidebar of width 350px that fills the main container vertically and a content div that fills the rest of the main container.
When the screen width is 650px or less, only the content div will be permanently displayed in the main container, while the sidebar will be toggled to hidden.
When the user hovers over an invisible div, 20px wide, at the left of the screen, the sidebar will be toggled to show, and slide out from the left of the screen. The sidebar will remain displayed until the user clicks a close button positioned in the top right of the sidebar. When the close button is clicked, the sidebar toggles back to hidden and slides out to the left of the screen.
The close button should only be visible in mobile mode (screen width 650px or less).
You should use a combination of html, css, and js to achieve this. The code should be written in separate files.
Do you have any questions to help clarify what I want you to do or any suggestions to improve this prompt before we begin coding?



__Prompt Components

Please label each of your replies with a unique slug to aid in referring back to specific replies later. These do not need to be human understandable.

Please number each of your questions individually.

Please use two spaces to indent and single quotes in any code you write.

Any html, css, and js should be written to separate files.

Do not write any code until you are sure you understand the request.

Please ask as many questions as you need to help clarify what I intend to do and/or give suggestions for improvements to my prompt.

Do you have any further questions to clarify my intentions?



Let's do some cleaning up in the rest of the app.
I have some questions:
1. Is index.html still required?