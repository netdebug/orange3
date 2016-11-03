from Orange.data import Table
from Orange.widgets.learners.owknn import OWKNNLearner as OWKNNBase


class OWKNNLearner(OWKNNBase):
    pass


if __name__ == "__main__":
    import sys
    from AnyQt.QtWidgets import QApplication

    a = QApplication(sys.argv)
    ow = OWKNNLearner()
    d = Table('iris')
    ow.set_data(d)
    ow.show()
    a.exec_()
    ow.saveSettings()
