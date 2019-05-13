from django.db import models


  

class Location(models.Model):

  name = models.CharField(max_length = 30)

  def save_location(self):

    self.save()

  def delete(self):

    self.delete()

  def update(self,field,val):
    Location.objects.filter(id = self.id).update(field = val)

  def __str__(self):
      return self.name


class Category(models.Model):

  name = models.CharField(max_length = 30)
  def save_category(self):

      self.save()

  def delete(self):

      Category.objects.get(id = self.id).delete()
  def update(self,field,val):

      Category.objects.get(id = self.id).update(field = val)

  def __str__(self):
      return self.name

class Image(models.Model):
  
    photo_image = models.ImageField(upload_to = "images/")
    name = models.CharField(max_length = 30)
    description = models.TextField()
    location = models.ForeignKey('Location',on_delete=models.deletion.CASCADE,)
    category = models.ForeignKey('Category',on_delete=models.deletion.CASCADE,)

    def save_image(self):
        """
        This is the function that we will use to save the instance of this class
        """
        self.save()

    def delete_image(self):
        """
        This is the function that we will use to delete the instance of this class
        """
        Image.objects.get(id = self.id).delete()

    def update_image(self,val):
        """
        Thisnews/models.py is the method to update the instance
        """
        Image.objects.filter(id = self.id).update(name = val)

    @classmethod
    def get_image_by_id(cls,image_id):
        """
        This is the method to get a specific image
        """
        return cls.objects.get(id = image_id)

    @classmethod
    def get_images(cls):
        return cls.objects.all()

    @classmethod
    def search_by_category(cls,search_term):
        image = cls.objects.filter(category__name__icontains=search_term)
        return image
        
        
    @classmethod
    def filter_by_location(cls,location):
        """
        This is the method to get images taken in a certain location
        """
        the_location = Location.objects.get(name = location)
        return cls.objects.filter(location_id = the_location.id)

    def __str__(self):
        return self.name
