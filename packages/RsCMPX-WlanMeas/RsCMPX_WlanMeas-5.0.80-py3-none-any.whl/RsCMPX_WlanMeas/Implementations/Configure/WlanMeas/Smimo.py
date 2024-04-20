from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SmimoCls:
	"""Smimo commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("smimo", core, parent)

	# noinspection PyTypeChecker
	def get_ctuple(self) -> enums.ConnectorTuple:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:SMIMo:CTUPle \n
		Snippet: value: enums.ConnectorTuple = driver.configure.wlanMeas.smimo.get_ctuple() \n
		No command help available \n
			:return: con_tuple: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:SMIMo:CTUPle?')
		return Conversions.str_to_scalar_enum(response, enums.ConnectorTuple)

	def set_ctuple(self, con_tuple: enums.ConnectorTuple) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:SMIMo:CTUPle \n
		Snippet: driver.configure.wlanMeas.smimo.set_ctuple(con_tuple = enums.ConnectorTuple.CT12) \n
		No command help available \n
			:param con_tuple: No help available
		"""
		param = Conversions.enum_scalar_to_str(con_tuple, enums.ConnectorTuple)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:SMIMo:CTUPle {param}')
