from django.contrib import admin
from Accounts.models import Profil
from Home.models import Faq, introFoto
from Lists.models import City, Category
from contact.models import Contact

class ProfilAdmin(admin.ModelAdmin):
    pass
admin.site.register(Profil, ProfilAdmin)

class FaqAdmin(admin.ModelAdmin):
    pass
admin.site.register(Faq, FaqAdmin)

class CityAdmin(admin.ModelAdmin):
    pass
admin.site.register(City, CityAdmin)
class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)

class IntroFotoAdmin(admin.ModelAdmin):
    pass
admin.site.register(introFoto, IntroFotoAdmin)