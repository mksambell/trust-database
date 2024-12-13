# **TrustDB**

**TrustDB** is an app designed to help organisations seeking funding gather information about relevant grant-making Trusts.

Information about the thousands of grant-making trusts based in the UK is publically available on the Charity Commission website; however, this information is not easy to browse through and there is limited capacity to search for related Trusts.

This app allows a user to gather information about Trusts publicly available from the Charity Commission into a database. The user is able to browse Trusts that operate in similar regions. Users can then use this information to complete funding bids, and can update information when necessary.


[**TrustDB**](https://trustdb-983e714115e8.herokuapp.com/)

![Responsive Screenshot](/trustdatabase/static/readme_images/responsive_screenshot.png)

## Contents

1. [**User Experience UX**](#1-user-experience-ux)
    - [Strategy](#strategy)
	  - [User Stories](#user-stories)
    - [Site Structure](#site-structure)
    - [Wireframes](#wireframes)
    - [Surface](#surface)
2. [**Features**](#2-features)
- [Existing Features](#existing-features)
    - [Title and instructions](#title-and-instructions)
- [Future Features](#future-features)
3. [**Technology used**](#3-technology-used)
4. [**Testing**](#4-testing)
5. [**Deployment**](#5-deployment)
6. [**Credits**](#6-credits)
7. [**Acknowledgements**](#7-acknowledgements)

# 1. User Experience UX

## Strategy

The app was designed in collaboration with a fundraising consultancy business, [Apostle Charity Consulting](https://www.apostlecharityconsulting.com/), which provides fundraising advice and services to charities and churches nationwide. They collate information about grant-making Trusts relevant to a charity's requirements and use that information to create funding bids. 

There are around 8,000 grant-making Trusts active in the UK. The process of gathering all the necessary information about a Trust is time-consuming: the Charity Commission publishes all current data on their website, but users need to navigate through several pages to access it all. It is also not easy to find related Trusts operating in a similar area.

The intention of this app is to provide a single place for all the relevant information to be stored and accessed easily. It also allows a user to create a network of Trusts related by region. For example, if a charity is seeking funding for a project in South London, they would be able to browse through all the Trusts that support activities in that location.

[Back to contents](#contents)

## User stories

As a user, I want to:
1. Create an entry in the database.
2. View all the current entries in the database.
3. Edit the information of an entry
4. Delete an entry
5. Browse through Trusts that are related by region.
6. Navigate easily through the site.
7. Know where I can find more information about a Trust


[Back to contents](#contents)


## Site Structure

The site is structured on three main pages which change according to user interaction

Home
- The landing page contains the title, a brief description, a link to the Add Entry page and displays all the trusts currently in the database in collapsed format. Each Trust listing has an edit and delete button visible when their tab is opened.

Add entry/Edit entry
- Contains a form for users to enter/amend information about new entries, a submit button and a reset form button

Browse by Region
- Displays the current list of regions in the database and an Add Region button. Each region has an edit and delete button. 
- When a region is selected, a list of related Trusts is displayed in the same format as the home page.
- An Add Region page displays when the button is clicked, with a single input form and submit button.

[Back to contents](#contents)

## Wireframes

The following wireframes were created in [Balsamiq](https://balsamiq.com/) and include responsive design ideas for Laptop, Tablet and Mobile devices. 




[Back to contents](#contents)


## Design choices

**Typography**

The 'Sen' font, from Google Fonts, is used throughout. It is a sans serif font, which provides clear text throughout at different scales.

**Icons**

Plus icons from [FontAwesome](https://fontawesome.com/) are used to give some visual direction on the 'Add Entry' and 'Add Region' buttons.

[Back to contents](#contents)

**Colours**

The colour scheme was chosen to give a high contrast and clean effect with splashes of colour for buttons. The blue colour of the navbar is derived from the Apostle Charity Consulting website. The green and red are the colours used in the bootstrap 'success' and 'danger' buttons.

![Colour palette](/trustdatabase/static/readme_images/palette.png)

**Styling**

- The aim is to make the page as intuitive to use as possible, and to keep the main buttons and features clearly visible and organised. Conventional design choices, such as the location of submit buttons and colour choices of the edit and delete buttons, have been made to help the user navigate the site easily.


[Back to contents](#contents)


## 2. Features

The site is intended to be easy to navigate around and intuitive to use. Common layout, terminology and icons are used to help the user find their way around easily, and high contrast between font and background has been used to make the text immediately clear.

## Existing Features



[Back to contents](#contents)

















[Back to contents](#contents)

## Future features



[Back to contents](#contents)

## 3. Technology used

- The wireframes were created using [Balsamiq](https://balsamiq.com/)
- The structure of the site was written in [HTML5](https://html.spec.whatwg.org/)
- The site was styled using [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
- The site was developed in [Gitpod](https://www.gitpod.io/) using a Github template from [Code Institute](https://github.com/Code-Institute-Org/ci-full-template)
- [Github](https://github.com/) was used for version control and for hosting
- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools) were used throughout development and for testing
- Responsive screenshots created with [Am I Responsive](https://ui.dev/amiresponsive)

[Back to contents](#contents)

## 4. Testing

For full testing details, including code validation, bugs, user story tests and developer tools tests, please see the separate [Testing](/TESTING.md) document.


## 5. Deployment



[Back to contents](#contents)

## 6. Credits

### Code


### Content and media


[Back to contents](#contents)

## 7. Acknowledgements

This app was developed for my third Milestone Project for the Full Stack Software Developer Diploma at Code Institute. I would like to thank my mentor, [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/), and all at Code Institute for their help and support. I would also like to thank my family for road testing the game and UX.

Mark Sambell 2024

[Back to contents](#contents)