def test_black():
    user_data = {'name': "Maksim", 'role': 'QA', 'permissions': ['service', 'expert']}
    buttons = ['btn_1', "btn_2", 'btn_3', "btn_4", 'btn_1', "btn_2", 'btn_3', "btn_4", 'btn_1', "btn_2", 'btn_3', "btn_4"]

    assert len(user_data) > 1, 'Not enough user data'
    assert len(buttons) > 5, 'Not enough buttons'