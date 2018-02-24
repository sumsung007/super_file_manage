# -*- coding: utf-8 -*-
import os, re
from importlib import import_module

from django.core.management.base import BaseCommand, CommandError
from django.db import models
from common.import_tb_to_db import import_table_to_database
import openpyxl

from django.conf import settings
from django.utils.log import configure_logging
configure_logging(settings.LOGGING_CONFIG, settings.COMMAND_LOGGING)  # init command logging



class Command(BaseCommand):
	help = "从.xlsx表中导出数据到数据库中"
	
	def add_arguments(self, parser):
		"""
		添加命令参数
		
		@param parser: see also: https://docs.python.org/3/library/argparse.html#module-argparse
		"""
		parser.add_argument("app")
		parser.add_argument("xlsfile")
		parser.add_argument("--clear-table", default = "True", choices = ["True", "False"], help = "是否自动清除相关表的数据。默认：True")

	def handle(self, *args, **options):
		"""
		"""
		app = options["app"]
		xlsfile = options["xlsfile"]
		clearTable = options["clear_table"] == "True" and True or False
		
		import_table_to_database(xlsfile, app, clearTable=clearTable,cmd=True)
	
