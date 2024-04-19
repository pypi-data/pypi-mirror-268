from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DftPrecodingCls:
	"""DftPrecoding commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dftPrecoding", core, parent)

	def set(self, bwp: enums.BandwidthPart, enable: bool, sEGMent=repcap.SEGMent.Default, carrierComponentExt=repcap.CarrierComponentExt.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>[:CC<carrier>]:BWPart:PUSCh:DFTPrecoding \n
		Snippet: driver.configure.nrMmwMeas.listPy.segment.cc.bwPart.pusch.dftPrecoding.set(bwp = enums.BandwidthPart.BWP0, enable = False, sEGMent = repcap.SEGMent.Default, carrierComponentExt = repcap.CarrierComponentExt.Default) \n
		Specifies whether the <BWP> on carrier <c> in segment <no> uses a transform precoding function. \n
			:param bwp: No help available
			:param enable: OFF: No transform precoding. ON: With transform precoding.
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('bwp', bwp, DataType.Enum, enums.BandwidthPart), ArgSingle('enable', enable, DataType.Boolean))
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:CC{carrierComponentExt_cmd_val}:BWPart:PUSCh:DFTPrecoding {param}'.rstrip())

	def get(self, bwp: enums.BandwidthPart, sEGMent=repcap.SEGMent.Default, carrierComponentExt=repcap.CarrierComponentExt.Default) -> bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>[:CC<carrier>]:BWPart:PUSCh:DFTPrecoding \n
		Snippet: value: bool = driver.configure.nrMmwMeas.listPy.segment.cc.bwPart.pusch.dftPrecoding.get(bwp = enums.BandwidthPart.BWP0, sEGMent = repcap.SEGMent.Default, carrierComponentExt = repcap.CarrierComponentExt.Default) \n
		Specifies whether the <BWP> on carrier <c> in segment <no> uses a transform precoding function. \n
			:param bwp: No help available
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: enable: OFF: No transform precoding. ON: With transform precoding."""
		param = Conversions.enum_scalar_to_str(bwp, enums.BandwidthPart)
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		response = self._core.io.query_str(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:CC{carrierComponentExt_cmd_val}:BWPart:PUSCh:DFTPrecoding? {param}')
		return Conversions.str_to_bool(response)
