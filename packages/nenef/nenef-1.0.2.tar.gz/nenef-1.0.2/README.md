Для использования пакета создайте класс шаблона, принимающий для создания веса нейросети.
Пример:

    class MyNetwork:
        def __init__(self, weights=None):
            if weights is None:
                self.network = ForwardBlock(4, 'perc', (3, 9, 3, 1))
                self.weights = self.network.weights
            else:
                self.network = ForwardBlock(4, 'perc', (3, 9, 3, 1), weights=weights)
                self.weights = weights
    
        def do(self, param):
            return self.network.do(param)
Также определите функцию для определения успешности(фитнесс-функцию)
. Она должна возвращать массив с результатами для каждой нейросети в 1 испытании.
То есть при соревновании 2 нейросетей функция должна возвращать 2 значения. При обучении 1 нейросети
1 значение соответственно.

