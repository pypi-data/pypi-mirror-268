from itertools import islice
import matplotlib.pyplot as plt


class Plots:
    """
    Plot different metrics curves for classification

    Parameters:

    classifiers: list of tuple
        List of (name, precisions, recalls) or (name, false positive rate, true positive rate) tuples.

    :param
        figure_size: tuple
            tuple of (width, length) of the plot in inches

    """

    def __init__(self, classifiers, figure_size=(6, 5)):
        self.classifiers = classifiers
        self.figure_size = figure_size
        self.figure = plt

    def _iter(self):

        """
        Generate (name, precisions, recalls) or (name, false positive rate, true positive rate) tuples from
         self.classifiers.
        """
        stop = len(self.classifiers)

        for (name, values_1, values_2) in islice(self.classifiers, 0, stop):
            yield name, values_1, values_2

    def plot_pr_curve(self):
        """

        Plot the precision-recall curve of the classifier.

        :param
        figure_size: tuple
            tuple of (width, length) of the plot in inches

        :return: plot of the pr-curve of the classifiers.
        """

        for name, precisions, recalls in self._iter():
            self.figure.figure(figsize=self.figure_size)
            plt.plot(precisions, recalls, linewidth=2, label=name)
            plt.xlabel("Precision")
            plt.ylabel("Recall")
            plt.grid()
            plt.legend(loc="best")
        plt.show()

    def plot_roc_curve(self):
        """
        Plot the precision-recall curve of the classifier.

        Parameters:

       :param
        figure_size: tuple
            tuple of (width, length) of the plot in inches


        :return: plot of the roc curve(s) of the classifier(s).
        """

        for name, fpr, tpr in self._iter():
            plt.figure(figsize=self.figure_size)
            plt.plot(fpr, tpr, linewidth=2, label=name)
            plt.plot([0, 1], [0, 1], 'k:', label="Random classifier's ROC curve")
            plt.xlabel('False Positive Rate (Fall-Out)')
            plt.ylabel('True Positive Rate (Recall)')
            plt.grid()
            plt.axis([0, 1, 0, 1])
            plt.legend(loc="best")
        plt.show()
