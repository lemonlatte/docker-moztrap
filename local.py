from os import environ

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "moztrap",
        "USER": "moztrap",
        "HOST": environ.get("MYSQL_PORT_3306_TCP_ADDR", ""),  # empty string == localhost
        "PASSWORD": "000000",
        "STORAGE_ENGINE": "InnoDB",
        "OPTIONS": {
            "init_command": "SET default_storage_engine=InnoDB"
        }
    }
}

USE_BROWSERID = False
