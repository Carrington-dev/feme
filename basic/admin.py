import csv
import datetime
from django.contrib import admin
from django.http import HttpResponse
from basic.models import *

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; \
            filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    writer.writerow([field.verbose_name for field in fields])

    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response

export_to_csv.short_description = 'Export to CSV'


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    '''Admin View for Contact'''
    list_display = ('name', 'email', 'subject', 'phone', 'message', 'date_recieved', 'date_last_viewed')
    list_filter = ('name', 'email',)
    readonly_fields = ('message',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    '''Admin View for Subscribe'''

    list_display = ('email', 'is_subscribed', 'date_recieved', 'date_last_viewed')
    list_filter = ('is_subscribed',)
    search_fields = ('email', )
    date_hierarchy = 'date_recieved'
    ordering = ('-pk',)
    list_per_page: int = 30
    actions = [export_to_csv]


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    '''Admin View for Network'''

    list_display = ('user', 'identity', 'full_name', 'email', 'contact', 'city', 'membership', 'allow_data_access', 'best_calltime', 'company_name', 'registration_number', 'age', 'company_address', 'business_size', 'category', 'industry', 'have_record', 'can_recieve_updates', 'allow_data_access', 'date_applied')
    list_filter = ('city',)
    raw_id_fields = ['user']
    # readonly_fields = ('identity',)
    search_fields = ('identity', 'company_name')
    date_hierarchy = 'date_applied'
    ordering = ('-pk',)