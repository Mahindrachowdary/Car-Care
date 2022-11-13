# Car-Wash

I have built this project using Django Framework. I have Focused more on the backend development.
Admin Interface:
Django By default provides an admin interface, we can access this interface by creating superuser.
I have created Four models Places, Services, Members, Bookings.
Places: For storing the locations of car wash services
Services: For storing different kinds of services provided
Members: For storing the data of registered Users
Bookings: For storing the bookings related to corresponding users and their approval status
At the admins interface, by default he has the privilege to make the changes to these models.
So admin can approve or decline pending statuses accordingly 

 Basically, the home Page Consists of Login, Sign up, Bookings, View Bookings. Whenever a user clicks on Login, corresponding Login form will be rendered. Similarly, Whenever a user clicks on Registration, corresponding Registration form will be rendered. Due to the time constraints,
I have made the application simpler, whenever a user clicks on Bookings, Booking form will be rendered where the user will be required to enter the corresponding user name and he also needs to select the corresponding location (for the time being I have considered 3 locations) and Services and then Submit. Now, in view Bookings page the user is required to enter his username to know his/her bookings and their corresponding status.
Status Codes:
S: Success
P: Pending
R: Rejected

 
