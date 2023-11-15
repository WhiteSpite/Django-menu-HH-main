from django.db.models import *
from django.utils.text import slugify


class Menu(Model):
    name = CharField(max_length=40, unique=True)
    parent = ForeignKey('self', on_delete=CASCADE, null=True, blank=True, related_name='children')
    nesting_level = IntegerField(default=1)
    slug = SlugField(blank=True, null=True, unique=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if self.parent:
            self.nesting_level = self.parent.nesting_level + 1
        else:
            if Menu.objects.exists():
                self.parent = Menu.objects.first()
                self.nesting_level = 1
            else:
                self.nesting_level = 0
        super(Menu, self).save(*args, **kwargs)
        
