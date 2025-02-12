from manim import *

from manim_kodisc import *


class ParticleSimulationExample(Scene):
    def construct(self):
        sim = ParticleSimulation(n_particles=30, container_dimensions=(2, 2), particle_colors=[PURPLE, ORANGE, GREEN])
        sim.move_to(ORIGIN)
        self.add(sim)
        self.play(UpdateFromFunc(sim, lambda x: x.update_particles(1 / config.frame_rate)), run_time=10)