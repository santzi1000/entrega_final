import random
import string
from django.contrib.auth.models import User
from django.test import TestCase
from nota.models import Nota


class NotaTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username="testuser",
            password="12345",
        )
        Nota.objects.create(name="Python", code=123, owner=self.test_user)
        Nota.objects.create(name="Docker", code=789, owner=self.test_user)

        nota_test_num = 20
        self.mock_names = [
            "".join(
                [
                    random.choice((string.ascii_letters + string.digits))
                    for _ in range(random.randint(4, 20))
                ]
            )
            for _ in range(nota_test_num)
        ]
        self.mock_codes = [
            int(
                "".join(
                    [
                        random.choice((string.digits))
                        for _ in range(random.randint(3, 9))
                    ]
                )
            )
            for _ in range(nota_test_num)
        ]

        for mock_name, mock_code in zip(self.mock_names, self.mock_codes):
            Nota.objects.create(name=mock_name, code=mock_code, owner=self.test_user)

    def test_nota_model(self):
        """Notas creation are correctly identified"""
        python_nota = Nota.objects.get(name="Python")
        docker_nota = Nota.objects.get(name="Docker")
        self.assertEqual(python_nota.owner.username, "testuser")
        self.assertEqual(docker_nota.owner.username, "testuser")
        self.assertEqual(python_nota.code, 123)
        self.assertEqual(docker_nota.code, 789)

    def test_nota_list(self):
        for mock_name, mock_code in zip(self.mock_names, self.mock_codes):
            nota_test = Nota.objects.get(name=mock_name)
            self.assertEqual(nota_test.owner.username, "testuser")
            self.assertEqual(nota_test.code, mock_code)
