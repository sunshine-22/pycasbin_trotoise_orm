from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "casbin_rule" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "ptype" VARCHAR(255) NOT NULL,
    "v0" VARCHAR(255),
    "v1" VARCHAR(255),
    "v2" VARCHAR(255),
    "v3" VARCHAR(255),
    "v4" VARCHAR(255),
    "v5" VARCHAR(255)
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "casbin_rule";"""
