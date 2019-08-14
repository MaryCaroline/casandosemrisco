Built for a college project using this [boilerplate](http://github.com/vintasoftware/django-react-boilerplate)

## Running
### Setup
- Inside the `backend` folder, do the following:
- Create the migrations for `users` app (do this, then remove this line from the README):  
  `python manage.py makemigrations`
- Run the migrations:  
  `python manage.py migrate`
- Create a facebook App, and add your Keys to `.env` file:  
  FACEBOOK_CLIENT_SECRET=`Your Facebook APP secret`  
  FACEBOOK_CLIENT_ID=`Your Facebook APP client Id`

### Running the project
- Open a command line window and go to the project's directory.
- `pipenv install --dev`
- `npm install`
- `npm run start`
- Open another command line window and go to the `backend` directory.
- `pipenv shell`
- `python manage.py runserver`
