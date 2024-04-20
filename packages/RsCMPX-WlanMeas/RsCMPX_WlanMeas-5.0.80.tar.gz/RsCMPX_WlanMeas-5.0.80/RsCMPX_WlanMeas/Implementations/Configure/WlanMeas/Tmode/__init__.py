from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TmodeCls:
	"""Tmode commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tmode", core, parent)

	@property
	def file(self):
		"""file commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_file'):
			from .File import FileCls
			self._file = FileCls(self._core, self._cmd_group)
		return self._file

	def get_no_antennas(self) -> int:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:TMODe:NOANtennas \n
		Snippet: value: int = driver.configure.wlanMeas.tmode.get_no_antennas() \n
		No command help available \n
			:return: no_of_antennas: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:TMODe:NOANtennas?')
		return Conversions.str_to_int(response)

	def set_no_antennas(self, no_of_antennas: int) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:TMODe:NOANtennas \n
		Snippet: driver.configure.wlanMeas.tmode.set_no_antennas(no_of_antennas = 1) \n
		No command help available \n
			:param no_of_antennas: No help available
		"""
		param = Conversions.decimal_value_to_str(no_of_antennas)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:TMODe:NOANtennas {param}')

	def clone(self) -> 'TmodeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TmodeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
