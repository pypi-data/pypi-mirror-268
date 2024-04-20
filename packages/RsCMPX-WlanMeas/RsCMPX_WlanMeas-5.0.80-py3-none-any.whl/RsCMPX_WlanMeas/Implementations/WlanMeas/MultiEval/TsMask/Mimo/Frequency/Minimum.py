from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MinimumCls:
	"""Minimum commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Out_Of_Tol: float: Out of tolerance result, i.e. the percentage of measurement intervals of the statistic count for spectrum emission measurements exceeding the specified transmit spectrum mask limits.
			- Margin_Xvals_Tx: List[float]: Comma-separated list of frequencies, one value per margin The number of margins equals the number of spectrum mask areas and depends on the selected standard, see Table 'Spectrum mask areas'."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Out_Of_Tol'),
			ArgStruct('Margin_Xvals_Tx', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol: float = None
			self.Margin_Xvals_Tx: List[float] = None

	def read(self, mimo=repcap.Mimo.Default) -> ResultData:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:TSMask:MIMO<n>:FREQuency:MINimum \n
		Snippet: value: ResultData = driver.wlanMeas.multiEval.tsMask.mimo.frequency.minimum.read(mimo = repcap.Mimo.Default) \n
		Return the X-positions of the limit line margins of the transmit spectrum mask, for MIMO measurements, antenna <n>,
		bandwidths > 160 MHz. The results are available for the left 160 MHz segment <1> and for the right 160 MHz segment <2>.
		The values described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead,
		one value for each result listed below. \n
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		return self._core.io.query_struct(f'READ:WLAN:MEASurement<Instance>:MEValuation:TSMask:MIMO{mimo_cmd_val}:FREQuency:MINimum?', self.__class__.ResultData())

	def fetch(self, mimo=repcap.Mimo.Default) -> ResultData:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:TSMask:MIMO<n>:FREQuency:MINimum \n
		Snippet: value: ResultData = driver.wlanMeas.multiEval.tsMask.mimo.frequency.minimum.fetch(mimo = repcap.Mimo.Default) \n
		Return the X-positions of the limit line margins of the transmit spectrum mask, for MIMO measurements, antenna <n>,
		bandwidths > 160 MHz. The results are available for the left 160 MHz segment <1> and for the right 160 MHz segment <2>.
		The values described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead,
		one value for each result listed below. \n
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:TSMask:MIMO{mimo_cmd_val}:FREQuency:MINimum?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Out_Of_Tol: enums.ResultStatus2: Out of tolerance result, i.e. the percentage of measurement intervals of the statistic count for spectrum emission measurements exceeding the specified transmit spectrum mask limits.
			- Margin_Xvals_Tx: List[enums.ResultStatus2]: Comma-separated list of frequencies, one value per margin The number of margins equals the number of spectrum mask areas and depends on the selected standard, see Table 'Spectrum mask areas'."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Out_Of_Tol', enums.ResultStatus2),
			ArgStruct('Margin_Xvals_Tx', DataType.EnumList, enums.ResultStatus2, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol: enums.ResultStatus2 = None
			self.Margin_Xvals_Tx: List[enums.ResultStatus2] = None

	def calculate(self, mimo=repcap.Mimo.Default) -> CalculateStruct:
		"""SCPI: CALCulate:WLAN:MEASurement<Instance>:MEValuation:TSMask:MIMO<n>:FREQuency:MINimum \n
		Snippet: value: CalculateStruct = driver.wlanMeas.multiEval.tsMask.mimo.frequency.minimum.calculate(mimo = repcap.Mimo.Default) \n
		Return the X-positions of the limit line margins of the transmit spectrum mask, for MIMO measurements, antenna <n>,
		bandwidths > 160 MHz. The results are available for the left 160 MHz segment <1> and for the right 160 MHz segment <2>.
		The values described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead,
		one value for each result listed below. \n
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		return self._core.io.query_struct(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:TSMask:MIMO{mimo_cmd_val}:FREQuency:MINimum?', self.__class__.CalculateStruct())
