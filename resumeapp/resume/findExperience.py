from datetime import datetime
import re

def findDatesFromText(text):
    lastDate = False

    for i in text.split("\n"):
        print(i)
        if "present" in i or "current" in i or "ongoing" in i.lower() or "since" in i.lower():
            currentDate = datetime.now()
            lastDate = str(currentDate.day) + "/" + str(currentDate.month) + "/" + str(currentDate.year)

    monthsToNum = {"jan": 1 , "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12, "sept": 9,
                  "january": 1 , "february": 2, "march": 3, "april": 4, "may": 5, "june": 6, "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12}
    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec", "sept",
            "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    yearNames = [*range(1990, 2022, 1)]
    
    #Dates in format June 2021
    listOfDates1 = re.findall(r'[A-Z,a-z]+\s\d{4}', text)
    listOfDates1 = list(set(listOfDates1))
    print("listOfDates1", listOfDates1)

    listOfDates1rev = []
    for i in range(0, len(listOfDates1)):
        print(listOfDates1[i].split(" ")[0])
        listOfDates1[i] = listOfDates1[i].replace(",", "")
        listOfDates1[i] = listOfDates1[i].replace(".", "")
        for j in months:
            #print(j)
            if j in listOfDates1[i].split(" ")[0].lower():
                print("j", j)
                date = "1/" + str(monthsToNum[j]) + "/" + str(listOfDates1[i].split(" ")[1])
                listOfDates1rev.append(date)
                break

    listOfDates1 = listOfDates1rev

    #Dates in format 02-2021
    listOfDates2 = re.findall(r'\d{1,2}-\d{4}', text)
    listOfDates2 = list(set(listOfDates2))
    for i in range(0, len(listOfDates2)):
        listOfDates2[i] = listOfDates2[i].replace("-", "/")
        date = "1/" + listOfDates2[i]
        listOfDates2[i] = date

    #Dates in format 02/2021
    listOfDates3 = re.findall(r'\d{1,2}/\d{4}', text)
    listOfDates3 = list(set(listOfDates3))
    for i in range(0, len(listOfDates3)):
        date = "1/" + listOfDates3[i]
        listOfDates3[i] = date

    #Dates in format 02/02/2021
    listOfDates4 = re.findall(r'\d{1,2}/\d{1,2}/\d{4}', text)
    listOfDates4 = list(set(listOfDates4))


    #Dates in format 02-02-2021
    listOfDates5 = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', text)
    listOfDates5 = list(set(listOfDates5))
    for i in range(0, len(listOfDates5)):
        listOfDates5[i] = listOfDates5[i].replace("-", "/")


    #Dates in format June-2021
    listOfDates6 = re.findall(r'[A-Z,a-z]+-\d{4}', text)
    listOfDates6 = list(set(listOfDates6))
    for i in range(0, len(listOfDates6)):
        date = "1/" + str(monthsToNum[listOfDates6[i].split("-")[0].lower()]) + "/" + str(listOfDates6[i].split("-")[1])
        listOfDates6[i] = date


    #Dates in format June/2021
    listOfDates7 = re.findall(r'[A-Z,a-z]+/\d{4}', text)
    listOfDates7 = list(set(listOfDates7))
    for i in range(0, len(listOfDates7)):
        date = "1/" + str(monthsToNum[listOfDates7[i].split("/")[0].lower()]) + "/" + str(listOfDates7[i].split("/")[1])
        listOfDates7[i] = date


    listOfDates = listOfDates1 + listOfDates2 + listOfDates3 + listOfDates4 + listOfDates5 + listOfDates6 + listOfDates7
    listOfDates = [i for i in listOfDates if int(i.split("/")[2]) in yearNames]
    listOfDates = sorted(listOfDates, key= lambda x: x.split("/")[2])

    print("listOfDates", listOfDates)

    if not lastDate:
        lastDate = listOfDates[-1]
    firstDate = listOfDates[0]
    
    print("firstDate", firstDate)
    print("lastDate", lastDate)

    days = int(lastDate.split("/")[0]) - int(firstDate.split("/")[0])
    months = int(lastDate.split("/")[1]) - int(firstDate.split("/")[1])
    years = int(lastDate.split("/")[2]) - int(firstDate.split("/")[2])
    print(days, months, years)
    experience = round(days/365 + months/12 + years, 1)
    return experience
