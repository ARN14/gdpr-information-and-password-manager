from src.gdpr_mask import mask


def test_nothing_to_mask():

    @mask()
    def get_client_details():
        return {
            'name': 'Jane Smith',
            'email': 'jane@coolmail.com',
            'telephones': {
                'mobile': '07999 987654'
            },
            'status': 'excellent'
        }

    assert get_client_details() == {
            'name': 'Jane Smith',
            'email': 'jane@coolmail.com',
            'telephones': {
                'mobile': '07999 987654'
            },
            'status': 'excellent'
        }


def test_masks_name():

    @mask("name")
    def get_client_details():
        return {
            'name': 'Jane Smith',
            'email': 'jane@coolmail.com',
            'telephones': {
                'mobile': '07999 987654'
            },
            'status': 'excellent'
        }

    assert get_client_details() == {
            'name': '**** *****',
            'email': 'jane@coolmail.com',
            'telephones': {
                'mobile': '07999 987654'
            },
            'status': 'excellent'
        }


def test_masks_multiple_fields():

    @mask("name", "email")
    def get_client_details():
        return {
            'name': 'Jane Smith',
            'email': 'jane@coolmail.com',
            'telephones': {
                'mobile': '07999 987654'
            },
            'status': 'excellent'
        }

    assert get_client_details() == {
            'name': '**** *****',
            'email': '*****************',
            'telephones': {
                'mobile': '07999 987654'
            },
            'status': 'excellent'
        }


def test_masks_nested_fields():

    @mask("mobile")
    def get_client_details():
        return {
            'name': 'Jane Smith',
            'email': 'jane@coolmail.com',
            'telephones': {
                'mobile': '07999 987654'
            },
            'status': 'excellent'
        }

    assert get_client_details() == {
            'name': 'Jane Smith',
            'email': 'jane@coolmail.com',
            'telephones': {
                'mobile': '***** ******'
            },
            'status': 'excellent'
        }


def test_masks_deeply_nested_fields():

    @mask("name", "office", "reception")
    def get_client_details():
        return {
            'name': 'Jane Smith',
            'email': 'jane@coolmail.com',
            'telephones': {
                'work': {
                    'office': '07999 987654',
                    'reception': '07346 842957'
                }
            },
            'status': 'excellent'
        }

    assert get_client_details() == {
            'name': '**** *****',
            'email': 'jane@coolmail.com',
            'telephones': {
                'work': {
                    'office': '***** ******',
                    'reception': '***** ******'
                }
            },
            'status': 'excellent'
        }
