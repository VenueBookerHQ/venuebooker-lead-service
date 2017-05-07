from rest_framework import viewsets
from web_app.pagination import StandardResultsSetPagination
from web_app.serializers import *


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class ContactViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class OrganisationViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer

class VenueViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class Event_campaignViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Event_campaign.objects.all()
    serializer_class = Event_campaignSerializer

class ContactResponseViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = ContactResponse.objects.all()
    serializer_class = ContactResponseSerializer

class QuoteViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

class EnquiryViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer

class Event_typeViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Event_type.objects.all()
    serializer_class = Event_typeSerializer

class LeadViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class RoomViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


