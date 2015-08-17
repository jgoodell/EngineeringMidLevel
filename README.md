# Engineering Project
This is a project that we use for testing potential employees on their technical skills.

## Feature Request App
Build a web application that allows the user to create "feature requests".

A "feature request" is a request for a new feature that will be added onto an existing piece of
software. Assume that the user is an employee at IWS who would be entering this information after
having some correspondence with the client that is requesting the feature.  The necessary fields
are:

* **Title:** A short, descriptive name of the feature request.
* **Description:** A long description of the feature request.
* **Client:** A selection list of clients (use "Client A", "Client B", "Client C")
* **Client Priority:** A numbered priority according to the client (1...n). Client Priority numbers
should not repeat for the given client, so if a priority is set on a new feature as "1", then all
other feature requests for that client should be reordered.
* **Target Date:** The date that the client is hoping to have the feature.
* **Ticket URL:** A field for storing any URL
* **Product Area:** A selection list of product areas (use 'Policies', 'Billing', 'Claims',
'Reports')

## Tech Stack
Use any reasonably modern technology that you want. We are evaluating both your coding skill as well
as your knowledge of modern technology.

Make sure that your instructions for accessing or otherwise running your code are extremely clear.

## Instructions for Submission

Build your own public repo on github, and call it whatever you like. Build your solution in your
repo, and include a README.md file that contains the detailed instructions for running your web app.
Email the URL for your github repo to chris@britecore.com by the date specified in the email I sent
you.

## Questions and other such clarification

One of the major goals in this project is to see how you fill in ambiguities in your own creative
way. There is no such thing as a perfect project here, just interpretations of the instructions
above, so we will not be answering any questions related to how to accomplish the project itself.

Do the best you can, then send us the link to your repo.

## Tips
We develop on mac laptops, and our deployment infrastructure is all Linux on AWS, so having some
skill at the command line, and specifically in a Linux environment is a big plus. One way to show
what you know is by making your webapp run fairly easily on a mac and/or deploying it in the free
tier of AWS's stack.

We also have a strong affinity for open source technology. If your go-to technology stack includes
proprietary software, you won't be helping yourself to use it in this project.

--------------------------------------------------------------------------------------------------

## Instructions
The technology stack for this application is ngynx, python/django, postgre, MacOSX

### ngynx

### python/django
From the command line type from the root of the git repository where the 'requirements.pip' file
is located.

    $ pip install -r requirements.pip

This will install all of the necessary python packages and modules for this application.

### postgre
Download the PostGre.app from postgreapp.com, drag the app to the Applications dicrectory. Double
click the application and you have a running postgre instance.