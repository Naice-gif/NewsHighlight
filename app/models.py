class Source:
    '''
    Source class to define source Objects
    '''

    def __init__(self,id,name,description,url,category,language,country):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country



# class Review:

#     all_reviews = []

#     def __init__(self,source_id,name,sourceurl,review):
#         self.source_id = source_id
#         self. name = name
#         self.souceurl = sourceurl
#         self.review = review


#     def save_review(self):
#         Review.all_reviews.append(self)


#     @classmethod
#     def clear_reviews(cls):
#         Review.all_reviews.clear()

#     @classmethod
#     def get_reviews(cls,id):

#         response = []

#         for review in cls.all_reviews:
#             if review.source_id == id:
#                 response.append(review)

#         return response