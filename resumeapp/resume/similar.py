def addSimilarKeywords(skillsFound):
    keywords = {"MySQL": ["SQL"], "Oracle SQL": ["SQL"],
                "PostgreSQL": ["SQL"], "Angular JS": ["Angular", "AngularJS"],
                "Angular": ["Angular JS", "AngularJS"], "AngularJS": ["Angular", "Angular JS"],
                "React JS": ["React", "ReactJS"],
                "React": ["React JS", "ReactJS"], "ReactJS": ["React", "React JS"],
                "Node JS": ["Node", "NodeJS", "Node.JS"],"Node": ["Node JS", "NodeJS", "Node.JS"],
                "NodeJS": ["Node", "Node JS", "Node.JS"], "Data Science": ["Machine Learning"],
                "Machine Learning": ["Data Science"], "Scikit-learn": ["Scikit learn"],
                "Artificial Intelligence": ["Machine Learning", "Data Science"],
                "AWS": ["EC2", "Lambda"], "EC2": ["AWS"], "Lambda": ["AWS"],
                "Linux": ["Unix"], "Unix": ["Linux"],
                "HTML5": ["HTML"], "HTML": ["HTML5"],
                "Javascript": ["JavaScript"], "JavaScript": ["Javascript"] 
                }
    newSkillsFound = skillsFound
    for i in keywords:
        for j in skillsFound:
            if i == j:
                newSkillsFound.extend(keywords[i])
    
    return list(set(newSkillsFound))