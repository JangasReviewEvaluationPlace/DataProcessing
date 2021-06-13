import psycopg2

import configs


class Postgres:
    def __enter__(self):
        self.con = psycopg2.connect(**configs.POSTGRES_CONFIGS)
        self.con.autocommit = True
        self.cur = self.con.cursor()
        return self

    def __exit__(self, *args, **kwargs):
        self.con.close()
