from flask import Flask, render_template, request, session
from classes.distribution import Distribution
from classes.region import Region
from classes.powerplant import Powerplant



prev_option = ""

def apps_distribution():
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == "edit":
            butshow, butedit = "disabled", "enabled"
        elif option == "delete":
            obj = Distribution.current()
            Distribution.remove(obj.id)
            if not Distribution.previous():
                Distribution.first()
        elif option == "insert":
            butshow, butedit = "disabled", "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            strobj = str(Distribution.get_id(0))
            strobj = strobj + ';' + request.form["distribution_date"] + ';' + \
            request.form["energy_supplied"] + ';' + request.form["powerplant_id"] + ';' + request.form["region_id"]
            obj = Distribution.from_string(strobj)
            Distribution.insert(obj.id)
            Distribution.last()
        elif prev_option == 'edit' and option == 'save':
            obj = Distribution.current()
            obj.distribution_date = request.form["distribution_date"]
            obj.energy_supplied = int(request.form["energy_supplied"])
            obj.powerplant_id = int(request.form["powerplant_id"])
            obj.region_id = int(request.form["region_id"])
            Distribution.update(obj.id)
        elif option == "first":
            Distribution.first()
        elif option == "previous":
            Distribution.previous()
        elif option == "next":
            Distribution.nextrec()
        elif option == "last":
            Distribution.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = Distribution.current()
        if option == 'insert' or len(Distribution.lst) == 0:
            id = 0
            id = Distribution.get_id(id)
            distribution_date = energy_supplied = powerplant_id = region_id = ""
        else:
            id = obj.id
            distribution_date = obj.distribution_date
            energy_supplied = obj.energy_supplied
            powerplant_id = obj.powerplant_id
            region_id = obj.region_id
        return render_template("distribution.html", butshow=butshow, butedit=butedit, 
                        id=id,distribution_date = distribution_date, powerplant_id=powerplant_id,region_id=region_id, 
                        ulogin=session.get("user"))
    else:
        return render_template("index.html", ulogin=ulogin)
# -*- coding: utf-8 -*-

