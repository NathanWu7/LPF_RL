import numpy as np

class LowPassFilter:
    def __init__(self, alpha):
        """
        alpha: smooth_factor,0~1;0-stronger effect;1-weaker effect
        """
        self.alpha = alpha
        self.previous_value = None

    def apply(self, current_value):
        """
        """
        if self.previous_value is None:
            # first frame
            filtered_value = current_value
        else:
            # filter
            filtered_value = self.alpha * current_value + (1 - self.alpha) * self.previous_value
            #dead zone
            #filtered_value[abs(filtered_value) < 0.005] = 0

        # update
        self.previous_value = filtered_value

        return filtered_value

if __name__ == "__main__":
    
    lpf = LowPassFilter(alpha=0.1)

    actions = np.array([[0,1,1],[1,5,0],[0,-1,2]])

    filtered_actions = [lpf.apply(action) for action in actions]

    print("Original actions: ", actions)
    print("Filtered actions: ", filtered_actions)
