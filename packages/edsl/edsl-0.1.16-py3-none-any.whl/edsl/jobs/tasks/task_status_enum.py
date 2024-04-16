from __future__ import annotations
from collections import UserDict
import enum
import time

from edsl.jobs.tasks.TaskStatusLogEntry import TaskStatusLogEntry


class TaskStatus(enum.Enum):
    "These are the possible states a task can be in."
    NOT_STARTED = enum.auto()
    WAITING_FOR_DEPENDENCIES = enum.auto()
    CANCELLED = enum.auto()
    PARENT_FAILED = enum.auto()
    WAITING_FOR_REQUEST_CAPACITY = enum.auto()
    WAITING_FOR_TOKEN_CAPACITY = enum.auto()
    API_CALL_IN_PROGRESS = enum.auto()
    SUCCESS = enum.auto()
    FAILED = enum.auto()


class TaskStatusDescriptor:
    "The descriptor ensures that the task status is always an instance of the TaskStatus enum."

    def __init__(self):
        self._task_status = None

    def __get__(self, instance, owner):
        return self._task_status

    def __set__(self, instance, value):
        """Ensure that the value is an instance of TaskStatus."""
        if not isinstance(value, TaskStatus):
            raise ValueError("Value must be an instance of TaskStatus enum")
        t = time.monotonic()
        if hasattr(instance, "status_log"):
            instance.status_log.append(TaskStatusLogEntry(t, value))
        self._task_status = value

    def __delete__(self, instance):
        self._task_status = None


status_colors = {
    TaskStatus.NOT_STARTED: "grey",
    TaskStatus.WAITING_FOR_DEPENDENCIES: "orange",
    TaskStatus.WAITING_FOR_REQUEST_CAPACITY: "yellow",
    TaskStatus.WAITING_FOR_TOKEN_CAPACITY: "gold",
    TaskStatus.CANCELLED: "white",
    TaskStatus.PARENT_FAILED: "darkred",
    TaskStatus.FAILED: "red",
    TaskStatus.API_CALL_IN_PROGRESS: "blue",
    TaskStatus.SUCCESS: "green",
}


def get_enum_from_string(str_key):
    """Parse the string to extract the enum member name."""
    try:
        _, member_name = str_key.split(".")
        enum_member = getattr(TaskStatus, member_name)
        return enum_member
    except ValueError:
        return str_key


class InterviewTaskLogDict(UserDict):
    """A dictionary of TaskStatusLog objects.

    The key is the name of the task.
    """

    @property
    def min_time(self):
        return min([log.min_time for log in self.values()])

    @property
    def max_time(self):
        return max([log.max_time for log in self.values()])

    def status_matrix(self, num_periods):
        """Return a matrix of status values."""
        start_time = self.min_time
        end_time = self.max_time
        time_increment = (end_time - start_time) / num_periods
        status_matrix = {}
        time_periods = [start_time + i * time_increment for i in range(num_periods)]
        for task_name, log in self.items():
            status_matrix[task_name] = [log.status_at_time(t) for t in time_periods]
        return status_matrix

    def numerical_matrix(self, num_periods):
        """Return a numerical matrix of status values."""
        status_dicts = self.status_matrix(num_periods)

        num_cols = num_periods
        num_rows = len(status_dicts)
        matrix = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

        for row_index, (task_name, status_list) in enumerate(status_dicts.items()):
            matrix[row_index] = [
                list(status_colors.keys()).index(status) for status in status_list
            ]

        index_to_names = {i: name for i, name in enumerate(status_dicts.keys())}
        return matrix, index_to_names

    def visualize(self, num_periods=10):
        """Visualize the status matrix with outlined squares."""
        import matplotlib.pyplot as plt
        from matplotlib.colors import ListedColormap
        import numpy as np
        from matplotlib.patches import Rectangle

        # Define your custom colormap
        custom_cmap = ListedColormap(list(status_colors.values()))

        # Generate the matrix
        matrix, index_to_names = self.numerical_matrix(num_periods)

        # Create the figure and axes
        plt.figure(figsize=(10, 5))
        ax = plt.gca()

        # Display the matrix and keep a reference to the imshow object
        im = ax.imshow(matrix, aspect="auto", cmap=custom_cmap)

        # Adding color bar, now correctly associating it with 'im'
        cbar = plt.colorbar(im, ticks=range(len(status_colors)), label="Task Status")

        cbar_labels = [status.name for status in status_colors.keys()]
        # breakpoint()
        cbar.set_ticklabels(cbar_labels)  # Setting the custom labels for the colorbar

        im.set_clim(
            -0.5, len(status_colors) - 0.5
        )  # Setting color limits directly on the imshow object

        # Outline each cell by drawing rectangles
        for (j, i), val in np.ndenumerate(matrix):
            ax.add_patch(
                Rectangle(
                    (i - 0.5, j - 0.5), 1, 1, fill=False, edgecolor="black", lw=0.5
                )
            )

        # Set custom y-axis ticks and labels
        yticks = list(index_to_names.keys())
        yticklabels = list(index_to_names.values())
        plt.yticks(ticks=yticks, labels=yticklabels)

        # Show the plot
        plt.show()


if __name__ == "__main__":
    pass
