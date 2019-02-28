# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 14:55:54 2019

@author: z3525552
"""

import sqlite3

def connect():
    conn=sqlite3.connect("scopusids.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS scopus (zid INTEGER PRIMARY KEY, lastname text, firstname text, scopusid integer)")
    conn.commit()
    conn.close()

def insert(zid,lastname, author, firstname, scopusid):
    conn=sqlite3.connect("scopusids")
    cur=conn.cursor()
    cur.execute("INSERT INTO scopus VALUES (NULL,?,?,?,?)",(zid,lastname, firstname, scopusid))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("scopusids")
    cur=conn.cursor()
    cur.execute("SELECT * FROM scopus")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(zid="", lastname="", firstname="", scopusid=""):
    conn=sqlite3.connect("scopusids")
    cur=conn.cursor()
    cur.execute("SELECT * FROM scopus WHERE zid=? OR lastname=? OR firstname=? OR scopusid=?", (zid, lastname, firstname, scopusid))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(zid):
    conn=sqlite3.connect("scopusids")
    cur=conn.cursor()
    cur.execute("DELETE FROM scopus WHERE zid=? ",(zid,))
    conn.commit()
    conn.close()

def update(zid, lastname, firstname, scopusid):
    conn=sqlite3.connect("scopusids")
    cur=conn.cursor()
    cur.execute("UPDATE book SET lastname=?, firstname=?, scopusid=? WHERE zid=?",(lastname, firstname, scopusid, zid))
    conn.commit()
    conn.close()