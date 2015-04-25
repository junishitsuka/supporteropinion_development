from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def team_list(request):
    teams = Team.objects.all().order_by('id')
    return render_to_response(
        'common/team_list.html',
        {'teams': teams},
        context_instance=RequestContext(request)
    )
