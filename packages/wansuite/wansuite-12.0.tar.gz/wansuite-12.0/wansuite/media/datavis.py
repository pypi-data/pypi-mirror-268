from wordcloud import WordCloud
import pyLDAvis
from pyLDAvis import gensim_models
import plotly.express as px

def LDA_graph(model,work_frequency,dictionary, notebook_enable=True):
    if notebook_enable==True:
        pyLDAvis.enable_notebook()
    return gensim_models.prepare(model,words_frequency,dictionary=dictionary)

def word_cloud(wordlist,width=1000, height=500, scheme="plotly_dark",margin=0, collocations=False):
    if wordlist[0][1]=="#":
        wc = " "
        for x in wordlist:
            wc = wc + x[1:] + " "
    else:
        wc = " "
        for x in wordlist:
            wc = wc + x[0:] + " "
    cloud=WordCloud(background_color="white", width=width, height=height, margin=margin, collocations=collocations).generate(wc)
    fig = px.imshow(cloud)
    fig.update_layout(
        title='',
        width=width,
        height=height, template=scheme
    )

    fig.show()
