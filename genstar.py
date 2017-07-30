# Copyright (c) 2017 Bart Massey

"""Generate a simulated EVE Online™ Project Discovery star
   luminance trace."""

from random import *
from math import *

samples_per_day = 144
days_per_trace = 26
instrument_noise_amplitude = 0.1

def gen_segment(nsegment,
                cycle_amplitude=None,
                cycle_period=None,
                cycle_phase=None,
                walk_amplitude=None):
    """Generate a segment of a simulated star luminance trace,
       consisting of segments with some combination of
       oscillation, random-walk noise and instrument
       noise. No attempt is made at this stage to do
       anything too fancy.
    """
    segment = []
    walk_state = 0.0
    for i in range(nsegment):
        s = gauss(0.0, 0.5) * instrument_noise_amplitude
        walk_state += gauss(0.0, 0.5) * walk_amplitude
        s += walk_state
        s += cos(2 * pi * (i + cycle_phase) / cycle_period) * cycle_amplitude
        segment.append(s)
    return segment

def gen_star():
    """Generate a simulated star luminance trace. The trace will
       have a mean of 0 and consist of samples in the range
       -1..1 or less.
    """
    cycle_period = int((0.1 + random() * 4.0) * samples_per_day)
    cycle_phase = randrange(int(cycle_period))
    cycle_amplitude = 0.0
    walk_amplitude = 0.0
    if random() < 0.3:
        cycle_amplitude = 0.01 + 0.1 * random()
    elif random() < 0.6:
        walk_amplitude = random() * 0.025
    # Calculate a trace as a series of segments.
    # Yes, this is left-biased. Meh.
    nsegments = max(1, int(gauss(0.5, 4.0)))
    nsamples = samples_per_day * days_per_trace
    samples = []
    while nsegments > 0:
        segment_max = nsamples - len(samples)
        if nsegments > 1:
            segment_bias = random() * 0.4 - 0.2
            nsegment = randrange(samples_per_day, segment_max)
        else:
            segment_bias = 0.0
            nsegment = segment_max
        segment = gen_segment(nsegment,
                              cycle_amplitude=cycle_amplitude,
                              cycle_period=cycle_period,
                              cycle_phase=cycle_phase,
                              walk_amplitude = walk_amplitude)
        samples += [s + segment_bias for s in segment]
        nsegments -= 1
    min_sample = samples[0]
    max_sample = samples[0]
    sum_samples = samples[0]
    for s in samples[1:]:
        min_sample = min(min_sample, s)
        max_sample = max(max_sample, s)
        sum_samples += s
    assert max_sample > min_sample
    scale = min(1.0, 1.0 / (max_sample - min_sample))
    bias = sum_samples / len(samples)
    return [(s - bias) * scale for s in samples]

if __name__ == '__main__':
    for s in gen_star():
        print(s)
