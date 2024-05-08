import sys

sys.path.insert(0, "D:/ZADANIA/Semestr6/Zmp")
from app_window_logic import AppWindowLogic
from unittest.mock import patch, MagicMock


def test_update_champions_ui():
    champions_data = [
        {
            "id": 1,
            "name": "Champion 1",
            "description": "Description 1",
            "image_link": "image1.jpg",
        },
        {
            "id": 2,
            "name": "Champion 2",
            "description": "Description 2",
            "image_link": "image2.jpg",
        },
        {
            "id": 3,
            "name": "Champion 3",
            "description": "Description 3",
            "image_link": "image3.jpg",
        },
    ]

    app_logic = AppWindowLogic()

    app_logic.update_champions_ui(champions_data)

    assert app_logic.ui.gridLayout_2.count() == len(champions_data)


def test_update_top_champions_ui():
    top_champions_data = [
        {
            "id": 1,
            "name": "Top Champion 1",
            "description": "Top Description 1",
            "image_link": "top_image1.jpg",
        },
        {
            "id": 2,
            "name": "Top Champion 2",
            "description": "Top Description 2",
            "image_link": "top_image2.jpg",
        },
        {
            "id": 3,
            "name": "Top Champion 3",
            "description": "Top Description 3",
            "image_link": "top_image3.jpg",
        },
    ]

    app_logic = AppWindowLogic()

    app_logic.update_top_champions_ui()

    assert app_logic.ui.gridLayout_4.count() == len(top_champions_data)


@patch("app_window_logic.keyring.get_password")
@patch("app_window_logic.requests.get")
def test_profile(mock_requests_get, mock_get_password):
    mock_get_password.return_value = "mocked_access_token"

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "name": "TestName",
        "email": "test@example.com",
        "logs": [],
        "likes": [],
    }
    mock_requests_get.return_value = mock_response

    app_logic = AppWindowLogic()

    app_logic.profile()

    assert app_logic.ui.summonerName.text() == "TestName"
    assert app_logic.ui.summonerEmail.text() == "test@example.com"


@patch("app_window_logic.requests.get")
def test_display_champion_details(mock_requests_get):
    mock_response = MagicMock()
    mock_response.content = b"mocked_image_data"
    mock_requests_get.return_value = mock_response

    app_logic = AppWindowLogic()

    champion_data = {
        "name": "Champion 1",
        "title": "Title 1",
        "roles": [{"name": "Role 1"}],
        "description": "Description 1",
        "likes_count": 10,
        "image_link": "http://example.com/image.jpg",
        "skills": [],
        "skins": [],
    }

    app_logic.display_champion_details(champion_data)

    assert app_logic.ui.championName.text() == "Champion 1"
    assert app_logic.ui.championTitle.text() == "Title 1"
    assert app_logic.ui.championRole.text() == "Role: Role 1"
    assert app_logic.ui.championDescription.text() == "Description 1"
    assert app_logic.ui.championLikes.text() == "Likes: 10"


@patch("app_window_logic.keyring.get_password")
@patch("app_window_logic.requests.get")
def test_search_and_display_profile(mock_requests_get, mock_get_password):
    mock_get_password.return_value = "mocked_access_token"

    app_logic = AppWindowLogic()

    username = "test_username"
    app_logic.ui.friendName.setText(username)

    app_logic.search_and_display_profile()

    mock_requests_get.assert_called_once_with(
        f"https://lolify.wheelwallet.cloud/api/profile/{username}",
        headers={
            "Authorization": "Bearer mocked_access_token",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )


@patch("app_window_logic.AppWindowLogic.fetch_champion_details")
@patch("app_window_logic.AppWindowLogic.display_champion_details")
def test_handle_champion_clicked(
    mock_display_champion_details, mock_fetch_champion_details
):
    mock_champion_data = {"id": 1, "name": "Champion 1", "description": "Description 1"}
    mock_fetch_champion_details.return_value = mock_champion_data

    app_logic = AppWindowLogic()

    app_logic.handle_champion_clicked(1)

    mock_fetch_champion_details.assert_called_once_with(1)
    mock_display_champion_details.assert_called_once_with(mock_champion_data)
