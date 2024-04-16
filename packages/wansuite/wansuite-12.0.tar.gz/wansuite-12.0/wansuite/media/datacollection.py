import numpy as np
import pandas as pd

def getlink(shareurl):
  return 'https://docs.google.com/uc?export=download&id='+shareurl.split('/')[-2]

def econnews():
  url = getlink("https://drive.google.com/file/d/1nfuhwK_hjqPsfbp7ybXgZOUWZkgPqyDe/view?usp=drive_link")
  return  pd.read_csv(url, index_col=0).drop_duplicates()


def stocknews():
  url = getlink("https://drive.google.com/file/d/1WZyAEmqSf0Lskx4_-qJq3rz4PEdGkQVA/view?usp=drive_link")
  return  pd.read_csv(url, index_col=0).drop_duplicates()

def yelprating():
  url = getlink("https://drive.google.com/file/d/1KR4rA1AlteQv1QEKHbWkdKhTRHcrr6oD/view?usp=drive_link")
  return  pd.read_csv(url, index_col=0).drop_duplicates()

def twitter():
  url = getlink("://drive.google.com/file/d/1frox8TLvzsK94rSu43dBVrwpvu8JL9Si/view?usp=sharing")
  return  pd.read_csv(url, index_col=0).drop_duplicates()

def eurusd():
  url = getlink("https://drive.google.com/file/d/1YJTJyklVqWKbHLVCUez-VMm3msOq-Dse/view?usp=share_link")
  return  pd.read_csv(url, index_col=0).drop_duplicates()

def forex():
  url = 'https://drive.google.com/uc?id=1Si7fsfE1rdA1xHOFF_vsA3tvFkQAYx-2'
  return  pd.read_csv(url, index_col=0).drop_duplicates()

def google():
  url = 'https://docs.google.com/uc?export=download&id=1fkteL4yNpnBsozMy0FtVRA2-r6hYkkiV'
  return  pd.read_csv(url, index_col=0).drop_duplicates()

def twitter116():
  url = 'https://docs.google.com/uc?export=download&id=1fi-Xf8obJzJ5JPwrvyMhxlKIK48SpU0F'
  return  pd.read_csv(url, index_col=0).drop_duplicates()

def keyword():
  url = 'https://docs.google.com/uc?export=download&id=1fQCoNqFzmKRDcOoYGJnwqi2deklh5FJl'
  return  pd.read_csv(url, index_col=0).drop_duplicates()

def news2023():
  url = 'https://docs.google.com/uc?export=download&id=1jHNpNJylqSScWnF9FIlS0dvoWEoqgDcp'
  return  pd.read_csv(url, index_col=0).drop_duplicates()

def inflation():
  url = getlink("https://drive.google.com/file/d/1a92uW0jmbpunugF-ZyzL2fN7fn25AU0C/view?usp=sharing")
  return  pd.read_csv(url, index_col=0).drop_duplicates()


def twitter_gpt():
  url = getlink("https://drive.google.com/file/d/1oJZiII2GiIZNpMm5jI1qKCJVZG_TyBdy/view?usp=drive_link")
  return  pd.read_csv(url, index_col=0).drop_duplicates()