from seCore.CustomLogging import logger

from seSql import sql
from seSql.dbc.JDBC import jdbcLoaded, jdbcDriver


def test_jdbc():
    oSql = sql()
    oSql.connect(
        server="SQL5101.site4now.net",
        port=1433,
        user="db_a82904_cybernetic_admin",
        password="tb7qiwqer8mee68",
        trust="no",
        driverOverride="jdbc"
    )
    if oSql.isConnected:
        # oSql.query("SELECT @@version as version")
        oSql.query("select @@version as version")

        # oSql.query("select * from dbo.winequality_red;")

        try:
            oSql.query("select * from dbo.winequality_red;")
        except Exception as e:
            logger.error(f'Exception: {e}')

        try:
            oSql.query("select * from dba.winequality_red;")
        except Exception as e:
            logger.error(f'Exception: {e}')


def test_jdbcLoaded():
    assert jdbcLoaded(3) is False


def test_jdbcDriver():
    assert jdbcDriver(3) == "Error finding JDBC driver"
