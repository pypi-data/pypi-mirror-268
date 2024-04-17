
from q1pulse.instrument import Q1Instrument

from init_pulsars import qcm0
from plot_util import plot_output

instrument = Q1Instrument('q1')
instrument.add_qcm(qcm0)
instrument.add_control('P1', qcm0.name, [2])
instrument.add_control('P2', qcm0.name, [3])

p = instrument.new_program('ramp')
p.repetitions = 2

P1 = p.P1
P2 = p.P2


P1.block_pulse(40, -0.25)
P1.ramp(160, 0.0, 0.5)
P1.block_pulse(40, 0.5)
P1.ramp(160, 0.5, 0.0)

p.wait(100)

p.describe()

p.compile(listing=True, annotate=True)

instrument.run_program(p)

plot_output([qcm0])
