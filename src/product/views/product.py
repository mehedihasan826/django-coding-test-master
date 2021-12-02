from django.views import generic

from product.models import Variant, Product, ProductVariantPrice, ProductVariant


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


class ProductListView(generic.ListView):
    paginate_by = 5
    model = Product
    context_object_name = 'product_list'

    template_name = 'products/list.html'

    def get_queryset(self):
        products = []
        queryset = Product.objects.all()
        for item in queryset:
            pvp = ProductVariantPrice.objects.filter(product_id=item.pk)
            item.variations = pvp
            products.append(item)
        return products


class VariantView(generic.ListView):
    model = Variant
    context_object_name = 'variant_list'
    queryset = Variant.objects.all()
    template_name = 'products/list.html'


