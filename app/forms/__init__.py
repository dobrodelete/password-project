from .login import LoginForm
from .registration import RegistrationForm
from .password import PasswordGenerationForm
from .edit_password import EditPasswordGenerationForm
from .account import UpdatePasswordForm

__all__ = [attr for attr in locals().keys() if not attr.startswith("_")]
