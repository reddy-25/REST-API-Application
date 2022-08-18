# Django-REST-API-application
A sample Django appplication with JWT token authentication and CRUD operations

#urls:

 adviser/ --> Takes POST request in which data (adviser name and photo url) has to be sent in JSON foramt.
 
 user/register/ --> Takes POST request of username and password and if the data is valid it will create a new user.
 
 user/login/    --> Takes POST request of username and password and returns the JWT token 
 
 user/<<user id>>/     --> Takes GET request and returns the details of the user id, username in JSON format (parameters: user id)
 
 user/<<id>>/advisor/ --> Takes GET request and returns all the advisors list (adviser name, adviser id, adviser phot url) (parameters: user id)
 
 user/<<id>>/advisor/<<adviser-id>>/ Takes POST request (booking_time in JSON) and creates a booking with the user and the adviser (parameters userid, advisor id)
 
 user/<<id>>/advisor/booking/ Takes GET request and returns a list of all bookings made by the user with each divisor with whom they made a booking (parameters: advisor id)

 
