from django.db import models

class Image(models.Model):
    image_url = models.ImageField(upload_to ="images/")
    name = models.CharField(max_length =30)
    description = models.CharField
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    def save_image(self):

      self.save()

    def delete_image(self):

      Image.objects.get(id =self.id).delete()

    def update_image(self,val):

      Image.objects.filter(id = self.id).update(name = val)

    @classmethod
    def get_image_by_id(cls,image_id):

      return class.objects.get(id = image_id) 

    @classmethod
    def get_images(cls):
        return cls.objects.all() 

    @classmethod
    def search_image(cls,category):
      try:
        searched_category = Category.objects.filter(name_icontains = category)[0]
        return cls.object.filter(category_id =searched_category.id)

      except Exeption:
        return "No images found"

    @classmethod
    def filter_by_location(cls,location):
        the_location = Loction.objects.get(name = location):
        return cla.objects.fiter(location_id = the_location.id)

    def __str__(self):
        return self.name 

  

class Location(models.Model):

  name = models.CharField(max_length = 30)

  def save_location(self):

    self.save()

  def delete(self):

    self.delete()

  def update(self,field,val):
    Location.objects.get(id = self.id).update(field = val)

  def __str__(self):
      return self.name


class Category