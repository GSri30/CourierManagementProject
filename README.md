## Courier Management System

<img align="right" src="__images/readme.gif" alt="png" width=150 height=150>
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![Version](https://img.shields.io/badge/version-1.0.0-green)]()
[![Issues](https://img.shields.io/github/issues-raw/GSri30/CourierManagementProject)](https://github.com/GSri30/CourierManagementProject/issues)
[![Closed Issues](https://img.shields.io/github/issues-closed-raw/GSri30/CourierManagementProject)](https://github.com/GSri30/CourierManagementProject/issues)
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)]() 
[![Pull Requests](https://img.shields.io/github/issues-pr/GSri30/CourierManagementProject)]()
[![Contributors](https://img.shields.io/github/contributors/GSri30/CourierManagementProject)]()


> The main aim of this project is to allow students to know about their couriers from any place. The project uses discord-webhooks to notify about the courier details.


### 🏠 [Homepage](#)

## 🛠️ Install
1.Install pipenv

```sh
pip3 install pipenv
```
2.Clone the project

```sh
git clone https://github.com/GSri30/CourierManagementProject.git
cd CourierManagementProject
```
3.Install the packages

```sh
pipenv shell
pipenv install --dev
```
4.Create a .env file inside "CourierManagement" folder and store the webhook url and django project secret key.
(For webhook url, create a discord channel and install a webhook into it and for secret key, use the "generate_secret.py" to get a random key or use secret.txt)
```sh
cd CourierManagement
echo WEBHOOK_URL="your url" >> .env
echo SECRET_KEY="your key" >> .env
```


5.Start the <a href="http://127.0.0.1:8000/">localhost</a> server

```sh
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

Alternatively, you can use the <a href="https://raw.githubusercontent.com/GSri30/CourierManagementProject/main/requirements.txt?token=ANBXICQM5X7WWYL7O6O7YRK75XYUI">requirements.txt</a> for installing the required packages.
 

## 🖮 Usage

```sh
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

<!--!Disabled-->
<!--Edit this section after making contributions. Only PRs of contributors will be merged!-->
<!-- ## 👤 Contributors
<table>
  <tr>
    <td align="center"><a href=""><img src="" width="100px;" alt=""/></td>
  </tr>
</table> -->

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/GSri30/CourierManagementProject/issues). 

## ☑️ Show your support

Give a ⭐️ if this project helped you!

## 📝 License

This project is [MIT](https://github.com/GSri30/CourierManagementProject/blob/main/LICENSE) licensed.