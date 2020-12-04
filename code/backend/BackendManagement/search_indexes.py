from haystack import indexes
from BackendManagement.models import Product

class ProductIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True)
    id = indexes.CharField(model_attr='id')
    name = indexes.CharField(model_attr='name')
    price = indexes.FloatField(model_attr='price')
    pics = indexes.CharField(model_attr='pics')

    autocomplete = indexes.EdgeNgramField()

    @staticmethod
    def prepare_autocomplete(obj):
        return ' '.join((obj.name, obj.price))
    
    def get_model(self):
        return Product