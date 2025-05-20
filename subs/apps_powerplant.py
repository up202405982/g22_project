from flask import Flask, render_template, request, session
from classes.powerplant import Powerplant
from classes.gridoperator import GridOperator

prev_option = ""

def apps_powerplant():
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == "edit":
            butshow, butedit = "disabled", "enabled"
        elif option == "delete":
            obj = Powerplant.current()
            Powerplant.remove(obj.id)
            if not Powerplant.previous():
                Powerplant.first()
        elif option == "insert":
            butshow, butedit = "disabled", "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            strobj = str(Powerplant.get_id(0))
            strobj = strobj + ';' + request.form["name"] + ';' + \
            request.form["capacity"] + ';' + request.form["plant type"] + ';' + request.form["operator id"]
            obj = Powerplant.from_string(strobj)
            Powerplant.insert(obj.id)
            Powerplant.last()
        elif prev_option == 'edit' and option == 'save':
            obj = Powerplant.current()
            obj.name = request.form["name"]
            obj.capacity = int(request.form["capacity"])
            obj.plant_type = request.form["plant type"]
            obj.operator_id = int(request.form["operator id"])
            
            Powerplant.update(obj.id)
        elif option == "first":
            Powerplant.first()
        elif option == "previous":
            Powerplant.previous()
        elif option == "next":
            Powerplant.nextrec()
        elif option == "last":
            Powerplant.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = Powerplant.current()
        if option == 'insert' or len(Powerplant.lst) == 0:
            id = 0
            id = Powerplant.get_id(id)
            name = capacity = plant_type = operator_id = ""
        else:
            id = obj.id
            name = obj.name
            capacity = obj.capacity
            plant_type = obj.plant_type
        return render_template("powerplant.html", butshow=butshow, butedit=butedit, 
                        id=id,name = name,capacity=capacity,plant_type=plant_type,operator_id=operator_id, 
                        ulogin=session.get("user"))
    else:
        return render_template("index.html", ulogin=ulogin)
# -*- coding: utf-8 -*-

