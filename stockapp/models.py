from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


kind_s = (
    ('فرز اول', 'فرز اول'),
    ('فرز ثاني', 'فرز ثاني'),
    ('فرز ثالث', 'فرز ثالث'),
)

kind22 = (
    ('سيراميك', 'سيراميك'),
    ('الادوات الصحية','الادوات الصحية')
)

class prodect(models.Model):
    kind2 = models.CharField(max_length=50, choices=kind22, verbose_name=("النوع"))
    name = models.CharField(max_length=50, verbose_name=("اسم المنتج"))
    cwan = models.DecimalField(max_digits=100, decimal_places=2,verbose_name=("عدد الكراتين الموجودة من المنتج"), help_text='اكتب عدد الكراتين الموجودة من هذا المنتج')
    brice = models.DecimalField(max_digits=100, decimal_places=2,verbose_name=("عدد الامتار في الكرتونة"))
    count_f = models.DecimalField(max_digits=100, decimal_places=2,verbose_name=(" عدد البلاط في الكرتونة الواحدة"), null=True)
    kind = models.CharField(max_length=50, choices=kind_s, verbose_name=("النوع"), null=True)
    buybrice = models.DecimalField(max_digits=100, decimal_places=2,verbose_name=(" سعر بيع المتر قطاعي "))
    jomlprice = models.DecimalField(max_digits=100, decimal_places=2,verbose_name=(" سعر بيع المتر لعملاء الجملة"))
    com = models.DecimalField(max_digits=100, decimal_places=2,verbose_name=("عدد الامتار الموجودة من المنتج"), null=True, blank=True)

    class Meta:
        verbose_name=_("صنف")
        verbose_name_plural = _("المخزن")


    def save(self, *args, **kwargs):
        cwn = self.cwan * self.brice
        self.com = cwn
        super(prodect, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
class mooward(models.Model):
    name = models.CharField(max_length=50, verbose_name=("اسم المورد"))
    caten = models.ForeignKey(prodect, verbose_name=("المنتج الذي اشتريته"), on_delete=models.CASCADE)
    coun = models.DecimalField(max_digits=30, decimal_places=2, verbose_name=("عدد الامتار الذي قد اشتريتها"))
    number = models.DecimalField(max_digits=90, decimal_places=2, verbose_name=("ثمن الشراء"))
    price2 = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=("سعر شراء المتر"))
    count = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=("عدد الكراتين"), blank=True, null=True)
    date_times = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, verbose_name=("وقت عملية الشراء"))
    class Meta:
        verbose_name=_("مشتري")
        verbose_name_plural = _("المشتريات")
    def __str__(self):
        return f"اسم العميل {self.name} - اسم المنتج {self.caten.name}"
    def save(self, *args, **kwargs):
        ss = self.coun / self.caten.brice
        self.count = ss
        x = self.caten.cwan + self.count
        self.caten.cwan = x
        self.caten.save()
        super().save(*args, **kwargs)

class orders5(models.Model):
    names = models.CharField(max_length=50, verbose_name=("اسم العميل"))
    prodects = models.ForeignKey(prodect,related_name='items', on_delete=models.CASCADE, verbose_name=("المنتج"))
    count = models.DecimalField(max_digits=7, decimal_places=2, verbose_name=("الامتار المطلوبة"))
    prodects_2 = models.ForeignKey(prodect,related_name='items2', on_delete=models.CASCADE, verbose_name=("المنتج"), null=True, blank=True)
    count_2 = models.DecimalField(max_digits=7, decimal_places=2,verbose_name=("الامتار المطلوبة"), null=True, default=0)
    prodects3 = models.ForeignKey(prodect,related_name='items3', on_delete=models.CASCADE, verbose_name=("المنتج"), null=True, blank=True)
    count_3 = models.DecimalField(max_digits=7, decimal_places=2,verbose_name=("الامتار المطلوبة"), null=True, default=0)
    prodects_4 = models.ForeignKey(prodect,related_name='items4', on_delete=models.CASCADE, verbose_name=("المنتج"), null=True, blank=True)
    count_4 = models.DecimalField(max_digits=7, decimal_places=2,verbose_name=("الامتار المطلوبة"), null=True, default=0)
    prodect_5 = models.ForeignKey(prodect,related_name='items5', on_delete=models.CASCADE, verbose_name=("المنتج"), null=True, blank=True)
    count_5 = models.DecimalField(max_digits=7, decimal_places=2,verbose_name=("الامتار المطلوبة"), null=True, default=0)
    prodects_6 = models.ForeignKey(prodect,related_name='items6', on_delete=models.CASCADE, verbose_name=("المنتج"), null=True, blank=True)
    count_6 = models.DecimalField(max_digits=7, decimal_places=2,verbose_name=("الامتار المطلوبة"), null=True)

    prodects2 = models.ForeignKey(prodect,related_name='items22', on_delete=models.CASCADE, verbose_name=("المنتج"))
    count2 = models.DecimalField(max_digits=7, decimal_places=2, verbose_name=("الامتار المطلوبة"))
    prodects_22 = models.ForeignKey(prodect,related_name='items222', on_delete=models.CASCADE, verbose_name=("المنتج"), null=True, blank=True)
    count_22 = models.DecimalField(max_digits=7, decimal_places=2,verbose_name=("الامتار المطلوبة"), null=True, default=0)
    prodects32 = models.ForeignKey(prodect,related_name='items32', on_delete=models.CASCADE, verbose_name=("المنتج"), null=True, blank=True)
    count_32 = models.DecimalField(max_digits=7, decimal_places=2,verbose_name=("الامتار المطلوبة"), null=True, default=0)
    prodects_42 = models.ForeignKey(prodect,related_name='items42', on_delete=models.CASCADE, verbose_name=("المنتج"), null=True, blank=True)
    count_42 = models.DecimalField(max_digits=7, decimal_places=2,verbose_name=("الامتار المطلوبة"), null=True, default=0)
    prodect_52 = models.ForeignKey(prodect,related_name='items52', on_delete=models.CASCADE, verbose_name=("المنتج"), null=True, blank=True)
    count_52 = models.DecimalField(max_digits=7, decimal_places=2,verbose_name=("الامتار المطلوبة"), null=True, default=0)
    prodects_62 = models.ForeignKey(prodect,related_name='items62', on_delete=models.CASCADE, verbose_name=("المنتج"), null=True, blank=True)
    count_62 = models.DecimalField(max_digits=7, decimal_places=2,verbose_name=("الامتار المطلوبة"), null=True)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, verbose_name=("وقت عملية الشراء"))
    date2= models.DateField(auto_now_add=True, verbose_name=("وقت العملية "), help_text='الامتار')
    # def get_brice(self):
    #     jj = self.prodects.brice
    #     return jj
    def get_karton(self):
        mag = self.count / self.prodects.brice 
        return mag
   
    def get_karton2(self):
        if self.count_2 :
            mag2 = self.count_2 / self.prodects_2.brice
            return mag2   
    def get_karton3(self):
        if self.count_3 :
            mag = self.count_3 / self.prodects3.brice 
            return mag    
    def get_karton4(self):
        if self.count_4 :
            mag = self.count_4 / self.prodects_4.brice
            return mag  
    def get_karton5(self):
        if self.count_5 :
            mag = self.count_5  / self.prodect_5.brice
            return mag  
    def get_karton6(self):
        if self.count_6:
            mag = self.count_6 / self.prodects_6.brice
            return mag  
    def get_balata(self):
        fir = self.prodects.count_f * self.get_karton()
        return fir
    def get_balata2(self):
        if self.get_karton2() :
            firss = self.prodects_2.count_f * self.get_karton2()
            return firss
    def get_balata3(self):
        if self.get_karton3() :
            fir = self.prodects3.count_f * self.get_karton3()
            return fir
    def get_balata4(self):
        if self.get_karton4() :
            fir = self.prodects_4.count_f * self.get_karton4()
            return fir
    def get_balata5(self):
        if self.get_karton5() :
            fir = self.prodect_5.count_f * self.get_karton5()
            return fir
    def get_balata6(self):
        if self.get_karton6() :
            fir = self.prodects_6.count_f * self.get_karton6()
            return fir
    def get_price(self):
        fer = self.prodects.buybrice * self.count
        return fer
    def get_price2(self):
        fer = self.prodects.buybrice * self.count_2
        return fer
    def get_price3(self):
        fer = self.prodects.buybrice * self.count_3
        return fer
    def get_price4(self):
        fer = self.prodects.buybrice * self.count_4
        return fer
    def get_price5(self):
        fer = self.prodects.buybrice * self.count_5
        return fer
    def get_price6(self):
        # if self.count_6 :
        fer = self.prodects.buybrice * self.count_6
        return fer
    def get_price_mets(self):
        if self.prodects.buybrice :
            return self.prodects.buybrice
    def get_price_mets2(self):
        if self.prodects_2:
            return self.prodects_2.buybrice
    def get_price_mets3(self):
        if self.prodects3 :
            return self.prodects3.buybrice
    def get_price_mets4(self):
        if self.prodects_4 :
            return self.prodects_4.buybrice
    def get_price_mets5(self):
        if self.prodect_5 :
            return self.prodect_5.buybrice
    def get_price_mets6(self):
        if self.prodects_6 :
            return self.prodects_6.buybrice

    def get_karton2(self):
        mag = self.count2 / self.prodects2.brice 
        return mag
   
    def get_karton22(self):
        if self.count_22 :
            mag22 = self.count_22 / self.prodects_22.brice
            return mag2 2  
    def get_karton32(self):
        if self.count_32 :
            mag2 = self.count_32 / self.prodects32.brice 
            return mag2    
    def get_karton42(self):
        if self.count_42 :
            mag = self.count_42 / self.prodects_42.brice
            return mag  
    def get_karton52(self):
        if self.count_52 :
            mag = self.count_52  / self.prodect_52.brice
            return mag  
    def get_karton62(self):
        if self.count_62:
            mag = self.count_62 / self.prodects_62.brice
            return mag  
    def get_balata2(self):
        fir = self.prodects2.count_f * self.get_karton22()
        return fir
    def get_balata22(self):
        if self.get_karton22() :
            firss = self.prodects_22.count_f * self.get_karton22()
            return firss
    def get_balata3(self):
        if self.get_karton32() :
            fir = self.prodects32.count_f * self.get_karton32()
            return fir
    def get_balata42(self):
        if self.get_karton42() :
            fir = self.prodects_42.count_f * self.get_karton42()
            return fir
    def get_balata52(self):
        if self.get_karton52() :
            fir = self.prodect_52.count_f * self.get_karton52()
            return fir
    def get_balata62(self):
        if self.get_karton62() :
            fir = self.prodects_62.count_f * self.get_karton62()
            return fir
    def get_price2(self):
        fer = self.prodects2.buybrice * self.count2
        return fer
    def get_price22(self):
        fer = self.prodects22.buybrice * self.count_22
        return fer
    def get_price3(self):
        fer = self.prodects.buybrice * self.count_3
        return fer
    def get_price4(self):
        fer = self.prodects.buybrice * self.count_4
        return fer
    def get_price5(self):
        fer = self.prodects.buybrice * self.count_5
        return fer
    def get_price6(self):
        # if self.count_6 :
        fer = self.prodects.buybrice * self.count_6
        return fer
    def get_price_mets(self):
        if self.prodects.buybrice :
            return self.prodects.buybrice
    def get_price_mets2(self):
        if self.prodects_2:
            return self.prodects_2.buybrice
    def get_price_mets3(self):
        if self.prodects3 :
            return self.prodects3.buybrice
    def get_price_mets4(self):
        if self.prodects_4 :
            return self.prodects_4.buybrice
    def get_price_mets5(self):
        if self.prodect_5 :
            return self.prodect_5.buybrice
    def get_price_mets6(self):
        if self.prodects_6 :
            return self.prodects_6.buybrice
    def save(self, *args, **kwargs):
        x = self.prodects.cwan - self.count
        self.prodects.cwan = x
        self.prodects.save()
        if self.count_2 :
            z = self.prodects_2.cwan - self.count_2
            self.prodects_2.cwan = z
            self.prodects_2.save()
        if self.count_3 :
            g = self.prodects3.cwan - self.count_3
            self.prodects3.cwan = g
            self.prodects3.save()
        if self.count_4:
            s = self.prodects_4.cwan - self.count_4
            self.prodects_4.cwan = s
            self.prodects_4.save()
        if self.count_5 :
            e = self.prodect_5.cwan - self.count_5
            self.prodect_5.cwan = s
            self.prodect_5.save()
        if self.count_6 :
            t = self.prodects_6.cwan - self.count_6
            self.prodects_6.cwan = s
            self.prodects_6.save()
        super().save(*args, **kwargs)
    class Meta:
        ordering = ['-date_time']
        verbose_name=_("فاتورة")
        verbose_name_plural = _("اضف او عدل فاتورة")
   
    def __str__(self):
        return self.names
   