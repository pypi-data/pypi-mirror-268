from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TrackingCls:
	"""Tracking commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tracking", core, parent)

	def get_phase(self) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:TRACking:PHASe \n
		Snippet: value: bool = driver.configure.wlanMeas.multiEval.compensation.tracking.get_phase() \n
		Activate or deactivate phase tracking. With enabled tracking, fluctuations are compensated. \n
			:return: phase: OFF: Tracking disabled ON: Tracking enabled
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:TRACking:PHASe?')
		return Conversions.str_to_bool(response)

	def set_phase(self, phase: bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:TRACking:PHASe \n
		Snippet: driver.configure.wlanMeas.multiEval.compensation.tracking.set_phase(phase = False) \n
		Activate or deactivate phase tracking. With enabled tracking, fluctuations are compensated. \n
			:param phase: OFF: Tracking disabled ON: Tracking enabled
		"""
		param = Conversions.bool_to_str(phase)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:TRACking:PHASe {param}')

	def get_timing(self) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:TRACking:TIMing \n
		Snippet: value: bool = driver.configure.wlanMeas.multiEval.compensation.tracking.get_timing() \n
		Activate or deactivate timing tracking. With enabled tracking, fluctuations are compensated. \n
			:return: timing: OFF: Tracking disabled ON: Tracking enabled
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:TRACking:TIMing?')
		return Conversions.str_to_bool(response)

	def set_timing(self, timing: bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:TRACking:TIMing \n
		Snippet: driver.configure.wlanMeas.multiEval.compensation.tracking.set_timing(timing = False) \n
		Activate or deactivate timing tracking. With enabled tracking, fluctuations are compensated. \n
			:param timing: OFF: Tracking disabled ON: Tracking enabled
		"""
		param = Conversions.bool_to_str(timing)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:TRACking:TIMing {param}')

	def get_level(self) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:TRACking:LEVel \n
		Snippet: value: bool = driver.configure.wlanMeas.multiEval.compensation.tracking.get_level() \n
		Activate or deactivate level tracking. With enabled tracking, fluctuations are compensated. \n
			:return: level: OFF: Tracking disabled ON: Tracking enabled
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:TRACking:LEVel?')
		return Conversions.str_to_bool(response)

	def set_level(self, level: bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:TRACking:LEVel \n
		Snippet: driver.configure.wlanMeas.multiEval.compensation.tracking.set_level(level = False) \n
		Activate or deactivate level tracking. With enabled tracking, fluctuations are compensated. \n
			:param level: OFF: Tracking disabled ON: Tracking enabled
		"""
		param = Conversions.bool_to_str(level)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:TRACking:LEVel {param}')
