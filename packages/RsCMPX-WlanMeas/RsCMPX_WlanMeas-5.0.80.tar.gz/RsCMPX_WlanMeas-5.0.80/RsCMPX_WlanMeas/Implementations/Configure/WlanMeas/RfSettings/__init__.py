from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettingsCls:
	"""RfSettings commands group definition. 13 total commands, 6 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfSettings", core, parent)

	@property
	def antenna(self):
		"""antenna commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_antenna'):
			from .Antenna import AntennaCls
			self._antenna = AntennaCls(self._core, self._cmd_group)
		return self._antenna

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def envelopePower(self):
		"""envelopePower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_envelopePower'):
			from .EnvelopePower import EnvelopePowerCls
			self._envelopePower = EnvelopePowerCls(self._core, self._cmd_group)
		return self._envelopePower

	@property
	def eattenuation(self):
		"""eattenuation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eattenuation'):
			from .Eattenuation import EattenuationCls
			self._eattenuation = EattenuationCls(self._core, self._cmd_group)
		return self._eattenuation

	@property
	def umargin(self):
		"""umargin commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_umargin'):
			from .Umargin import UmarginCls
			self._umargin = UmarginCls(self._core, self._cmd_group)
		return self._umargin

	@property
	def lrStart(self):
		"""lrStart commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lrStart'):
			from .LrStart import LrStartCls
			self._lrStart = LrStartCls(self._core, self._cmd_group)
		return self._lrStart

	def get_santennas(self) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:RFSettings:SANTennas \n
		Snippet: value: bool = driver.configure.wlanMeas.rfSettings.get_santennas() \n
		No command help available \n
			:return: sep_ant: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:RFSettings:SANTennas?')
		return Conversions.str_to_bool(response)

	def set_santennas(self, sep_ant: bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:RFSettings:SANTennas \n
		Snippet: driver.configure.wlanMeas.rfSettings.set_santennas(sep_ant = False) \n
		No command help available \n
			:param sep_ant: No help available
		"""
		param = Conversions.bool_to_str(sep_ant)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:RFSettings:SANTennas {param}')

	def get_ml_offset(self) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:RFSettings:MLOFfset \n
		Snippet: value: float = driver.configure.wlanMeas.rfSettings.get_ml_offset() \n
		No command help available \n
			:return: ml_offset: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:RFSettings:MLOFfset?')
		return Conversions.str_to_float(response)

	def set_ml_offset(self, ml_offset: float) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:RFSettings:MLOFfset \n
		Snippet: driver.configure.wlanMeas.rfSettings.set_ml_offset(ml_offset = 1.0) \n
		No command help available \n
			:param ml_offset: No help available
		"""
		param = Conversions.decimal_value_to_str(ml_offset)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:RFSettings:MLOFfset {param}')

	def get_foffset(self) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:RFSettings:FOFFset \n
		Snippet: value: float = driver.configure.wlanMeas.rfSettings.get_foffset() \n
		No command help available \n
			:return: freq_offset: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:RFSettings:FOFFset?')
		return Conversions.str_to_float(response)

	def set_foffset(self, freq_offset: float) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:RFSettings:FOFFset \n
		Snippet: driver.configure.wlanMeas.rfSettings.set_foffset(freq_offset = 1.0) \n
		No command help available \n
			:param freq_offset: No help available
		"""
		param = Conversions.decimal_value_to_str(freq_offset)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:RFSettings:FOFFset {param}')

	def get_lr_interval(self) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:RFSettings:LRINterval \n
		Snippet: value: float = driver.configure.wlanMeas.rfSettings.get_lr_interval() \n
		Defines the measurement interval for level adjustment. \n
			:return: lvl_rang_interval: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:RFSettings:LRINterval?')
		return Conversions.str_to_float(response)

	def set_lr_interval(self, lvl_rang_interval: float) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:RFSettings:LRINterval \n
		Snippet: driver.configure.wlanMeas.rfSettings.set_lr_interval(lvl_rang_interval = 1.0) \n
		Defines the measurement interval for level adjustment. \n
			:param lvl_rang_interval: No help available
		"""
		param = Conversions.decimal_value_to_str(lvl_rang_interval)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:RFSettings:LRINterval {param}')

	def clone(self) -> 'RfSettingsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RfSettingsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
