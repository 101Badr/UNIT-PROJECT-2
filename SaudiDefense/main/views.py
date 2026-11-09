from django.shortcuts import render
from django.http import Http404


SECTORS = {
    'aerospace': {
        'title': 'الصناعات الجوية',
        'description': 'تعرف على تطور الصناعات الجوية في المملكة العربية السعودية.'
    },
    'land': {
        'title': 'الصناعات البرية',
        'description': 'اكتشف مجالات تصنيع وصيانة الأنظمة والمركبات البرية.'
    },
    'naval': {
        'title': 'الصناعات البحرية',
        'description': 'تعرف على الصناعات البحرية وبناء وصيانة السفن.'
    },
    'technology': {
        'title': 'التقنيات الدفاعية',
        'description': 'استكشف الإلكترونيات والاتصالات والبحث والتطوير.'
    }
}


def home(request):
    return render(request, 'main/home.html')


def history(request):
    return render(request, 'main/history.html')


def sector_detail(request, slug):
    sector = SECTORS.get(slug)

    if sector is None:
        raise Http404('القطاع غير موجود')

    return render(request, 'main/sector_detail.html', {
        'sector': sector
    })


def companies(request):
    return render(request, 'main/companies.html')


def vision(request):
    return render(request, 'main/vision.html')


def about(request):
    return render(request, 'main/about.html')