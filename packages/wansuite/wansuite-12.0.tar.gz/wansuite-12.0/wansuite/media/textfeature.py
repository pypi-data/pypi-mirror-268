from gensim.models import Word2Vec
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from top2vec import Top2Vec
from sklearn.feature_extraction.text import TfidfVectorizer
def Word2Vector(wordlist,vectorsize=5,windowsize=2,ignore_freq=1,method="cbow"):
    '''

    :param textlist: list of wordlist
    :param vectorsize:
    :param windowsize:
    :param ignore_freq:
    :param method: "cbow" or "skip-gram"
    :return:
    '''
    if method=="cbow":
        kk=0
    elif method=="skip-gram":
        kk=1
    return Word2Vec(wordlist, vector_size=vectorsize, window=windowsize, min_count=ignore_freq, sg=kk)


def Doc2Vector(wordlist,vectorsize=20,windowsize=2,ignore_freq=1,docvector_only=True,workers=4,epochs=100):
    '''

    :param wordlist:
    :param vectorsize:
    :param windowsize:
    :param ignore_freq:
    :param docvector_only:  – If set to False trains word-vectors (in skip-gram fashion) simultaneous with DBOW doc-vector training; If True, only trains doc-vectors (faster).
    :param workers:
    :param epochs:
    :return:
    '''
    if docvector_only==True:
        kk=0
    else:
        kk=1
    tagged_data = [TaggedDocument(words=doc, tags=[i]) for i, doc in enumerate(wordlist)]
    model = Doc2Vec(vector_size=vectorsize, window=windowsize, min_count=ignore_freq, dbow_words=kk, workers=workers, epochs=epochs)
    # Build the vocabulary
    model.build_vocab(tagged_data)

    # Train the model
    model.train(tagged_data, total_examples=model.corpus_count, epochs=model.epochs)
    doc_embeddings = [model.infer_vector(doc) for doc in wordlist]
    return model,tagged_data,doc_embeddings


def Topic2Vector(textlist,  doc2vec_model='universal-sentence-encoder',ignore_freq=1,speed="slow",workers=4):
    '''

    :param textlist: doc2vec,  universal-sentence-encoder ,universal-sentence-encoder-large, universal-sentence-encoder-multilingual,universal-sentence-encoder-multilingual-large, distiluse-base-multilingual-cased,all-MiniLM-L6-v2, paraphrase-multilingual-MiniLM-L12-v2
    :param doc2vec_model:
    :param ignore_freq:
    :param speed:
    :param workers:
    :return:
    '''
    if speed=="slow":
        speed="learn"
    model = Top2Vec(documents=textlist, embedding_model=doc2vec_model, min_count=ignore_freq, speed=speed,workers=workers)
    return model

def TF_IDF(sentence):
    vectorizer = TfidfVectorizer()
    return vectorizer.fit_transform(sentence).toarray()


