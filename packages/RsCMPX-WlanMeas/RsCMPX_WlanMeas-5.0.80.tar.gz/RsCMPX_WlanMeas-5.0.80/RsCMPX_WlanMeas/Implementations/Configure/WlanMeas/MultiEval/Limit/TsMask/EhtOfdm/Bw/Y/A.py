from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ACls:
	"""A commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("a", core, parent)

	def set(self, tsm_lim_yrel_lev_a: float, bandwidthF=repcap.BandwidthF.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:EHTofdm:BW<bandwidth>:Y:A \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.tsMask.ehtOfdm.bw.y.a.set(tsm_lim_yrel_lev_a = 1.0, bandwidthF = repcap.BandwidthF.Default) \n
		Defines the relative spectral density limit for point A (frequency offset: 2*bandwidth) on the transmit spectrum mask for
		802.11be signals with the specified <bandwidth>. See 'Transmit spectrum mask OFDM, default masks' for background
		information. \n
			:param tsm_lim_yrel_lev_a: No help available
			:param bandwidthF: optional repeated capability selector. Default value: Bw20 (settable in the interface 'Bw')
		"""
		param = Conversions.decimal_value_to_str(tsm_lim_yrel_lev_a)
		bandwidthF_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthF, repcap.BandwidthF)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:EHTofdm:BW{bandwidthF_cmd_val}:Y:A {param}')

	def get(self, bandwidthF=repcap.BandwidthF.Default) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:EHTofdm:BW<bandwidth>:Y:A \n
		Snippet: value: float = driver.configure.wlanMeas.multiEval.limit.tsMask.ehtOfdm.bw.y.a.get(bandwidthF = repcap.BandwidthF.Default) \n
		Defines the relative spectral density limit for point A (frequency offset: 2*bandwidth) on the transmit spectrum mask for
		802.11be signals with the specified <bandwidth>. See 'Transmit spectrum mask OFDM, default masks' for background
		information. \n
			:param bandwidthF: optional repeated capability selector. Default value: Bw20 (settable in the interface 'Bw')
			:return: tsm_lim_yrel_lev_a: No help available"""
		bandwidthF_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthF, repcap.BandwidthF)
		response = self._core.io.query_str(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:EHTofdm:BW{bandwidthF_cmd_val}:Y:A?')
		return Conversions.str_to_float(response)
