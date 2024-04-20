from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LowerCls:
	"""Lower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lower", core, parent)

	def set(self, center: float, side: float, bandwidthE=repcap.BandwidthE.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:VHTofdm:BW<bandwidth>:LOWer \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.spectrFlatness.vhtOfdm.bw.lower.set(center = 1.0, side = 1.0, bandwidthE = repcap.BandwidthE.Default) \n
		Defines lower limits for the spectrum flatness of the center subcarriers and the side subcarriers for 802.11ac signals
		with the specified <bandwidth>. The lower limits must be smaller than the upper limit. \n
			:param center: No help available
			:param side: No help available
			:param bandwidthE: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('center', center, DataType.Float), ArgSingle('side', side, DataType.Float))
		bandwidthE_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthE, repcap.BandwidthE)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:VHTofdm:BW{bandwidthE_cmd_val}:LOWer {param}'.rstrip())

	# noinspection PyTypeChecker
	class LowerStruct(StructBase):
		"""Response structure. Fields: \n
			- Center: float: No parameter help available
			- Side: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Center'),
			ArgStruct.scalar_float('Side')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Center: float = None
			self.Side: float = None

	def get(self, bandwidthE=repcap.BandwidthE.Default) -> LowerStruct:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:VHTofdm:BW<bandwidth>:LOWer \n
		Snippet: value: LowerStruct = driver.configure.wlanMeas.multiEval.limit.spectrFlatness.vhtOfdm.bw.lower.get(bandwidthE = repcap.BandwidthE.Default) \n
		Defines lower limits for the spectrum flatness of the center subcarriers and the side subcarriers for 802.11ac signals
		with the specified <bandwidth>. The lower limits must be smaller than the upper limit. \n
			:param bandwidthE: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
			:return: structure: for return value, see the help for LowerStruct structure arguments."""
		bandwidthE_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthE, repcap.BandwidthE)
		return self._core.io.query_struct(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:VHTofdm:BW{bandwidthE_cmd_val}:LOWer?', self.__class__.LowerStruct())
