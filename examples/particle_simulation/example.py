from manim import *

from manim_kodisc import *


class ParticleSimulationExample(Scene):
    def construct(self):
        temp = ValueTracker(273)

        text = Text(f"Temperature: {round(temp.get_value())} K", font_size=24)
        text.to_corner(UL)
        text.add_updater(lambda x: x.become(Text(f"Temperature: {round(temp.get_value())} K", font_size=24).to_corner(UL)))
        self.add(text)

        sim = ParticleSimulation(n_particles=30, container_dimensions=(2, 2), temp=temp.get_value(), particle_colors=[PURPLE, ORANGE, GREEN])
        sim.move_to(ORIGIN)
        sim.add_updater(lambda x: x.set_temp(temp.get_value()))
        self.add(sim)

        self.play(UpdateFromFunc(sim, lambda x: x.update_particles(1 / config.frame_rate)), temp.animate.set_value(3000), run_time=10)