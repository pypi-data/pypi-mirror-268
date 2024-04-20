from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OfdmCls:
	"""Ofdm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ofdm", core, parent)

	def get_elength(self) -> int:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:ISIGnal:OFDM:ELENgth \n
		Snippet: value: int = driver.configure.wlanMeas.isignal.ofdm.get_elength() \n
		Specifies the evaluation length of the burst for OFDM signals. \n
			:return: evaluation_length_symbols: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:ISIGnal:OFDM:ELENgth?')
		return Conversions.str_to_int(response)

	def set_elength(self, evaluation_length_symbols: int) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:ISIGnal:OFDM:ELENgth \n
		Snippet: driver.configure.wlanMeas.isignal.ofdm.set_elength(evaluation_length_symbols = 1) \n
		Specifies the evaluation length of the burst for OFDM signals. \n
			:param evaluation_length_symbols: Number of payload symbols
		"""
		param = Conversions.decimal_value_to_str(evaluation_length_symbols)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:ISIGnal:OFDM:ELENgth {param}')
