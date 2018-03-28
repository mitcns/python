# !/usr/bin/env python
# coding=utf-8

from distutils.log import warn as printf
import os
from random import randrange as rand

if isinstance(__builtins__, dict) and 'raw_input' in __builtins__:
    scanf = raw_input
elif hasattr(__builtins__, 'raw_input'):
    scanf = raw_input
else:
    scanf = input

COLSIZ = 10
FIELDS = ('login', 'userid', 'projid')
RDBMSs = {
    's': 'sqlite',
    'm': 'mysql',
    'g': 'gadfly'
}
DBNAME = 'test1'
DBUSER = '10k'
DB_EXC = None
NAMELEN = 16

tformat = lambda s: str(s).title().ljust(COLSIZ)
cformat = lambda s: s.upper().ljust(COLSIZ)

def setup():
    return RDBMSs[scanf('''
Choose a database system:

(M)ySQL
(G)adfly
(S)QLite

Enter choice:''').strip().lower()[0]]

def connect(db):
    global DB_EXC
    dbDir = '%s_%s' % (db, DBNAME)

    if db == 'sqlite':
        try:
            import sqlite3
        except ImportError:
            try:
                from pysqlite2 import dbapi2 as sqlite3
            except ImportError:
                return None
        DB_EXC = sqlite3
        if not os.path.isdir(dbDir):
            os.mkdir(dbDir)
        cxn = sqlite3.connect(os.path.join(dbDir, DBNAME))
    elif db == 'mysql':
        try:
            import MySQLdb
            import _mysql_exceptions as DB_EXC
            try:
                cxn = MySQLdb.connect(user=DBUSER)
                cxn.query('DROP DATABASE %s' % DBNAME)
                cxn.query('CREATE DATABASE %s' % DBNAME)
                cxn.query("GRANT ALL ON *.* to '10k'@'localhost'")
                cxn.commit()
                cxn.close()
                cxn = MySQLdb.connect(db=DBNAME)
            except DB_EXC.OperationalError:
                return None
        except ImportError:
            try:
                import mysql.connector
                import mysql.connector.errors as DB_EXC
                try:
                    cxn = mysql.connector.Connect(**{
                        'database': DBNAME,
                        'user': DBUSER
                    })
                except DB_EXC.InterfaceError:
                    return None
            except ImportError:
                return None
    elif db == 'gadfly':
        try:
            from gradly import gadfly
            DB_EXC = gadfly
        except ImportError:
            return None
        try:
            cxn = gadfly(DBNAME, dbDir)
        except IOError:
            cxn = gadfly()
            if not os.path.isdir(dbDir):
                os.mkdir(dbDir)
            cxn.startup(DBNAME, dbDir)
    else:
        return None
    return cxn

def create(cur):
    try:
        cur.execute('''
        CREATE TABLE users (login VARCHAR(%d),
        usrid INTEGER,
        projid INTEGER)
        ''' % NAMELEN)
    except DB_EXC.OperationalError as e:
        drop(cur)
        create(cur)

drop = lambda cur: cur.execute('DROP TABLE users')

NAMES = (
    ('Mavin', 2009), ('Kevin', 4326), ('Rouge', 2048),
    ('MIT', 1988), ('mitcns', 2015), ('lanmomo', 2010),
    ('ma', 1989), ('xiaoma', 2024), ('laoma', 2088)
)

def randName():
    pick = set(NAMES)
    while pick:
        yield pick.pop()

def insert(cur, db):
    if db == 'sqlite':
        cur.executemany("INSERT INTO users VALUES (?, ?, ?)", [(who, uid, rand(1, 5)) for who, uid in randName()])
    elif db == 'gadfly':
        for who, uid in randName():
            cur.execute("INSERT INTO users VALUES (?, ?, ?)", (who, uid, rand(1, 5)))
    elif db == 'mysql':
        cur.executemany("INSERT INTO users VALUES (%s, %s, %s)", [(who, uid, rand(1, 5)) for who, uid in randName()])

getRC = lambda cur: cur.rowcount if hasattr(cur, 'rowcount') else -1

def update(cur):
    fr = rand(1, 5)
    to = rand(1, 5)
    cur.execute("UPDATE users SET projid=%d WHERE projid=%d" % (to, fr))
    return fr, to, getRC(cur)

def delete(cur):
    rm = rand(1, 5)
    cur.execute("DELETE FROM users WHENE projid=%d" % rm)
    return rm, getRC(cur)

def dbDump(cur):
    cur.execute("SELECT * FROM users")
    printf('\n%s' % ''.join(map(cformat, FIELDS)))
    for data in cur.fetchall():
        printf(''.join(map(tformat, data)))

def main():
    db = setup()
    printf('*** Connect to %r database' % db)
    cxn = connect(db)
    if not cxn:
        printf('ERROR: %r not supported or unreachable, exit' % db)
        return
    cur = cxn.cursor()

    printf('\n*** Creating users table')
    create(cur)

    printf('Inserting names into table')
    insert(cur, db)
    dbDump(cur)

    printf('\n*** Randomly moving folks')
    fr, to, num = update(cur)
    printf('\t(%d users moved) from (%d) to (%d)' % (num, fr, to))
    dbDump(cur)

    printf('\n*** Dropping users table')
    drop(cur)
    printf('\n*** Close cxns')
    cur.close()
    cxn.commit()
    cxn.close()

if __name__ == '__main__':
    main()
