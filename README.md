# Trading App

## For Production

### Requirements 
- Ansible
- Vagrant
- Virtual Box

For Ansible you can install with pip.
```
pip install ansible
```

You cand download Vagrant [here](https://www.vagrantup.com/downloads.html)
You cand download VirtualBox [here](https://www.virtualbox.org/wiki/Downloads)

### Quick start

Execute command:

```
vagrant up
```
This command will create a virtual machine with all services and requirements

Also you can execute this command: 

```
vagrant provision
```

When the script ends you cand see in 
-   http://192.168.33.10:3400/  the frontedApp.
-   http://192.168.33.10/api/1.0/ Api browsable.

In API Browsable you can create two or more money code to test the front-end app.

### DATA 

The data for [fixer.io](http://fixer.io/) should be the name for coins api like EUR,GBP, USD ...

## For Development

### Backend App

#### Requirements 
- Python 3.5 or more
- virtualenv
```
pip install virtualenv
```
#### Quick start

First clone the repository: 

```
>>  git clone https://github.com/JoseAntpr/tradingApp.git
>>  cd tradingApp 
```

You need virtualenv installed to work in a virtual enviroment:
```
# Create virtual enviroment 
>> virtualenv -p python3 <nameVirtualEnv>
# Activate virtual enviroment
>> source <nameVirtualEnv>/bin/activate
# Install the required Python Packages
```

Optional commands for virtualenv:
```
# Disable Python virtual enviroment
>> deactivate
# Add a requirement to the virtualenv requirements
>> pip freeze > requirements.txt
```

#### Development server
Run `python manage.py runserver` for a dev server. Navigate to `http://localhost:80000/`.

#### test

```
>> (venv) python manage.py test
```

### Frontend App

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 1.3.1.

#### Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

#### Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

#### Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `-prod` flag for a production build.

# License
MIT
