# Job-Posting-Application

This is a mini project given to me by Univelcity.

## 1. API Backend of a Job Posting Application

You are to develop an API backend of a simple job posting application. The application will
contain three entities; Job Advert, Job Application, and User. A job advert can optionally
have a job application. Below are the components that make up the entities within the
application.

### User

- Username or email
- password

### Job Advert

- Title
- Company name
- Employment type (full-time, contract, remote, part-time)
- Experience level ( Entry level, Mid-level, Senior)
- Description
- Location
- Job description

### Job Application

- First name
- Last name
- Email address
- Phone
- Linkedin profile URL
- GitHub profile URL
- Website (optional)
- Years of experience (0 - 1, 1 - 2, 3 - 4, 5 - 6, 7 and above)
- Cover letter (Should be optional and can be a CharField)

## Specifications

The application should have the following functionalities:
● An API to login and logout users
● An API that returns a list of Job adverts in the DB. The response should also contain
applicant count and publish status. Published adverts should come first followed by
adverts with the highest applicant count and then recently created adverts can come
next.
● An API that retrieves the detail of a job advert
● An API to update a Job Advert
● An API to delete a Job Advert
● An API to publish and unpublish a Job Advert.
● An API that retrieves all the job applications that belong to a job advert
● An API that retrieves a single Job Application
● An API to submit a Job application for a job advert
● An API to delete a Job Application

## Requirements

Below are the requirements of the application:
● Users can signup and activate their account
● Only the endpoint that returns the list of published job adverts and allows the
applicants to submit a Job Application should be accessible to guest users. Other
endpoints should require authentication.
● A Job Advert can only be deleted only after it has been unpublished
● A Job Advert can be published and unpublished.
● Job Applications can only be submitted for a Job advert that has been published.
● Guest users can only see published job adverts.
● All the DB queries should be made with Django ORM.

## Technologies

The following technologies should be used in developing the application.
● Python
● Django
● Django Rest Framework
Other libraries that improve code formatting and quality are welcomed.
