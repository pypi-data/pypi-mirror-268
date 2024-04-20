from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	# noinspection PyTypeChecker
	class ReadStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: str: No parameter help available
			- Ab_Aver: float: No parameter help available
			- Cd_Aver: float: No parameter help available
			- Dc_Aver: float: No parameter help available
			- Ba_Aver: float: No parameter help available
			- Out_Of_Tol: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_raw_str('Reliability'),
			ArgStruct.scalar_float('Ab_Aver'),
			ArgStruct.scalar_float('Cd_Aver'),
			ArgStruct.scalar_float('Dc_Aver'),
			ArgStruct.scalar_float('Ba_Aver'),
			ArgStruct.scalar_float('Out_Of_Tol')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: str = None
			self.Ab_Aver: float = None
			self.Cd_Aver: float = None
			self.Dc_Aver: float = None
			self.Ba_Aver: float = None
			self.Out_Of_Tol: float = None

	def read(self) -> ReadStruct:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:TSMask:DSSS:AVERage \n
		Snippet: value: ReadStruct = driver.wlanMeas.multiEval.tsMask.dsss.average.read() \n
		No command help available \n
			:return: structure: for return value, see the help for ReadStruct structure arguments."""
		return self._core.io.query_struct(f'READ:WLAN:MEASurement<Instance>:MEValuation:TSMask:DSSS:AVERage?', self.__class__.ReadStruct())

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Ab_Aver: float: No parameter help available
			- Cd_Aver: float: No parameter help available
			- Dc_Aver: float: No parameter help available
			- Ba_Aver: float: No parameter help available
			- Out_Of_Tol: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Ab_Aver'),
			ArgStruct.scalar_float('Cd_Aver'),
			ArgStruct.scalar_float('Dc_Aver'),
			ArgStruct.scalar_float('Ba_Aver'),
			ArgStruct.scalar_float('Out_Of_Tol')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ab_Aver: float = None
			self.Cd_Aver: float = None
			self.Dc_Aver: float = None
			self.Ba_Aver: float = None
			self.Out_Of_Tol: float = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:TSMask:DSSS:AVERage \n
		Snippet: value: FetchStruct = driver.wlanMeas.multiEval.tsMask.dsss.average.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:TSMask:DSSS:AVERage?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Ab_Aver: enums.ResultStatus2: No parameter help available
			- Cd_Aver: enums.ResultStatus2: No parameter help available
			- Dc_Aver: enums.ResultStatus2: No parameter help available
			- Ba_Aver: enums.ResultStatus2: No parameter help available
			- Out_Of_Tol: enums.ResultStatus2: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Ab_Aver', enums.ResultStatus2),
			ArgStruct.scalar_enum('Cd_Aver', enums.ResultStatus2),
			ArgStruct.scalar_enum('Dc_Aver', enums.ResultStatus2),
			ArgStruct.scalar_enum('Ba_Aver', enums.ResultStatus2),
			ArgStruct.scalar_enum('Out_Of_Tol', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ab_Aver: enums.ResultStatus2 = None
			self.Cd_Aver: enums.ResultStatus2 = None
			self.Dc_Aver: enums.ResultStatus2 = None
			self.Ba_Aver: enums.ResultStatus2 = None
			self.Out_Of_Tol: enums.ResultStatus2 = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:WLAN:MEASurement<Instance>:MEValuation:TSMask:DSSS:AVERage \n
		Snippet: value: CalculateStruct = driver.wlanMeas.multiEval.tsMask.dsss.average.calculate() \n
		No command help available \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:TSMask:DSSS:AVERage?', self.__class__.CalculateStruct())
