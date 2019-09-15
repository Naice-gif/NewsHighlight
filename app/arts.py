class Article:
    '''
    Article class to define article Objects
    '''

    def __init__(self,id,name,title,author,description,url,urlToImage, category,publishedAt,content):
        self.id =id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.publishedAt = publishedAt