class Automaton():

    def __init__(self, config_file):
        self.config_file = config_file
        print("Hi, I'm an automaton!")

    def validate(self):
        """Return a Boolean

        Validates the config file.
        """
        return "I can't tell if the config file is valid... yet!"

    def accepts_input(self, input_str):
        """Return a Boolean

        The method returns True if the input is accepted,
        and it returns False if the input is rejected.
        """
        pass

    def read_input(self, input_str):
        """Return an Automation
        
        If the input is rejected, the method raises a
        RejectionException.
        """
        pass
    

if __name__ == "__main__":
    a = Automaton('your_config_file')
    print(a.validate())
