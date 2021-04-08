import django
from django.shortcuts import render

from datacenter.models import format_duration, get_duration, is_visit_long, Passcard, Visit


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)

    visits = Visit.objects.all()

    this_passcard_visits = []
    for visit in visits:
        passcard_info = {}
        is_strange = is_visit_long(visit)
        entered_at = django.utils.timezone.localtime(visit.entered_at)
        seconds_duration = get_duration(visit)
        duration = format_duration(seconds_duration)
        passcard_info.update({
            "entered_at": entered_at,
            "duration": duration,
            "is_strange": is_strange
        })
        this_passcard_visits.append(passcard_info)

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
