# project/config.py


class BaseConfig:
	"""Base Configuration"""
	DEBUG = False
	TESTING = False


class DevelopmentConfig(BaseConfig):
	"""Development configuratiion"""
	DEBUG = True


class TestingConfig(BaseConfig):
	"""Testing configuration"""
	DEBUG = True
	TESTING  = True


class ProductionConfig(BaseConfig):
	"""Production configuration"""
	DEBUG = False
