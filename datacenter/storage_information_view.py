import django
from django.shortcuts import render

from datacenter.models import format_duration, get_duration, Visit


def storage_information_view(request):
    visits = Visit.objects.all()
    not_leaved_at = visits.filter(leaved_at=None)
    non_closed_visits = []
    for visit in not_leaved_at:
        users = {}
        user = visit.passcard.owner_name
        entered_at = django.utils.timezone.localtime(visit.entered_at)
        seconds_duration = get_duration(visit)
        duration = format_duration(seconds_duration)
        users.update({'who_entered': user,
                      'entered_at': entered_at,
                      'duration': duration})
        non_closed_visits.append(users)
    context = {"non_closed_visits": non_closed_visits}
    return render(request, 'storage_information.html', context)
