"""
Created on July 2020

@author: Claudio Munoz Crego (ESAC)

Python module to handle my_sql connection
"""

import os
import sys
import logging
import mysql.connector

from mysql.connector import errorcode


class MysqlConnector(object):
    """
    This class allows to connect to my_sql using my_sql python package.
    """

    def __init__(self, config_connection=None, output_path=None):
            
        self.db = 'database_tbd'
        self.db_user = 'user_tbd'
        self.passwd = 'password_tbd'

        if config_connection is None:
            config_connection = {}
        self.__connect__(config_connection)

        self.output_dir = output_path
        if output_path is None:
            self.output_dir = './'

    def get_mysql_connector(self):
        """
        Returns my_sql connector
        """

        return self.cnx 
        
    def __connect__(self, config_connection):
        """ 
        Connects to my_sql handling connection errors,
        use the try statement and catch all errors using the errors.Error exception
        """

        try:

            if config_connection is None:

                self.cnx = mysql.connector.connect(option_files='~/.myJuice.cnf')

            elif isinstance(config_connection, dict):

                self.cnx = mysql.connector.connect(**config_connection)

                self.db = config_connection['database']
                self.db_user = config_connection['user']
                self.passwd = config_connection['password']

            elif os.path.exists(config_connection):

                self.__connect_via_cnf_file__(config_connection)

            elif isinstance({}, config_connection):

                self.cnx = mysql.connector.connect(**config_connection)

                self.db = config_connection['database']
                self.db_user = config_connection['user']
                self.passwd = config_connection['password']

            else:

                logging.error('No database connexion parameters provided')
                sys.exit()

        except mysql.connector.Error as e:

            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            elif e.errno == errorcode.ER_USER_DOES_NOT_EXIST:
                print('Mysql user does not exist')

            errorcode.ER_ABORTING_CONNECTION
            print("Mysql connection error code:", e.errno)  # error number
            print("SQLSTATE value:", e.sqlstate)  # SQLSTATE value
            # print("Error message:", e.msg)  # error message
            print("Error message::", e)  # errno, sqlstate, msg values

            sys.exit()

    def __connect_via_cnf_file__(self, config_connection):
        """
        Connects to my_sql handling connection errors,
        use the try statement and catch all errors using the errors

        :param config_connection: config file connexion parameters
        :type: string
        """

        try:

            self.cnx = mysql.connector.connect(option_files=config_connection)

            if os.path.exists(config_connection):

                param = {}
                with open(config_connection) as config_file:
                    for line in config_file:
                        if '=' in line:
                            name, var = line.strip().split('=')
                            param[name] = var

                self.db = param['database']
                self.db_user = param['user']
                self.passwd = param['password']

                return param

            else:

                logging.error('File does not exist: {}'.format(config_connection))
                sys.exit()

        except mysql.connector.Error as e:

            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            elif e.errno == errorcode.ER_USER_DOES_NOT_EXIST:
                print('Mysql user does not exist')

            errorcode.ER_ABORTING_CONNECTION
            print("Mysql connection error code:", e.errno)  # error number
            print("SQLSTATE value:", e.sqlstate) # SQLSTATE value
            # print("Error message:", e.msg)  # error message
            print("Error message::", e)  # errno, sqlstate, msg values

            sys.exit()

    def table_exists(self, table_name):
        """
        Check is table exists in current db

        :param table_name: name of table
        """

        cnx = self.get_mysql_connector()
        cursor = cnx.cursor()

        query = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name like '{}' ".format(table_name)
        cursor.execute(query)

        if cursor.fetchone()[0] == 1:
            logging.debug('Table {1} exists in db {0}'.format('juicedb', table_name))
            return True
        else:
            logging.debug('Table {1} does not exist in db {0}'.format('juicedb', table_name))
            return False

    def drop_table(self, table_name):
        """
        Drop table if exists in current db

        :param table_name: name of table
        """

        cnx = self.get_mysql_connector()
        cursor = cnx.cursor()

        query = "DROP TABLE IF EXISTS " + table_name
        cursor.execute(query)
        logging.info('table {} deleted from db {}'.format(table_name, 'juicedb'))

        cnx.commit

    def remove_row(self, table_name, field, record):
        """
        Remove specific record where table field = record value

        :param table_name: name of table
        :param field: field of table
        :param record: filter value for a given table field
        """

        cursor = self.cnx.cursor()
        # record = record[0]
        # query = "DELETE FROM %s WHERE %s LIKE '%s'" %(table, field, record)
        query = "DELETE FROM %s WHERE %s=%s" % (table_name, field, record)
        cursor.execute(query)
        self.cnx.commit()

    def close(self):
        """
        Close database connection
        """

        self.cnx.close()

    def insert_into_table(self, table_name, values=[]):
        """
        Insert values in table

        :param table_name:
        :param values:
        :return:
        """

        try:
            cursor = self.cnx.cursor()
            if isinstance(values[0], list):
                for val in values:
                    # logging.debug('insert into {} {} values {}'.format(table_name, col_names, tuple(val)))
                    val.insert(0, 0)  # add 0/Null into an indexed AUTO_INCREMENT
                    # query = "insert into `{}` values {}".format(table_name, tuple(val))
                    cursor.execute("insert into {} values {}".format(table_name, tuple(val)))
            else:
                # logging.debug('insert into {} {} values {}'.format(table_name, col_names, tuple(values)))
                values.insert(0, 0)  # add 0/Null into an indexed AUTO_INCREMENT
                cursor.execute("insert into {} values {}".format(table_name, tuple(values)))

            self.cnx.commit()
        except (Exception, mysql.connector.DatabaseError) as error:
            print(error)
            sys.exit()

    def dump_table(self, table):
        """
        Dump database table

        :param table: name of table
        :return:
        """

        import subprocess

        output_file = os.path.join(self.output_dir, table + '.sql')

        command = 'mysqldump -u{} -p{} {} {} > {}'.format(self.db_user, self.passwd, self.db, table, output_file)

        try:
            p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

            while True:
                line = p.stdout.readline()
                if not line:
                    break
                elif 'Error' in '{}'.format(line):
                    logging.debug('{}'.format(line))
                # self.log_file.write('\n{}'.format(line))

            p.wait()

            if p.returncode != 0:
                print(p.returncode, p.stdout, p.stderr)
                p.terminate()

            logging.debug('Execution completed!')
            logging.info('Sql dump file created: {}'.format(output_file))

        except Exception:

            logging.error('command failed: {} '.format(command))




