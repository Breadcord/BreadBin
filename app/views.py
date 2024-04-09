from django.http import FileResponse
from django.shortcuts import render

from .models import Module, Package


def index(request):
    return render(request, 'index.html')


def simple_index(request):
    return render(request, 'simple_index.html', context={'modules': Module.objects.order_by('id')})


def simple_module(request, module_id: str):
    module = Module.objects.get(id=module_id)
    context = {
        'module': module,
        'packages': Package.objects.filter(module=module).order_by('file_name')
    }
    return render(request, 'simple_module.html', context=context)


def download_package(request, module_id: str, file_name: str):
    module = Module.objects.get(id=module_id)
    package = Package.objects.get(module=module, file_name=file_name)

    return FileResponse(package.file, filename=package.file_name)
