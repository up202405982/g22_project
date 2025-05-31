from flask import Flask, render_template, request, session
from classes.gridoperator import GridOperator

prev_option = ""

def apps_gridoperator():
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == "edit":
            butshow, butedit = "disabled", "enabled"
        elif option == "delete":
            obj = GridOperator.current()
            GridOperator.remove(obj.id)
            if not GridOperator.previous():
                GridOperator.first()
        elif option == "insert":
            butshow, butedit = "disabled", "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            strobj = str(GridOperator.get_id(0))
            strobj = strobj + ';' + request.form["name"] + ';' + \
            request.form["contact"] 
            obj = GridOperator.from_string(strobj)
            GridOperator.insert(obj.id)
            GridOperator.last()
        elif prev_option == 'edit' and option == 'save':
            obj = GridOperator.current()
            obj.name = request.form["name"]
            obj.contact = request.form["contact"]
            
            GridOperator.update(obj.id)
        elif option == "first":
            GridOperator.first()
        elif option == "previous":
            GridOperator.previous()
        elif option == "next":
            GridOperator.nextrec()
        elif option == "last":
            GridOperator.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = GridOperator.current()
        if option == 'insert' or len(GridOperator.lst) == 0:
            id = 0
            id = GridOperator.get_id(id)
            name = contact = ""
        else:
            id = obj.id
            name = obj.name
            contact = obj.contact
            
        return render_template("gridoperator.html", butshow=butshow, butedit=butedit, 
                        id=id,name = name,contact=contact, 
                        ulogin=session.get("user"))
    else:
        return render_template("index.html", ulogin=ulogin)
# -*- coding: utf-8 -*-

