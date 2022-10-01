import pandas as pd
import numpy as np
from datetime import datetime
import re
from resumeapp.resume.cleanText import cleanTextUsingNLP
from resumeapp.resume.findExperienceText import findSubtextForExperienceSearch
from resumeapp.resume.findExperience import findDatesFromText
from resumeapp.resume.similarity import findCosineSimilarity

def scoringAndExperienceCheck(primarySkill, secondarySkill, extractedText, jobDescription):
    df = pd.read_excel("SkillsList.xlsx")

    cleanedTextAsString = cleanTextUsingNLP(extractedText)
    print(cleanedTextAsString)
    skillsFound = []
    for language in df['Skills']:
        #if language in cleaned_text:
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
        print("pointsAchieved", pointsAchieved)

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
    print("numberOfSkills", numberOfSkills)
    #additionalPoints = 25 if additionalPoints >25 else additionalPoints
    print("Additional Points", additionalPoints)
    pointsAchieved += additionalPoints
    print("Points Achieved", pointsAchieved)
    pointsLost = 100 - pointsAchieved

    matchPercent = pointsAchieved
    matchPercent = round(matchPercent, 0)

    experienceText = findSubtextForExperienceSearch(extractedText.lower())

    experienceInYears = findDatesFromText(experienceText)
    
    #finding cosine similarity
    resumeText = cleanedTextAsString
    #print("resumeText")
    #print(resumeText)
    print()
    jobDescriptionText = cleanTextUsingNLP(jobDescription)
    #print("jobDescriptionText")
    #print(jobDescriptionText)
    print()
    similarityPercent = findCosineSimilarity(jobDescriptionText, resumeText) * 100
    similarityPercent = round(similarityPercent, 0)
    
    #calculating final percent
    totalScore = round((matchPercent * .80) + (similarityPercent * 0.20), 0)
    
    #printing outputs
    print("matchPercent", matchPercent)
    print("skillsFound", skillsFound)
    print("skillsNotFound", skillsNotFound)
    print("experienceInYears", experienceInYears)
    print("pointsAchieved", pointsAchieved)
    print("pointsLost", pointsLost)
    print("similarityPercent", similarityPercent)
    print("total Percent", totalScore)
    
    
    
    return (matchPercent, skillsFound, skillsNotFound, experienceInYears, pointsAchieved, 
            pointsLost, similarityPercent, totalScore)
