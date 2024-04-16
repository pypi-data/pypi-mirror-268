"""
Created on Nov, 2020

@author: Claudio Munoz Crego (ESAC)

Python module to handle sqlite3 tables

"""

import os
import sqlite3


class Sqlite3Handler(object):
    """
    Class to connect to postgres qla db and query contents
    """

    def __init__(self, db_file):

        self.db_file = db_file


def create_sql_table(my_data, table_name=''):

    conn = sqlite3.connect("pythonsqlite.db")

    cur = conn.cursor()

    ##push the dataframe to sql
    my_data.to_sql(my_data, conn, if_exists="replace")

    pd.read_sql_query("select * from {};".format(my_data), conn)

    ##create the table

    cur.execute(
        """
        create table {} as 
        select * from {}
        """.format(table_name, my_data))

    cur.commit()

    conn.close()


def getTableDump(db_file, table_to_dump, output_dir='./'):
    """
    Create Table dump from sqlite3

    :param db_file: sqlite3 file db
    :param table_to_dump: table name
    :param output_dir: output directory
    :return:
    """

    conn = sqlite3.connect(':memory:')

    cur = conn.cursor()
    cur.execute("attach database '" + db_file + "' as attached_db")
    cur.execute("select sql from attached_db.sqlite_master "
               "where type='table' and name='" + table_to_dump + "'")
    sql_create_table = cur.fetchone()[0]
    cur.execute(sql_create_table);
    cur.execute("insert into " + table_to_dump +
               " select * from attached_db." + table_to_dump)
    conn.commit()
    cur.execute("detach database attached_db")
    sql_contents = "\n".join(conn.iterdump())

    conn.close()

    output_dir = './'
    sql_file = os.path.join(output_dir, table_to_dump + '.sql')

    file_out = open(sql_file, 'w')

    for line in sql_contents:
        file_out.write(line)

    file_out.close()

    logging.info('New file created: {}'.format(sql_file))

if __name__ == '__main__':

    import logging
    import datetime

    import pandas as pd

    from esac_juice_pyutils.commons.my_log import setup_logger

    print('\n-----------------------------------------------\n')
    # setup_logger()
    setup_logger('debug')

    conn = sqlite3.connect("flights.db")

    cur = conn.cursor()

    # cur.execute('DROP TABLE {}'.format('daily_flights'))

    cur.execute("CREATE TABLE IF NOT EXISTS daily_flights" +
                '''(`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                `id2` integer, 
                `departure` date, 
                `arrival` date, 
                `number` text, 
                `route_id` integer)''')

    cur.execute("insert into daily_flights values (1, 1, '2016-09-28 0:00', '2016-09-28 12:00', 'T1', 1)")
    conn.commit()

    df = pd.read_sql_query("select * from daily_flights;", conn)

    print(df)

    sql_contents = "\n".join(conn.iterdump())

    conn.close()

    output_dir = './'
    sql_file = os.path.join(output_dir, 'table_to_dump' + '.sql')

    file_out = open(sql_file, 'w')

    for line in sql_contents:
        file_out.write(line)
    file_out.close()

    logging.info('New file created: {}'.format(sql_file))


    df = pd.DataFrame(
        [[1, datetime.datetime(2016, 9, 29, 0, 0),
          datetime.datetime(2016, 9, 29, 12, 0), 'T1', 1]],
        columns=["id", "departure", "arrival", "number", "route_id"])

    df.to_sql("daily_flights", conn, if_exists="replace")


    df = pd.read_sql_query("select * from daily_flights;", conn)

    print(df)




    logging.info('end test!')
