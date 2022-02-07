from django.core.validators import RegexValidator

from django.contrib.auth.models import AbstractUser
from django.db import models


# #
# nickname: CHAR(20) NOT NULL
# name: CHAR(30) NOT NULL
# password: CHAR(20) NOT NULL
# phone_number: CHAR(16) NOT NULL
# email: CHAR(50) NOT NULL
# region: CHAR(20) NOT NULL
# password_quiz: CHAR(30) NOT NULL
# password_quiz_answer: CHAR(30) NOT NULL
# created_at: DATETIME NOT NULL
# updated_at: DATETIME NOT NULL

#


class User(AbstractUser):
    # createsuperuser를 할 시에, 받을 username 필드를 뭘로 지정?
    USERNAME_FIELD = 'userID'
    REQUIRED_FIELDS = []
    first_name = None
    last_name = None
    date_joined = None


    userID = models.CharField(max_length=18, unique=True, null=False,primary_key=True)
    nickname = models.CharField(max_length=20, unique=True, null=False)
    name = models.CharField(
        max_length=30
        , null=False
    )

    phone_number = models.CharField(max_length=16,
                                    null=False,
                                    validators=[
                                        # 정규표현식, message='패턴이 조합되지 않으면 출력될 메시지
                                        RegexValidator(r"^\d{3}-?\d{4}-?\d{4}$", message="전화번호를 입력해주세요.")
                                    ],
                                    help_text="입력 예) 042-1234-1234")

    email = models.EmailField(max_length=50, unique=True, null=False)

    region = models.CharField(
        max_length=2,
        choices=[
            ("Se", "Seoul"),
            ("Bu", "Busan"),
            ("Gu", "Daegu"),
            ("In", "Incheon"),
            ("Da", "Daejeon"),
            ("Se", "Sejong"),
            ("Je", "Jeju"),
            ("Ga", "Gangwon"),
        ],
        blank=False)

    password_quiz = models.CharField(
        max_length=1,
        choices=[
            ("1", "내 보물1호는?"),
            ("2", "처음 키운 반려동물 이름은?"),
            ("3", "어머니 성함은?"),
            ("4", "아버지 성함은?"),
            ("5", "좋아하는 음식은?"),
        ],
        blank=True)

    password_quiz_answer = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
