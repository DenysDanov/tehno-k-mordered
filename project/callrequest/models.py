from django.db import models
from django.utils.translation import gettext as _

class CallRequestStatus(models.Model):

    name = models.CharField(_('Название статуса'), max_length=50)

    def __str__(self) -> str:
        return self.name


class ClientActivitySphere(models.Model):
    name = models.CharField(_('Сфера деятельности клиента'), max_length=50)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('Сфера деятельности клиента')
        verbose_name_plural = _('Сферы деятельности клиента')



class CallRequest(models.Model):

    name = models.CharField(_('Имя заявителя'), max_length=100)
    phone = models.CharField(_('Телефон'), max_length=20)
    status = models.ForeignKey(to=CallRequestStatus, on_delete=models.DO_NOTHING)
    
    #optional 
    activity = models.ForeignKey(to=ClientActivitySphere, on_delete=models.DO_NOTHING, default=None, null=True, blank=True)
    textarea = models.TextField(_('О компании клиента'), blank=True, null=True)
    def __str__(self) -> str:
        return f"Заявка №{self.pk}"
    
    class Meta:
        verbose_name = _('Заявка на звонок')
        verbose_name_plural = _('Заявки на звонок')


class CallRequestComment(models.Model):
    
    call_request = models.ForeignKey(to=CallRequest, on_delete=models.CASCADE)
    comment = models.TextField(_('Комментарий'))
    
    class Meta:
        verbose_name = _('Комментарий к заявке')
        verbose_name_plural = _('Комментарии к заявке')