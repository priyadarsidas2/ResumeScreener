def classifyJobProfile(cleanedTextAsString):
    
    titles = {
        "Java/J2EE Full Stack Developer": "Java Developer", "Full stack Java Developer": "Java Developer",
        "Java Developer": "Java Developer",  "Sr. Java Developer": "Java Developer", "Java Programmer": "Java Developer",
        
        "Software Quality Assurance": "Testing",
        "Tester": "Testing", "ETL Tester": "Testing",
        "Backend SQL Tester": "Testing", "QA Engineer": "Testing",
        "QA Automation Engineer": "Testing", "QA Selenium Engineer": "Testing",
        "Software Test Specialist": "Testing", "Sr. QA Test Data Manager": "Testing",
        "Sr. Quality Assurance Analyst": "Testing", 
        
        "ETL Architect": "ETL Developer",
        "Senior ETL Lead Developer": "ETL Developer", "ETL Architect": "ETL Developer",
        "Sr. ETL Developer": "ETL Developer", "ETL Lead Developer": "ETL Developer",
        "ETL Lead": "ETL Developer", 
        
        "SQL Developer": "SQL Developer", "Data Engineer":"SQL Developer",
        "SQL Report Analyst": "SQL Developer", "Data Warehouse Developer": "SQL Developer",
        
        "Sr. Python Developer": "Python Developer", "Python Developer": "Python Developer"
    }
    
    frequencyOfTitles = {"Java Developer": 0, "Testing": 0, "ETL Developer": 0,
                         "SQL Developer": 0, "Python Developer":0}
    
    for title in titles:
        countOfOccurances = cleanedTextAsString.count(title.lower())
        thisTitle = titles[title]
        frequencyOfTitles[thisTitle] += countOfOccurances
        #print(title)
        #if title in cleanedTextAsString:
        #    thisTitle = titles[title]
        #    frequencyOfTitles[thisTitle] += 1
    print(frequencyOfTitles)
    keymax = max(frequencyOfTitles, key = lambda x: frequencyOfTitles[x])
    return keymax.lower()
