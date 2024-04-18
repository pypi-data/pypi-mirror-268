from __init__ import json, np, random, randrange


def sigmoid(x: float) -> float:
    return 1 / (1 + np.exp(-x))


def line_function(x: float, k: float, b: float) -> float:
    return k * x + b


def tanh(x: float) -> float:
    return np.tanh(x)


def softmax(x: float) -> float:
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)


class Neuron:  # base neuron class to build
    """
    It is the base neuron class. If you want to create yourself net you should use this class to neurons.
    It is use ReLU function to activate neurons.
    """

    __slots__ = 'weights', 'bias'

    def __init__(self, weights: list or np.array, bias: float):
        self.weights = weights
        self.bias = bias

    def activate(self, params: list or tuple) -> float:
        total = np.dot(self.weights, params) + self.bias
        return max(0, total)


class BinaryNeuron(Neuron):
    """
    It is neuron, that use liminal activation.
    If S wi*xi > 0 => 1 | < 0 => -1 | == 0 => 0 (0 save last statement of neuron).
    It used in Hopfield networks and Boltzmann machines.
    """

    def activate(self, params: list or tuple) -> float:
        total = np.dot(self.weights, params) + self.bias
        if total > 0:
            return 1
        elif total < 0:
            return -1
        return 0


class LeakyReLUNeuron(Neuron):
    """
    It is Neuron that use Leaky ReLU activation. It is help to avoid death neurons in net.
    """

    def __init__(self, weights: list or np.array, bias: float, a: float):
        super().__init__(weights, bias)
        self.a = a

    def activate(self, params: list or tuple) -> float:
        total = np.dot(self.weights, params) + self.bias
        return max(self.a * total, total)


class SiLUNeuron(Neuron):
    """
    It is Neuron that use SiLU activation.
    It is slower than ReLU, but it used to avoid death neurons and explosions.
    """

    def activate(self, params: list or tuple) -> float:
        total = np.dot(self.weights, params) + self.bias
        return sigmoid(total) * total


class ELUNeuron(Neuron):
    """
    It is Neuron that use ELU activation. It is help to avoid death neurons.
    """

    def __init__(self, weights: list or np.array, bias: float, a: float):
        super().__init__(weights, bias)
        self.a = a

    def activate(self, params: list or tuple) -> float:
        total = np.dot(self.weights, params) + self.bias
        if total > 0:
            return total
        return (np.exp(total) - 1) * self.a


class LineNeuron(Neuron):
    """
    It is Neuron, that use line function to activate. You should use it to solve regressive problems
    """

    def __init__(self, weights: list or np.array, bias: float, k: float, b: float):
        super().__init__(weights, bias)
        self.k = k
        self.b = b

    def activate(self, params: list or tuple) -> float:  # activation function
        """Activation function"""
        total = np.dot(self.weights, params) + self.bias
        return line_function(total, self.k, self.b)


class SigmoidNeuron(Neuron):
    """
    It is Neuron, that use sigmoid function to activate.
    You should use it to classify on classes which count more 2
    """

    def activate(self, params: list or tuple) -> float:
        total = np.dot(self.weights, params) + self.bias
        return sigmoid(total)


class TanhNeuron(Neuron):
    """
    It is Neuron, that use hyperbolic tangens to activate. Uses same like sigmoid.
    """

    def activate(self, params: list or tuple) -> float:
        total = np.dot(self.weights, params) + self.bias
        return tanh(total)


class SoftMaxNeuron(Neuron):
    """
    It is Neuron, that use softmax function to activate. Uses same like sigmoid.
    """

    def activate(self, params: list or tuple) -> float:
        total = np.dot(self.weights, params) + self.bias
        return softmax(total)


NEURON_TYPES = {'base': Neuron, 'line': LineNeuron, 'sigm': SigmoidNeuron, 'tanh': TanhNeuron,
                'smax': SoftMaxNeuron, 'elu': ELUNeuron, 'silu': SiLUNeuron, 'lrel': LeakyReLUNeuron}


def generate_weights(size: int, before_size: int, can_be_negative=True, max_value=1) -> list:
    if can_be_negative:
        return [[random() * max_value * (int(random() * 2) * 2 - 1) for _ in range(before_size + 1)]
                for __ in range(size)]
    return [[random() * max_value for _ in range(before_size + 1)]
            for __ in range(size)]


class PerceptronSlice:
    def __init__(self, size: int, before_size: int, weights=None, type_of_neurons='base', **kwargs):
        self.size = size
        self.neuron_type = NEURON_TYPES[type_of_neurons]
        if weights is not None:
            self.weights = weights
            self.neurons = [self.neuron_type(weights[i][:-1], weights[i][-1], **kwargs) for i in range(size)]
        else:
            self.weights = np.array(generate_weights(size, before_size))
            self.neurons = [self.neuron_type(self.weights[i][:-1], self.weights[i][-1], **kwargs) for i in range(size)]

    def do_step(self, param: list) -> list:
        output = []
        for neuron in self.neurons:
            output.append(neuron.activate(param))
        return output

    def __len__(self):
        return self.size


class RecurrentNeuron:
    def __init__(self, weight1: float, weight2: float, bias: float):
        self.neuron = TanhNeuron((weight1, weight2), bias)

    def results(self, inputs: list or tuple):
        pref = inputs[0]
        output = []
        for x in inputs[1: -1]:
            pref = self.neuron.activate((pref, x))
            output.append(pref)
        return output


class LSTM:
    def __init__(self):
        pass


class RestrictedBoltzmannMachine:
    def __init__(self, size_first_slice, size_second_slice, weights=None, type_of_neurons='base'):
        pass


'''class HopfieldNetwork:
    def __init__(self, size):
        self.memories = []
        self.size = size
        self.neurons = []
        self.weights = np.zeros((size, size))

    def save_memory(self, instance):
        new_memory = np.zeros((self.size, self.size))
        for i in range(self.size):
            for j in range(self.size):
                if i != j:
                    new_memory[i][j] = instance[i] * instance[j]
        self.memories.append(new_memory)
        self.weights = self.weights + new_memory

    def update_neurons(self):
        self.neurons = [BinaryNeuron(self.weights[i], 0) for i in range(self.size)]

    def result(self, sample, sync=False):
        previous_step = sample
        step = copy.copy(previous_step)
        while True:
            for i in range(self.size):
                x = 0
                for j in range(self.size):
                    x += step[j] * self.weights[i][j]
                step[i] = x
            if previous_step == step:
                break
            previous_step = copy.copy(step)
        return step'''
TYPES_OF_SLICES = {'perc': PerceptronSlice, 'recc': RecurrentNeuron}


class ForwardBlock:
    """
    This is basic block. It can be used like perceptron.
    """

    def __init__(self, count_of_slices: int, type_of_slice: str, sizes_of_slices: tuple or list, weights=None):
        if weights is None:
            self.slices = [TYPES_OF_SLICES[type_of_slice](sizes_of_slices[i], sizes_of_slices[i - 1]) for i in
                           range(1, count_of_slices)]
            self.weights = [self.slices[i].weights for i in range(count_of_slices - 1)]
        else:
            self.slices = [TYPES_OF_SLICES[type_of_slice](sizes_of_slices[i], sizes_of_slices[i - 1], weights[i - 1])
                           for i in range(1, count_of_slices)]

    def do(self, param: list) -> list:
        for slice in self.slices:
            param = slice.do_step(param)
        return param


class RecursiveBlock(ForwardBlock):
    def do(self, param: list) -> list:
        step = param[0:self.slices[-1].size]
        dif = self.slices[0].size - self.slices[-1].size
        for i in range(dif - (len(param) % dif)):
            param.append(0)
        for i in range(self.slices[-1].size, len(param), dif):
            for slice in self.slices:
                step = slice.do_step(step)
            step.append(param[i:i + dif])
        return param


def take_index(numbers: list, max_num=True) -> int:
    if max_num:
        return numbers.index(max(numbers))
    return numbers.index(min(numbers))


class GeneticEducation:
    def __init__(self, template, population, ages, fitness_func, count_competition_in_age, competitive=True,
                 count_in_competition=2):
        self.population = [template() for _ in range(population)]
        self.template = template
        self.ages = ages
        self.fitness_func = fitness_func
        self.competitive = competitive
        self.number = [0] * population
        self.count = count_competition_in_age
        self.count_in_competition = count_in_competition
        self.size_of_population = population

    def educate(self):
        for _ in range(self.ages):
            if self.competitive:
                for i in range(self.count):
                    indexes = []
                    for _ in range(self.count_in_competition):
                        indexes.append(randrange(0, self.size_of_population))
                    result = self.fitness_func(*[self.population[indexes[j]] for j in range(self.count_in_competition)])
                    for j in range(self.count_in_competition):
                        self.number[indexes[j]] += result[j]
                i1 = take_index(self.number)
                i2 = take_index(self.number, max_num=False)
                self.population[i2] = self.template(self.population[i1].weights)
                for j in range(self.size_of_population):
                    self.population[j].weights = self.mutation(self.population[j].weights)
                    self.population[j] = self.template(self.population[j].weights)
                self.number = [0] * self.size_of_population
            else:
                pass
        for j in range(self.size_of_population):
            self.population[j].weights = self.mutation(self.population[j].weights, power=0)
        weights = [self.population[i].weights for i in range(len(self.population))]
        json.dump(weights, open('../../weights.json', 'w'))

    def mutation(self, weights, chance=0.2, power=0.03):
        if type(weights) is np.array or type(weights) is np.ndarray:
            weights = weights.tolist()
        if type(weights) is list or type(weights) is tuple:
            for i in range(len(weights)):
                weights[i] = self.mutation(weights[i], chance, power)
            return weights
        elif type(weights) is float or (type(weights) is int) or (type(weights) is np.float64) or \
                type(weights) is np.float16 or type(weights) is np.float32:
            if randrange(0, int(1 / chance)) == 0:
                weights += (random() - 0.5) * 2 * power
                return weights
            else:
                return weights
        else:
            return 0
