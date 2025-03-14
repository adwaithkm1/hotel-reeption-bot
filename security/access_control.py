class AccessControl:
    roles = {
        "receptionist": ["view_bookings", "manage_guests"],
        "admin": ["view_bookings", "manage_guests", "manage_staff", "view_financials"]
    }

    def __init__(self, user_role):
        self.user_role = user_role

    def has_permission(self, action):
        return action in self.roles.get(self.user_role, [])
