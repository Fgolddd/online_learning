from django.db import models

# Create your models here.
class Order(models.Model):
    ORDER_STATUS = (
        (1, '待支付'),
        (2, '已支付'),
    )

    PAY_TYPES = (
        (1, '支付宝'),
        (2, '微信'),
    )

    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='用户')
    order_code = models.CharField(verbose_name='订单编号', max_length=50)
    amount = models.DecimalField(verbose_name='订单金额', max_digits=10, decimal_places=2)
    status = models.SmallIntegerField(verbose_name='订单状态', default=1, choices=ORDER_STATUS)
    pay_type = models.SmallIntegerField(verbose_name='支付方式', default=1, blank=True, choices=PAY_TYPES)
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        db_table = 'onlearn_order'
        ordering = ['-created_at',]
        verbose_name = '订单表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_code

class OrderCourse(models.Model):
    order = models.ForeignKey('Order', verbose_name='所属订单', on_delete=models.CASCADE)
    course = models.ForeignKey('course.Course', verbose_name='课程', on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='商品价格', max_digits=10, decimal_places=2)
    number = models.IntegerField(verbose_name='商品数量', default=1)

    class Meta:
        db_table = 'onlearn_order_course'
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name