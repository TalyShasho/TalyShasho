# Base class: General Neuron
class Neuron:
    def __init__(self, firing_rate=0.0):
        self.firing_rate = firing_rate

    def activate(self, stimulus_strength):
        """Calculates firing rate based on stimulus strength."""
        self.firing_rate = stimulus_strength * 0.5  # Example calculation
        print(f"Neuron activated with firing rate: {self.firing_rate}")


# Intermediate class: Sensory Neuron
class SensoryNeuron(Neuron):
    def __init__(self, firing_rate=0.0, receptor_type=""):
        super().__init__(firing_rate)
        self.receptor_type = receptor_type

    def sense_stimulus(self, stimulus_strength):
        """Processes the specific stimulus it is sensitive to."""
        print(f"Sensing {self.receptor_type} stimulus with strength {stimulus_strength}")
        self.activate(stimulus_strength)


# Intermediate class: Motor Neuron
class MotorNeuron(Neuron):
    def __init__(self, firing_rate=0.0, target_muscle=""):
        super().__init__(firing_rate)
        self.target_muscle = target_muscle

    def control_muscle(self, activation_level):
        """Controls the target muscle based on activation level."""
        print(f"Controlling {self.target_muscle} with activation level: {activation_level}")
        self.firing_rate = activation_level


# Leaf class: Photoreceptor
class Photoreceptor(SensoryNeuron):
    def __init__(self, firing_rate=0.0):
        super().__init__(firing_rate, receptor_type="light")

    def detect_light(self, light_intensity):
        """Unique behavior for light detection."""
        print(f"Detecting light intensity: {light_intensity}")
        self.activate(light_intensity * 1.2)  # Enhanced sensitivity to light


# Leaf class: Mechanoreceptor
class Mechanoreceptor(SensoryNeuron):
    def __init__(self, firing_rate=0.0):
        super().__init__(firing_rate, receptor_type="pressure")

    def detect_pressure(self, pressure_level):
        """Unique behavior for pressure detection."""
        print(f"Detecting pressure level: {pressure_level}")
        self.activate(pressure_level * 0.8)  # Sensitivity to pressure


# Leaf class: Alpha Motor Neuron
class AlphaMotorNeuron(MotorNeuron):
    def __init__(self, firing_rate=0.0):
        super().__init__(firing_rate, target_muscle="skeletal muscle")

    def skeletal_muscle_control(self, activation_level):
        """Unique control for skeletal muscle."""
        print(f"Initiating rapid contraction for {self.target_muscle}")
        self.control_muscle(activation_level * 1.5)  # Strong rapid contractions


# Leaf class: Gamma Motor Neuron
class GammaMotorNeuron(MotorNeuron):
    def __init__(self, firing_rate=0.0):
        super().__init__(firing_rate, target_muscle="muscle spindle")

    def muscle_spindle_control(self, activation_level):
        """Unique control for muscle spindles."""
        print(f"Adjusting tension for {self.target_muscle}")
        self.control_muscle(activation_level * 0.7)  # Slower, gradual response

