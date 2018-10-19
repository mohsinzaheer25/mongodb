#!/bin/python2.7
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["customerroles"]
mycol = mydb["appA"]

appid = raw_input('Please enter the appid: ')
env = raw_input('Please enter the environment: ')
modes = ['r', 'rw', 'app']

if mycol.find({"appID": appid}).count() > 0:
    count = 0
    for i in modes:
        groupname = []
        gid = []
        digitsofappid = appid[7:]
        groupname = appid.lower() + "_" + env + "_" + "db2" + "_" + i
        gid = mycol.find({"appID": appid}, {"_id": 0, "gid": 1}).sort('gid', pymongo.DESCENDING)
        rolename = groupname
    for x in gid:
        new_gid = int(x['gid']) + 3
        print(new_gid)
        mydata = [
            {"appID": appid, "env": env, "gid": new_gid,
                "groupname": groupname,
                "rolename": rolename},
        ]
        x = mycol.insert_many(mydata)
        count += 1
    print(`count` + " " + "columns inserted")
else:
    print("New App ID Found. Creating New App ID")
    counts = 1
    for i in modes:
        groupname = []
        gid = []
        digitsofappid = appid[7:]
        groupname = appid.lower() + "_" + env + "_" + "db2" + "_" + i
        gid = `1` + digitsofappid + `0` + `counts`
        rolename = groupname
        print(gid)
        counts += 1
        if mycol.find({"gid": gid}).count() > 0:
            print("Group ID already exists")
        else:
            mydata = [
                {"appID": appid, "env": env, "gid": gid,
                    "groupname": groupname,
                    "rolename": rolename},
            ]
            x = mycol.insert_many(mydata)
    col_count = counts - 1
    print(`col_count` + " " + "columns inserted")
