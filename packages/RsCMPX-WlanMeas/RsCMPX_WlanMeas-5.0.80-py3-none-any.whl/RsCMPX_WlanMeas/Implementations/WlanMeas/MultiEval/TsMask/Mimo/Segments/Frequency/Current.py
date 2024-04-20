from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Out_Of_Tol_Seg_1: float: No parameter help available
			- Out_Of_Tol_Seg_2: float: No parameter help available
			- Margin_Xvals_Seg_1_Tx: List[float]: No parameter help available
			- Margin_Xvals_Seg_2_Tx: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Out_Of_Tol_Seg_1'),
			ArgStruct.scalar_float('Out_Of_Tol_Seg_2'),
			ArgStruct('Margin_Xvals_Seg_1_Tx', DataType.FloatList, None, False, True, 1),
			ArgStruct('Margin_Xvals_Seg_2_Tx', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol_Seg_1: float = None
			self.Out_Of_Tol_Seg_2: float = None
			self.Margin_Xvals_Seg_1_Tx: List[float] = None
			self.Margin_Xvals_Seg_2_Tx: List[float] = None

	def read(self, mimo=repcap.Mimo.Default) -> ResultData:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:TSMask:MIMO<n>:SEGMents:FREQuency:CURRent \n
		Snippet: value: ResultData = driver.wlanMeas.multiEval.tsMask.mimo.segments.frequency.current.read(mimo = repcap.Mimo.Default) \n
		No command help available \n
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		return self._core.io.query_struct(f'READ:WLAN:MEASurement<Instance>:MEValuation:TSMask:MIMO{mimo_cmd_val}:SEGMents:FREQuency:CURRent?', self.__class__.ResultData())

	def fetch(self, mimo=repcap.Mimo.Default) -> ResultData:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:TSMask:MIMO<n>:SEGMents:FREQuency:CURRent \n
		Snippet: value: ResultData = driver.wlanMeas.multiEval.tsMask.mimo.segments.frequency.current.fetch(mimo = repcap.Mimo.Default) \n
		No command help available \n
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:TSMask:MIMO{mimo_cmd_val}:SEGMents:FREQuency:CURRent?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Out_Of_Tol_Seg_1: enums.ResultStatus2: No parameter help available
			- Out_Of_Tol_Seg_2: enums.ResultStatus2: No parameter help available
			- Margin_Xvals_Seg_1_Tx: List[enums.ResultStatus2]: No parameter help available
			- Margin_Xvals_Seg_2_Tx: List[enums.ResultStatus2]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Out_Of_Tol_Seg_1', enums.ResultStatus2),
			ArgStruct.scalar_enum('Out_Of_Tol_Seg_2', enums.ResultStatus2),
			ArgStruct('Margin_Xvals_Seg_1_Tx', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Margin_Xvals_Seg_2_Tx', DataType.EnumList, enums.ResultStatus2, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol_Seg_1: enums.ResultStatus2 = None
			self.Out_Of_Tol_Seg_2: enums.ResultStatus2 = None
			self.Margin_Xvals_Seg_1_Tx: List[enums.ResultStatus2] = None
			self.Margin_Xvals_Seg_2_Tx: List[enums.ResultStatus2] = None

	def calculate(self, mimo=repcap.Mimo.Default) -> CalculateStruct:
		"""SCPI: CALCulate:WLAN:MEASurement<Instance>:MEValuation:TSMask:MIMO<n>:SEGMents:FREQuency:CURRent \n
		Snippet: value: CalculateStruct = driver.wlanMeas.multiEval.tsMask.mimo.segments.frequency.current.calculate(mimo = repcap.Mimo.Default) \n
		No command help available \n
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		return self._core.io.query_struct(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:TSMask:MIMO{mimo_cmd_val}:SEGMents:FREQuency:CURRent?', self.__class__.CalculateStruct())
