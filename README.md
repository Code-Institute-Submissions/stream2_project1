# Paraphernalia
## Full Stack Development Milestone Project for the Code Institute

The ask for this brief was to build a web app that fulfils some actual (or imagined) real-world need. I chose to build a house content list manager or inventory manager. It was also briefed that the web app should follow the principles of a CRUD app, connect to a MongoDB database and be deployed through Heroku. I chose to build the house content list manager as it allows the user to create content, read content, update content and delete content, which fulfils the first requirement, but also because of the way by which I planned to store the content in a database. Through learning about the difference between SQL and NoSQL databases I wanted to ensure I used MongoDB in the way it is intended to be used, i.e. as a document-orientated database. The set-up of the house content list manager is such that there are many rooms and each room has many items. Therefore, each room is a collection and each item is a document within the respective collection.

My goal for this project was to demonstrate my understanding of Python fundamentals and showcase what I learnt about the Flask micro-framework, use of a NoSQL database, and deployment through the Heroku platform. The app itself is functional in its execution, however, I was also able to utilise the skills I gleaned in stream 1, front-end user-centric development, to present the information in a visually appealing way.

A live version of the site can be viewed [here](https://code-inst-contentlistmanager.herokuapp.com/), hosted on Heroku.

## UX

The web app default view is a collapsible navigation detailing rooms and respective items and the ability to add rooms and items through a fixed button in the bottom right and corner. However, when a user first accesses the app, they are shown a landing/splash page with branding and instruction on how to use the app. This page was a late addition, but I feel an important one from a UX point of view as it presents the only real branding present throughout the site and also a quick introduction to the utility of the app, which should enhance the first experience and encourage re-use. Branding is minimal throughout the rest of the app, restricted to a brand link in the nav-bar that returns the user to the default view. The remainder of the app is a collection of detail pages, for the rooms, for the items and respective creation and update pages. There is also a utility to print the detail pages should there be a need to, say if something went missing and the police or the users insurance company required a reference.

The web app is fully responsive and content and layout has been accommodated for mobile, tablet and desktop.

**No template was used in the building of this site.**

Wireframes for this project can be viewed in the "wireframe" folder above. Wireframes were created using [Balsamiq](https://balsamiq.com/).

User requirements/stories were met in the following way;
- As a user, I want to understand how to use the app, so that I can begin adding content.

A user is presented with a landing/splash page upon visiting the app that details how to use the app. Also, the utility of the app has been kept simple and should be considered intuitive as it uses form input and function familiar to UX design.

- As a user, I want to add a room or item, so that I can begin to record my house contents.

A user is able to add rooms or items by clicking on the "plus" fixed button in the bottom right hand corner. They will then be taken to a form page and asked to fill out the requisite detail. Not all detail is required, but there is a minimum amount of detail required for the functioning of the app.

- As a user, I want to edit or delete a room or an item, so that I can maintain an up-to-date record of my house contents.

A user is able to edit or delete a room or an item by visiting the respective room or item detail page and clicking on the sequential dots button in the card header. They will then be taken to either a form page with prefilled fields where they can edit and save or to a confirmation page where they can confirm deletion. 

- As a user, I want to print off a detail page for an item, to provide to the police or to my insurance company.

A user is able to print off a detail page for an item by visiting the respective item detail page and clicking on the sequential dots button in the card header. The respective browsers print confirmation page will appear and ask the user to confirm print quantities etc.

## Technologies used

- HTML
    - This project uses HTML for site structure.
- CSS
    - This project uses CSS for styling.
- [Bootstrap 4](https://getbootstrap.com/)
    - This project uses Bootstrap 4 for additional site structure, styling, but also for interaction and most importantly responsiveness. 
- [Google Fonts](https://fonts.google.com/)
    - This project uses Google Fonts for styling.
- [Font Awesome](https://fontawesome.com/)
    - This project uses Font Awesome for styling.
- [Coolors](https://coolors.co/)
    - This project uses Coolors for styling.
- Python 3
    - This project used Python 3 as the programming language.
- PyMongo 3.7.2
    - This project used PyMongo, which is a Python distribution containing tools for working with MongoDB.
- Flask 1.0.2
    - This project uses Flask as the Python web framework.
- mLab
    - This project uses mLab as the cloud hosted MongoDB platform
- Heroku
    - This project uses Heroku as the cloud platform hosting service.

## Features

### Existing features
- Links and buttons allowing the user to navigate the site and reset/control the site functionality.
- Button to add rooms (collections) and items (documents).
- Button to edit rooms (collections) and items (documents).
- Button to delete rooms (collections) and items (documents).
- Button to print item detail.

### Features left to implement

## Testing

Cross browser and multi-device testing was employed to test site responsiveness using [BrowserStack](https://www.browserstack.com).

User testing was carried out to ensure;
- All links and buttons worked as desired.


## Deployment

This site is hosted on Heroku.

In order to run this site locally, in your terminal, type or paste; git clone https://github.com/al3xk3nny/stream2_project1.

## Credits

### Media

- Images used were sourced from [Pexels](https://www.pexels.com/).
- Icons used were sourced from [Font Awesome](https://fontawesome.com/).
- The colour palette was generated using [Coolors](https://coolors.co/). A reference of the colour palette used can be viewed in the "static/images" folder above.
- Fonts used were sourced from Google Fonts.

### Acknowledgements

I would also like to thank my lecturer, Richard Dalton for his dedicated and competent direction throughout the duration of stream 2 and my TA, Michael Park for his advice and encouragement during this project.