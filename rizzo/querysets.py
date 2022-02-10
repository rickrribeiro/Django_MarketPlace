from django.db.models import QuerySet
import operator
from .helpers import truncate


class CategoryQuerySet(QuerySet):
    def specific_category(self, id): 
        category = self.filter(id=id)
        
        return category
    
    def get_by_name(self, name): 
        category = self.filter(name=name)
        
        return category
    
    def spotlight(self, bool): 
        categories = self.filter(spotlight=bool)
        return categories

class UserQuerySet(QuerySet):

    def specific_category(self, id): 
        users = self.filter(category=id)
        return users

    def famous(self, bool): 
        users = self.filter(is_famous=bool)
        return users

    def filterByName(self, name): 
        
        users = self.filter(name__contains=name)
        return users

    def spotlight(self, bool):
        users = self.filter(spotlight=bool)
        return users

    def total_by_category(self, category_id):
        total = self.filter(category=category_id).count()
        return total

class SaleQuerySet(QuerySet):

    def top_donators(self):
        users = {}
        for sale in self:
            if sale.service.famous.to_ngo == True and sale.done == True:
                if sale.service.famous.username not in users:
                    users[sale.service.famous.username] = sale.service.famous
                    users[sale.service.famous.username].total_donate = int(sale.service.price*(sale.service.famous.ngo_percentage/100))
                    users[sale.service.famous.username].services_count = 1
                    users[sale.service.famous.username].rating = sale.rating
                else:    
                    users[sale.service.famous.username].total_donate += int(sale.service.price*(sale.service.famous.ngo_percentage/100))
                    users[sale.service.famous.username].services_count += 1 
                    users[sale.service.famous.username].rating += sale.rating
        users = dict(sorted(users.items(), key=lambda x: x[1].total_donate, reverse=True))
        
        return users

    def getUserSalesStatistics(self, user):
        user.total_donate = 0
        user.rating = 0
        user.services_count = 0
        for sale in self:
            if sale.service.famous == user and sale.done == True:
                user.total_donate += int(sale.service.price*(sale.service.famous.ngo_percentage/100))
                user.services_count += 1 
                user.rating += sale.rating
        if user.services_count != 0:        
            user.rating = truncate(user.rating/user.services_count,1)
        
        return user

    def getFamousProfileVideos(self,famous_id):
        videos = []
        for sale in self:
            if sale.service.famous.id == famous_id and sale.done == True and sale.toProfile == True and sale.video is not None:
                videos.append(sale.video)
        if(len(videos)>0):
            return videos
        else:
            return None
        
class ServiceQuerySet(QuerySet):

    def smallest_price(self, famous):
       
        self = self.filter(famous=famous)
        
        price = 0
        for p in self:
            if price == 0:
                price = p.price
            elif p.price < price:
                price = p.price

        return price


    def getServiceByFamous(self, famous):
        self = self.filter(famous= famous)
        return self
