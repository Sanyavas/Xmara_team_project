prompt_for_ai = """ 
# Xmara Web App (GoIT final Project)

## Xmara is a web application coded on Django framework and Python, that allows you to store and handle your contacts, notes, and files in one place safely and remotely.

## How to setup web app:

- Clone the repository to your computer:

```sh
$ git clone https://github.com/DenBilokon/Xmara.git

```

- Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```
- Create your **.env file** using env.example:
    - Create **Postgres** database to storage data and fill the neccessary fields in **.env file** ( DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT ).
    - Use your email account credentials to fill the neccessary fields in **.env file** ( EMAIL_PORT,EMAIL_HOST_USER, EMAIL_HOST_PASSWORD ).
    - Create your **Cloudinary account** ( https://cloudinary.com/ ) in order to obtain credentials for **.env file** ( CLOUD_NAME, CLOUD_API_KAY, CLOUD_API_SECRET ). On your **Cloudinary** account **Dashboard** use data from variables **Cloud Name**, **API Key**, **API Secret**.
    - Create your **OPEN AI** account ( https://openai.com/blog/openai-api ) and find API Key in order to obtain credentials for **.env file** ( OPENAI_KEY ).
    - Create your **Coin API** account (https://customerportal.coinapi.io/login) to obtain credentials for **.env file** (CRYPTO_API_KEY).
- Install the dependencies.
- Make Migrations.
- Move to ../contacts_web_app directory and run the program:

```sh
(env)$ cd contacts_web_app
(env)$ python manage.py runserver
```
- Follow the link  `http://127.0.0.1:8000/`.
- Enjoy!
# What Xmara can do:
When running Xmara app and following link http://localhost:8000/ you have opportunity:
- read fresh news ( war news, sport news, war statistic, weather, currency )
- login or register for more features
- only logined users can:
  - communicate with Open AI for help and advise
  - add contacts, notes, files
  - edit contacts, notes, files
  - delete contacts, notes, files
  - search contacts, notes, files
  - sort contacts, notes, files
  - filter files
  - download different type of files
  - upload files
  - look your likely tags in the notes
  - mark your notes as active or done
  - check when your contact has birthdays and never forget to congratulate him/her
  - change your avatar


# Used technologies:
- Python 3.11
- Django 4.2.2
- BeautifulSoup 4
- Sphinx
- PostgreSQL 12.0
- OpenAI API
- Cloudinary
- Privatbank API
- Coin API
- Bootswatch
- HTML5
- CSS3
- Docker
- GitHub
- Fly

# Developers:
1. Denis Bilokon
2. Oleksand Vasylyna
3. Denis Zaytsev
4. Oleksii Latypov
"""