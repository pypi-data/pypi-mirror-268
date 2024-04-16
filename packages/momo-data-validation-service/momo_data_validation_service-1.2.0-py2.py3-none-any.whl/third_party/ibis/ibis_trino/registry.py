import sqlalchemy as sa
from ibis.backends.base.sql.alchemy import sqlalchemy_operation_registry


operation_registry = sqlalchemy_operation_registry.copy()

def to_utf8(t):
    return sa.func.convert(t, sa.sql.literal_column("'UTF8'"))

def to_hex(t):
    return sa.func.hex(t)

def sha256(t):
    return sa.func.standard_hash(t, sa.sql.literal_column("'SHA256'"))