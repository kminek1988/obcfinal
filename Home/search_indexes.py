from Accounts.models import Profil
from haystack import indexes


class ProfilIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True, template_name='search/indexes/home/profil_text.txt')

    def get_model(self):
        return Profil

    def index_queryset(self, using=None):
        return self.get_model().objects.all()