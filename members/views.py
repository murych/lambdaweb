from django.template.response import TemplateResponse

from team.models import Member


def members_list(request):
    """
    Список организаторов и почетных участников (основателей и проч.)
    :param request:
    :return:
    """
    context = {}
    context['organizators'] = Member.objects.filter(groups__name='display_organizator')
    context['honored'] = Member.objects.filter(groups__name='display_honored')
    return TemplateResponse(request, "frontend/members/members_list.html", context)
