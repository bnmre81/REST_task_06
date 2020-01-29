from rest_framework.permissions import BasePermission
from datetime import date


class IsBookingOwnerOrStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.user == request.user):
            return True
        else:
            return False


class UpcomingBooking(BasePermission):
	message = "too late!"
	def has_object_permission(self, request, view, obj):
		if (obj.date - date.today()).days >= 3:
			return True
		return False



