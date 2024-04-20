from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RbIndexCls:
	"""RbIndex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rbIndex", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Out_Of_Tolerance: int: Out of tolerance result, i.e. the percentage of measurement intervals of the statistic count for modulation measurements exceeding the specified modulation limits.
			- Rb_Index: int: Resource block index for the general margin (at non-allocated RBs)
			- Iq_Image: int: Resource block index for the I/Q image margin (at image frequencies of allocated RBs)
			- Carr_Leakage: int: Resource block index for the carrier leakage margin (at carrier frequency)"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_int('Rb_Index'),
			ArgStruct.scalar_int('Iq_Image'),
			ArgStruct.scalar_int('Carr_Leakage')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tolerance: int = None
			self.Rb_Index: int = None
			self.Iq_Image: int = None
			self.Carr_Leakage: int = None

	def fetch(self, carrierComponent=repcap.CarrierComponent.Default, layer=repcap.Layer.Default) -> FetchStruct:
		"""SCPI: FETCh:NRSub:MEASurement<Instance>:MEValuation[:CC<no>][:LAYer<layer>]:IEMission:MARGin:CURRent:RBINdex \n
		Snippet: value: FetchStruct = driver.nrSubMeas.multiEval.cc.layer.iemission.margin.current.rbIndex.fetch(carrierComponent = repcap.CarrierComponent.Default, layer = repcap.Layer.Default) \n
		Return resource block indices for in-band emission margins, for carrier <no>, layer/antenna <l>. At these RB indices, the
		CURRent, AVERage and EXTReme margins have been detected (see method RsCMPX_NrFr1Meas.NrSubMeas.MultiEval.Cc.Layer.
		Iemission.Margin.Current.fetch and ...:AVERage/EXTReme) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param layer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Layer')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		layer_cmd_val = self._cmd_group.get_repcap_cmd_value(layer, repcap.Layer)
		return self._core.io.query_struct(f'FETCh:NRSub:MEASurement<Instance>:MEValuation:CC{carrierComponent_cmd_val}:LAYer{layer_cmd_val}:IEMission:MARGin:CURRent:RBINdex?', self.__class__.FetchStruct())
