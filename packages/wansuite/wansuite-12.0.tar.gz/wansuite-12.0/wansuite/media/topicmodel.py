from gensim import models
from gensim.models.coherencemodel import CoherenceModel
def LDA_Model(words_frequency,dictionary,num_topics=50, alpha=0.5, beta=0.5,passes=20,random_state = 100):
    return models.ldamodel.LdaModel(words_frequency, num_topics=num_topics, id2word =dictionary,passes=passes,alpha=alpha,eta=beta,random_state = random_state)

def coherence_measure_lda(model,words_frequency,coherence='u_mass'):
    return CoherenceModel(model=model, corpus=words_frequency, coherence=coherence)

