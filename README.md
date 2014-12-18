# Moztrap

This is a test case management system base on Python/Django

## Additional Information

[Ubuntu: Piloting a new test case management tool](https://blueprints.launchpad.net/ubuntu/+spec/other-p-qa-test-case-management-tool)

## Installation

### Setup and Run a MySQL Server

``` shell
$ docker pull orchardup/mysql
$ docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=qwerty --name mysql orchardup/mysql
```

### Initiate Moztrap

``` shell
docker run -i -t --link=mysql:mysql -e MYSQL_ENV_MYSQL_PASS=qwerty docker-moztrap /moztrap-init.sh
```

This command will initiate database for Moztrap.

### Run Moztrap

``` shell
$ docker run -i -t --link=mysql:mysql -p 8000:8000 docker-moztrap
```

### Additional Command

``` shell
$ docker run -i -t --link=mysql:mysql -p 8000:8000 docker-moztrap /moztrap-add-user.sh user user@localhost qwerty
```

## Simple User Tutorial

### Some basic steps

1. Create an environment
2. Create a product
3. Create a version
4. Create a test suit
5. Create test cases
6. Create a test run
7. Run a test and submit its result (Pass/Failed)
