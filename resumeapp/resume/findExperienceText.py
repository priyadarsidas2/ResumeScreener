def findSubtextForExperienceSearch(extractedText):

    extractedText = extractedText.lower()

    educationKeywords = ["education\n", "academics\n", "educational qualification\n", "qualifications\n", "qualification\n",
                        "e d u c a t i o n\n", "a c a d e m i c s\n", "e d u c a t i o n a l  q u a l i f i c a t i o n\n", 
                        "q u a l i f i c a t i o n s\n", "q u a l i f i c a t i o n\n"]
    experienceKeywords = ["experience\n", "work experience\n", "employment history\n",
                         "e x p e r i e n c e\n", "w o r k  e x p e r i e n c e\n", "e m p l o y m e n t  h i s t o r y\n"]
    
    skillsKeywords = ["skills\n", "software exposure", "skill\n", "softwares\n", "technical skills\n", "software skills\n",
                     "s k i l l s\n", "s o f t w a r e  e x p o s u r e", "s k i l l\n", "s o f t w a r e s\n", "t e c h n i c a l  s k i l l s\n",
                      "s o f t w a r e  s k i l l s\n"]
    certificationsKeywords = ["certifications\n", "certification\n", "c e r t i f i c a t i o n s\n", "c e r t i f i c a t i o n\n"]
    contactKeywords = ["contact\n", "contact details\n", "connect\n", "info\n",
                      "c o n t a c t\n", "c o n t a c t  d e t a i l s\n", "c o n n e c t\n", "i n f o\n"]
    internshipKeywords = ["internships\n", "internship\n", "i n t e r n s h i p s\n", "i n t e r n s h i p\n"]
    achievementKeywords = ["awards and achievements\n", "achievements\n", "a w a r d s  a n d  a c h i e v e m e n t s\n", "a c h i e v e m e n t s\n"]

    educationIndex, experienceIndex, skillsIndex, certificationIndex, contactIndex, internshipIndex, achievementIndex = float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), float("inf")

    for i in educationKeywords:
        if extractedText.find(i) > 0 and extractedText.find(i) < educationIndex:
            educationIndex = extractedText.find(i)
            
    for i in experienceKeywords:
        print(i, extractedText.find(i))
        print()
        if extractedText.find(i) > 0 and extractedText.find(i) < experienceIndex:
            #print(experienceIndex)
            experienceIndex = extractedText.find(i)
        
    for i in skillsKeywords:
        if extractedText.find(i) > 0 and extractedText.find(i) < skillsIndex:
            skillsIndex = extractedText.find(i)
        
    for i in certificationsKeywords:
        if extractedText.find(i) > 0 and extractedText.find(i) < certificationIndex:
            certificationIndex = extractedText.find(i)
    
    for i in contactKeywords:
        if extractedText.find(i) > 0 and extractedText.find(i) < contactIndex:
            contactIndex = extractedText.find(i)
            
        
    for i in internshipKeywords:
        if extractedText.find(i) > 0 and extractedText.find(i) < internshipIndex:
            internshipIndex = extractedText.find(i)
            
        
    for i in achievementKeywords:
        if extractedText.find(i) > 0 and extractedText.find(i) < achievementIndex:
            achievementIndex = extractedText.find(i)
            
    
    #print("educationIndex", educationIndex, "experienceIndex", experienceIndex,
    #         "skillsIndex", skillsIndex, "certificationIndex", certificationIndex, "contactIndex", contactIndex,
    #         "internshipIndex", internshipIndex, "achievementIndex", achievementIndex)
    indexReference = {educationIndex: "education", experienceIndex: "experience", skillsIndex: "skills", certificationIndex: "certification", 
                      contactIndex: "contact", internshipIndex: "internship", achievementIndex: "achievement"}
    indexList = [educationIndex, experienceIndex, skillsIndex, certificationIndex, contactIndex, internshipIndex, achievementIndex]
    indexList = [i for i in indexList if i != float("inf")]
    indexList.sort()
    print("indexList", indexList)
    print("indexReference", indexReference)
    resumeContentAsJson = {}
    
    try:
        for i in range(0, len(indexList)-1):
            if indexList[i] != float("inf"):
                keyword = indexReference[indexList[i]]
                resumeContentAsJson[keyword] = extractedText[indexList[i]:indexList[i+1]]
        keyword = indexReference[indexList[-1]]
        resumeContentAsJson[keyword] = extractedText[indexList[-1]:-1]

        return resumeContentAsJson["experience"]
    
    except:
        return extractedText
