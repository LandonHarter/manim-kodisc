from manim import *

from manim_kodisc import *


class ParticleSimulationExample(Scene):
    def construct(self):
        sim = ParticleSimulation(n_particles=100, container_dimensions=(6, 4))
        sim.move_to(ORIGIN)
        self.add(sim)
        self.play(UpdateFromFunc(sim, lambda x: x.update_particles()), run_time=10)