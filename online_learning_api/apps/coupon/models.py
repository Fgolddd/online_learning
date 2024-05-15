from django.db import models

# Create your models here.
from apps.user.models import User

class Coupon(models.Model):
    name = models.CharField(max_length=50, verbose_name='优惠券名称')
    type = models.IntegerField(choices=((1, '满减券'), (2, '折扣券')), verbose_name='优惠券类型')
    money = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='优惠券面值')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='优惠券用户')
    description = models.CharField(max_length=200)  # 优惠券描述
    total = models.IntegerField(blank=True, default=100, verbose_name="发放数量")
    remain = models.IntegerField(blank=True, default=100, verbose_name="剩余数量")
    start_time = models.DateTimeField(verbose_name="启用时间")
    end_time = models.DateTimeField(verbose_name="过期时间")
    condition = models.IntegerField(blank=True, default=0, verbose_name="满足使用优惠券的价格条件")
    per_limit = models.SmallIntegerField(default=1, verbose_name="每人限制领取数量")

    class Meta:
        db_table = "onlearn_coupon"
        verbose_name = '优惠券'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.user.username + '的优惠券'