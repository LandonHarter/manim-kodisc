# Particle Simulation

Particle simulation is a box containing n number of particles that bounce around the box. This is great for representing concepts like the ideal gas law or the kinetic theory of gases.

## Reference

```python
class ParticleSimulation(Group):
    def __init__(self, container_dimensions = (1, 1), n_particles=100, temp=273, particle_colors=[BLUE,WHITE,RED], **kwargs)
    def update_particles(self, dt = 1 / config.frame_rate)
    def set_temp(self, temp)
```

### Constructor
- `container_dimensions`: The dimensions of the container. This is a tuple of the form (width, height).
- `n_particles`: The number of particles in the container.
- `temp`: The temperature of the container in Kelvin.
- `particle_colors`: A list of colors to use for the particles.

### update_particles
- `dt`: The time step for the simulation. Automatically set to the inverse of the frame rate.

### set_temp
- `temp`: The new temperature of the container in Kelvin.

## Example

```python
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

        self.play(UpdateFromFunc(sim, lambda x: x.update_particles()), temp.animate.set_value(3000), run_time=10)
```