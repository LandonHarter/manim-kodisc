from manim import *


class ParticleSimulation(Group):
    def __init__(self, container_dimensions = (1, 1), n_particles=100, temp=273, particle_colors=[BLUE,WHITE,RED], **kwargs):
        super().__init__(**kwargs)
        self.container_dimensions = container_dimensions
        self.container = Rectangle(width=container_dimensions[0] + 0.2, height=container_dimensions[1] + 0.2, stroke_width=1)
        self.container.shift(RIGHT * 0.5 + UP * 0.5)
        self.add(self.container)

        self.particles = []
        self.temp = temp
        for i in range(n_particles):
            col = particle_colors[i % len(particle_colors)]
            particle = Dot(radius=0.05, color=col)
            pos = np.array([np.random.rand() * container_dimensions[0], np.random.rand() * container_dimensions[1], 0])
            particle.move_to(pos)
            self.particles.append({
                "particle": particle,
                "pos": pos,
                "velocity": [np.random.rand() for _ in range(2)]
            })
            self.add(particle)

    def update_particles(self, dt = 1 / config.frame_rate):
        for particle in self.particles:
            pos = particle["pos"]
            velocity = particle["velocity"]
            for i in range(2):
                pos[i] += velocity[i] * dt * (self.temp / 273 /2)
                if pos[i] < 0 or pos[i] > self.container_dimensions[i]:
                    velocity[i] *= -1
            particle["pos"] = pos
            particle["velocity"] = velocity
            particle["particle"].move_to(np.array([pos[0] + (self.container.get_center()[0] - (self.container_dimensions[0] / 2)), pos[1] + (self.container.get_center()[1] - (self.container_dimensions[1] / 2)), 0]))

    def set_temp(self, temp):
        self.temp = temp