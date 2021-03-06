from django.test import RequestFactory, TestCase, override_settings

from gem.context_processors import compress_settings, detect_freebasics


class TestDetectFreebasics(TestCase):
    def setUp(self):
        self.request_factory = RequestFactory()

    def test_returns_false_by_default(self):
        request = self.request_factory.get('/')
        self.assertEqual(
            detect_freebasics(request),
            {'is_via_freebasics': False},
        )

    def test_returns_true_if_internetorg_in_httpvia(self):
        request = self.request_factory.get('/', HTTP_VIA='Internet.org')
        self.assertEqual(
            detect_freebasics(request),
            {'is_via_freebasics': True},
        )

    def test_returns_true_if_internetorgapp_in_user_agent(self):
        request = self.request_factory.get(
            '/',
            HTTP_USER_AGENT='InternetOrgApp',
        )
        self.assertEqual(
            detect_freebasics(request),
            {'is_via_freebasics': True},
        )

    def test_returns_true_if_true_in_xiorgsfbs(self):
        request = self.request_factory.get('/', HTTP_X_IORG_FBS='true')
        self.assertEqual(
            detect_freebasics(request),
            {'is_via_freebasics': True},
        )


class TestCompressSettings(TestCase):
    @override_settings(ENV='test_env', STATIC_URL='test_static_url')
    def test_returns_settings(self):
        request = RequestFactory().get('/')
        self.assertEqual(
            compress_settings(request),
            {
                'ENV': 'test_env',
                'STATIC_URL': 'test_static_url',
            }
        )
