"""
Default settings for the ``mezzanine.LECTURE`` app. Each of these can be
overridden in your project's settings module, just like regular
Django settings. The ``editable`` argument for each controls whether
the setting is editable via Django's admin.

Thought should be given to how a setting is actually used before
making it editable, as it may be inappropriate - for example settings
that are only read during startup shouldn't be editable, since changing
them would require an application reload.
"""
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import register_setting


register_setting(
    name="LECTURE_USE_FEATURED_IMAGE",
    description=_("Enable featured images in LECTURE posts"),
    editable=False,
    default=False,
)

_LECTURE_URLS_DATE_FORMAT = ""
if getattr(settings, "LECTURE_URLS_USE_DATE", False):
    _LECTURE_URLS_DATE_FORMAT = "day"
    from warnings import warn
    warn("LECTURE_URLS_USE_DATE setting is deprecated, please use the "
        "LECTURE_URLS_DATE_FORMAT setting with a value of 'year', 'month', "
        "or 'day'.")

register_setting(
    name="LECTURE_URLS_DATE_FORMAT",
    label=_("LECTURE post URL date format"),
    description=_("A string containing the value ``year``, ``month``, or "
        "``day``, which controls the granularity of the date portion in the "
        "URL for each LECTURE post. Eg: ``year`` will define URLs in the format "
        "/LECTURE/yyyy/slug/, while ``day`` will define URLs with the format "
        "/LECTURE/yyyy/mm/dd/slug/. An empty string means the URLs will only "
        "use the slug, and not contain any portion of the date at all."),
    editable=False,
    default=_LECTURE_URLS_DATE_FORMAT,
)

register_setting(
    name="LECTURE_POST_PER_PAGE",
    label=_("LECTURE posts per page"),
    description=_("Number of LECTURE posts shown on a LECTURE listing page."),
    editable=True,
    default=5,
)

# register_setting(
#     name="LECTURE_RSS_LIMIT",
#     label=_("LECTURE posts RSS limit"),
#     description=_("Number of most recent LECTURE posts shown in the RSS feed. "
#         "Set to ``None`` to display all LECTURE posts in the RSS feed."),
#     editable=False,
#     default=20,
# )

register_setting(
    name="LECTURE_SLUG",
    description=_("Slug of the page object for the LECTURE."),
    editable=False,
    default="LECTURE",
)