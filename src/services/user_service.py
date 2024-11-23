from repositories.user_repository import UserRepository

class UserService:
    @staticmethod
    def get_all_users():
        return UserRepository.get_all_users()

