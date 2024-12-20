# Testing

# Contents

- [Code validation](#code-validation)
- [Navigation links](#navigation-links)
- [Responsive test](#responsive-test)
- [Browser compatibility](#browser-compatibility)
- [Testing user stories](#testing-user-stories)
- [Bugs](#bugs)
    - [Resolved](#resolved)
    - [Unresolved](#unresolved)
- [Additional tests](#additional-tests)
    - [Lighthouse](#lighthouse)

## Code validation

**TrustDB** has been thoroughly tested. 

The HTML code has been validated by the W3C [W3C HTML Validator](https://validator.w3.org/). Some minor errors were identified and have been fixed and retested (see [Bugs: Resolved](#resolved)). The site now gives the following message:

![html ok](/trustdatabase/static/readme_images/html_valid.png)

The CSS has been validated with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and no errors or warnings were found. The validator displays the following message:

![css ok](/trustdatabase/static/readme_images/css_valid.png)


[Back to top](#contents)

## Navigation

All links and modals have been manually tested by the developer. All work as intended, including defensive programming to prevent user accidentally deleting entries or regions. Links to external sites open in new tabs.

## Responsive test

The responsiveness of the site was tested using [Google Chrome DevTools](https://developer.chrome.com/docs/devtools).

| iPhone SE  | Galaxy TabS4 | iPhone 14 Pro | iPad Air | iPad Pro | Display <1200px | Display >1200px |
|------------|--------------|---------------|----------|----------|-----------------|-----------------|
| pass       | pass         | pass          | pass     | pass     | pass            | pass            |


Pages displayed as expected at the breakpoints.


[Back to top](#contents)

## Browser compatibility

The site was tested manually in the following broswers:
- Google Chrome
- Microsoft Edge
- Safari
- Mozilla Firefox

The site functioned as expected on all browsers, in a range of device sizes; functionality, responsiveness and appearance worked as expected. 


[Back to top](#contents)

## Testing user stories

1. Create an entry in the database.
    - The Add Entry button is prominent on the home page as a button and navbar link
    - The form on the Add Entry page gives opportunity for user to input various data fields.

2. View all the current entries in the database.
    - The homepage displays all the current entries in the database, listed in order by the registered charity number.

3. Edit the information of an entry
    - Opening the collapsible features of each displayed trust on the home page or in the browse section shows the Edit button.
    - Users can amend info and confirm changes on the Edit Entry page.

4. Delete an entry
    - Users can delete a trust entry on the home page or through the browse section.
    - Users can delete a region entry on the browse page
    - Confirmation is requested to avoid any accidental deletions.

5. Browse through Trusts that are related by region.
    - The Browse page allows users to select a region to see all the Trusts that support activities in that area.

6. Navigate easily through the site.
    - The navbar and footer remain fixed throughout all pages
    - Features such as Return to Browse button when a region's Trusts are displayed mean that the user never has to use the 'Back page' button on the browser.

7. Know where I can find more information about a Trust
    - A link to the Charity Commission is given on the Add Entry and Edit Entry pages


[Back to top](#contents)

## Bugs

### Resolved

- During validation, a duplicate ID was detected in HTML for the modal pop ups - an oversight in development. The HTML and relevant CSS are now amended.
- During tests, an issue with the About modal appeared. The modal would pop up but could not be closed - the whole display was greyed out and neither the Close button or dismiss function worked. The issue was that the modal was appearing behind other features. A CSS fix was implemented, giving the modal a higher z-index. It now works as expected.
- On entering a phone number into the input field of the Add Entry form, the beginning '0' of the phone number was being cut. The Integer range for the phone number entry was not large enough, so this was changed to a text field. It now works as expected.

### Unresolved

- Users need to ensure that a region exists before selecting it in the Add Entry form. This is a potentially frustrating aspect of the UI, as the form will not submit if the region is not selected - users could input data and lose this input if the form does not submit first time. A solution would be to give the user the opporunity to add a region from the Add Entry page if it does not already exist.

[Back to top](#contents)

## Additional tests

### Lighthouse

The site was tested with [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview), one of Google Chrome's developer tools.

The initial test of the home page gave the following result:

![Lighthouse Test](/trustdatabase/static/readme_images/lighthouse.png)

#### Future Improvements

As suggested by the Lighthouse tests, further site improvements could include:
- Rduce unused CSS
- Enable text compression
- Eliminating elements that block the initial render

[Back to top](#contents)

Return to [Readme](/README.md#4-testing)