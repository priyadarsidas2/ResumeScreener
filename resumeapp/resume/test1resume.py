import pandas as pd
from scoringAndExperience import scoringAndExperienceCheck
from readpdf import extractTextFromPDF
import warnings
warnings.filterwarnings("ignore")


#single i
i = 6

#find the skills and experience
df = pd.read_excel("JDv3.xlsx")

jobProfile = df["Title"][i]
jobDescription = df["Description"][i]
filename = df["Resume"][i] + ".pdf"
extractedText = extractTextFromPDF(filename)
(relevantSkills,skillsMatched, skillsNotFound, pointsFromProfile, primarySkillsInRelevantSkills,
            secondarySkillsInRelevantSkills, pointsFromPrimarySkills, 
            pointsFromSecondarySkills, matchPercent) = scoringAndExperienceCheck(jobProfile, extractedText, jobDescription)

"""
#multiple i
df = pd.read_excel("JDv5.xlsx")

relevantSkillsList = []
skillsMatchedList = []
skillsNotFoundList = []
pointsFromProfileList = []
primarySkillsInRelevantSkillsList = []
secondarySkillsInRelevantSkillsList = []
pointsFromPrimarySkillsList = []
pointsFromSecondarySkillsList = []
matchPercentList = []


for i in range(0,20):
    #find the skills and experience
    jobProfile = df["Title"][i]
    jobDescription = df["Description"][i]
    filename = df["Resume"][i] + ".pdf"
    extractedText = extractTextFromPDF(filename)
    (relevantSkills, skillsMatched, skillsNotFound, pointsFromProfile, primarySkillsInRelevantSkills,
                secondarySkillsInRelevantSkills, pointsFromPrimarySkills,
                pointsFromSecondarySkills, matchPercent) = scoringAndExperienceCheck(jobProfile, extractedText, jobDescription)
    
    relevantSkillsList.append(relevantSkills)
    skillsMatchedList.append(skillsMatched)
    skillsNotFoundList.append(skillsNotFound)
    pointsFromProfileList.append(pointsFromProfile)
    primarySkillsInRelevantSkillsList.append(primarySkillsInRelevantSkills)
    secondarySkillsInRelevantSkillsList.append(secondarySkillsInRelevantSkills)
    pointsFromPrimarySkillsList.append(pointsFromPrimarySkills)
    pointsFromSecondarySkillsList.append(pointsFromSecondarySkills)
    matchPercentList.append(matchPercent)

resumeList = df["Resume"]
titleList = df["Title"]
descriptionList = df["Description"]

scoring = pd.DataFrame(zip(resumeList, titleList, descriptionList, relevantSkillsList, skillsMatchedList,
                           skillsNotFoundList, pointsFromProfileList, primarySkillsInRelevantSkillsList,
                           secondarySkillsInRelevantSkillsList, pointsFromPrimarySkillsList,
                           pointsFromSecondarySkillsList, matchPercentList),
                       columns=["Resume", "Title", "Description", "Relevant Skills",
                                "Skills Matched", "Skills Not Found", "Points From Profile", "Primary Skills", 
                                "Secondary Skills", "Primary Skills Points", "Secondary Skills Points", "Match Percent"])

scoring.to_excel("Final Scoring.xlsx")
"""