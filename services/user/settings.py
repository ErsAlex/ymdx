from common.database.settings import BaseDatabaseSettings
from global_settings import DB_DSN
class UserDatabaseSettings(BaseDatabaseSettings):
    db_dsn: str = DB_DSN