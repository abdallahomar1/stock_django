from django.contrib import admin
from .models import prodect, orders5, mooward
from django.urls import reverse
from django.shortcuts import redirect

# Register your models here.
admin.site.site_header = 'الترهوني للسيراميك والبرسلين والادوات الصحية '
admin.site.site_title = 'الترهوني '
class prodectAdmin(admin.ModelAdmin):
    list_display = ('name','cwan','brice', 'buybrice')
    search_fields = ('name', 'brice')
    list_filter = ('kind2', 'kind')
    # def response_add(self, request, obj, post_url_continue=None):
    #     #اضف المسار الذي تريد توجية  بعد الحفظ
    #     return redirect('home:fatora')
    # def response_change(self, request, obj):
    #     #اضف المسار الذي تريد توجية  بعد الحفظ
    #     return redirect('/')
    def view_on_site(self, obj):
        url = reverse('home:all_orders')
        return url
    # list_filter = ('kind')
class orderadmin(admin.ModelAdmin):
    raw_id_fields = ('prodects','prodects_2', 'prodects3','prodects_4','prodect_5','prodects_6')
    def response_add(self, request, obj, post_url_continue=None):
        #اضف المسار الذي تريد توجية  بعد الحفظ
        return redirect(reverse('fatora', args=[str(obj.id)]))
    def response_change(self, request, obj):
        #اضف المسار الذي تريد توجية  بعد الحفظ
        return redirect(reverse('home:fatora', args=[str(obj.id)]))
admin.site.register(prodect, prodectAdmin)
admin.site.register(orders5, orderadmin)
admin.site.register(mooward)

# class PaymentAdmin(VersionAdmin, admin.ModelAdmin): 
#     def response_add(self, request, obj, post_url_continue=None): return redirect('/admin/sales/invoice')
#     def response_change(self, request, obj): return redirect('/admin/sales/invoice')