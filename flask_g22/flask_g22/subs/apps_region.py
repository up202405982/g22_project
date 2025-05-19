from flask import Flask, render_template, request, session
from classes.region import Region
from classes.powerplant import Powerplant
from classes.distribution import Distribution

prev_option = ""

def apps_region():
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == "edit":
            butshow, butedit = "disabled", "enabled"
        elif option == "delete":
            obj = Region.current()
            Region.remove(obj.id)
            if not Region.previous():
                Region.first()
        elif option == "insert":
            butshow, butedit = "disabled", "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            strobj = str(Region.get_id(0))
            strobj = strobj + ';' + request.form["name"] + ';' + \
            request.form["area"] + ';' + request.form["population"]
            obj = Region.from_string(strobj)
            Region.insert(obj.id)
            Region.last()
        elif prev_option == 'edit' and option == 'save':
            obj = Region.current()
            obj.name = request.form["name"]
            obj.area = int(request.form["area"])
            obj.population = int(request.form["population"])
            Region.update(obj.id)
        elif option == "first":
            Region.first()
        elif option == "previous":
            Region.previous()
        elif option == "next":
            Region.nextrec()
        elif option == "last":
            Region.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = Region.current()
        if option == 'insert' or len(Region.lst) == 0:
            id = 0
            id = Region.get_id(id)
            name = area = population = ""
        else:
            id = obj.id
            name = obj.name
            area = obj.area
            population = obj.population
        return render_template("region.html", butshow=butshow, butedit=butedit, 
                        id=id,name = name,area=area,population=population, 
                        ulogin=session.get("user"))
    else:
        return render_template("index.html", ulogin=ulogin)
# -*- coding: utf-8 -*-

