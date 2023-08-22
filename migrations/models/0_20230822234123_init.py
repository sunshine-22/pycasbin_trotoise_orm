from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "contact" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL,
    "phone_number" VARCHAR(20) NOT NULL
);
CREATE TABLE IF NOT EXISTS "usertable" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS "country" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "country_name" VARCHAR(100) NOT NULL,
    "created_by_id" UUID REFERENCES "usertable" ("id") ON DELETE SET NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
