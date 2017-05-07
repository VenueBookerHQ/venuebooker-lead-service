from rest_framework import serializers
from web_app.models import *


# Serializers define the REST API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('url', 'username', 'email', 'is_staff')


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('first_name', 'surname', 'telephone', 'mobile', 'email')

class OrganisationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organisation
        fields = ('name', 'image', 'primary_contact', 'address', 'description')

class ContactResponseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactResponse
        fields = ('name', 'email', 'phone', 'message', 'timestamp')

class VenueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'facebook_link', 'twitter_link', 'instagram_link', 'description', 'nearest_transport_link', 'organisation')

class Event_campaignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event_campaign
        fields = ('name', 'type', 'details', 'startTime', 'endTime', 'capacity', 'cost_per_capacity_unit', 'venue')

class EnquirySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Enquiry
        fields = ('message', 'attendeeNum', 'date', 'event_campaign', 'user', 'approved')

class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quote
        fields = ('description', 'cost', 'accepted', 'enquiry')

class Event_typeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event_type
        fields = ('name', 'description', 'active', 'seasonal')

class LeadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lead
        fields = ('name', 'email', 'budget', 'comments', 'created', 'date_from', 'date_to', 'location', 'guests', 'occasion', 'received')

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('name', 'description', 'capacity', 'size', 'venue')
