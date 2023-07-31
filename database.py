TORTOISE_ORM = {
    "connections": {"default": "postgres://root:root@localhost:5432/test_db"},
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        },
    },
}