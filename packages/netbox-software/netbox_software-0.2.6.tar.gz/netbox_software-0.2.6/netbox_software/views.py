from django.contrib.auth.mixins import PermissionRequiredMixin
from netbox.views import generic
from utilities.views import register_model_view
from . import forms, models, tables, filtersets


#from rest_framework import status, viewsets
#from rest_framework.response import Response


### Vendor
@register_model_view(models.Vendor)
class VendorView(PermissionRequiredMixin, generic.ObjectView):
    permission_required = "netbox_software.view_vendor"
    queryset = models.Vendor.objects.all()


class VendorListView(PermissionRequiredMixin, generic.ObjectListView):
    permission_required = "netbox_software.view_vendor"
    queryset = models.Vendor.objects.all()
    table = tables.VendorTable
    filterset = filtersets.VendorFilterSet
    filterset_form = forms.VendorFilterForm


@register_model_view(models.Vendor, 'edit')
class VendorEditView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = "netbox_software.change_vendor"
    queryset = models.Vendor.objects.all()
    form = forms.VendorForm

    template_name = 'netbox_software/vendor_edit.html'


@register_model_view(models.Vendor, 'delete')
class VendorDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = "netbox_software.delete_vendor"
    queryset = models.Vendor.objects.all()


### SoftwareType
@register_model_view(models.SoftwareType)
class SoftwareTypeView(PermissionRequiredMixin, generic.ObjectView):
    permission_required = "netbox_software.view_softwaretype"
    queryset = models.SoftwareType.objects.all()


class SoftwareTypeListView(PermissionRequiredMixin, generic.ObjectListView):
    permission_required = "netbox_software.view_softwaretype"
    queryset = models.SoftwareType.objects.all()
    table = tables.SoftwareTypeTable
    filterset = filtersets.SoftwareTypeFilterSet
    filterset_form = forms.SoftwareTypeFilterForm


@register_model_view(models.SoftwareType, 'edit')
class SoftwareTypeEditView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = "netbox_software.change_softwaretype"
    queryset = models.SoftwareType.objects.all()
    form = forms.SoftwareTypeForm
    template_name = 'netbox_software/softwaretype_edit.html'


@register_model_view(models.SoftwareType, 'delete')
class SoftwareTypeDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = "netbox_software.delete_softwaretype"
    queryset = models.SoftwareType.objects.all()


### Application
class ApplicationView(PermissionRequiredMixin, generic.ObjectView):
    permission_required = "netbox_software.view_application"
    queryset = models.Application.objects.all()


class ApplicationListView(PermissionRequiredMixin, generic.ObjectListView):
    permission_required = "netbox_software.view__application"
    queryset = models.Application.objects.all()
    table = tables.ApplicationTable
    filterset = filtersets.ApplicationFilterSet
    filterset_form = forms.ApplicationFilterForm


class ApplicationEditView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = "netbox_software.change_application"
    queryset = models.Application.objects.all()
    form = forms.ApplicationForm

    template_name = 'netbox_software/application_edit.html'


class ApplicationDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = "netbox_software.delete_application"
    queryset = models.Application.objects.all()


### ApplicationVersion
class ApplicationVersionView(PermissionRequiredMixin, generic.ObjectView):
    permission_required = "netbox_software.view_applicationversion"
    queryset = models.ApplicationVersion.objects.all()


class ApplicationVersionListView(PermissionRequiredMixin, generic.ObjectListView):
    permission_required = "netbox_software.view_applicationversion"
    queryset = models.ApplicationVersion.objects.all()
    table = tables.ApplicationVersionTable
    filterset = filtersets.ApplicationVersionFilterSet
    filterset_form = forms.ApplicationVersionFilterForm


class ApplicationVersionEditView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = "netbox_software.change_applicationversion"
    queryset = models.ApplicationVersion.objects.all()
    form = forms.ApplicationVersionForm

    template_name = 'netbox_software/applicationversion_edit.html'


class ApplicationVersionDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = "netbox_software.delete_applicationversion"
    queryset = models.ApplicationVersion.objects.all()


### DeviceSoftware
class DeviceSoftwareView(PermissionRequiredMixin, generic.ObjectView):
    permission_required = "netbox_software.view_devicesoftware"
    queryset = models.DeviceSoftware.objects.all()


class DeviceSoftwareListView(PermissionRequiredMixin, generic.ObjectListView):
    permission_required = "netbox_software.view_devicesoftware"
    queryset = models.DeviceSoftware.objects.all()
    table = tables.DeviceSoftwareTable
    filterset = filtersets.DeviceSoftwareFilterSet
    filterset_form = forms.DeviceSoftwareFilterForm


class DeviceSoftwareEditView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = "netbox_software.change_devicesoftware"
    queryset = models.DeviceSoftware.objects.all()
    form = forms.DeviceSoftwareForm

    template_name = 'netbox_software/devicesoftware_edit.html'


class DeviceSoftwareDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = "netbox_software.delete_devicesoftware"
    queryset = models.DeviceSoftware.objects.all()
