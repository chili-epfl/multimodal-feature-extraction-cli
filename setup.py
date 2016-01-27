from setuptools import setup


setup(
	name='mmfe',
	version='1.0',
	py_modules=['mmfe'],
	install_requires=[
		'Click',
	],
	entry_points='''
		[console_scripts]
		mmfe=mmfe:cli
	''',
)
