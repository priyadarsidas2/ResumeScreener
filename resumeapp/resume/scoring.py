import pandas as pd
import numpy as np
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import time
from googlesearch import search
from newspaper import Article
import random
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('omw-1.4')
stop_words = stopwords.words('english')
stopset = set(nltk.corpus.stopwords.words('english'))
import string
punct = string.punctuation
#lemmatization
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
nltk.download('wordnet')
from datetime import datetime

def scoringAndExperienceCheck(primarySkill, secondarySkill, extractedText):
    df = pd.read_excel("SkillsList.xlsx")

    #remove stopwords
    cleaned_text = []
    for word in nltk.word_tokenize(extractedText):
        if word not in punct:
            if word not in stop_words and word.isalpha():
                cleaned_text.append(word)


    cleanedTextAsString = " ".join(cleaned_text)

    skillsFound = []
    for language in df['Skills']:

        if (language + " " in cleanedTextAsString or language + "\n" in cleanedTextAsString):
            skillsFound.append(language)
    skillsFound = list(set(skillsFound))

    skillsNotFound = []
    pointsAchieved = 0

    primarySkillFound = False
    secondarySkillFound = False

    for i in skillsFound:
        if not primarySkillFound:
            if primarySkill.lower() in i.lower():
                pointsAchieved += 50
                primarySkillFound = True
        if not secondarySkillFound:
            if secondarySkill.lower() in i.lower():
                pointsAchieved += 25
                secondarySkillFound = True


    if not primarySkillFound:
        skillsNotFound.append(primarySkill)

    if not secondarySkillFound:
        skillsNotFound.append(secondarySkill)

    numberOfSkills = 0
    if primarySkillFound:
        numberOfSkills -= 1
    if secondarySkillFound:
        numberOfSkills -= 1
    numberOfSkills += len(skillsFound)
    numberOfSkills = 5 if numberOfSkills > 5 else numberOfSkills
    additionalPoints = 5 * numberOfSkills

    pointsAchieved += additionalPoints
    pointsLost = 100 - pointsAchieved

    matchPercent = pointsAchieved
    matchPercent = round(matchPercent, 2)

    monthsToNum = {"jan": 1 , "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12, "sept": 9,
              "january": 1 , "february": 2, "march": 3, "april": 4, "may": 5, "june": 6, "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12}

    monthNames = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    yearNames = [*range(2000, 2022, 1)]
    experienceRange = []
    months = []
    years = []
    experienceText = findSubtextForExperienceSearch(extractedText.lower())

    lastMonth = False
    lastYear = False

    for i in experienceText.split("\n"):
        if "present" in i or "current" in i or "ongoing" in i.lower():
            lastMonth = datetime.now().month
            lastYear = datetime.now().year
        for j in monthNames:
            if j in i and "-" in i:

                try:
                    if "Present" in i.split("-")[1]:
                        experienceRange.append(i.split("-")[0])
                        #experienceRange.append(i.split("-")[1])
                        break
                    else:
                        firstPart = i.split("-")[0].isalpha() == False
                        secondPart = i.split("-")[1].isalpha() == False
                        if firstPart and secondPart:
                            experienceRange.append(i.split("-")[0])
                            experienceRange.append(i.split("-")[1])
                        break
                except:
                    pass
            elif j in i and "—" in i and i.split("—")[0].isalpha() == False and i.split("—")[1].isalpha() == False:

                try:
                    if "Present" in i.split("—")[1]:
                        experienceRange.append(i.split("—")[0])
                        #experienceRange.append(i.split("—")[1])
                        break
                    else:
                        firstPart = i.split("—")[0].isalpha() == False
                        secondPart = i.split("—")[1].isalpha() == False
                        if firstPart and secondPart:
                            experienceRange.append(i.split("—")[0])
                            experienceRange.append(i.split("—")[1])
                        break
                except:
                    pass
            elif j in i and "to" in i and i.split("to")[0].isalpha() == False and i.split("to")[1].isalpha() == False:

                try:
                    if "Present" in i.split("to")[1]:
                        experienceRange.append(i.split("to")[0])
                        #experienceRange.append(i.split("to")[1])
                        break
                    else:
                        firstPart = i.split("to")[0].isalpha() == False
                        secondPart = i.split("to")[1].isalpha() == False
                        if firstPart and secondPart:
                            experienceRange.append(i.split("to")[0])
                            experienceRange.append(i.split("to")[1])
                        break
                except:
                    pass
    try:

        experienceRange = cleanExperienceRange(experienceRange, monthNames, yearNames)

        lastExperienceMonthYear = experienceRange[1]
        firstExperienceMonthYear = experienceRange[-2]


        if lastMonth and lastYear:
            pass
        else:
            lastMonth = monthsToNum[lastExperienceMonthYear.split(" ")[0]]
            lastYear = lastExperienceMonthYear.split(" ")[1]

        firstMonth = monthsToNum[firstExperienceMonthYear.split(" ")[0]]
        firstYear = int(firstExperienceMonthYear.split(" ")[1])

        experienceInYears = (((int(lastYear) - int(firstYear)) * 12) + abs(int(lastMonth) - int(firstMonth)))/12
    except:
        experienceInYears = "Could not be screened, try with a different format."

    return matchPercent, skillsFound, skillsNotFound, experienceInYears, pointsAchieved, pointsLost

def findSubtextForExperienceSearch(extractedText):

    extractedText = extractedText.lower()
    extractedText = extractedText.replace(" ", "")

    try:
        if extractedText.find("education\n") > 0:
            educationIndex = extractedText.find("education\n")

        elif extractedText.find("academics\n") > 0:
            educationIndex = extractedText.find("academics\n")

        elif extractedText.find("educational qualification\n") > 0:
            educationIndex = extractedText.find("educational qualification\n")

        elif extractedText.find("qualifications\n") > 0:
            educationIndex = extractedText.find(" qualifications\n")

        if extractedText.find("experience\n") > 0:
            experienceIndex = extractedText.find("experience\n")

        elif extractedText.find("work experience\n") > 0:
            experienceIndex = extractedText.find("work experience\n")



        if educationIndex > experienceIndex:
            experienceText = extractedText[experienceIndex: educationIndex]
        else:
            experienceText = extractedText[experienceIndex:]

        return experienceText
    except:
        return extractedText

def cleanExperienceRange(experienceRange, monthNames, yearNames):
    cleanedExperienceRange = []

    for i in range(0, len(experienceRange)):
        cleanedExperience = ""

        if "present" in experienceRange[i] or "current" in experienceRange[i]:
            cleanedExperienceRange.append("present")
            break
        hasMonth = False
        for j in monthNames:
            if j in experienceRange[i]:

                cleanedExperience += j
                hasMonth = True
        hasYear = False
        for k in yearNames:
            if str(k) in experienceRange[i]:

                cleanedExperience += " " + str(k)
                hasYear = True

        if hasMonth and hasYear:
            cleanedExperienceRange.append(cleanedExperience)

    return cleanedExperienceRange
