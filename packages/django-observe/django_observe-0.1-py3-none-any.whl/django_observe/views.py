import json
from typing import Callable
from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.db.models.functions import TruncHour, TruncMinute, TruncDay
from django.db.models import Count
from django.contrib.admin.views.decorators import staff_member_required

from dataclasses import dataclass

import datetime

from django_observe.models import Event

# Create your views here.


@dataclass
class Config:
    name: str
    days: int
    trunc_method: Callable


CONFIGS = {
    "daily": Config("daily", 1, TruncMinute),
    "weekly": Config("weekly", 7, TruncHour),
    "monthly": Config("monthly", 30, TruncDay),
}


def group_by_minutes(data, group_size=15):
    new_data = {}
    for stamp, count in data.items():
        stamp = datetime.datetime.fromisoformat(stamp)
        stamp = stamp.replace(
            minute=((stamp.minute // group_size) * group_size), second=0, microsecond=0
        )
        stamp = stamp.isoformat()
        new_data[stamp] = new_data.get(stamp, 0) + count
    return new_data


def get_top_routes(events, limit=20):
    routes = {}
    for event in events:
        if event.path not in routes:
            routes[event.path] = {
                "key": event.path.replace("/", "__"),
                "2xx": 0,
                "3xx": 0,
                "4xx": 0,
                "5xx": 0,
                "count": 0,
                "events": [],
            }

        routes[event.path]["count"] += 1
        if event.status_code < 300:
            routes[event.path]["2xx"] += 1
        elif event.status_code < 400:
            routes[event.path]["3xx"] += 1
        elif event.status_code < 500:
            routes[event.path]["4xx"] += 1
        else:
            routes[event.path]["5xx"] += 1
        routes[event.path]["events"].append(
            {
                "method": event.method,
                "path": event.path,
                "status_code": event.status_code,
                "remote_addr": event.remote_addr,
                "user_agent": event.user_agent,
                "time": event.timestamp.isoformat(),
            }
        )

    top_routes = sorted(routes.items(), key=lambda v: -1 * v[1]["count"])[:limit]
    return top_routes


def get_time_series(events, config):
    event_mapping = {}

    # Fill out zeroes for empty data
    match config.name:
        case "daily":
            date = datetime.datetime.now().date()
            for hour in range(24):
                for minute in range(60):
                    event_datetime = datetime.datetime.fromisoformat(date.isoformat())
                    event_datetime = event_datetime.replace(hour=hour, minute=minute)
                    event_mapping[event_datetime.isoformat()] = 0
        case "weekly":
            for day in range(7):
                date = (datetime.datetime.now() - datetime.timedelta(days=day)).date()
                for hour in range(24):
                    event_datetime = datetime.datetime.fromisoformat(date.isoformat())
                    event_datetime = event_datetime.replace(hour=hour)
                    event_mapping[event_datetime.isoformat()] = 0
        case "monthly":
            for day in range(30):
                date = (datetime.datetime.now() - datetime.timedelta(days=day)).date()
                event_datetime = datetime.datetime.fromisoformat(date.isoformat())
                event_mapping[event_datetime.isoformat()] = 0

    time_series = (
        events.annotate(trunc_time=config.trunc_method("timestamp"))
        .values("trunc_time")
        .annotate(count=Count("id"))
    )

    for events in time_series:
        event_mapping[events["trunc_time"].replace(tzinfo=None).isoformat()] = events[
            "count"
        ]

    if config.name == "daily":
        event_mapping = group_by_minutes(event_mapping, group_size=5)

    return sorted([(k, v) for k, v in event_mapping.items()], key=lambda v: v[0])


@staff_member_required
def glass(request):
    timespan = request.GET.get("timespan", "daily")

    config = CONFIGS.get(timespan)
    if not config:
        return HttpResponseBadRequest("Invalid timespan")

    events = Event.objects.filter(
        timestamp__gte=datetime.datetime.now() - datetime.timedelta(days=config.days)
    )

    context = {
        "hit_data": json.dumps(get_time_series(events, config)),
        "route_data": json.dumps(get_top_routes(events)),
    }
    return render(request, "django_observe/glass.html", context)
