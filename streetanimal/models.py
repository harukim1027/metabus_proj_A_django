from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    CATEGORY = (
        ("강아지", "강아지"),
        ("고양이", "고양이"),
        ("기타동물", "기타동물"),
    )
    name = models.CharField(
        choices=CATEGORY, db_index=True, verbose_name="품종", max_length=10, unique=True
    )

    def __str__(self):
        return self.name


class Animal(TimestampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="동물 종", default=1)
    animal_no = models.AutoField(primary_key=True)
    animal_reg_num = models.CharField(max_length=50, unique=True)
    size = models.CharField(max_length=3, choices=(
        ("1", "소형"),
        ("2", "중형"),
        ("3", "대형"),
    ), default=1)
    sex = models.CharField(max_length=3, choices=(
        ("1", "암컷"),
        ("2", "수컷"),
    ), default=1)
    age = models.IntegerField()
    date_of_discovery = models.DateTimeField()
    place_of_discovery = models.CharField(max_length=30)
    physical_condition = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    protection_status = models.CharField(max_length=30, choices=(
        ("1", "입양 대기"),
        ("2", "입양 매칭 중"),
        ("3", "입양 완료!"),
    ), default=1)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.animal_reg_num


