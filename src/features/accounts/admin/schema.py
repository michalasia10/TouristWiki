from src.features.accounts.common.schema import UserSignIn, UserSingUp, User


class Admin(User):
    pass


class AdminSignIn(UserSignIn):
    pass


class AdminSingUp(UserSingUp):
    pass
