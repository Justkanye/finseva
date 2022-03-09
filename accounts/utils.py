from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

class TokenGenerator(PasswordResetTokenGenerator):
	"""docstring for TokenGenerator"""
	def _make_hash_value(self, user, timestamp):
		return six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.has_verified_email)

generate_token = TokenGenerator()