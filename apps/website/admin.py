# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import StringIO
import xlwt

from django.contrib import admin
from django.http.response import HttpResponse

from website.models.configuration import Configuration
from website.models.registration import Registration, RegistrationFile
from django.contrib import admin
from solo.admin import SingletonModelAdmin

class RegistrationFileInline(admin.TabularInline):
    model = RegistrationFile
    extra = 0
    verbose_name = "Załącznik"
    verbose_name_plural = "Załączniki"

    def get_readonly_fields(self, request, obj=None):
        return ['created_at', 'file']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


class RegistrationAdmin(admin.ModelAdmin):
    change_form_template = "website/admin/change_form_registration.html"
    change_list_template = "website/admin/change_list_registration.html"
    inlines = [RegistrationFileInline]
    list_display = ('created_at', 'company_name', 'name', 'get_category_display', 'email')
    list_filter = ('category',)
    search_fields = ('company_name', 'email')
    actions = ("export_items",)
    exclude = ('category',)

    def get_readonly_fields(self, request, obj=None):
        return ['created_at', 'company_name', 'get_category_display', 'name', 'company_address', 'phone', 'fax',
                'email', 'description_1', 'description_2', 'description_3', 'allow_scan']

    def has_delete_permission(self, request, obj=None):
        return request.user.username == "biuro@silvercube.pl"

    def has_add_permission(self, request):
        return False

    def get_actions(self, request):
        actions = super(RegistrationAdmin, self).get_actions(request)
        if 'delete_selected' in actions and request.user.username != "biuro@silvercube.pl":
            del actions['delete_selected']
        return actions
    
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context["changelist_filters"] = request.GET.get("_changelist_filters")
        return super(RegistrationAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    def _get_field_verbose_name(self, field_name):
        return Registration._meta.get_field(field_name).verbose_name.title()

    def _export_items(self, queryset):
        style_red = xlwt.easyxf('font: color red;')
        style_empty = xlwt.easyxf()
        queryset = queryset.order_by("created_at")

        date_format = xlwt.XFStyle()
        date_format.num_format_str = 'dd.mm.yyyy'

        wb = xlwt.Workbook(encoding="UTF-8")

        headers = [
            (self._get_field_verbose_name("created_at"), 15),
            (self._get_field_verbose_name("company_name"), 30),
            (self._get_field_verbose_name("category"), 30),
            (self._get_field_verbose_name("name"), 30),
            (self._get_field_verbose_name("company_address"), 30),
            (self._get_field_verbose_name("phone"), 30),
            (self._get_field_verbose_name("fax"), 30),
            (self._get_field_verbose_name("email"), 30),
            (self._get_field_verbose_name("description_1"), 50),
            (self._get_field_verbose_name("description_2"), 50),
            (self._get_field_verbose_name("description_3"), 50),
            ("Ilość załączników", 30),
        ]

        current_sheet = wb.add_sheet("Zgłoszenia")

        column = 0
        for header in headers:
            current_sheet.write(0, column, header[0])
            current_sheet.col(column).width = 256 * header[1]
            column += 1

        row = 1
        for item in queryset.all():
            current_sheet.write(row, 0, item.created_at, date_format)
            current_sheet.write(row, 1, item.company_name)
            current_sheet.write(row, 2, item.get_category_display())
            current_sheet.write(row, 3, item.name)
            current_sheet.write(row, 4, item.company_address)
            current_sheet.write(row, 5, item.phone)
            current_sheet.write(row, 6, item.fax)
            current_sheet.write(row, 7, item.email)
            current_sheet.write(row, 8, item.description_1)
            current_sheet.write(row, 9, item.description_2)
            current_sheet.write(row, 10, item.description_3)
            current_sheet.write(row, 11, item.registrationfile_set.count())
            row += 1

        return wb

    def export_items(self, request, queryset):
        wb = self._export_items(queryset)
        f = StringIO.StringIO()
        wb.save(f)
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="zgloszenia_rigips_trophy.xls"'
        response.write(f.getvalue())
        return response
    export_items.short_description = "Eksportuj"

admin.site.register(Registration, RegistrationAdmin)


admin.site.register(Configuration, SingletonModelAdmin)
