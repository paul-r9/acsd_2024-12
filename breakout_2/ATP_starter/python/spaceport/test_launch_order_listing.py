import datetime
from launch_info import LaunchInfo
from spaceline_launch_info_provider import SpacelineLaunchInfoProvider
from spaceport_departure_board import SpaceportDepartureBoard


def test_launches_are_sorted_by_destination_when_destinations_are_unique():
    launch_info = LaunchInfoProviderStubUnique()
    # launch_info is sorted in __init__
    sut = SpaceportDepartureBoard(launch_info)
    destination_names = [info.destination for info in sut.launch_list]
    expected_names = ["Jupiter", "Mars", "Venus"]

    assert destination_names == expected_names


def test_launches_are_sorted_by_destination_then_launch_time():
    launch_info = LaunchInfoProviderStubMultiple()
    # launch_info is sorted in __init__
    sut = SpaceportDepartureBoard(launch_info)
    # Using launch_id to ensure the oldest Mars LaunchInfo object comes first
    destination_launch_ids = [info.launch_id for info in sut.launch_list]
    expected_launch_ids = [3, 4, 1, 2]

    assert destination_launch_ids == expected_launch_ids


class LaunchInfoProviderStubUnique(SpacelineLaunchInfoProvider):
    def get_current_launches(self):
        return [
            LaunchInfo(1, "Mars", datetime.datetime.now()),
            LaunchInfo(2, "Venus", datetime.datetime(2025, 1, 1, 5, 3, 2, 0)),
            LaunchInfo(3, "Jupiter", datetime.datetime(2025, 2, 3, 4, 5, 6, 0)),
        ]


class LaunchInfoProviderStubMultiple(SpacelineLaunchInfoProvider):
    def get_current_launches(self):
        return [
            LaunchInfo(1, "Mars", datetime.datetime.now()),
            LaunchInfo(2, "Venus", datetime.datetime(2025, 1, 1, 5, 3, 2, 0)),
            LaunchInfo(3, "Jupiter", datetime.datetime(2025, 2, 3, 4, 5, 6, 0)),
            LaunchInfo(4, "Mars", datetime.datetime(2024, 1, 2, 3, 4, 5, 6)),
        ]
