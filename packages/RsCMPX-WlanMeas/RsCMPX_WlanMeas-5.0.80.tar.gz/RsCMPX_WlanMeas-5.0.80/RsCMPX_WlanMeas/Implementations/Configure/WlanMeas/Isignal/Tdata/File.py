from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FileCls:
	"""File commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("file", core, parent)

	def get_date(self) -> str:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:ISIGnal:TDATa:FILE:DATE \n
		Snippet: value: str = driver.configure.wlanMeas.isignal.tdata.file.get_date() \n
		No command help available \n
			:return: file_date: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:ISIGnal:TDATa:FILE:DATE?')
		return trim_str_response(response)
