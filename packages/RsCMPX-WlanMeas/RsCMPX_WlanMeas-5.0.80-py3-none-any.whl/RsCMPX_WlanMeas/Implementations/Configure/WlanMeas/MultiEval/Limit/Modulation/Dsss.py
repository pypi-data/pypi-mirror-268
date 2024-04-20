from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DsssCls:
	"""Dsss commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dsss", core, parent)

	def get_evm_ems(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:DSSS:EVMRms \n
		Snippet: value: float or bool = driver.configure.wlanMeas.multiEval.limit.modulation.dsss.get_evm_ems() \n
		Defines and activates upper limits for the error vector magnitude (EVM) RMS values of the data carriers (transmission
		scheme DSSS) . \n
			:return: evm_rms: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:DSSS:EVMRms?')
		return Conversions.str_to_float_or_bool(response)

	def set_evm_ems(self, evm_rms: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:DSSS:EVMRms \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.modulation.dsss.set_evm_ems(evm_rms = 1.0) \n
		Defines and activates upper limits for the error vector magnitude (EVM) RMS values of the data carriers (transmission
		scheme DSSS) . \n
			:param evm_rms: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(evm_rms)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:DSSS:EVMRms {param}')

	def get_evm_peak(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:DSSS:EVMPeak \n
		Snippet: value: float or bool = driver.configure.wlanMeas.multiEval.limit.modulation.dsss.get_evm_peak() \n
		Defines and activates upper limits for the error vector magnitude (EVM) peak values of the data carriers (transmission
		scheme DSSS) . \n
			:return: evm_peak: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:DSSS:EVMPeak?')
		return Conversions.str_to_float_or_bool(response)

	def set_evm_peak(self, evm_peak: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:DSSS:EVMPeak \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.modulation.dsss.set_evm_peak(evm_peak = 1.0) \n
		Defines and activates upper limits for the error vector magnitude (EVM) peak values of the data carriers (transmission
		scheme DSSS) . \n
			:param evm_peak: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(evm_peak)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:DSSS:EVMPeak {param}')

	def get_iq_offset(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:DSSS:IQOFfset \n
		Snippet: value: float or bool = driver.configure.wlanMeas.multiEval.limit.modulation.dsss.get_iq_offset() \n
		Defines and activates an upper limit for the I/Q origin offset (transmission scheme DSSS) . \n
			:return: iq_offset: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:DSSS:IQOFfset?')
		return Conversions.str_to_float_or_bool(response)

	def set_iq_offset(self, iq_offset: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:DSSS:IQOFfset \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.modulation.dsss.set_iq_offset(iq_offset = 1.0) \n
		Defines and activates an upper limit for the I/Q origin offset (transmission scheme DSSS) . \n
			:param iq_offset: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(iq_offset)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:DSSS:IQOFfset {param}')

	def get_cf_error(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:DSSS:CFERror \n
		Snippet: value: float or bool = driver.configure.wlanMeas.multiEval.limit.modulation.dsss.get_cf_error() \n
		Defines and activates an upper limit for the center frequency error (transmission scheme DSSS) . \n
			:return: freq_error: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:DSSS:CFERror?')
		return Conversions.str_to_float_or_bool(response)

	def set_cf_error(self, freq_error: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:DSSS:CFERror \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.modulation.dsss.set_cf_error(freq_error = 1.0) \n
		Defines and activates an upper limit for the center frequency error (transmission scheme DSSS) . \n
			:param freq_error: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(freq_error)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:DSSS:CFERror {param}')

	def get_cc_error(self) -> float or bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:DSSS:CCERror \n
		Snippet: value: float or bool = driver.configure.wlanMeas.multiEval.limit.modulation.dsss.get_cc_error() \n
		Defines and activates an upper limit for the chip clock error (transmission scheme DSSS) . \n
			:return: clock_error: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:DSSS:CCERror?')
		return Conversions.str_to_float_or_bool(response)

	def set_cc_error(self, clock_error: float or bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:DSSS:CCERror \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.modulation.dsss.set_cc_error(clock_error = 1.0) \n
		Defines and activates an upper limit for the chip clock error (transmission scheme DSSS) . \n
			:param clock_error: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(clock_error)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:DSSS:CCERror {param}')
