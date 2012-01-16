from utils import HotelWebsite


class Doubletree(HotelWebsite):
    _availability_selector = "#roomViewRegularView"
    _params = {
        "arrival": "arrivalDate",
        "departure": "departureDate"
    }
    _pages = [{
        "url": "https://secure3.hilton.com/en_US/dt/reservation/book.htm",
        "data": {
            "ctyhocn": "YYZIPDT"                #UNKNOWN: City Hotel Code?
        }
    }, {
        "url": "https://secure3.hilton.com/en_US/dt/reservation/book.htm?execution=e1s1",
        "data": {
            "arrivalDate": "25 May 2012",
            "departureDate": "27 May 2012",
            "_flexibleDates": "on",
            "_rewardBooking": "on",
            "numberOfRooms": "1",
            "numberOfAdults[0]": "4",
            "numberOfChildren[0]": "0",
            "numberOfAdults[1]": "1",
            "numberOfChildren[1]": "0",
            "numberOfAdults[2]": "1",
            "numberOfChildren[2]": "0",
            "numberOfAdults[3]": "1",
            "numberOfChildren[3]": "0",
            "promoCode": "",
            "srpId": "",
            "onlineValueRate": "",
            "groupCode": "AME",
            "corporateId": "",
            "_rememberCorporateId": "on",
            "_aaaRate": "on",
            "_aarpRate": "on",
            "_governmentRate": "on",
            "_travelAgentRate": "on",
            "_eventId_findRoom": "Continue",
            "execution": "e5s2"
        }
    }]
