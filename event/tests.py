from django.test import TestCase

from .models import Event, EventLocation


class EntryModelTest(TestCase):
    def test_event(self):
        event = Event(title="My entry title",
                      slug="my-entry-title",
                      sub_title="sub title")
        self.assertEqual(str(event), event.title)

    def test_event_location(self):
        event_location = EventLocation(name='lambda',
                                       address='Dubosekovskaya ul., 4A/1, Moskva, 125080')
        self.assertEqual(str(event_location), event_location.name, event_location.address)
