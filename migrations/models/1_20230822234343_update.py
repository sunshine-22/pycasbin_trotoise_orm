from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "state" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "state_name" VARCHAR(100) NOT NULL,
    "country_id" UUID REFERENCES "country" ("id") ON DELETE SET NULL,
    "created_by_id" UUID REFERENCES "usertable" ("id") ON DELETE SET NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "state";"""
