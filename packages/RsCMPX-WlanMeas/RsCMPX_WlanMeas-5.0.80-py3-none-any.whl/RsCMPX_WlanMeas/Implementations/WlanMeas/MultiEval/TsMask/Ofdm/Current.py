from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


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
			- Margins_11_Ag: List[float]: No parameter help available
			- Margins_11_P: List[float]: No parameter help available
			- Margins_11_Parib: List[float]: No parameter help available
			- Out_Of_Tol: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Margins_11_Ag', DataType.FloatList, None, False, False, 8),
			ArgStruct('Margins_11_P', DataType.FloatList, None, False, False, 10),
			ArgStruct('Margins_11_Parib', DataType.FloatList, None, False, False, 4),
			ArgStruct.scalar_float('Out_Of_Tol')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Margins_11_Ag: List[float] = None
			self.Margins_11_P: List[float] = None
			self.Margins_11_Parib: List[float] = None
			self.Out_Of_Tol: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:TSMask:OFDM:CURRent \n
		Snippet: value: ResultData = driver.wlanMeas.multiEval.tsMask.ofdm.current.read() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WLAN:MEASurement<Instance>:MEValuation:TSMask:OFDM:CURRent?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:TSMask:OFDM:CURRent \n
		Snippet: value: ResultData = driver.wlanMeas.multiEval.tsMask.ofdm.current.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:TSMask:OFDM:CURRent?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Margins_11_Ag: List[enums.ResultStatus2]: No parameter help available
			- Margins_11_P: List[enums.ResultStatus2]: No parameter help available
			- Margins_11_Parib: List[float]: No parameter help available
			- Out_Of_Tol: enums.ResultStatus2: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Margins_11_Ag', DataType.EnumList, enums.ResultStatus2, False, False, 8),
			ArgStruct('Margins_11_P', DataType.EnumList, enums.ResultStatus2, False, False, 10),
			ArgStruct('Margins_11_Parib', DataType.FloatList, None, False, False, 4),
			ArgStruct.scalar_enum('Out_Of_Tol', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Margins_11_Ag: List[enums.ResultStatus2] = None
			self.Margins_11_P: List[enums.ResultStatus2] = None
			self.Margins_11_Parib: List[float] = None
			self.Out_Of_Tol: enums.ResultStatus2 = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:WLAN:MEASurement<Instance>:MEValuation:TSMask:OFDM:CURRent \n
		Snippet: value: CalculateStruct = driver.wlanMeas.multiEval.tsMask.ofdm.current.calculate() \n
		No command help available \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:TSMask:OFDM:CURRent?', self.__class__.CalculateStruct())
