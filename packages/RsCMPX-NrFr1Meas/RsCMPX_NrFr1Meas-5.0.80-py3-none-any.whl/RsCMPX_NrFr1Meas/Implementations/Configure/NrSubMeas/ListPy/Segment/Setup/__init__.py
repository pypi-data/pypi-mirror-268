from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SetupCls:
	"""Setup commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("setup", core, parent)

	@property
	def additional(self):
		"""additional commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_additional'):
			from .Additional import AdditionalCls
			self._additional = AdditionalCls(self._core, self._cmd_group)
		return self._additional

	# noinspection PyTypeChecker
	class SetupStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Segment_Length: int: Number of subframes in the segment
			- Level: float: Expected nominal power in the segment. The range can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the specifications document.
			- Duplex_Mode: enums.DuplexModeB: Duplex mode used in the segment
			- Band: enums.Band: TDD UL: OB34 | OB38 | ... | OB41 | OB46 | OB47 | OB48 | OB50 | OB51 | OB53 | OB77 | ... | OB84 | OB86 | OB89 | OB90 | OB95 | ... | OB99 | OB101 | OB104 Operating band used in the segment
			- Retrigger_Flag: enums.RetriggerFlag: Specifies whether the measurement waits for a trigger event before measuring the segment, or not. The retrigger flag is ignored for trigger mode ONCE and evaluated for trigger mode SEGMent, see [CMDLINKRESOLVED Trigger.NrSubMeas.ListPy#Mode CMDLINKRESOLVED].
				- OFF: Measure the segment without retrigger. For the first segment, the value OFF is interpreted as ON.
				- ON: Wait for a trigger event from the trigger source configured via TRIGger:NRSub:MEASi:MEValuation:SOURce.
				- IFPower: Wait for a trigger event from the trigger source IF Power.The trigger evaluation bandwidth is 160 MHz.
				- IFPNarrowband: Wait for a trigger event from the trigger source IF Power.The trigger evaluation bandwidth is configured via TRIGger:NRSub:MEASi:LIST:NBANdwidth.
			- Evaluat_Offset: int: Number of subframes at the beginning of the segment that are not evaluated
			- Network_Sig_Val: enums.NetworkSigVal: Optional setting parameter. Network signaled value to be used for the segment"""
		__meta_args_list = [
			ArgStruct.scalar_int('Segment_Length'),
			ArgStruct.scalar_float('Level'),
			ArgStruct.scalar_enum('Duplex_Mode', enums.DuplexModeB),
			ArgStruct.scalar_enum('Band', enums.Band),
			ArgStruct.scalar_enum('Retrigger_Flag', enums.RetriggerFlag),
			ArgStruct.scalar_int('Evaluat_Offset'),
			ArgStruct.scalar_enum_optional('Network_Sig_Val', enums.NetworkSigVal)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Segment_Length: int = None
			self.Level: float = None
			self.Duplex_Mode: enums.DuplexModeB = None
			self.Band: enums.Band = None
			self.Retrigger_Flag: enums.RetriggerFlag = None
			self.Evaluat_Offset: int = None
			self.Network_Sig_Val: enums.NetworkSigVal = None

	def set(self, structure: SetupStruct, sEGMent=repcap.SEGMent.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:LIST:SEGMent<no>:SETup \n
		Snippet with structure: \n
		structure = driver.configure.nrSubMeas.listPy.segment.setup.SetupStruct() \n
		structure.Segment_Length: int = 1 \n
		structure.Level: float = 1.0 \n
		structure.Duplex_Mode: enums.DuplexModeB = enums.DuplexModeB.FDD \n
		structure.Band: enums.Band = enums.Band.OB1 \n
		structure.Retrigger_Flag: enums.RetriggerFlag = enums.RetriggerFlag.IFPNarrowband \n
		structure.Evaluat_Offset: int = 1 \n
		structure.Network_Sig_Val: enums.NetworkSigVal = enums.NetworkSigVal.NS01 \n
		driver.configure.nrSubMeas.listPy.segment.setup.set(structure, sEGMent = repcap.SEGMent.Default) \n
		Defines the length and analyzer settings of segment <no>. For carrier-specific settings, there are additional commands.
		This command and the other segment configuration commands must be sent for all segments to be measured (method
		RsCMPX_NrFr1Meas.Configure.NrSubMeas.MultiEval.ListPy.Lrange.set) . \n
			:param structure: for set value, see the help for SetupStruct structure arguments.
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
		"""
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		self._core.io.write_struct(f'CONFigure:NRSub:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:SETup', structure)

	def get(self, sEGMent=repcap.SEGMent.Default) -> SetupStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:LIST:SEGMent<no>:SETup \n
		Snippet: value: SetupStruct = driver.configure.nrSubMeas.listPy.segment.setup.get(sEGMent = repcap.SEGMent.Default) \n
		Defines the length and analyzer settings of segment <no>. For carrier-specific settings, there are additional commands.
		This command and the other segment configuration commands must be sent for all segments to be measured (method
		RsCMPX_NrFr1Meas.Configure.NrSubMeas.MultiEval.ListPy.Lrange.set) . \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for SetupStruct structure arguments."""
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		return self._core.io.query_struct(f'CONFigure:NRSub:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:SETup?', self.__class__.SetupStruct())

	def clone(self) -> 'SetupCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SetupCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
