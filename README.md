# TicketLine

A project for cyber security course at the University of Helsinki.

Project is implemented via Django.

## Before launching the app

Navigate to root directory.
*Create or reset the test data:*
`python3 manage.py test_data`

This command creates:
  - Three users:
    - username: esim, password: 1234
    - username: exmpl, password: 4321
    - username: admin, password: admin
  - Two events

You can use these to play around the app.

## Launching the app
`python3 manage.py runserver`

## Using the app
Admin can be used to create new events. The two normal users are there to try out the
user experience of the application, each with 200 credits as default.
