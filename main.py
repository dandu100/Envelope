from abc import abstractmethod, ABC


class AbstractStrategy(ABC):
    def __init__(self, envelops_list):
        self.envelops_list = envelops_list

    @abstractmethod
    def play(self):
        return


class More_then_N_percent_group_strategy(AbstractStrategy):
    def __init__(self, envelops_list):
        AbstractStrategy.__init__(self, envelops_list)
        self.percent =

    def play(self):
