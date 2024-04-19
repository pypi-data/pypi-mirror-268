import os.path
import json
import datetime as dt

def usr_settings(service) -> dict:
    # open settings json file, if not exists, generate new one
    #TODO: fix case where settings.json is empty
    if not os.path.exists("settings.json"):
        usr_settings_gen(service)
    return json.load(open("settings.json", "r"))


def usr_settings_gen(service)-> None:
    # creates settings json file
    with (open("settings.json", "w")) as settings:
        settings.write(json.dumps({
            "primaryCal": "",
            "role": "",
            "timezone": ""
        }))
    usr_settings_edit(json.load(open("settings.json", "r")), service)


def usr_settings_print(settings: dict) -> None:
    # prints settings
    for i in settings:
        print (f"{i}: {settings[i]}")
    
    
def usr_settings_edit(settings:dict, service: object) -> None:
    # edit settings
    usr_settings_print(settings)
    usrInput = input("What would you like to edit? \n\n[p] - edit which Google calendar will be considered\n[t] - edit timezone\n[e] - exit\n\n-:")
    if usrInput in ["primaryCal", "p"]:
        usr_settings_primaryCal(settings, service)
    elif usrInput in ["timezone", "t"]:
        usr_settings_timezone(settings)
    elif usrInput in ["exit", "e", "q"]:
        return
    else:
        print ("Invalid input. Please try again.")
        usr_settings_edit(service)


def usr_settings_primaryCal(settings: dict, service: object) -> None:
    # edits primary calendar in settings json file

    calendars = service.calendarList().list().execute()
    calendar_list = []
    calendar_id = []
    for index, calendar in enumerate(calendars["items"]):
        print (str(index) + " " + calendar["summary"])
        calendar_list.append(calendar["summary"])
        calendar_id.append(calendar["id"])
        
    usr_c = input("Which calendar would you like to set as primary? \n\n-:")
    access = service.acl().list(calendarId=calendar_id[int(usr_c)]).execute()
    role = access["items"][-1]["role"] #are you kidding me? who came up with this
    try:
        settings["primaryCal"] = calendar_id[int(usr_c)]
        settings["role"] = role
        json.dump(settings, open("settings.json", "w"))
        print (f"Primary calendar set to {calendar_list[int(usr_c)]}")
    except:
        print ("Invalid input. Exiting")
        return
    
    
def usr_settings_timezone(settings:dict) -> None:
    settings["timezone"] = str(dt.timezone(dt.timedelta(hours=1)))
    json.dump(settings, open("settings.json", "w"))


def usr_settings_delete() -> None:
    #deletes user settings
    os.remove("settings.json")


def event_create(settings:dict, service: object) -> None:
    # crete event in primary calendar
    if settings["primaryCal"] == "":
        print ("Primary calendar not set. Please set primary calendar.")
        usr_settings_primaryCal(settings, service)
    if settings["role"] != "owner":
        print ("You do not have permission to edit this calendar. Select a different calendar.")
        return
    calendar = usr_settings(service)
    calId = calendar["primaryCal"]
    event = event_construct(settings)
    
    service.events().insert(calendarId=calId, body=event, sendNotifications=False).execute()
    
    
def event_construct(settings: dict) -> dict:
    today = dt.date.today()
    date = input("Date of the event (day-month): ").split("-") 
    if dt.datetime.strptime(date[1], "%m").month < today.month:
        date = str(today.year + 1) + "-" + date[1] + "-" + date[0]
    else:
        date = str(today.year) + "-" + date[1] + "-" + date[0]
    print (date)
    summaryInp = str(input("Name of the event: "))
    event = {
    'summary': summaryInp,
    'start': {
            'date': date,
            'timeZone': settings["timezone"],
        },
        'end': {
            'date': date,
            'timeZone': settings["timezone"],
        }, 
    }

    return event
    
    
def event_edit(service:object, settings:dict) -> None:
    # edit event in primary calendar
    print("Editing event")
    events = event_list(settings, service, 10)
    for index, event in enumerate(events):
        print (f"{index}: {event['summary']} - {event['end']['date']}")
    usrInput = int(input("\n\n Which event would you like to edit?\n-:"))
    service.events().edit(calendarId=settings["primaryCal"], eventId=events[usrInput]["id"]).execute()
    
    
def event_delete(settings:dict, service:object) -> None:
    # delete upcoming event in primary calendar
    print("Deleting event")
    events = event_list(settings, service, 10)
    for index, event in enumerate(events):
        print (f"{index}: {event['summary']} - {event['end']['date']}")
    usrInput = int(input("\n\n Which event would you like to delete?\n-:"))
    service.events().delete(calendarId=settings["primaryCal"], eventId=events[usrInput]["id"]).execute()


def event_list(settings:dict, service:object, num:int) -> list:
    eventList = []
    events = service.events().list(calendarId=settings["primaryCal"]).execute()
    index = 0
    for event in events["items"]:
        #TODO clean this up
        try:
            eventDate = dt.datetime.strptime(event["end"]["date"], "%Y-%m-%d")
            if eventDate.date() > dt.date.today():
                eventList.append(event)
                index += 1
        except:
            eventDate = dt.datetime.strptime(event["end"]["dateTime"], "%Y-%m-%dT%H:%M:%S%z")
            if eventDate.date() > dt.date.today():
                eventList.append(event) #TODO find a solution to print time as well in this case
                index += 1
        if index == num:
            return eventList
    return eventList


def event_list_print(eventList:list) -> None:
    for event in eventList:
        print (f"{event['summary']} - {event['end']['date']}")
        
def account_remove(settings:dict) -> None:
    usrInput = input(f"Currently signed in as {settings} Are you sure you want to remove account? This will also remove saved settings (y/n)")
    if usrInput in ["yes", "y"]:
        os.remove("token.json")
        usr_settings_delete()