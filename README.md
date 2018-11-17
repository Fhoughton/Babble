# Babble
Babble is a lightweight public blog framework built using the python web development library Django. It has many safety features and aims to be easy to use and configure into a deployable website.

![Preview](https://i.imgur.com/OPEPFdA.png)
![Edit Profile Preview](https://i.imgur.com/3vyRxg1.png)

## Features
- User registration, profiles and profile pictures
- A hashed database and XSS protection to prevent attacks by third parties
- Pagination
- The ability to create, update and delete blog posts

## Setup
1. Install Django by opening command prompt and typing 'pip install Django'
```
$ pip install Django
```
2. Extract the zip file of the repository
3. CD to directory of extracted zip
```
$ cd Downloads/Babble
```
4. Run the command 'python manage.py runserver'
```
$ python manage.py runserver
```
5. Navigate to localhost:8000 in your browser

## Backing up the server

To back up the server open command prompt and execute 'python backup.py', the database backup can be found in the backups directory.
```
$ python backup.py
```

## Authors

* **[Fhoughton](https://github.com/Fhoughton)** - Initial project

See also the list of [contributors](https://github.com/Fhoughton/Digit-Recognizer/contributors) who participated in this project.

## License

This project is licensed under the MIT license which means you can copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software under certain conditions. For more read: https://opensource.org/licenses/MIT

## Acknowledgments

* Thanks to [CoreyMSchafer](https://github.com/CoreyMSchafer)
* The [Django Project](https://www.djangoproject.com/)
