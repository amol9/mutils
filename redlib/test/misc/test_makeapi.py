from unittest import TestCase, main as ut_main
import sys


class TestMakeAPI(TestCase):

	def test_import(self):
		from redlib.api import system

		system_dir = ['FrequencyError', 'PlatformError', 'Scheduler', 'get_scheduler', 'sys_command', 'CronDBus', 'is_linux', 'in_cron']
		for i in system_dir:
			self.assertIn(i, dir(system))


		from redlib.api import misc

		misc_dir = ['log', 'Logger', 'Retry', 'Singleton', 'trim_docstring', 'TextFile']
		for i in misc_dir:
			self.assertIn(i, dir(misc))

		from redlib.api import py23

		py23_dir = ['pickledump', 'pickleload']
		for i in py23_dir:
			self.assertIn(i, dir(py23))

		from redlib.api import web

		web_dir = ['cdns', 'tlds', 'AbsUrl']
		for i in web_dir:
			self.assertIn(i, dir(web))


	def test_moves(self):
		from redlib.api.misc import trim
		
		self.assertEqual(trim.__name__, 'trim_docstring')


	def test_exclude(self):
		import redlib.api

		red_importer = None
		for i, importer in enumerate(sys.meta_path):
			if (type(importer).__name__ == "_RedMetaPathImporter" and importer.name == 'redlib.api'):
				red_importer = importer
				break

		known_modules = [m[m.rfind('.') + 1:] for m in red_importer.known_modules]
		excluded = ['test', 'version']

		for e in excluded:
			self.assertNotIn(e, known_modules)

		included = ['colors', 'html', 'image', 'misc', 'prnt', 'py23', 'system', 'testlib', 'web']
		for i in included:
			self.assertIn(i, known_modules)


if __name__ == '__main__':
	ut_main()

