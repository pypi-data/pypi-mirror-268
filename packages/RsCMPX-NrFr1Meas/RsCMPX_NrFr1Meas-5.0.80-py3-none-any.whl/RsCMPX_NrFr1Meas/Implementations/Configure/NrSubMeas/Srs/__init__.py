from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SrsCls:
	"""Srs commands group definition. 30 total commands, 8 Subgroups, 9 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("srs", core, parent)

	@property
	def tcomb(self):
		"""tcomb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tcomb'):
			from .Tcomb import TcombCls
			self._tcomb = TcombCls(self._core, self._cmd_group)
		return self._tcomb

	@property
	def rmapping(self):
		"""rmapping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rmapping'):
			from .Rmapping import RmappingCls
			self._rmapping = RmappingCls(self._core, self._cmd_group)
		return self._rmapping

	@property
	def rtype(self):
		"""rtype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rtype'):
			from .Rtype import RtypeCls
			self._rtype = RtypeCls(self._core, self._cmd_group)
		return self._rtype

	@property
	def modulation(self):
		"""modulation commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import ModulationCls
			self._modulation = ModulationCls(self._core, self._cmd_group)
		return self._modulation

	@property
	def pdynamics(self):
		"""pdynamics commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pdynamics'):
			from .Pdynamics import PdynamicsCls
			self._pdynamics = PdynamicsCls(self._core, self._cmd_group)
		return self._pdynamics

	@property
	def scount(self):
		"""scount commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_scount'):
			from .Scount import ScountCls
			self._scount = ScountCls(self._core, self._cmd_group)
		return self._scount

	@property
	def result(self):
		"""result commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_result'):
			from .Result import ResultCls
			self._result = ResultCls(self._core, self._cmd_group)
		return self._result

	@property
	def limit(self):
		"""limit commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import LimitCls
			self._limit = LimitCls(self._core, self._cmd_group)
		return self._limit

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:TOUT \n
		Snippet: value: float = driver.configure.nrSubMeas.srs.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually. When the measurement has completed the first measurement
		cycle (first single shot) , the statistical depth is reached and the timer is reset. If the first measurement cycle has
		not been completed when the timer expires, the measurement is stopped. The measurement state changes to RDY.
		The reliability indicator is set to 1, indicating that a measurement timeout occurred. Still running READ, FETCh or
		CALCulate commands are completed, returning the available results. At least for some results, there are no values at all
		or the statistical depth has not been reached. A timeout of 0 s corresponds to an infinite measurement timeout. \n
			:return: timeout: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:SRS:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:TOUT \n
		Snippet: driver.configure.nrSubMeas.srs.set_timeout(timeout = 1.0) \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually. When the measurement has completed the first measurement
		cycle (first single shot) , the statistical depth is reached and the timer is reset. If the first measurement cycle has
		not been completed when the timer expires, the measurement is stopped. The measurement state changes to RDY.
		The reliability indicator is set to 1, indicating that a measurement timeout occurred. Still running READ, FETCh or
		CALCulate commands are completed, returning the available results. At least for some results, there are no values at all
		or the statistical depth has not been reached. A timeout of 0 s corresponds to an infinite measurement timeout. \n
			:param timeout: No help available
		"""
		param = Conversions.decimal_value_to_str(timeout)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:SRS:TOUT {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.nrSubMeas.srs.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:return: repetition: SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:SRS:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:REPetition \n
		Snippet: driver.configure.nrSubMeas.srs.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:param repetition: SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:SRS:REPetition {param}')

	# noinspection PyTypeChecker
	def get_scondition(self) -> enums.StopCondition:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:SCONdition \n
		Snippet: value: enums.StopCondition = driver.configure.nrSubMeas.srs.get_scondition() \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:return: stop_condition: NONE: Continue measurement irrespective of the limit check. SLFail: Stop measurement on limit failure.
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:SRS:SCONdition?')
		return Conversions.str_to_scalar_enum(response, enums.StopCondition)

	def set_scondition(self, stop_condition: enums.StopCondition) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:SCONdition \n
		Snippet: driver.configure.nrSubMeas.srs.set_scondition(stop_condition = enums.StopCondition.NONE) \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:param stop_condition: NONE: Continue measurement irrespective of the limit check. SLFail: Stop measurement on limit failure.
		"""
		param = Conversions.enum_scalar_to_str(stop_condition, enums.StopCondition)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:SRS:SCONdition {param}')

	def get_mo_exception(self) -> bool:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:MOEXception \n
		Snippet: value: bool = driver.configure.nrSubMeas.srs.get_mo_exception() \n
		Specifies whether measurement results that the CMP180 identifies as faulty or inaccurate are rejected. \n
			:return: meas_on_exception: OFF: Faulty results are rejected. ON: Results are never rejected.
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:SRS:MOEXception?')
		return Conversions.str_to_bool(response)

	def set_mo_exception(self, meas_on_exception: bool) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:MOEXception \n
		Snippet: driver.configure.nrSubMeas.srs.set_mo_exception(meas_on_exception = False) \n
		Specifies whether measurement results that the CMP180 identifies as faulty or inaccurate are rejected. \n
			:param meas_on_exception: OFF: Faulty results are rejected. ON: Results are never rejected.
		"""
		param = Conversions.bool_to_str(meas_on_exception)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:SRS:MOEXception {param}')

	def get_sequence(self) -> int:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:SEQuence \n
		Snippet: value: int = driver.configure.nrSubMeas.srs.get_sequence() \n
		No command help available \n
			:return: sequence_id: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:SRS:SEQuence?')
		return Conversions.str_to_int(response)

	def set_sequence(self, sequence_id: int) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:SEQuence \n
		Snippet: driver.configure.nrSubMeas.srs.set_sequence(sequence_id = 1) \n
		No command help available \n
			:param sequence_id: No help available
		"""
		param = Conversions.decimal_value_to_str(sequence_id)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:SRS:SEQuence {param}')

	def get_sposition(self) -> int:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:SPOSition \n
		Snippet: value: int = driver.configure.nrSubMeas.srs.get_sposition() \n
		No command help available \n
			:return: start_position: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:SRS:SPOSition?')
		return Conversions.str_to_int(response)

	def set_sposition(self, start_position: int) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:SPOSition \n
		Snippet: driver.configure.nrSubMeas.srs.set_sposition(start_position = 1) \n
		No command help available \n
			:param start_position: No help available
		"""
		param = Conversions.decimal_value_to_str(start_position)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:SRS:SPOSition {param}')

	# noinspection PyTypeChecker
	def get_no_symbols(self) -> enums.NumberSymbols:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:NOSYmbols \n
		Snippet: value: enums.NumberSymbols = driver.configure.nrSubMeas.srs.get_no_symbols() \n
		No command help available \n
			:return: number_symbols: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:SRS:NOSYmbols?')
		return Conversions.str_to_scalar_enum(response, enums.NumberSymbols)

	def set_no_symbols(self, number_symbols: enums.NumberSymbols) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:NOSYmbols \n
		Snippet: driver.configure.nrSubMeas.srs.set_no_symbols(number_symbols = enums.NumberSymbols.N1) \n
		No command help available \n
			:param number_symbols: No help available
		"""
		param = Conversions.enum_scalar_to_str(number_symbols, enums.NumberSymbols)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:SRS:NOSYmbols {param}')

	# noinspection PyTypeChecker
	def get_periodicity(self) -> enums.SrsPeriodicity:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:PERiodicity \n
		Snippet: value: enums.SrsPeriodicity = driver.configure.nrSubMeas.srs.get_periodicity() \n
		Configures the periodicity of the SRS transmissions in slots. \n
			:return: periodicity: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:SRS:PERiodicity?')
		return Conversions.str_to_scalar_enum(response, enums.SrsPeriodicity)

	def set_periodicity(self, periodicity: enums.SrsPeriodicity) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:PERiodicity \n
		Snippet: driver.configure.nrSubMeas.srs.set_periodicity(periodicity = enums.SrsPeriodicity.SL1) \n
		Configures the periodicity of the SRS transmissions in slots. \n
			:param periodicity: No help available
		"""
		param = Conversions.enum_scalar_to_str(periodicity, enums.SrsPeriodicity)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:SRS:PERiodicity {param}')

	def get_no_sub_frames(self) -> int:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:NOSubframes \n
		Snippet: value: int = driver.configure.nrSubMeas.srs.get_no_sub_frames() \n
		Configures the number of subframes captured for the power vs symbol result diagram. \n
			:return: number_subframes: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:SRS:NOSubframes?')
		return Conversions.str_to_int(response)

	def set_no_sub_frames(self, number_subframes: int) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:NOSubframes \n
		Snippet: driver.configure.nrSubMeas.srs.set_no_sub_frames(number_subframes = 1) \n
		Configures the number of subframes captured for the power vs symbol result diagram. \n
			:param number_subframes: No help available
		"""
		param = Conversions.decimal_value_to_str(number_subframes)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:SRS:NOSubframes {param}')

	def clone(self) -> 'SrsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SrsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
