from operator import attrgetter


class SpaceportDepartureBoard():
    def __init__(self, launch_info_provider):
        self.launch_list = launch_info_provider.get_current_launches()
        self.sort_launches()

    def get_launch_list(self):
        return self.launch_list

    def sort_launches(self):
        self.launch_list.sort(key=attrgetter("destination", "launch_time"))
