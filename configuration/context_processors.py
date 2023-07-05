from configuration.models import Configuration


def configuration_hotel(request):
    elements = Configuration.objects.all()
    for element in elements:
        obj = element.id

    configuration = Configuration.objects.get(id=obj)
    return {'configuration': configuration}