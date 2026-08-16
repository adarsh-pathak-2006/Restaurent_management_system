from rest_framework.throttling import UserRateThrottle

class RegisterThrottle(UserRateThrottle):
    rate="15/hour"

class TokenObtainThrottle(UserRateThrottle):
    rate="30/hour"

class TokenRefreshThrottle(UserRateThrottle):
    rate="20/hour"

class GeneralThrottle(UserRateThrottle):
    rate="40/minute"