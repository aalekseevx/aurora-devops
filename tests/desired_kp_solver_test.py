from app.utils.desired_kp_solver import get_desired_kp


def test_get_desired_kp():
    expected_kps = {
        (55.75222, 37.61556): 7,  # Moscow
        (61.77347, 34.36569): 4,  # Petrozavodsk
        (59.93863, 30.31413): 5,  # Saint-Petersburg
    }
    for coords, expected in expected_kps.items():
        assert expected == get_desired_kp(*coords)
