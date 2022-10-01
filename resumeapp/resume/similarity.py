from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

def findCosineSimilarity(jobDescriptionText, resumeText):
    doc1 = jobDescriptionText
    doc2 = resumeText

    data = [doc1, doc2]
    count_vectorizer = CountVectorizer()
    vector_matrix = count_vectorizer.fit_transform(data)
    print(vector_matrix)
    
    tokens = count_vectorizer.get_feature_names()
    tokens
    
    vector_matrix.toarray()
    
    create_dataframe(vector_matrix.toarray(),tokens)
    
    cosine_similarity_matrix = cosine_similarity(vector_matrix)
    create_dataframe(cosine_similarity_matrix,['doc_1','doc_2'])
    
    return cosine_similarity_matrix[1,0]

def create_dataframe(matrix, tokens):

    doc_names = [f'doc{i+1}' for i, _ in enumerate(matrix)]
    df = pd.DataFrame(data=matrix, index=doc_names, columns=tokens)
    print(df)
    return