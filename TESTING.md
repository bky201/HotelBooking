## Functional Testing

**Authentication**

Description:

Ensure a user can sign up to the website

Steps:

1. Navigate to [Hotel-Room-Booking](https://roombooking-9c7bc437dd80.herokuapp.com) and click Register
2. Enter email, username and password 
3. Click Sign up

Expected:

An email is recieved with a link to sign up, upon clicking the link, registration is successful

Actual: 

An email is recieved with a link to sign up, upon clicking the link, registration is successful

<hr>

Description:

Ensure a user can log in once signed up

Steps:
1. Navigate to [Hotel-Room-Booking](https://roombooking-9c7bc437dd80.herokuapp.com)
2. Enter login details created in previous test case
3. Click login

Expected:

User is successfully logged in and redirected to the home page

Actual:

User is successfully logged in and redirected to the home page

<hr>

Description:

Ensure a user can sign out

Steps:

1. Login to the website
2. Click the logout button
3. Click confirm on the confirm logout page

Expected:

User is logged out

Actual:

User is logged out

**Booking Forms**

Description:

Ensure a new booking can be created.

Steps:

1. Navigate to [Hotel-Room-Booking](https://roombooking-9c7bc437dd80.herokuapp.com) - Login if prompted.
2. Enter the following:
    - Room user: bookuser
    - Room title: Single-bedroom Room no.-1
    - Booking start date: Any future date
    - Booking end date: Any future date after start date
3. Click Create

Expected:

Form successfully submits and a toast is shown to alert the user of successful booking.

Actual:

Form successfully submits and a toast is shown to alert the user of successful booking.

<hr> 

Description:

Ensure a booking can be edited.

Steps:

1. Navigate to [page](https://sizzle-and-steak.herokuapp.com/booking/managebookings/) - Login if prompted.
2. Enter the following:
    - Room user: bookuser
    - Room title: Single-bedroom Room no.-1
    - Booking start date: Any future date
    - Booking end date: Any future date after start date
3. Click Edit

Expected:

Form successfully submits and a toast is shown to alert the user of updated booking.

Actual:

Form successfully submits and a toast is shown to alert the user of updated booking.

<hr>

Description:

Ensure user can successfully delete a booking.

Steps:
1. Login as a user with a booking or create a new booking
2. Click the Manage Booking nav link
3. Click the delete button on a booking
4. Click the confirm button on the delete page

Expected:

Booking is successfully deleted

Actual:

Booking is successfully deleted

<hr>

**Rooms Pages**

Description:

Ensure a new Room can be created

Steps:

1. Sign in as an admin user
2. Select the Create rooms item in the room nav bar
3. Enter the follow details:
    -title = Single-bedroom
    -number = 10
    -features = Balcony/terrace'
    -beds = 1
    -size = 30
    -serviceOne = Laundry and Dry-cleaner
    -serviceTwo = Laundry and Dry-cleaner'
    -price = 40
    -image = image-A
    -imageOne = image-1
    -imageTwo = image-2
4. Click Create

Expected:

New menu is created and can be viewed on the View Menus page

Actual:

New menu is created and can be viewed on the View Menus page

<hr>

**Navigation Links**

Testing was performed to ensure all navigation links on the respective pages, navigated to the correct pages as per design. This was done by clicking on the navigation links on each page.

- Home -> index.html
- About -> about.html
- Rooms -> room_list.html
- Bookings Drop Down, Manage Bookings -> room_booking.html
- Bookings Drop Down, New Booking -> booking_form.html
- Profile -> profile.html
- Logout -> Sign out all auth page
- Login -> Sign in all auth page
- Register -> Sign up all auth page
- Reviews -> room_reviews.html

All navigation links directed to the corect pages as expected.

<hr>

**Footer**

Testing was performed on the footer links by clicking the font awesome icons and ensuring that the facebook, twitter, linkedin and youtube icon opened in a new tab. These behaved as expected.

## Negative Testing

Tests were performed on the create booking to ensure that:

1. A customer cannot book a date in the past
2. A customer cannot book if booking are available for the check in and check out dates
3. Forms cannot be submitted when required fields are empty

## Unit Testing

Unit tests were created to test some basic functionality such as templates used and redirects. These can be found in the tests.py files in the respective apps.

Results:

![unit tests](./docs/testing/unittest.png)

