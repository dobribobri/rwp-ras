from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.conf import settings as params
from django.utils.encoding import escape_uri_path
from django.db.models import Q
from django.utils.http import unquote
import os
import re
from .models import *
from .forms import *


def get_username(request):
    try:
        name = request.user.get_full_name()
    except AttributeError:
        name = ''
    if not name:
        name = request.user.username
    return name


def get_rMessages():
    return RightBlockMessage.objects.all()


def index(request):
    q = request.GET.get('q')
    if q:
        return search(request)
    blocks = IndexBlock.objects.all()
    return render(request, 'index.html', {'blocks': blocks,
                                          'messages': get_rMessages(),
                                          'username': get_username(request)})


def structure(request):
    q = request.GET.get('q')
    if q:
        return search(request)
    blocks = SectionsBlock.objects.all()
    try:
        b = blocks[0]
    except IndexError:
        b = None
    members = BureauMember.objects.all()
    return render(request, 'structure.html', {'block': b,
                                              'members': members,
                                              'messages': get_rMessages(),
                                              'username': get_username(request)})


def sections(request):
    q = request.GET.get('q')
    if q:
        return search(request)
    blocks = SectionsBlock.objects.all()
    try:
        b = blocks[0]
    except IndexError:
        b = None
    return render(request, 'sections.html', {'block': b,
                                             'messages': get_rMessages(),
                                             'username': get_username(request)})


def bureau(request):
    q = request.GET.get('q')
    if q:
        return search(request)
    members = BureauMember.objects.all()
    return render(request, 'bureau.html', {'blocks': members,
                                           'messages': get_rMessages(),
                                           'username': get_username(request)})


def work(request):
    q = request.GET.get('q')
    if q:
        return search(request)
    announcements = AnnouncementBlock.objects.all()
    return render(request, 'work.html', {'announcements': announcements,
                                         'messages': get_rMessages(),
                                         'username': get_username(request)})


def announcement(request):
    q = request.GET.get('q')
    if q:
        return search(request)
    blocks = AnnouncementBlock.objects.all()
    return render(request, 'announcement.html', {'blocks': blocks,
                                                 'messages': get_rMessages(),
                                                 'username': get_username(request)})


def protocol(request):
    q = request.GET.get('q')
    if q:
        return search(request)
    items = ItemProtocol.objects.all()

    return render(request, 'protocol.html', {'items': items,
                                             'messages': get_rMessages(),
                                             'username': get_username(request)})


def plan(request):
    q = request.GET.get('q')
    if q:
        return search(request)
    items = ItemPlan.objects.all()
    return render(request, 'plan.html', {'items': items,
                                         'messages': get_rMessages(),
                                         'username': get_username(request)})


def achievements(request):
    q = request.GET.get('q')
    if q:
        return search(request)
    items = ItemAchievement.objects.all()
    return render(request, 'achievements.html', {'items': items,
                                                 'messages': get_rMessages(),
                                                 'username': get_username(request)})


def suggestions(request):
    q = request.GET.get('q')
    if q:
        return search(request)
    items = ItemSuggestions.objects.all()
    return render(request, 'suggestions.html', {'items': items,
                                                'messages': get_rMessages(),
                                                'username': get_username(request)})


def participation(request):
    q = request.GET.get('q')
    if q:
        return search(request)
    items = ItemParticipation.objects.all()
    return render(request, 'participation.html', {'items': items,
                                                  'messages': get_rMessages(),
                                                  'username': get_username(request)})


def docs(request):
    # Выключено
    q = request.GET.get('q')
    if q:
        return search(request)
    items = ItemNDocs.objects.all()
    return render(request, 'docs.html', {'items': items,
                                         'messages': get_rMessages(),
                                         'username': get_username(request)})


def decisions(request):
    # Выключено
    q = request.GET.get('q')
    if q:
        return search(request)
    items = ItemDecision.objects.all()
    return render(request, 'decisions.html', {'items': items,
                                              'messages': get_rMessages(),
                                              'username': get_username(request)})


def reports(request):
    q = request.GET.get('q')
    if q:
        return search(request)
    items = ItemReport.objects.all()
    return render(request, 'reports.html', {'items': items,
                                            'messages': get_rMessages(),
                                            'username': get_username(request)})


def other(request):
    q = request.GET.get('q')
    if q:
        return search(request)
    items = ItemOther.objects.all()
    return render(request, 'other.html', {'items': items,
                                          'messages': get_rMessages(),
                                          'username': get_username(request)})


def community(request):
    q = request.GET.get('q')
    if q:
        return search(request)
    conferences = ConferenceBlock.objects.all()
    seminars = SeminarBlock.objects.all()
    projects = ProjectBlock.objects.all()
    return render(request, 'community.html', {'conferences': conferences,
                                              'seminars': seminars,
                                              'projects': projects,
                                              'messages': get_rMessages(),
                                              'username': get_username(request)})


def conferences(request):
    q = request.GET.get('q')
    if q:
        return search(request)
    blocks = ConferenceBlock.objects.all()
    return render(request, 'conferences.html', {'blocks': blocks,
                                                'messages': get_rMessages(),
                                                'username': get_username(request)})


def seminars(request):
    q = request.GET.get('q')
    if q:
        return search(request)
    blocks = SeminarBlock.objects.all()
    return render(request, 'seminars.html', {'blocks': blocks,
                                             'messages': get_rMessages(),
                                             'username': get_username(request)})


def projects(request):
    q = request.GET.get('q')
    if q:
        return search(request)
    blocks = ProjectBlock.objects.all()
    return render(request, 'projects.html', {'blocks': blocks,
                                             'messages': get_rMessages(),
                                             'username': get_username(request)})


def contacts(request):
    q = request.GET.get('q')
    if q:
        return search(request)
    blocks = ContactsBlock.objects.all()
    try:
        b = blocks[0]
    except IndexError:
        b = None
    return render(request, 'contacts.html', {'block': b,
                                             'messages': get_rMessages(),
                                             'username': get_username(request)})


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]


def get_query(query_string, search_fields):
    query = None
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query


def search(request):
    query_string = ''
    not_found = False
    members_ = None
    announcements_ = None
    achievements_, reports_, plans_, suggestions_, protocols_, participations_, others_ = \
        None, None, None, None, None, None, None
    conferences_, seminars_, projects_ = None, None, None
    if ('q' in request.GET) and request.GET['q'].strip():
        
        query_string = unquote(request.GET['q'])

        entry_query = get_query(query_string, ['fio', 'desc', ])
        members_ = BureauMember.objects.filter(entry_query)

        entry_query = get_query(query_string, ['caption', 'desc', 'id', 'when', 'where', ])
        announcements_ = AnnouncementBlock.objects.filter(entry_query)

        entry_query = get_query(query_string, ['caption', 'desc', 'filetype', ])
        achievements_ = ItemAchievement.objects.filter(entry_query)
        reports_ = ItemReport.objects.filter(entry_query)
        plans_ = ItemPlan.objects.filter(entry_query)
        suggestions_ = ItemSuggestions.objects.filter(entry_query)
        protocols_ = ItemProtocol.objects.filter(entry_query)
        participations_ = ItemParticipation.objects.filter(entry_query)
        others_ = ItemOther.objects.filter(entry_query)

        entry_query = get_query(query_string, ['caption', 'desc', 'when', 'where', ])
        conferences_ = ConferenceBlock.objects.filter(entry_query)
        seminars_ = SeminarBlock.objects.filter(entry_query)

        entry_query = get_query(query_string, ['caption', 'desc', ])
        projects_ = ProjectBlock.objects.filter(entry_query)

    if not members_ and not announcements_ and \
        not achievements_ and not reports_ and not plans_ and not suggestions_ and \
        not protocols_ and not participations_ and not others_ and \
        not conferences_ and not seminars_ and not projects_:
            not_found = True

    return render(request, 'search.html', {'query_string': query_string,
                                           'nf': not_found,

                                           'members': members_,

                                           'announcements': announcements_,

                                           'achievements': achievements_,
                                           'reports': reports_,
                                           'plans': plans_,
                                           'suggestions': suggestions_,
                                           'protocols': protocols_,
                                           'participations': participations_,
                                           'others': others_,

                                           'conferences': conferences_,
                                           'seminars': seminars_,
                                           'projects': projects_,
                                           'messages': get_rMessages(),
                                           'username': get_username(request)})


def download(request):
    target = request.GET.get('target')
    ID = request.GET.get('id')
    if (not target) or (not ID):
        raise Http404
    obj = None
    if target == "protocol":
        obj = ItemProtocol.objects.filter(id=ID)
    if target == "plan":
        obj = ItemPlan.objects.filter(id=ID)
    if target == "achievements":
        obj = ItemAchievement.objects.filter(id=ID)
    if target == "suggestions":
        obj = ItemSuggestions.objects.filter(id=ID)
    if target == "participation":
        obj = ItemParticipation.objects.filter(id=ID)
    if target == "docs":
        obj = ItemNDocs.objects.filter(id=ID)
    if target == "decisions":
        obj = ItemDecision.objects.filter(id=ID)
    if target == "reports":
        obj = ItemReport.objects.filter(id=ID)
    if target == "other":
        obj = ItemOther.objects.filter(id=ID)
    if (not obj) or (not obj[0].file):
        raise Http404
    file_path = os.path.join(params.MEDIA_ROOT, obj[0].file.path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/force-download")
            file_name = escape_uri_path(re.split(r'/', file_path)[-1])
            # response['Content-Disposition'] = 'inline; filename=' + file_name
            response['Content-Disposition'] = "attachment; filename=" + file_name
            return response
    raise Http404


@login_required
@transaction.atomic
def settings(request):
    q = request.GET.get('q')
    if q:
        return search(request)
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            profile.fulfilled = True
            profile.save(update_fields=["filled"])
            return render(request, 'settings.html', {
                'user_form': user_form,
                'profile_form': profile_form,
                'profile': profile,
                'messages': get_rMessages(),
                'username': get_username(request)
            })
        else:
            pass
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    return render(request, 'settings.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile,
        'messages': get_rMessages(),
        'username': get_username(request)
    })
