from q1pulse.instrument import Q1Instrument
import numpy as np

from init_pulsars import qcm0
from plot_util import plot_output

instrument = Q1Instrument('q1')
instrument.add_qcm(qcm0)

instrument.add_control('q1', qcm0.name, [2,3], nco_frequency=0e6)

instrument.add_control('P1', qcm0.name, [1])

p = instrument.new_program('long_chirp')

P1 = p.P1

P1.block_pulse(100, 0.5)
p.wait(100)
#add_long_chirp(10000, -10e6, 10e6, 0.5, p.q1)

N = 250
f_start = 8e6
f_step = -2*f_start/(N-1)
amplitude = 0.5
n_samples = 16

seq = p.q1
waves = []
for i in range(N//2):
    t = np.arange(n_samples) * 1e-9
    f = f_start + i * f_step
    phase = 2*np.pi * f * t
    wave0 = seq.add_wave(f'chirp_I{i}', np.sin(phase))
    wave1 = seq.add_wave(f'chirp_Q{i}', np.cos(phase))
    waves.append((wave0, wave1))


seq.set_gain(amplitude, amplitude)
for i in range(N//2):
    f = f_start + i * f_step
    phase_step = (2 * f * n_samples * 1e-9 + 1) % 2 -1
    wave0, wave1 = waves[i]
    seq.shaped_pulse(wave0, None, wave1, None)
    with seq._seq_repeat(1):
        seq.shift_phase(-phase_step)
        seq.shaped_pulse(wave0, None, wave1, None)
        seq.shift_phase(-phase_step)
        seq.shaped_pulse(wave0, None, wave1, None)
        seq.shift_phase(-phase_step)
        seq.shaped_pulse(wave0, None, wave1, None)
    seq.shift_phase(-phase_step)

# add 180 degrees phase shift, include last phase_step (it will be overwritten...)
seq.shift_phase(-phase_step % 2 -1)
# invert Q
seq.set_gain(amplitude, -amplitude)
for i in range(N//2):
    j = i + N//2
    f = f_start + j * f_step
    phase_step = (2 * f * n_samples * 1e-9 + 1) % 2 -1
    wave0, wave1 = waves[N//2-1-i]
    seq.shaped_pulse(wave0, None, wave1, None)
    with seq._seq_repeat(1):
        seq.shift_phase(-phase_step)
        seq.shaped_pulse(wave0, None, wave1, None)
        seq.shift_phase(-phase_step)
        seq.shaped_pulse(wave0, None, wave1, None)
        seq.shift_phase(-phase_step)
        seq.shaped_pulse(wave0, None, wave1, None)
    seq.shift_phase(-phase_step)

p.compile(listing=True, annotate=False)

instrument.run_program(p)

plot_output([qcm0])

#import math
#
#for i in range(8,50):
#    t = 1024*i + 16
#    n12 = math.floor(t/12)
#    rep12 = math.ceil(n12/1024)
#    m12 = n12//rep12
#
#    n16 = math.floor(t/16)
#    rep16 = math.ceil(n16/1024)
#    m16 = n16//rep16
#
#    print(f'{t}, 12:{rep12},{m12:4} 16:{rep16},{m16:4}; {max(m12,m16)}')
#
