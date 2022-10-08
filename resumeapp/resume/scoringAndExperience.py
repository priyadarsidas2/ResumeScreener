import pandas as pd
from resumeapp.resume.cleanText import cleanTextUsingNLP
from resumeapp.resume.similar import addSimilarKeywords
from resumeapp.resume.classify import classifyJobProfile
import warnings
warnings.filterwarnings("ignore")

def scoringAndExperienceCheck(jobProfile, extractedText, jobDescription):
    df = pd.read_excel("SkillsList.xlsx")
    
    #skills in resume
    cleanedTextAsString = cleanTextUsingNLP(extractedText)
    cleanedTextAsString = cleanedTextAsString.lower()
    
    print(cleanedTextAsString)
    skillsFound = []
    for language in df['Skills']:
        if (language.lower() + " " in cleanedTextAsString or language.lower() + "\n" in cleanedTextAsString or 
            language.lower() + "," in cleanedTextAsString or language.lower() + "/" in cleanedTextAsString):
            skillsFound.append(language.lower())
            
    print("skillsFound before adding similar keywords", skillsFound)
    skillsFound = list(set(skillsFound))
    skillsFound = addSimilarKeywords(skillsFound)
    
    #finding the job profile from resume text
    profile = classifyJobProfile(cleanedTextAsString)
    
    
    #finding the skills from job description
    cleanedJD = cleanTextUsingNLP(jobDescription)
    cleanedJD = cleanedJD.lower()
    relevantSkills = []
    for language in df['Skills']:
        
        if (language.lower() + " " in cleanedJD or language.lower() + "\n" in cleanedJD or 
            language.lower() + "," in cleanedJD or language.lower() + "/" in cleanedJD):
            relevantSkills.append(language.lower())

    relevantSkills = list(set(relevantSkills))
    
    #matching skills in resume to relevant skills in job description
    skillsMatched = []

    for skill in relevantSkills:
        if skill in skillsFound:
            skillsMatched.append(skill)

    skillsMatched = list(set(skillsMatched))
            
    print("relevantSkills", relevantSkills)
    print("skillsMatched", skillsMatched)
    
    skillsNotFound = [i for i in relevantSkills if i not in skillsMatched]
    
    primarySkillList = ["python", "java", "sql", "aws", "spring", "springboot"]
    primarySkillsInRelevantSkills = [i for i in relevantSkills if i in primarySkillList]
    secondarySkillsInRelevantSkills = [i for i in relevantSkills if i not in primarySkillList]
    
    numberOfPrimarySkills = len(primarySkillsInRelevantSkills)
    numberOfSecondarySkills = len(secondarySkillsInRelevantSkills)
    
    try:
        pointsPerPrimarySkill = 60 / numberOfPrimarySkills
    except:
        pointsPerPrimarySkill = 0
    try:
        pointsPerSecondarySkill = 20 / numberOfSecondarySkills
    except:
        pointsPerSecondarySkill = 0
        
    primarySkillsFoundInResume = [i for i in skillsMatched if i in primarySkillsInRelevantSkills]
    secondarySkillsFoundInResume = [i for i in skillsMatched if i in secondarySkillsInRelevantSkills]
    
    pointsFromPrimarySkills = len(primarySkillsFoundInResume) * pointsPerPrimarySkill
    pointsFromSecondarySkills = len(secondarySkillsFoundInResume) * pointsPerSecondarySkill
    
    pointsFromProfile = 0
    jobProfile = jobProfile.lower()
    
    for word in jobProfile.split(" "):
        if word in profile.split(" "):
            print(word)
            pointsFromProfile = 20
    
    matchPercent = pointsFromProfile + pointsFromPrimarySkills + pointsFromSecondarySkills
    
    matchPercent = round(matchPercent, 2)

    #cleaning skillsFound
    skillsFound = cleanTextUsingNLP(" ".join(skillsFound))
    skillsFound = skillsFound.split(" ")
    skillsFound = list(set(skillsFound))
    skillsFound = sorted(skillsFound)
    
    #printing outputs
    print("skillsFound", skillsMatched)
    print("skillsNotFound", skillsNotFound)
    print("pointsFromProfile", pointsFromProfile)
    print("primarySkillsInRelevantSkills", primarySkillsInRelevantSkills)
    print("secondarySkillsInRelevantSkills", secondarySkillsInRelevantSkills)
    print("pointsFromPrimarySkills", pointsFromPrimarySkills)
    print("pointsFromSecondarySkills", pointsFromSecondarySkills)
    print("matchPercent", matchPercent)
    return (relevantSkills,skillsMatched, skillsNotFound, pointsFromProfile, primarySkillsInRelevantSkills,
            secondarySkillsInRelevantSkills, pointsFromPrimarySkills, pointsFromSecondarySkills, matchPercent)