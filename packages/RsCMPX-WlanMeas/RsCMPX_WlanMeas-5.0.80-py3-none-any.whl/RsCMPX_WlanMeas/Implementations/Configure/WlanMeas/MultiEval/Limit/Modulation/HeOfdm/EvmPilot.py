from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EvmPilotCls:
	"""EvmPilot commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("evmPilot", core, parent)

	def get_tb_high(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMPilot:TBHigh \n
		Snippet: value: float or bool = driver.configure.wlanMeas.multiEval.limit.modulation.heOfdm.evmPilot.get_tb_high() \n
		Sets EVM limits for a pilot subcarrier in 802.11ax trigger-based signals, when transmit power is larger than the maximum
		power of MCS 7. \n
			:return: evm_pilot: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMPilot:TBHigh?')
		return Conversions.str_to_float_or_bool(response)

	def set_tb_high(self, evm_pilot: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMPilot:TBHigh \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.modulation.heOfdm.evmPilot.set_tb_high(evm_pilot = 1.0) \n
		Sets EVM limits for a pilot subcarrier in 802.11ax trigger-based signals, when transmit power is larger than the maximum
		power of MCS 7. \n
			:param evm_pilot: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(evm_pilot)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMPilot:TBHigh {param}')

	def get_tb_low(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMPilot:TBLow \n
		Snippet: value: float or bool = driver.configure.wlanMeas.multiEval.limit.modulation.heOfdm.evmPilot.get_tb_low() \n
		Sets EVM limits for a pilot subcarrier in 802.11ax trigger-based signals, when transmit power is less than or equal to
		the maximum power of MCS 7. \n
			:return: evm_pilot: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMPilot:TBLow?')
		return Conversions.str_to_float_or_bool(response)

	def set_tb_low(self, evm_pilot: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMPilot:TBLow \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.modulation.heOfdm.evmPilot.set_tb_low(evm_pilot = 1.0) \n
		Sets EVM limits for a pilot subcarrier in 802.11ax trigger-based signals, when transmit power is less than or equal to
		the maximum power of MCS 7. \n
			:param evm_pilot: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(evm_pilot)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMPilot:TBLow {param}')

	def get_value(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMPilot \n
		Snippet: value: float or bool = driver.configure.wlanMeas.multiEval.limit.modulation.heOfdm.evmPilot.get_value() \n
		Defines and activates an upper limit for the error vector magnitude (EVM) of the pilot carriers in 802.11ax signals. \n
			:return: evm_pilot: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMPilot?')
		return Conversions.str_to_float_or_bool(response)

	def set_value(self, evm_pilot: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMPilot \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.modulation.heOfdm.evmPilot.set_value(evm_pilot = 1.0) \n
		Defines and activates an upper limit for the error vector magnitude (EVM) of the pilot carriers in 802.11ax signals. \n
			:param evm_pilot: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(evm_pilot)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:EVMPilot {param}')
